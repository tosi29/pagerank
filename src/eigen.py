import numpy as np


def eigen1():
    array = np.array([
        [0, 1 / 3, 0, 1 / 3, 0, 1 / 3],
        [0, 0, 0, 1, 0, 0, ],
        [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],
        [0, 0, 0, 0, 1 / 2, 1 / 2],
        [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],
        [0, 0, 0, 1, 0, 0]
    ]).T

    print(array)

    w, v = np.linalg.eig(array)

    for i in w:
        print(i)

    print()
    for i in v:
        print(i)

    print()
    print("eig vector 1 ")
    for i in v[:, 0]:
        print(i/np.linalg.norm(v[:, 0]))
    print()


eigen1()
