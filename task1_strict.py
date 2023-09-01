import inspect


def strict(f):
    def wrapper(*args):
        idx = 0
        data = [*args]
        f_sig = inspect.signature(f)

        for k, v in f_sig.parameters.items():
            a = data[idx]
            if not isinstance(a, v.annotation):
                raise TypeError(
                    f"arg {k}={a} {type(a)} does not match func signature type {v}"
                )
            idx += 1

        return f(*args)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
