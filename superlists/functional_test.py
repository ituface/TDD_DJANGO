from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.brower=webdriver.Chrome('/Users/finup/Desktop/chromedriver')
        self.brower.implicitly_wait(3)
    def tearDown(self):
        self.brower.quit()

    def check_for_row_in_list_table(self,row_text):
        table=self.brower.find_element_by_id('id_list_table')
        rows=table.find_element_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])
    def test_can_start_a_list_and_retrieve_it_later(self):
         self.brower.get('http://localhost:8000')
         self.assertIn('To-Do',self.brower.title)
         header_text=self.brower.find_element_by_tag_name('h1').text
         self.assertIn('To-Do',header_text)
         inputbox=self.brower.find_element_by_id('id_new_item')
         self.assertEqual(inputbox.get_attribute('placeholder'),
                          'Enter a to-do item'
                          )
         inputbox.send_keys('Buy peacock feathers')
         inputbox.send_keys(Keys.ENTER)
         table=self.brower.find_element_by_id('id_list_table')
         rows=table.find_elements_by_tag_name('tr')
         self.assertIn(
             '1:Buy peacock feathers' ,[row.text for row in rows])

         self.assertIn('2:Use peacock feathers to make a fly',[row.text for row in rows])

         #她按了回车键后，页面更新了
         #待办事项表格中显示了'1：Buy peacock feathers'
         inputbox.send_keys(Keys.ENTER)
         self.check_for_row_in_list_table('1:Buy peacock feathers')

         inputbox=self.brower.find_element_by_id('id_new_item')
         inputbox.send_keys('Use peapcock feathers to make a fly')
         inputbox.send_keys(Keys.ENTER)

         self.check_for_row_in_list_table('1:Buy peacock feathers')
         self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')
         self.fail('Finsh the test')

if __name__=='__main__':
    unittest.main(warnings='ignore')