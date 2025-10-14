from matriks.matrix import Matrix

def mean(values):
    """Menghitung rata-rata dari list 1D."""
    return sum(values) / len(values)

def correlation(x, y):
    """Korelasi Pearson antara dua variabel."""
    if isinstance(x, Matrix):
        x = [row[0] for row in x.data]
    if isinstance(y, Matrix):
        y = [row[0] for row in y.data]

    if len(x) != len(y):
        raise ValueError("Panjang x dan y harus sama.")

    x_mean = mean(x)
    y_mean = mean(y)

    numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    denominator = (sum((xi - x_mean)**2 for xi in x) * sum((yi - y_mean)**2 for yi in y)) ** 0.5

    if denominator == 0:
        return 0

    return numerator / denominator


def correlation_matrix(matrix, header=None):
    """
    Menghitung korelasi antar semua kolom numerik pada matriks.
    - matrix: Matrix atau list of lists
    - header: list nama kolom (opsional)
    """
    if isinstance(matrix, Matrix):
        data = matrix.data
    else:
        data = matrix

    # Kalau ada header di baris pertama → lewati
    if all(isinstance(val, str) for val in data[0]):
        header_row = data[0]
        data = data[1:]
    else:
        header_row = header or [f"X{i}" for i in range(len(data[0]))]

    # Ambil hanya kolom numerik
    numeric_cols = []
    numeric_names = []
    for j in range(len(data[0])):
        try:
            col = [float(row[j]) for row in data if str(row[j]).replace('.', '', 1).isdigit()]
            if len(col) == len(data):  # semua baris valid numerik
                numeric_cols.append(col)
                numeric_names.append(header_row[j])
        except Exception:
            continue

    n = len(numeric_cols)
    result = [[0.0 for _ in range(n)] for _ in range(n)]

    # Hitung korelasi antar semua kolom
    for i in range(n):
        for j in range(n):
            result[i][j] = correlation(numeric_cols[i], numeric_cols[j])

    return numeric_names, Matrix(result)
