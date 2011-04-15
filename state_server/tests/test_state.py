#!/usr/bin/env python
import unittest

from state_server.core import state

class testState(unittest.TestCase):
    def setUp(self):
        self.st = state.State()

    def test_empty_get(self):
        self.assertEqual(self.st.get('no_such_val'), None)

    def test_set_get(self, num=100):
        for seq in range(0, num):
            self.st.set('name_%d' % seq, 'value_%d' % seq)

        for seq in range(0, num):
            self.assertEqual(self.st.get('name_%d' % seq), 'value_%d' % seq)

    def test_large_seq(self):
        self.test_set_get(100000)

    def test_dump(self):
        self.test_set_get(100)
        dump = self.st.dump()
        for seq in range(100):
            self.assertTrue('name_%d' % seq in dump)
            self.assertEqual(dump['name_%d' % seq], 'value_%d' % seq)

    def test_preserve_type(self):
        self.st.set('int', 1)
        self.st.set('list', [])
        self.st.set('dict', {})

        self.assertTrue(type(self.st.get('int')) == int)
        self.assertTrue(type(self.st.get('list')) == list)
        self.assertTrue(type(self.st.get('dict')) == dict)

if __name__ == "__main__":
    unittest.main()
