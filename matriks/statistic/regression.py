# matriks/operations/regresi_linier.py
from matriks.operations.transpose import transpose
from matriks.operations.inverse import inverse
from matriks.operations.multiplier import multiply_matrices
from matriks.matrix import Matrix

def regresi_linier(X, y):
    """
    Menghitung regresi linier sederhana atau berganda menggunakan metode OLS.
    Rumus: β = (XᵀX)⁻¹ Xᵀy
    """

    # Pastikan y berbentuk kolom
    if not isinstance(y[0], list):
        y = [[val] for val in y]

    Xt = transpose(X)
    XtX = multiply_matrices(Xt, X)
    XtX_inv = inverse(XtX)
    XtY = multiply_matrices(Xt, Matrix(y))
    beta = multiply_matrices(XtX_inv, XtY)

    return beta


def prediksi(X, beta):
    """Menghitung nilai prediksi y_hat = X * beta"""
    return multiply_matrices(X, beta)


def evaluasi(y_asli, y_pred):
    """Menghitung metrik evaluasi: SSE, MSE, dan R²"""

    # ubah ke list 1D
    y_asli = [val[0] if isinstance(val, list) else val for val in y_asli]
    y_pred = [val[0] if isinstance(val, list) else val for val in y_pred]

    n = len(y_asli)
    mean_y = sum(y_asli) / n
    residuals = [y_asli[i] - y_pred[i] for i in range(n)]

    # SSE (Sum of Squared Errors)
    SSE = sum(r**2 for r in residuals)

    # SST (Total Sum of Squares)
    SST = sum((y - mean_y)**2 for y in y_asli)

    # R² dan MSE
    R2 = 1 - (SSE / SST)
    MSE = SSE / n

    return {
        "SSE": SSE,
        "MSE": MSE,
        "R2": R2,
        "residuals": residuals
    }
