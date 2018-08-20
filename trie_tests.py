import unittest
from . import trie


class TrieTest(unittest.TestCase):
    def testHasWord(self):
        tr = self.__getTrie()
        self.assertTrue(tr.hasWord('Ola'))

    def testNegativeHasWord(self):
        tr = self.__getTrie()
        self.assertFalse(tr.hasWord('SomeWord'))

    def testWordsWithPrefix(self):
        tr = self.__getTrie()
        expected = ['Ouch', 'Ola', 'Olala']
        self.assertTrue(self.__checkAreListsEqual(expected, tr.getWordsWithPrefix('O')))

    def testWordsWithPrefixAndDots(self):
        tr = self.__getTrie()
        expected = ['Ola', 'Olala']
        self.assertTrue(self.__checkAreListsEqual(expected, tr.getWordsWithPrefix('Ol...')))

    def testDeleteWord(self):
        tr = self.__getTrie()
        expected = ['Ouch', 'Ola']
        tr.deleteWord('Olala')
        self.assertTrue(self.__checkAreListsEqual(expected, tr.getWordsWithPrefix('O')))

    # Get Trie object with dummy values
    def __getTrie(self):
        tr = trie.Trie()
        tr.add('word')
        tr.add('Ola')
        tr.add('Ouch')
        tr.add('Olala')

        return tr

    # Method which checks if 2 lists contain the same values
    def __checkAreListsEqual(self, l1, l2):
        return len(l1) == len(l2) and sorted(l1) == sorted(l2)
