#!/usr/bin/env python
import unittest


import test_state
import test_server
import test_handler

def get_suite():
    ts = unittest.TestSuite()
    loader = unittest.TestLoader()
    classes = [test_state.testState, test_handler.testHandler,
        test_server.testStateServer]
    for cls in classes:
        ts.addTest(loader.loadTestsFromTestCase(cls))

    return ts

def main():
    unittest.TextTestRunner().run(get_suite())

if __name__ == "__main__":
    main()
