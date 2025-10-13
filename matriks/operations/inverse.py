from matriks.matrix import Matrix

def inverse(matrix: Matrix) -> Matrix:
    """Mengembalikan invers dari objek Matrix (jika persegi dan tidak singular)."""
    if matrix.rows != matrix.cols:
        raise ValueError("Matriks harus persegi untuk dihitung inversnya.")

    n = matrix.rows
    A = [row[:] for row in matrix.data]
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for i in range(n):
        pivot = A[i][i]
        if pivot == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    I[i], I[k] = I[k], I[i]
                    pivot = A[i][i]
                    break
            else:
                raise ValueError("Matriks singular, tidak punya invers.")

        # Normalisasi pivot
        for j in range(n):
            A[i][j] /= pivot
            I[i][j] /= pivot

        # Eliminasi baris lain
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                    I[k][j] -= factor * I[i][j]

    return Matrix(I)

