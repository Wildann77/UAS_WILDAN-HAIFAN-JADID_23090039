from soal3 import PengaturanQueue

def main():
    queue_manager = PengaturanQueue()

    while True:
        print(f'Antrian Sekarang : {queue_manager.current()}')
        print(f'Antrian selanjutnya: {queue_manager.next()}')
        print('Pilihan:')
        print('1. Tambah Antrian')
        print('2. Antrian Selanjutnya')
        print('3. Keluar\n\n')
        p = input('Masukkan Pilihan: ')
        if p == '1':
            n = input('Masukkan Pesanan: ')
            queue_manager.queue(n)
            print()
        elif p == '2':
            if len(queue_manager.q) > 0:
                queue_manager.call_next()
                print()
            else:
                print("Queue kosong")
        elif p == '3':
            break
main()