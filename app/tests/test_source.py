import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("James Brown",'Corona spreads like wildfire','A shocking story of how fast the disease spreads','https://www.nation.co.ke')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


