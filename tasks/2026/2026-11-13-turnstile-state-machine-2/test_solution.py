import unittest
from solution import Turnstile

class TestTurnstile(unittest.TestCase):
    def test_initial_state(self):
        t = Turnstile()
        self.assertEqual(t.get_state(), 'locked')

    def test_coin_unlocks(self):
        t = Turnstile()
        result = t.process_event('coin')
        self.assertEqual(result, 'unlocked')
        self.assertEqual(t.get_state(), 'unlocked')

    def test_push_locks_after_unlock(self):
        t = Turnstile()
        t.process_event('coin')   # -> unlocked
        result = t.process_event('push')
        self.assertEqual(result, 'locked')
        self.assertEqual(t.get_state(), 'locked')

    def test_push_when_locked_stays_locked(self):
        t = Turnstile()
        result = t.process_event('push')
        self.assertEqual(result, 'locked')
        self.assertEqual(t.get_state(), 'locked')

    def test_coin_when_unlocked_stays_unlocked(self):
        t = Turnstile()
        t.process_event('coin')   # -> unlocked
        result = t.process_event('coin')
        self.assertEqual(result, 'unlocked')
        self.assertEqual(t.get_state(), 'unlocked')

    def test_invalid_event_raises(self):
        t = Turnstile()
        with self.assertRaises(ValueError):
            t.process_event('token')
        # State should remain unchanged after failed event
        self.assertEqual(t.get_state(), 'locked')

if __name__ == '__main__':
    unittest.main()
