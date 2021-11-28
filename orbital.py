"""Orbital wavefunctions for Hydrogen."""

from PIL import Image, ImageDraw
import numpy as np


def scaled_wf(n, l, m, x, y):
    """Scaled Wave function cΨ.

    Args:
        n: Principal quantum number (1, 2, 3).
        l: Azimuthal quantum number (0, 1, 2).
        m: Magnetic quantum number (0, ±1, ±2).
        x: x - coordinate.
        y: y - coordinate.
    """
    nlm = [n, l, m]
    r = np.sqrt(x ** 2 + y ** 2)
    exp = np.exp(- r / n)
    rem = 1

    if nlm == [1, 0, 0]:
        rem = 2
    
    if nlm == [2, 0, 0]:
        rem = 4 * (1 - r / 2)

    elif nlm == [2, 1, 0]:
        rem = 1.5 * y
    elif nlm == [2, 1, 1]:
        rem = 1.5 * x
    
    elif nlm == [3, 0, 0]:
        rem = 7 * (1 - 2 * r / 3 + 2 * (r ** 2) / 27)
    elif nlm == [3, 1, 0]:
        rem = 4 * y * (1 - r / 6)
    elif nlm == [3, 1, 1]:
        rem = 4 * x * (1 - r / 6)
    elif nlm == [3, 2, 0]:
        rem = (1 / 7) * (3 * (y ** 2) - (r ** 2))
    elif nlm == [3, 2, 1]:
        rem = (1 / 2) * x * y
    elif nlm == [3, 2, 2]:
        rem = (1 / 4) * (x ** 2 - y ** 2)
    
    return rem * exp


if __name__ == '__main__':
    pix = 400
    thresh = 0.0

    for n in [1, 2, 3]:
        lim = 5 * (n ** 2 - n + 2) / 2
        
        for l in range(n):
            for m in range(l + 1):
                im = Image.new('HSV', (pix, pix), (0, 0, 0))
                draw = ImageDraw.Draw(im)

                for x in range(pix):
                    for y in range(pix):
                        xx = - lim + (x / pix) * (2 * lim)
                        yy = - lim + (y / pix) * (2 * lim)

                        wf = scaled_wf(n, l, m, xx, yy)
                        wf = 0 if abs(wf) < thresh else wf
                        draw.point([x, y], (0 if wf >= 0 else 171, abs(int(255 * wf)), 255))

                im.convert('RGB').save(f'Orbitals\\n{n}-l{l}-m{m}.png', 'PNG')
