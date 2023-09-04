"""Calculator for mutual working time"""


def intersect_intervals(l_start, l_finish, p_start, p_finish, t_start, t_finish):
    """Calculates intersected intervals"""

    mutual_time = 0
    for idx, start1 in enumerate(p_start):
        for jdx, finish2 in enumerate(t_finish):
            if start1 < finish2 and t_start[jdx] < p_finish[idx]:
                max_start = max(start1, t_start[jdx])
                min_finish = min(p_finish[idx], finish2)
                if max_start < l_start:
                    max_start = l_start
                    print(max_start)
                if min_finish > l_finish:
                    min_finish = l_finish
                    print(min_finish)
                mutual_time += min_finish - max_start
            else:
                continue

    return mutual_time
