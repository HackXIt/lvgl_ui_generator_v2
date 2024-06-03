import os

README_path = os.path.join('README.md')
with open(README_path, 'r') as f:
    README = f.read()

# Fix the path of images in the READM: https://github.com/mitmproxy/pdoc/issues/696
README.replace('./docs/assets/', './assets/')

__doc__ = README