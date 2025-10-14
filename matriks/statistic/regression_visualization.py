import matplotlib.pyplot as plt
from matriks.matrix import Matrix

def plot_regresi(X, y, beta, judul="Visualisasi Regresi Linier"):
    """
    Menampilkan scatter plot data dan garis hasil regresi linier.
    Hanya cocok untuk regresi linier sederhana (1 variabel independen).
    """
    if isinstance(X, Matrix):
        X_data = [row[1] if len(row) > 1 else row[0] for row in X.data]  # lewati kolom bias 1
    else:
        X_data = [row[1] if len(row) > 1 else row[0] for row in X]

    if isinstance(y, Matrix):
        y_data = [row[0] for row in y.data]
    else:
        y_data = [row[0] if isinstance(row, list) else row for row in y]

    # Jika X punya kolom bias → ambil slope dan intercept
    if len(beta.data) == 2:
        intercept, slope = beta.data[0][0], beta.data[1][0]
    else:
        intercept, slope = 0, beta.data[0][0]

    # Prediksi garis regresi
    y_pred = [intercept + slope * xi for xi in X_data]

    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(X_data, y_data, color="#FF6B6B", label="Data Aktual")
    plt.plot(X_data, y_pred, color="#1A535C", linewidth=2, label="Garis Regresi")
    plt.title(judul, fontsize=14, fontweight="bold")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()
