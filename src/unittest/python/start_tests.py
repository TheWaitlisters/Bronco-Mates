from mockito import mock, verify
import unittest

from app import start

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        start(out)

        verify(out).write("Successfully starting up")