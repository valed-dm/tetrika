"""Mutual pupil, tutor lesson time counter"""

from utils.task3 import Intervals, intersect_intervals, tests


def appearance(intervals: dict[str, list[int]]) -> int:
    """Counts pure lesson's working time"""

    ivls = Intervals(intervals)
    data = ivls.get_intervals()
    mutual_time = intersect_intervals(*data)
    print("mutual time in seconds ->", mutual_time)

    return mutual_time


if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
