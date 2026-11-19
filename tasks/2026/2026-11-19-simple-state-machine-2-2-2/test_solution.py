import unittest

from solution import StateMachine, InvalidTransition


class StateMachineTest(unittest.TestCase):
    def setUp(self):
        self.transitions = {
            ('locked', 'coin'): 'unlocked',
            ('unlocked', 'push'): 'locked',
        }
        self.machine = StateMachine('locked', self.transitions)

    def test_initial_state(self):
        self.assertEqual(self.machine.state, 'locked')

    def test_send_returns_new_state(self):
        result = self.machine.send('coin')
        self.assertEqual(result, 'unlocked')
        self.assertEqual(self.machine.state, 'unlocked')

    def test_invalid_transition_raises_and_keeps_state(self):
        with self.assertRaises(InvalidTransition):
            self.machine.send('push')
        self.assertEqual(self.machine.state, 'locked')

    def test_full_cycle(self):
        self.machine.send('coin')
        self.assertEqual(self.machine.state, 'unlocked')
        self.machine.send('push')
        self.assertEqual(self.machine.state, 'locked')

    def test_transition_table_is_copied(self):
        original = {
            ('a', 'go'): 'b',
            ('b', 'back'): 'a',
        }
        machine = StateMachine('a', original)
        original[('a', 'go')] = 'c'
        self.assertEqual(machine.send('go'), 'b')


if __name__ == '__main__':
    unittest.main()
