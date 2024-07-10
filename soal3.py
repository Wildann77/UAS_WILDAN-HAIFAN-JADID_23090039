class PengaturanQueue:
    def __init__(self):
        self.q = []

    def queue(self, i):
        self.q.append(i)

    def call_next(self):
        if len(self.q) > 0:
            self.q.pop(0)

    def current(self) -> str:
        return self.q[0] if len(self.q) > 0 else "Tidak ada"

    def next(self) -> str:
        return self.q[1] if len(self.q) > 1 else "Tidak ada"
