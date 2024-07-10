class dataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self, nim, name):
        self.data.append({'NIM': nim, 'Name': name})

    def tampilkan(self):
        if not self.data:
            print("Tidak ada data mahasiswa.")
        else:
            print("\nData Mahasiswa:")
            for student in self.data:
                print(f"NIM: {student['NIM']}, Nama: {student['Name']}")

def main():
    student_data = dataMahasiswa()

    while True:
        nim = input('Masukkan NIM: ')
        name = input('Masukkan Nama: ')
        student_data.tambah(nim, name)

        pilihan = input('Tambah lagi? (ya/tidak): ').strip().lower()
        if pilihan != 'ya':
            break

    student_data.tampilkan()

if __name__ == "__main__":
    main()
