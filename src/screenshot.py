import lvgl as lv
from struct import pack
# import jpeg

# NOTE The following code is taken from the JPEG encoder of: https://github.com/xxyxyz/flat/blob/master/flat/jpeg.py

# copy-pasta from jpeg.jpy
_z_z = bytes([ # Zig-zag indices of AC coefficients
         1,  8, 16,  9,  2,  3, 10, 17, 24, 32, 25, 18, 11,  4,  5,
    12, 19, 26, 33, 40, 48, 41, 34, 27, 20, 13,  6,  7, 14, 21, 28,
    35, 42, 49, 56, 57, 50, 43, 36, 29, 22, 15, 23, 30, 37, 44, 51,
    58, 59, 52, 45, 38, 31, 39, 46, 53, 60, 61, 54, 47, 55, 62, 63])

_luminance_quantization = bytes([ # Luminance quantization table in zig-zag order
    16, 11, 12, 14, 12, 10, 16, 14, 13, 14, 18, 17, 16, 19, 24, 40,
    26, 24, 22, 22, 24, 49, 35, 37, 29, 40, 58, 51, 61, 60, 57, 51,
    56, 55, 64, 72, 92, 78, 64, 68, 87, 69, 55, 56, 80,109, 81, 87,
    95, 98,103,104,103, 62, 77,113,121,112,100,120, 92,101,103, 99])
_chrominance_quantization = bytes([ # Chrominance quantization table in zig-zag order
    17, 18, 18, 24, 21, 24, 47, 26, 26, 47, 99, 66, 56, 66, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99])

