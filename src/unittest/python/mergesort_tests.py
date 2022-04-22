import unittest

from mergesort import mergeSort

class MergeSortTest(unittest.TestCase):
    def test_if_array_is_sorted(self):
        testArray = [3, 1, 2]
        correctArray = [1, 2, 3]

        self.assertEqual(correctArray, mergeSort(testArray))

    def test_negative_numbers(self):
        testArray = [5, -1, 3, -2]
        correctArray = [-2, -1, 3, 5]

        self.assertEqual(correctArray, mergeSort(testArray))

    def test_array_with_letters(self):
        testArray = ['F', 'E', 'D', 'C', 'B', 'A']
        correctArray = ['A', 'B', 'C', 'D', 'E', 'F']

        self.assertEqual(correctArray, mergeSort(testArray))