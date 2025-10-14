# matriks/importers/csv_importer.py
import csv
from matriks.matrix import Matrix

def import_from_csv(nama_file):
    """Mengimpor data matriks dari file CSV."""
    data = []
    with open(nama_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # ubah ke float bila memungkinkan
            data.append([float(x) if x.replace('.', '', 1).isdigit() else x for x in row])
    print(f"Matriks berhasil diimpor dari {nama_file}")
    return Matrix(data)
