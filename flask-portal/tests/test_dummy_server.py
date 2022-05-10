import unittest
from app.dummy_server import dummy_response

class Test_Dummy_Server(unittest.TestCase):
    
    def test_dummy_response(self):
        expected_response = "<p>Hello, World!</p>"
        response = dummy_response()
        self.assertEqual(response, expected_response)