"""Prepares intervals data"""

from dataclasses import dataclass, field

from utils.task3 import merge_intervals


def get_merged_intervals(start, finish):
    """Merges overlapping intervals"""

    intervals_to_merge = list(map(list, zip(start, finish)))
    merged = merge_intervals(intervals_to_merge)
    unpacked = [j for i in merged for j in i]
    merged_start = unpacked[::2]
    merged_finish = unpacked[1::2]

    print(merged_start)
    print(merged_finish)

    return merged_start, merged_finish


@dataclass
class Intervals:
    """Processes input data"""

    intervals: dict[str, list[int]]
    lesson: list[int] = field(default_factory=list)
    pupil: list[int] = field(default_factory=list)
    tutor: list[int] = field(default_factory=list)

    def get_intervals(self):
        """Prepares input data for further processing"""

        l_start = self.lesson[0]
        l_finish = self.lesson[1]
        p_start = self.pupil[::2]
        p_finish = self.pupil[1::2]
        t_start = self.tutor[::2]
        t_finish = self.tutor[1::2]
        p_start, p_finish = get_merged_intervals(p_start, p_finish)

        return l_start, l_finish, p_start, p_finish, t_start, t_finish

    def __post_init__(self):
        self.lesson = self.intervals["lesson"]
        self.pupil = self.intervals["pupil"]
        self.tutor = self.intervals["tutor"]
