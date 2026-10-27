import unittest
from solution import DoorStateMachine


class TestDoorStateMachine(unittest.TestCase):
    def setUp(self):
        self.dsm = DoorStateMachine()

    def test_initial_state(self):
        self.assertEqual(self.dsm.state, 'CLOSED')

    def test_valid_transitions(self):
        result = self.dsm.process_event('open')
        self.assertEqual(result, 'OPEN')
        self.assertEqual(self.dsm.state, 'OPEN')

        result = self.dsm.process_event('close')
        self.assertEqual(result, 'CLOSED')
        self.assertEqual(self.dsm.state, 'CLOSED')

        result = self.dsm.process_event('lock')
        self.assertEqual(result, 'LOCKED')
        self.assertEqual(self.dsm.state, 'LOCKED')

        result = self.dsm.process_event('unlock')
        self.assertEqual(result, 'CLOSED')
        self.assertEqual(self.dsm.state, 'CLOSED')

    def test_invalid_events_raise_error(self):
        # lock a locked door
        self.dsm.state = 'LOCKED'
        with self.assertRaises(ValueError):
            self.dsm.process_event('lock')

        # open a locked door
        self.dsm.state = 'LOCKED'
        with self.assertRaises(ValueError):
            self.dsm.process_event('open')

        # unknown event
        self.dsm.state = 'CLOSED'
        with self.assertRaises(ValueError):
            self.dsm.process_event('fly')

        # close an open door? That's allowed, but not close a closed door
        self.dsm.state = 'CLOSED'
        with self.assertRaises(ValueError):
            self.dsm.process_event('close')

    def test_multiple_transitions(self):
        # OPEN -> CLOSED -> LOCKED -> CLOSED -> OPEN
        self.dsm.process_event('open')      # OPEN
        self.dsm.process_event('close')     # CLOSED
        self.dsm.process_event('lock')      # LOCKED
        self.dsm.process_event('unlock')    # CLOSED
        self.dsm.process_event('open')      # OPEN
        self.assertEqual(self.dsm.state, 'OPEN')


if __name__ == '__main__':
    unittest.main()
