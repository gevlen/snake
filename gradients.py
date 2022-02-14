import pygame


def horizontal(size, startcolor, endcolor):
    """
    Draws a horizontal linear gradient filling the entire surface. Returns a
    surface filled with the gradient (numeric is only 2-3 times faster).
    """
    width = size[0]
    bigSurf = pygame.Surface((width, 1)).convert_alpha()
    dd = 1.0/width
    sr, sg, sb, sa = startcolor
    er, eg, eb, ea = endcolor
    rm = (er-sr)*dd
    gm = (eg-sg)*dd
    bm = (eb-sb)*dd
    am = (ea-sa)*dd
    for y in range(width):
        bigSurf.set_at((y,0),
                        (int(sr + rm*y),
                         int(sg + gm*y),
                         int(sb + bm*y),
                         int(sa + am*y))
                      )
    return pygame.transform.scale(bigSurf, size)





