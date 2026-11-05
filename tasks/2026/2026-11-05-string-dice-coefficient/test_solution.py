import unittest
from solution import dice_coefficient

class TestDiceCoefficient(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(dice_coefficient('', ''), 1.0)
        self.assertEqual(dice_coefficient('', 'abc'), 0.0)
        self.assertEqual(dice_coefficient('xyz', ''), 0.0)

    def test_single_char_strings(self):
        self.assertEqual(dice_coefficient('a', 'a'), 1.0)
        self.assertEqual(dice_coefficient('a', 'b'), 0.0)
        self.assertEqual(dice_coefficient('a', 'ab'), 0.0)

    def test_identical_strings(self):
        self.assertAlmostEqual(dice_coefficient('hello', 'hello'), 1.0)
        self.assertAlmostEqual(dice_coefficient('abcde', 'abcde'), 1.0)

    def test_no_common_bigrams(self):
        self.assertAlmostEqual(dice_coefficient('ab', 'cd'), 0.0)
        self.assertAlmostEqual(dice_coefficient('xy', 'ab'), 0.0)

    def test_partial_overlap(self):
        # 'ab' and 'abc' share bigram 'ab'
        self.assertAlmostEqual(dice_coefficient('ab', 'abc'), 2*1/(1+2))
        # 'night' and 'nacht' share 'ch'? Actually 'night' bigrams: ni,ig,gh,ht; 'nacht': na,ac,ch,ht -> common: ht -> 2*1/(4+4)=0.25
        self.assertAlmostEqual(dice_coefficient('night', 'nacht'), 0.25)

    def test_identical_different_length(self):
        # 'test' and 'test' bigrams: te,es,st -> 3, intersection 3 -> 2*3/(3+3)=1.0
        self.assertAlmostEqual(dice_coefficient('test', 'test'), 1.0)

if __name__ == '__main__':
    unittest.main()