_ld_lengths = bytes([ # Luminance DC code lengths
    0, 1, 5, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
_ld_values = bytes([ # Luminance DC values
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
_la_lengths = bytes([ # Luminance AC code lengths
    0, 2, 1, 3, 3, 2, 4, 3, 5, 5, 4, 4, 0, 0, 1, 125])
_la_values = bytes([ # Luminance AC values
      1,  2,  3,  0,  4, 17,  5, 18, 33, 49, 65,  6, 19, 81, 97,  7, 34,113,
     20, 50,129,145,161,  8, 35, 66,177,193, 21, 82,209,240, 36, 51, 98,114,
    130,  9, 10, 22, 23, 24, 25, 26, 37, 38, 39, 40, 41, 42, 52, 53, 54, 55,
     56, 57, 58, 67, 68, 69, 70, 71, 72, 73, 74, 83, 84, 85, 86, 87, 88, 89,
     90, 99,100,101,102,103,104,105,106,115,116,117,118,119,120,121,122,131,
    132,133,134,135,136,137,138,146,147,148,149,150,151,152,153,154,162,163,
    164,165,166,167,168,169,170,178,179,180,181,182,183,184,185,186,194,195,
    196,197,198,199,200,201,202,210,211,212,213,214,215,216,217,218,225,226,
    227,228,229,230,231,232,233,234,241,242,243,244,245,246,247,248,249,250])
_cd_lengths = bytes([ # Chrominance DC code lengths
    0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
_cd_values = bytes([ # Chrominance DC values
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
_ca_lengths = bytes([ # Chrominance AC code lengths
    0, 2, 1, 2, 4, 4, 3, 4, 7, 5, 4, 4, 0, 1, 2, 119])
_ca_values = bytes([ # Chrominance AC values
      0,  1,  2,  3, 17,  4,  5, 33, 49,  6, 18, 65, 81,  7, 97,113, 19, 34,
     50,129,  8, 20, 66,145,161,177,193,  9, 35, 51, 82,240, 21, 98,114,209,
     10, 22, 36, 52,225, 37,241, 23, 24, 25, 26, 38, 39, 40, 41, 42, 53, 54,
     55, 56, 57, 58, 67, 68, 69, 70, 71, 72, 73, 74, 83, 84, 85, 86, 87, 88,
     89, 90, 99,100,101,102,103,104,105,106,115,116,117,118,119,120,121,122,
    130,131,132,133,134,135,136,137,138,146,147,148,149,150,151,152,153,154,
    162,163,164,165,166,167,168,169,170,178,179,180,181,182,183,184,185,186,
    194,195,196,197,198,199,200,201,202,210,211,212,213,214,215,216,217,218,
    226,227,228,229,230,231,232,233,234,242,243,244,245,246,247,248,249,250])

def _quantization_table(table, quality):
    quality = max(0, min(quality, 100))
    if quality < 50:
        q = 5000//quality
    else:
        q = 200 - quality*2
    return bytes([max(1, min((i*q + 50)//100, 255)) for i in table])

def _huffman_table(lengths, values):
    table = [None]*(max(values) + 1)
    code = 0
    i = 0
    size = 1
    for a in lengths:
        for j in range(a):
            table[values[i]] = code, size
            code += 1
            i += 1
        code *= 2
        size += 1
    return table

def _scale_factor(table):
    factor = [0]*64
    factor[0] = table[0]*8
    i = 1
    for z in _z_z:
        factor[z] = table[i]*8
        i += 1
    return factor

def _marker_segment(marker, data):
    return b'\xff' + marker + pack('>H', len(data) + 2) + data

def _forward_dct(block):
    # Ref.: Independent JPEG Group's "jfdctint.c", v8d
    # Copyright (C) 1994-1996, Thomas G. Lane
    # Modification developed 2003-2009 by Guido Vollbeding
    for i in range(0, 64, 8):
        tmp0 = block[i] + block[i+7]
        tmp1 = block[i+1] + block[i+6]
        tmp2 = block[i+2] + block[i+5]
        tmp3 = block[i+3] + block[i+4]
        tmp10 = tmp0 + tmp3
        tmp12 = tmp0 - tmp3
        tmp11 = tmp1 + tmp2
        tmp13 = tmp1 - tmp2
        tmp0 = block[i] - block[i+7]
        tmp1 = block[i+1] - block[i+6]
        tmp2 = block[i+2] - block[i+5]
        tmp3 = block[i+3] - block[i+4]
        block[i] = (tmp10 + tmp11 - 8*128) << 2 # PASS1_BITS
        block[i+4] = (tmp10 - tmp11) << 2
        z1 = (tmp12 + tmp13)*4433 # FIX_0_541196100
        z1 += 1024 # 1 << (CONST_BITS-PASS1_BITS-1)
        block[i+2] = (z1 + tmp12*6270) >> 11 # FIX_0_765366865
        block[i+6] = (z1 - tmp13*15137) >> 11 # FIX_1_847759065
        tmp10 = tmp0 + tmp3
        tmp11 = tmp1 + tmp2
        tmp12 = tmp0 + tmp2
        tmp13 = tmp1 + tmp3
        z1 = (tmp12 + tmp13)*9633 # FIX_1_175875602
        z1 += 1024 # 1 << (CONST_BITS-PASS1_BITS-1)
        tmp0 = tmp0*12299 # FIX_1_501321110
        tmp1 = tmp1*25172 # FIX_3_072711026
        tmp2 = tmp2*16819 # FIX_2_053119869
        tmp3 = tmp3*2446 # FIX_0_298631336
        tmp10 = tmp10*-7373 # FIX_0_899976223
        tmp11 = tmp11*-20995 # FIX_2_562915447
        tmp12 = tmp12*-3196 # FIX_0_390180644
        tmp13 = tmp13*-16069 # FIX_1_961570560
        tmp12 += z1
        tmp13 += z1
        block[i+1] = (tmp0 + tmp10 + tmp12) >> 11
        block[i+3] = (tmp1 + tmp11 + tmp13) >> 11
        block[i+5] = (tmp2 + tmp11 + tmp12) >> 11
        block[i+7] = (tmp3 + tmp10 + tmp13) >> 11
    for i in range(8):
        tmp0 = block[i] + block[i+56]
        tmp1 = block[i+8] + block[i+48]
        tmp2 = block[i+16] + block[i+40]
        tmp3 = block[i+24] + block[i+32]
        tmp10 = tmp0 + tmp3 + 2 # 1 << (PASS1_BITS-1)
        tmp12 = tmp0 - tmp3
        tmp11 = tmp1 + tmp2
        tmp13 = tmp1 - tmp2
        tmp0 = block[i] - block[i+56]
        tmp1 = block[i+8] - block[i+48]
        tmp2 = block[i+16] - block[i+40]
        tmp3 = block[i+24] - block[i+32]
        block[i] = (tmp10 + tmp11) >> 2 # PASS1_BITS
        block[i+32] = (tmp10 - tmp11) >> 2
        z1 = (tmp12 + tmp13)*4433 # FIX_0_541196100
        z1 += 16384 # 1 << (CONST_BITS+PASS1_BITS-1)
        block[i+16] = (z1 + tmp12*6270) >> 15 # FIX_0_765366865, CONST_BITS+PASS1_BITS
        block[i+48] = (z1 - tmp13*15137) >> 15 # FIX_1_847759065
        tmp10 = tmp0 + tmp3
        tmp11 = tmp1 + tmp2
        tmp12 = tmp0 + tmp2
        tmp13 = tmp1 + tmp3
        z1 = (tmp12 + tmp13)*9633 # FIX_1_175875602
        z1 += 16384 # 1 << (CONST_BITS+PASS1_BITS-1)
        tmp0 = tmp0*12299 # FIX_1_501321110
        tmp1 = tmp1*25172 # FIX_3_072711026
        tmp2 = tmp2*16819 # FIX_2_053119869
        tmp3 = tmp3*2446 # FIX_0_298631336
        tmp10 = tmp10*-7373 # FIX_0_899976223
        tmp11 = tmp11*-20995 # FIX_2_562915447
        tmp12 = tmp12*-3196 # FIX_0_390180644
        tmp13 = tmp13*-16069 # FIX_1_961570560
        tmp12 += z1
        tmp13 += z1
        block[i+8] = (tmp0 + tmp10 + tmp12) >> 15 # CONST_BITS+PASS1_BITS
        block[i+24] = (tmp1 + tmp11 + tmp13) >> 15
        block[i+40] = (tmp2 + tmp11 + tmp12) >> 15
        block[i+56] = (tmp3 + tmp10 + tmp13) >> 15


class _entropy_encoder(object):
    
    def __init__(self):
        c = [i for j in reversed(range(16)) for i in range(1 << j)]
        s = [j for j in range(1, 16) for i in range(1 << (j - 1))]
        s = [0] + s + list(reversed(s))
        self.codes, self.sizes = c, s
        self.value, self.length = 0, 0
        self.data = bytearray()
    
    def encode(self, previous, block, scale, dc, ac):
        _forward_dct(block)
        for i in range(64):
            block[i] = (((block[i] << 1)//scale[i]) + 1) >> 1
        d = block[0] - previous
        if d == 0:
            self.write(*dc[0])
        else:
            s = self.sizes[d]
            self.write(*dc[s])
            self.write(self.codes[d], s)
        n = 0
        for i in _z_z:
            if block[i] == 0:
                n += 1
            else:
                while n > 15:
                    self.write(*ac[0xf0])
                    n -= 16
                s = self.sizes[block[i]]
                self.write(*ac[n*16 + s])
                self.write(self.codes[block[i]], s)
                n = 0
        if n > 0:
            self.write(*ac[0])
        return block[0]
    
    def write(self, value, length):
        data = self.data
        value += (self.value << length)
        length += self.length
        while length > 7:
            length -= 8
            v = (value >> length) & 0xff
            if v == 0xff:
                data.append(0xff)
                data.append(0)
            else:
                data.append(v)
        self.value = value & 0xff
        self.length = length
    
    def dump(self):
        return self.data

class image():
    def __init__(self, width: int, height: int, kind: str, data: bytes):
        if kind not in ('g', 'rgb', 'cmyk'):
            raise ValueError('Invalid image kind.')
        self.width = width
        self.height = height
        self.kind = kind
        self.n = 1 if kind == 'g' else 3 if kind == 'rgb' else 4
        self.data = data

def serialize(image, quality):
    w, h, n, data = image.width, image.height, image.n, image.data
    ydc = udc = vdc = kdc = 0
    yblock, ublock, vblock, kblock = [0]*64, [0]*64, [0]*64, [0]*64
    lq = _quantization_table(_luminance_quantization, quality)
    ld = _huffman_table(_ld_lengths, _ld_values)
    la = _huffman_table(_la_lengths, _la_values)
    ls = _scale_factor(lq)
    if n == 3:
        cq = _quantization_table(_chrominance_quantization, quality)
        cd = _huffman_table(_cd_lengths, _cd_values)
        ca = _huffman_table(_ca_lengths, _ca_values)
        cs = _scale_factor(cq)
    e = _entropy_encoder()
    for y in range(0, h, 8):
        for x in range(0, w, 8):
            i = 0
            for yy in range(y, y + 8):
                for xx in range(x, x + 8):
                    j = (min(xx, w - 1) + min(yy, h - 1)*w)*n
                    if n == 1:
                        yblock[i] = data[j]
                    elif n == 3:
                        r, g, b = data[j], data[j + 1], data[j + 2]
                        yblock[i] = (19595*r + 38470*g + 7471*b + 32768) >> 16
                        ublock[i] = (-11056*r - 21712*g + 32768*b + 8421376) >> 16
                        vblock[i] = (32768*r - 27440*g - 5328*b + 8421376) >> 16
                    else: # n == 4
                        yblock[i] = data[j]
                        ublock[i] = data[j + 1]
                        vblock[i] = data[j + 2]
                        kblock[i] = data[j + 3]
                    i += 1
            ydc = e.encode(ydc, yblock, ls, ld, la)
            if n == 3:
                udc = e.encode(udc, ublock, cs, cd, ca)
                vdc = e.encode(vdc, vblock, cs, cd, ca)
            elif n == 4:
                udc = e.encode(udc, ublock, ls, ld, la)
                vdc = e.encode(vdc, vblock, ls, ld, la)
                kdc = e.encode(kdc, kblock, ls, ld, la)
    e.write(0x7f, 7) # padding
    app = b'Adobe\0\144\200\0\0\0\0' # tag, version, flags0, flags1, transform
    sof = b'\10' + pack('>HHB', h, w, n) + b'\1\21\0' # depth, id, sampling, qtable
    sos = pack('B', n) + b'\1\0' # id, htable
    dqt = b'\0' + lq
    dht = b'\0' + _ld_lengths + _ld_values + b'\20' + _la_lengths + _la_values
    if n == 3:
        sof += b'\2\21\1\3\21\1'
        sos += b'\2\21\3\21'
        dqt += b'\1' + cq
        dht += b'\1' + _cd_lengths + _cd_values + b'\21' + _ca_lengths + _ca_values
    elif n == 4:
        sof += b'\2\21\0\3\21\0\4\21\0'
        sos += b'\2\0\3\0\4\0'
    sos += b'\0\77\0' # start, end, approximation
    return b''.join([
        b'\xff\xd8', # SOI
        _marker_segment(b'\xee', app) if n == 4 else b'',
        _marker_segment(b'\xdb', dqt),
        _marker_segment(b'\xc0', sof),
        _marker_segment(b'\xc4', dht),
        _marker_segment(b'\xda', sos),
        e.dump(),
        b'\xff\xd9']) # EOI

def bgr_to_rgb(data):
    """Swap the BGR values to RGB in a flat bytearray."""
    # Assume data is a flat bytearray in BGR format
    for i in range(0, len(data), 3):
        data[i], data[i+2] = data[i+2], data[i]  # Swap the B and R values
    return data

def take_screenshot(container: lv.obj, output_file: str, quality:int = 100):
    """Take a screenshot of a container using the LVGL snapshot API and save it to a JPG file."""
    snapshot = lv.snapshot_take(container, lv.COLOR_FORMAT.NATIVE)
    print(f"Snapshot: {snapshot} ({type(snapshot)}, {snapshot.data_size} bytes)")
    data_size = snapshot.data_size
    buffer = snapshot.data.__dereference__(data_size)
    img = image(container.get_width(), container.get_height(), "rgb", bgr_to_rgb(buffer))
    try:
        with open(output_file, 'wb') as f:
            f.write(serialize(img, quality))
    except MemoryError as e:
        print(e)
    finally:
        lv.snapshot_free(snapshot)