import os
import struct
import xml.etree.ElementTree as ET

assets = [
    'assets/pdfhub-preview.png',
    'assets/imagehub-preview.svg',
    'assets/cyberguard-preview.png',
    'assets/habitsgrow-preview.png',
    'assets/compressor-preview.svg',
    'assets/termux-preview.svg',
    'assets/passport-preview.svg',
    'assets/audio-preview.svg',
    'assets/task-manager-preview.svg',
    'assets/deployment-preview.svg'
]

def get_png_size(path):
    with open(path, 'rb') as f:
        data = f.read(24)
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            w, h = struct.unpack('>LL', data[16:24])
            return w, h
    return None

for p in assets:
    if os.path.exists(p):
        if p.endswith('.png'):
            size = get_png_size(p)
            print(f"{p}: PNG size={size}")
        elif p.endswith('.svg'):
            tree = ET.parse(p)
            root = tree.getroot()
            vb = root.get('viewBox')
            w = root.get('width')
            h = root.get('height')
            print(f"{p}: SVG viewBox={vb} width={w} height={h}")
    else:
        print(f"{p}: NOT FOUND")
