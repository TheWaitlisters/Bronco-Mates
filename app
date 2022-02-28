from mockito import mock, verify
import unittest

from app import startup

class app(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        app(out)

        verify(out).write("Hello world")