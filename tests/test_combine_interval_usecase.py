from unittest import TestCase
from usecases.combine_intervals import combine_intervals_usecase, combine_overlapping_intervals


class CombineListTest(TestCase):
    def test_combine_overlapping_intervals_with_valid_interval_list(self):
        ordered_interval_list = [
            (1, 5), 
            (2, 6), 
            (9, 16), 
            (15, 22), 
            (22, 30), 
            (31, 45)
        ]

        expected_return_value = [
            (1, 6),
            (9, 30),
            (31, 45)
        ]

        actual_return_value = combine_overlapping_intervals(ordered_interval_list)
        assert actual_return_value == expected_return_value
