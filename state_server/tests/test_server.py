#!/usr/bin/env python
import unittest

from state_server.core import server

class testStateServer(unittest.TestCase):
    def setUp(self):
        host, port = 'localhost', 22301
        self.st = server.StateServer(host, port)

    def tearDown(self):
        self.st.close()

    def test_init(self):
        pass

    def test_handle_accept(self):
        self.st.handle_accept()

if __name__ == "__main__":
    unittest.main()
