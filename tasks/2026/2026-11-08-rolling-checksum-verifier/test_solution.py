import unittest
from solution import RollingChecksum

class TestRollingChecksum(unittest.TestCase):

    def test_small_window_sliding(self):
        rc = RollingChecksum(1)
        rc.update(10)
        self.assertEqual(rc.digest(), 10)
        rc.update(20, old_byte=10)
        self.assertEqual(rc.digest(), 20)
        rc.update(30, old_byte=20)
        self.assertEqual(rc.digest(), 30)

    def test_multiple_updates_before_slide(self):
        rc = RollingChecksum(3)
        rc.update(1)
        rc.update(2)
        rc.update(3)
        # sum = 1+2+3 = 6 ≡ 6 mod 256
        self.assertEqual(rc.digest(), 6)
        # now slide: remove 1, add 4
        rc.update(4, old_byte=1)
        self.assertEqual(rc.digest(), (2+3+4) % 256)  # 9

    def test_large_byte_values_modulo(self):
        rc = RollingChecksum(2)
        rc.update(255)
        rc.update(255)
        # 255+255 = 510 ≡ 254 mod 256
        self.assertEqual(rc.digest(), 254)
        rc.update(0, old_byte=255)
        # remove one 255, add 0 => 255+0 = 255
        self.assertEqual(rc.digest(), 255)

    def test_window_size_one_repeated_slide(self):
        rc = RollingChecksum(1)
        for val in [50, 100, 150, 200]:
            rc.update(val, old_byte=val-50 if val != 50 else None)
            if val == 50:
                continue  # first update had no old_byte
        self.assertEqual(rc.digest(), 200)

    def test_edge_negative_modulo(self):
        rc = RollingChecksum(3)
        rc.update(0)
        rc.update(0)
        rc.update(0)
        self.assertEqual(rc.digest(), 0)
        rc.update(1, old_byte=0)
        # 0+0+1 = 1
        self.assertEqual(rc.digest(), 1)

if __name__ == '__main__':
    unittest.main()
