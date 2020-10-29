import unittest
from scripts.helper import scrape

class TestScraping(unittest.TestCase):

	def test_check_xml_path_is_valid(self):
		conditions_today, conditions_today_plus1, conditions_today_plus2, _ = scrape(['2019-12-01'], 'sea-to-sky', 'No')
		self.assertEqual(conditions_today[0], ['2019-12-01', 'Low', 1, 'Low', 1, 'Low', 1])
		self.assertEqual(conditions_today_plus1[0], ['2019-12-02', 'Low', 1, 'Low', 1, 'Low', 1])
		self.assertEqual(conditions_today_plus2[0], ['2019-12-03', 'Low', 1, 'Low', 1, 'Low', 1])

if __name__ == '__main__':
	unittest.main()