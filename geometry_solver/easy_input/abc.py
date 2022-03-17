from geometry_solver.entity import Point


def points(*ids):
    """Create a seris of points"""
    ps = [Point(i) for i in ids]
    return ps


A, B, C, D, E, F, G, H, I = points('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
J, K, L, M, N, O, P, Q, R = points('J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R')
S, T, U, V, W, X, Y, Z = points('S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


__all__ = list(map(chr, range(65, 91)))
