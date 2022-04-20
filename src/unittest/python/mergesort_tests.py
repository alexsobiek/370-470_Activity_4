import unittest

from mergesort import mergeSort

class MergeSortTest(unittest.TestCase):
    def test_if_array_is_sorted(self):
        testArray = [3, 1, 2]
        correctArray = [1, 2, 3]

        self.assertEqual(correctArray, mergeSort(testArray))


    def test_fail(self):
        testArray = [3, 1, 2]
        failArray = [3, 1, 2]

        self.assertEqual(failArray, mergeSort(testArray))
