# matriks/main.py
from matriks.matrix import Matrix
from matriks.operations.adder import add_matrices
from matriks.operations.multiplier import multiply_matrices
from matriks.operations.transpose import transpose
from matriks.operations.inverse import inverse
from matriks.statistic.regression import regresi_linier, prediksi, evaluasi
from matriks.utilities import print_matrix
from matriks.exporters.csv_exporter import export_to_csv

if __name__ == "__main__":
    matriks_a = Matrix([[1, 2], [3, 4]])
    matriks_b = Matrix([[5, 6], [7, 8]])

    print("Hasil Penjumlahan:")
    hasil_penjumlahan = add_matrices(matriks_a, matriks_b)
    print_matrix(hasil_penjumlahan)

    print("\nHasil Perkalian:")
    hasil_perkalian = multiply_matrices(matriks_a, matriks_b)
    print_matrix(hasil_perkalian)

    print("\nHasil Transpose Matriks A:")
    hasil_transpose = transpose(matriks_a)
    print_matrix(hasil_transpose)

    print("\nHasil Transpose Matriks B:")
    hasil_transpose = transpose(matriks_b)
    print_matrix(hasil_transpose)

    print("\nHasil Invers Matriks A:")
    hasil_invers = inverse(matriks_a)
    print_matrix(hasil_invers)

    print("\nHasil Invers Matriks B:")
    hasil_invers = inverse(matriks_b)
    print_matrix(hasil_invers)

    matrix_c = Matrix([[10, 20], [30, 40]])
    print("\nMenyimpan Matriks C ke file CSV:")
    export_to_csv(matrix_c, "matriks_c.csv")

    print("\n=== Regresi Linier (OLS) ===")

    # Contoh data
    X = Matrix([[1, 1], [1, 2], [1, 3], [1, 4]])  # 1 untuk intercept
    y = [2, 3, 4, 5]

    beta = regresi_linier(X, y)
    print("Koefisien (β):", beta.data)

    y_pred = prediksi(X, beta)
    print("Prediksi (ŷ):", y_pred.data)

    hasil_eval = evaluasi([[val] for val in y], y_pred.data)
    print("Evaluasi Model:")
    print("  SSE =", hasil_eval["SSE"])
    print("  MSE =", hasil_eval["MSE"])
    print("  R²  =", hasil_eval["R2"])
