import unittest
from app.models import Review

class MovieTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Review class
    '''

    def setUp(self):
        '''
        Setup method that will run before every test
        '''
        self.new_review = Review(1234, 'A review', 'https://image.tmdb.org/t/p/w500/kusjha27hbs', 'A very long review')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))



if __name__ == '__main__':
    unittest.main()