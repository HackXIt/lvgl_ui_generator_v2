from invoke import task
import os
import subprocess

lv_micropython_dir = os.path.join(os.path.curdir, 'lv_micropython')
micropython = os.path.join(os.path.curdir, 'lv_micropython', 'ports', 'unix', 'build-standard', 'micropython')
main = os.path.join(os.path.curdir, 'src', 'main.py')
jpg_conversion = os.path.join(os.path.curdir, 'src', 'jpg_conversion.py')
lv_conf_project = os.path.join(os.path.curdir, 'lv_conf.h')
lv_conf_original = os.path.join(os.path.curdir, 'lv_micropython', 'lib', 'lv_bindings', 'lv_conf.h')
lv_conf_temp = os.path.join(os.path.curdir, 'lv_conf.tmp')

@task
def generate(ctx):
    widget_list = ['button', 'label', 'line', 'bar', 'slider', 'switch', 'checkbox', 'roller', 'dropdown', 'textarea', 'chart']
    subprocess.run([micropython, main, '-W', '420', '-H', '320', '-c', '1', '-t', ' '.join(widget_list), '-o', 'screenshot.raw', '-l', 'none'])

@task
def sample(ctx, type='button', count='1', width='420', height='320', layout='none'):
    subprocess.run([micropython, main, '-W', width, '-H', height, '-c', count, '-t', type, '-o', 'screenshot.bin', '-l', layout])
    subprocess.run(['poetry', 'run', 'python', jpg_conversion, '-W', width, '-H', height, '-i', 'screenshot.bin', '-o', 'screenshot.jpg'])

@task
def clear(ctx):
    subprocess.run(['rm', 'screenshot.raw', 'screenshot.bin', 'screenshot.jpg'])

@task
def test(ctx):
    ...

@task
def build(ctx):
    # Move lv_conf.h to a temporary location
    subprocess.run(['mv', lv_conf_original, lv_conf_temp])
    # Override lv_conf.h
    subprocess.run(['cp', lv_conf_project, lv_conf_original])
    mpy_cross = subprocess.run(['make', '-j4', '-C', 'mpy-cross'], cwd=lv_micropython_dir, capture_output=True)
    unix_port_submodules = subprocess.run(['make', '-j4', '-C', 'ports/unix', 'submodules'], cwd=lv_micropython_dir, capture_output=True)
    unix_port = subprocess.run(['make', '-j4', '-C', 'ports/unix'], cwd=lv_micropython_dir, capture_output=True)
    # Restore lv_conf.h so that git doesn't complain about dirty changes
    subprocess.run(['mv', lv_conf_temp, lv_conf_original])    
    if mpy_cross.returncode == 0 and unix_port_submodules.returncode == 0 and unix_port.returncode == 0:
        # Copy the micropython binary to the root .venv directory
        subprocess.run(['cp', micropython, os.path.join(os.path.curdir, '.venv', 'bin', 'micropython')])
    else:
        print("Build failed.")
        print(mpy_cross.stderr)
        print(unix_port_submodules.stderr)
        print(unix_port.stderr)
