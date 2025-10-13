#matriks/exporters/json_exporter.py
import json

def export_to_json(matriks, nama_file):
    """
    Fungsi: mengekspor objek atau SparseMatrix ke file JSON.
    """
    # Konversi data matriks ke list of lits (jika perlu)
    data_list = matriks.data
    #Konversi ke string JSON
    json_str = json.dumps(data_list, indent=4)
    # Tulis ke file
    with open(nama_file, mode='w') as file:
         file.write(json_str)
    # Tampilkan pesan sukse
    print(f"Matriks berhasil diekspor ke {nama_file}")
