import unittest
import src.helpers as helpers

class TestHelpers(unittest.TestCase):

    helper = helpers.Helpers()

    def test_get_hemisphere(self):
        self.assertEqual(self.helper.get_hemisphere('29.4572'), 'norte')
        self.assertEqual(self.helper.get_hemisphere('-37.3159'), 'sul')

if __name__ == '__main__':
    unittest.main()
