import numpy as np
from skimage import img_as_float


def align(img, g_coord):
    row_g, col_g = g_coord
    # считаем сдвиги каналов

    img = img_as_float(img)
    h = img.shape[0] // 3

    b_width = int(img.shape[1] * 0.15)
    b_height = int(h * 0.15)

    b = img[:h, :]
    g = img[h:h * 2, :]
    r = img[h * 2:h * 3, :]

    r = r[b_height:-1 - b_height, b_width:-1 - b_width]
    g = g[b_height:-1 - b_height, b_width:-1 - b_width]
    b = b[b_height:-1 - b_height, b_width:-1 - b_width]

    # сдвигаем точку на зеленом канале
    # на другие каналы
    bdx, bdy, rdx, rdy = 0, 0, 0, 0

    d_correlation = -1
    for dy in range(-15, 16):
        for dx in range(-15, 16):
            db = np.roll(b, dy, axis=0)
            db = np.roll(db, dx, axis=1)
            correlation = (db * g).sum()
            if d_correlation < correlation:
                d_correlation = correlation
                bdy = dy
                bdx = dx

    b = np.roll(b, bdy, axis=0)
    b = np.roll(b, bdx, axis=1)

    d_correlation = -1
    for dy in range(-15, 16):
        for dx in range(-15, 16):
            dr = np.roll(r, dy, axis=0)
            dr = np.roll(dr, dx, axis=1)
            correlation = (dr * g).sum()
            if d_correlation < correlation:
                d_correlation = correlation
                rdy = dy
                rdx = dx

    r = np.roll(r, rdy, axis=0)
    r = np.roll(r, rdx, axis=1)

    return (row_g - h - bdy, col_g - bdx), (row_g + h - rdy, col_g - rdx)
