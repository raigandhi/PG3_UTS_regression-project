from matriks.matrix import Matrix

def transpose(matrix: Matrix) -> Matrix:
    """Mengembalikan transpose dari objek Matrix."""
    transposed_data = [
        [matrix.data[i][j] for i in range(matrix.rows)]
        for j in range(matrix.cols)
    ]
    return Matrix(transposed_data)
