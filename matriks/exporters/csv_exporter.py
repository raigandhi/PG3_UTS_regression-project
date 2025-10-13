# matriks/exporters/csv_exporter.py
import csv

def export_to_csv(matriks, nama_file):
    """Mengekspor data matriks ke file CSV."""
    with open(nama_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(matriks.data)
    print(f"Matriks berhasil diekspor ke {nama_file}")
