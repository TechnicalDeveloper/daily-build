from solution import StateMachine
import unittest

class TestStateMachine(unittest.TestCase):

    def test_valid_transition(self):
        sm = StateMachine('idle', {('idle', 'start'): 'running', ('running', 'stop'): 'idle'})
        self.assertEqual(sm.send('start'), 'running')
        self.assertEqual(sm.current_state(), 'running')

    def test_invalid_transition_returns_current_state(self):
        sm = StateMachine('idle', {('idle', 'start'): 'running'})
        result = sm.send('stop')  # stop not defined for idle
        self.assertEqual(result, 'idle')
        self.assertEqual(sm.current_state(), 'idle')

    def test_empty_transitions(self):
        sm = StateMachine('initial', {})
        self.assertEqual(sm.send('anything'), 'initial')
        self.assertEqual(sm.current_state(), 'initial')

    def test_self_transition(self):
        sm = StateMachine('on', {('on', 'toggle'): 'on', ('on', 'off'): 'off'})
        self.assertEqual(sm.send('toggle'), 'on')
        self.assertEqual(sm.current_state(), 'on')
        self.assertEqual(sm.send('off'), 'off')
        self.assertEqual(sm.current_state(), 'off')

    def test_chain_of_transitions(self):
        sm = StateMachine('a', {('a','x'): 'b', ('b','y'): 'c', ('c','z'): 'a'})
        sm.send('x')
        self.assertEqual(sm.current_state(), 'b')
        sm.send('y')
        self.assertEqual(sm.current_state(), 'c')
        sm.send('z')
        self.assertEqual(sm.current_state(), 'a')

if __name__ == '__main__':
    unittest.main()
