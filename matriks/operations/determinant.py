# matriks/operations/determinant.py
from ..matrix import Matrix

def find_determinant(matrix):
    """
    Menghitung determinan dari sebuah matriks.
    Fungsi ini hanya bekerja untuk matriks 2x2.
    """
    # Periksa apakah matriks adalah matriks 2x2
    if matrix.rows != 2 or matrix.cols != 2:
        raise ValueError("Fungsi ini hanya mendukung matriks 2x2.")

    # Hitung determinan (ad - bc)
    determinant = (matrix.data[0][0] * matrix.data[1][1]) - (matrix.data[0][1] * matrix.data[1][0])
    return determinant
