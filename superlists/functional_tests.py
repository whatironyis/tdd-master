from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):

		self.browser = webdriver.Chrome('chromedriver')
		self.browser.implicitly_wait(3)
	#otwarcie przegladarki
	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')
	#pomysl na liste rzeczy do zrobienia i otwarcie konkretnego adresu
		self.assertIn('Listy',self.browser.title) #sprawdza czy strona ma w sobie listy
		self.fail('Zakonczenie testu')
#w polu tekstowym wpisuje rzeczy do zrobienia
#klawiszem enter zatwierdza
#1.Kupic pawie piora
#kolejne zadanie
#strona zostala zaktualniona i wyswietla dwie rzeczy
#sprawdzenie czy strona zapamietuje te rzeczy
#jeszcze raz wchodzi na strone
#udalo sie idziemy spac
if __name__ == '__main__':
	unittest.main(warnings='ignore')
