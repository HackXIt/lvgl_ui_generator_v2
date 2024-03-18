from invoke import task
import os
import subprocess

lv_micropython_dir = os.path.join(os.path.curdir, 'lv_micropython')
micropython = os.path.join(os.path.curdir, 'lv_micropython', 'ports', 'unix', 'build-standard', 'micropython')
main = os.path.join(os.path.curdir, 'src', 'main.py')
jpg_conversion = os.path.join(os.path.curdir, 'src', 'jpg_conversion.py')

@task
def generate(ctx):
    widget_list = ['button', 'label', 'line', 'bar', 'slider', 'switch', 'checkbox', 'roller', 'dropdown', 'textarea', 'chart']
    subprocess.run([micropython, main, '-W', '420', '-H', '320', '-c', '1', '-t', ' '.join(widget_list), '-o', 'screenshot.raw', '-l', 'none'])

@task
def sample(ctx, type='button', count='1', width='420', height='320', layout='none'):
    subprocess.run([micropython, main, '-W', width, '-H', height, '-c', count, '-t', type, '-o', 'screenshot.bin', '-l', layout])
    subprocess.run(['poetry', 'run', 'python', jpg_conversion])

@task
def test(ctx):
    ...

@task
def build(ctx):
    subprocess.run(['make', '-C', 'mpy-cross'], cwd=lv_micropython_dir)
    subprocess.run(['make', '-C', 'ports/unix', 'submodules'], cwd=lv_micropython_dir)
    subprocess.run(['make', '-C', 'ports/unix'], cwd=lv_micropython_dir)
