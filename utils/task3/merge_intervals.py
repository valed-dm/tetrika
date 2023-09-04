"""Algorithm to merge overlapped intervals"""


def merge_intervals(data: list[list[int]]) -> list[list[int]]:
    """Merges overlapped intervals"""

    if len(data) <= 1:
        return data
    output = []
    data.sort()

    current = data[0]
    output.append(current)

    for i, value in enumerate(data):
        current2 = current[1]
        next1 = value[0]
        next2 = value[1]

        if current2 >= next1:
            current[1] = max(current2, next2)
        else:
            current = data[i]
            output.append(current)

    return output
