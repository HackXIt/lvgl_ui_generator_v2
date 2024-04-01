from invoke import task
import os
import subprocess

lv_micropython_dir = os.path.join(os.path.curdir, 'lv_micropython')
micropython = os.path.join(os.path.curdir, 'lv_micropython', 'ports', 'unix', 'build-standard', 'micropython')
main = os.path.join(os.path.curdir, 'src', 'main.py')
jpg_conversion = os.path.join(os.path.curdir, 'src', 'bin_to_jpg_conversion.py')
lv_conf_project = os.path.join(os.path.curdir, 'lv_conf.h')
lv_conf_original = os.path.join(os.path.curdir, 'lv_micropython', 'lib', 'lv_bindings', 'lv_conf.h')
lv_conf_temp = os.path.join(os.path.curdir, 'lv_conf.tmp')

@task
def generate_random(ctx, widget_list: str = 'button label line bar slider switch checkbox roller dropdown textarea chart', width: int = 420, height: int = 320, count: int = 1, layout: str = 'none', output: str = 'screenshot.jpg', normalize: bool = False):
    args = [micropython, main, '-m', 'generator', '-W', str(width), '-H', str(height), '-c', str(count), '-o', output, '-l', layout]
    args.append('-t')
    for widget in widget_list.split(' '):
        args.append(widget)
    if normalize:
        args.append('--normalize')
    subprocess.run(args)

@task
def generate_design(ctx, design_file: str ='designs/example.json', output: str = 'screenshot.jpg', normalize: bool = False):
    if not os.path.exists(design_file):
        print(f"Design file {design_file} does not exist.")
        return
    args = [micropython, main, '-m', 'design', '-f', design_file, '-o', output]
    if normalize:
        args.append('--normalize')
    subprocess.run(args)

@task
def convert(ctx, width='420', height='320', input='screenshot.bin', output='screenshot.jpg'):
    subprocess.run(['poetry', 'run', 'python', jpg_conversion, '-W', width, '-H', height, '-i', input, '-o', output])

@task
def sample(ctx, type='button', count='1', width='420', height='320', layout='none', output='screenshot.jpg', normalize: bool = False):
    if normalize:
        gen = subprocess.run([micropython, main, '-m', 'generator' '-W', width, '-H', height, '-c', count, '-t', type, '-o', output, '-l', layout, '-n'])
    else:
        gen = subprocess.run([micropython, main, '-m', 'generator', '-W', width, '-H', height, '-c', count, '-t', type, '-o', output, '-l', layout])
    if gen.returncode == 0:
        print("UI sample generation successful.")
    else:
        print("UI sample generation generation failed.")

@task
def clear(ctx):
    subprocess.run(['rm', 'screenshot.raw', 'screenshot.bin', 'screenshot.jpg'])

@task
def test(ctx):
    ...

def run_and_print(cmd, cwd):
    with subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as proc:
        for line in proc.stdout:
            print(line, end='')
        return proc.wait()  # Wait for the subprocess to finish and get the return code

@task
def build(ctx):
    # Move lv_conf.h to a temporary location
    subprocess.run(['mv', lv_conf_original, lv_conf_temp])
    # Override lv_conf.h
    subprocess.run(['cp', lv_conf_project, lv_conf_original])
    mpy_cross_returncode = run_and_print(['make', '-j4', '-C', 'mpy-cross'], lv_micropython_dir)
    unix_port_submodules_returncode = run_and_print(['make', '-j4', '-C', 'ports/unix', 'submodules'], lv_micropython_dir)
    unix_port_returncode = run_and_print(['make', '-j4', '-C', 'ports/unix'], lv_micropython_dir)
    # Restore lv_conf.h so that git doesn't complain about dirty changes
    subprocess.run(['mv', lv_conf_temp, lv_conf_original])
    return_codes = [mpy_cross_returncode, unix_port_submodules_returncode, unix_port_returncode]
    if all(code == 0 for code in return_codes):
        # Copy the micropython binary to the root .venv directory
        subprocess.run(['cp', micropython, os.path.join(os.path.curdir, '.venv', 'bin', 'micropython')])
    else:
        print("Build failed.")
