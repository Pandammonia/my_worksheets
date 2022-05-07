import unittest
from nameformat import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for nameformat"""

	def test_first_last_name(self):
		"""Do names like Luke Peacock work"""
		formattedname = get_formatted_name('luke', 'peacock')
		self.assertEqual(formattedname, 'Luke Peacock')

	def test_firt_last_middle_name(self):
		"""Do names like Luke J Peacock work"""
		formattedname = get_formatted_name('luke', 'peacock', 'J')
		self.assertEqual(formattedname, 'Luke J Peacock')

if __name__ == '__main__':
	unittest.main()