from app import hello_World
import unittest


class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_World(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()