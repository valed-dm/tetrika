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
