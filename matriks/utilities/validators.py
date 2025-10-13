# matriks/utilities/validators.py
from ..matrix import Matrix

def is_square(matrix):
    """
    Memeriksa apakah sebuah matriks adalah matriks persegi.
    """
    return matrix.rows == matrix.cols

def is_symmetric(matrix):
    """
    Memeriksa apakah sebuah matriks adalah matriks simetris.
    Matriks simetris adalah matriks persegi yang sama dengan transposenya.
    """
    # Periksa apakah matriks adalah matriks persegi
    if not is_square(matrix):
        return False

    # Periksa apakah elemen (i, j) sama dengan elemen (j, i)
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            if matrix.data[i][j] != matrix.data[j][i]:
                return False

    return True
