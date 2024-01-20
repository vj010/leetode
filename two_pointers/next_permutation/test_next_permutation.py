import unittest

next_permutation = __import__("next_permutation")
Solution = next_permutation.Solution
quick_sort = Solution.quick_sort


class TestSolution(unittest.TestCase):
    tests = [
        # [[1, 2, 3], [1, 3, 2], "length 3 - all unique"],
        # [[1, 2], [2, 1], "length 2 - all unique "],
        [[1], [1], "length 1 "],
        [[1, 1], [1, 1], "length 2 - all same"],
        [[1, 1, 3], [1, 3, 1], "length 3 - non - unique"],
        [[1, 3, 5, 4], [1, 4, 3, 5], "length 4 - all unique"],
        [[1, 1, 3, 4], [1, 1, 4, 3], "length 4 - non - unique 1"],
        [[1, 1, 4, 3], [1, 3, 1, 4], "length 4 - non - unique 2"],
    ]

    # def test_nextPermutation(self):
    #     for test in TestSolution.tests:
    #         input = test[0]
    #         expected_output = test[1]
    #         error_message = test[2]
    #         solver = Solution()
    #         output_list = input[:]
    #         solver.nextPermutation(output_list)
    #         self.assertListEqual(expected_output, output_list, error_message)

    def test_quick_sort(self):
        tests = [
            [[5, 4, 7, 1], [1, 4, 5, 7], "quick sort - 4 elements all unique"],
            [[1], [1], "quick sort - single element"],
            [
                [54, 45, 1, 3, 54],
                [1, 3, 45, 54, 54],
                "quick sort - 5 elements with duplicates",
            ],
            [
                [1, 1, 1, 1, 2],
                [1, 1, 1, 1, 2],
                "quick sort - 5 elements with 1 unique",
            ],
            [
                [3, 2, 1],
                [1, 2, 3],
                "quick sort - 5 elements with 1 unique",
            ],
            [
                [1, 1, 1],
                [1, 1, 1],
                "quick sort - 3 elements all same",
            ],
        ]
        for test in tests:
            input = test[0]
            expected = test[1]
            error_message = test[2]
            quick_sort(input, 0, len(input) - 1)
            self.assertListEqual(input, expected, error_message)
