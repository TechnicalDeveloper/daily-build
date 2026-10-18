
import unittest
from solution import Turnstile

class TestTurnstile(unittest.TestCase):
    def test_initial_state(self):
        t = Turnstile()
        self.assertEqual(t.get_state(), "locked")

    def test_coin_from_locked(self):
        t = Turnstile()
        t.action("coin")
        self.assertEqual(t.get_state(), "unlocked")

    def test_push_from_locked(self):
        t = Turnstile()
        t.action("push")
        self.assertEqual(t.get_state(), "locked")

    def test_coin_from_unlocked(self):
        t = Turnstile()
        t.action("coin")
        t.action("coin")  # second coin while unlocked
        self.assertEqual(t.get_state(), "unlocked")

    def test_push_from_unlocked(self):
        t = Turnstile()
        t.action("coin")
        t.action("push")
        self.assertEqual(t.get_state(), "locked")

    def test_invalid_action(self):
        t = Turnstile()
        with self.assertRaises(ValueError):
            t.action("kick")
