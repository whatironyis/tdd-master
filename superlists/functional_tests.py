from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome('chromedriver') #otwarcie przegladarki
		self.browser.implicitly_wait(5)

	def tearDown(self):
		self.browser.quit() #zamkniecie przegladarki
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Listy',self.browser.title) #sprawdza czy strona ma w sobie listy

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Lista',header_text) #sprawdza czy naglowek ma listy

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Wpisz rzecz do zrobienia'
		)

		#w polu tekstowym wpisuje rzeczy do zrobienia
		inputbox.send_keys('Kupic cos tam')
		#klawiszem enter zatwierdza
		inputbox.send_keys(Keys.ENTER)
		#sprawdzenie czy w tabeli jest 'Kupic cos tam'

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1.Kupic cos tam' for row in rows),
			'nie pokazuje nowej rzeczy w tabeli'
		)
		self.fail('Zakonczenie testu')
#kolejne zadanie
#strona zostala zaktualniona i wyswietla dwie rzeczy
#sprawdzenie czy strona zapamietuje te rzeczy
#jeszcze raz wchodzi na strone
#udalo sie idziemy spac
if __name__ == '__main__':
	unittest.main(warnings='ignore')
