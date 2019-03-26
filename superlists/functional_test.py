from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.brower=webdriver.Chrome('/Users/finup/Desktop/chromedriver')
        self.brower.implicitly_wait(3)
    def tearDown(self):
        self.brower.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
         self.brower.get('http://localhost:8000')
         self.assertIn('Django',self.brower.title)
         self.fail('Finsh the test')

if __name__=='__main__':
    unittest.main(warnings='ignore')