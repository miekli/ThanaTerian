from enum import Enum  # Import modul Enum untuk membuat enumerasi (defenisikan arah)
import random          # Import modul random untuk menghasilkan angka secara acak

class Direction(Enum):
    # Definisikan empat arah sebagai Enum
    up = 0
    down = 1
    left = 2
    right = 3
    @staticmethod
    def random():
        # Mengembalikan secara acak salah satu dari empat arah
        return random.choice([Direction.up, Direction.down, Direction.left, Direction.right])
