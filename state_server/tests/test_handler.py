#!/usr/bin/env python
import unittest

from state_server.core import handler
from state_server.core import state

class TestSocket(object):
    def setblocking(self, i):
        pass

    def close(self):
        pass

    def fileno(self):
        return 0

    def getpeername(self):
        return 0

    def recv(self, buffer_size):
        return self.test_str

    def send(self, data):
        self.output = data

    def set_data(self, data):
        self.test_str = data

class testHandler(unittest.TestCase):
    def setUp(self):
        sock = TestSocket()
        self.h = handler.QueryHandler(sock)
        self.h.state_obj = state.State()

    def test_init(self):
        pass

    def test_handle_na(self):
        self.h.set_data('name_0\n')
        self.h.handle_read()
        self.assertEqual(self.h.output, handler.NA_MSG+'\n')

    def test_handle_ok(self):
        self.h.set_data('name_1 value\n')
        self.h.handle_read()
        self.assertEqual(self.h.output, handler.OK_MSG+'\n')

        self.h.set_data('name_1 \n')
        self.h.handle_read()
        self.assertEqual(self.h.output, handler.OK_MSG+'\nvalue\n')

    def test_handle_cmd(self):
        self.assertEqual(self.h.handle_cmd('name_0'), handler.NA_MSG)
        self.assertEqual(self.h.handle_cmd('name_0', 'value'), handler.OK_MSG)
        self.assertEqual(self.h.handle_cmd('name_0'), 'value')

if __name__ == "__main__":
    unittest.main()
