import unittest
from solution import RollingHash

class TestRollingHash(unittest.TestCase):
    def test_window_size_one(self):
        rh = RollingHash(1)
        rh.ingest(b'\x05')
        self.assertEqual(rh.current_hash(), 5)
        rh.ingest(b'\x03')
        self.assertEqual(rh.current_hash(), 3)

    def test_window_size_three(self):
        rh = RollingHash(3)
        rh.ingest(b'\x01\x02\x03')
        # indices 0,1,2 -> 1*1 + 2*2 + 3*3 = 1+4+9 = 14
        self.assertEqual(rh.current_hash(), 14)
        rh.ingest(b'\x04')
        # window now [0x02, 0x03, 0x04] -> 2*1 + 3*2 + 4*3 = 2+6+12 = 20
        self.assertEqual(rh.current_hash(), 20)

    def test_less_than_window_size(self):
        rh = RollingHash(5)
        rh.ingest(b'abc')
        self.assertEqual(rh.current_hash(), 0)

    def test_large_values_mod(self):
        rh = RollingHash(2)
        rh.ingest(b'\xff\xff')
        # 255*1 + 255*2 = 255 + 510 = 765
        self.assertEqual(rh.current_hash(), 765)
        rh.ingest(b'\x01')
        # window [0xff, 0x01] -> 255*1 + 1*2 = 257
        self.assertEqual(rh.current_hash(), 257)

if __name__ == '__main__':
    unittest.main()
