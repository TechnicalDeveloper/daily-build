import unittest
from solution import StateMachine


class TestStateMachine(unittest.TestCase):
    def setUp(self):
        self.sm = StateMachine('idle')
        self.sm.add_transition('idle', 'start', 'running')
        self.sm.add_transition('running', 'stop', 'idle')
        self.sm.add_transition('running', 'pause', 'paused')
        self.sm.add_transition('paused', 'resume', 'running')

    def test_initial_state(self):
        self.assertEqual(self.sm.state, 'idle')

    def test_valid_transition(self):
        self.assertEqual(self.sm.send('start'), 'running')
        self.assertEqual(self.sm.state, 'running')

    def test_invalid_event_from_current_state(self):
        with self.assertRaises(ValueError):
            self.sm.send('stop')

    def test_same_event_different_states(self):
        self.sm.send('start')
        self.sm.send('pause')
        self.assertEqual(self.sm.state, 'paused')
        self.assertEqual(self.sm.send('resume'), 'running')

    def test_long_sequence(self):
        self.sm.send('start')
        self.sm.send('stop')
        self.sm.send('start')
        self.assertEqual(self.sm.state, 'running')


if __name__ == '__main__':
    unittest.main()
