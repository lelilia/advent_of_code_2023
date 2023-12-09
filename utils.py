def get_input_lines(filename):
    with open(filename, "r") as f:
        return f.readlines()


def get_input(filename):
    with open(filename, "r") as f:
        return f.read()


def asserting(query, expected):
    assert (result := query) == expected, f"Expected {expected}, got {result}"


def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i = i + 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    assert (result := prime_factorization(3)) == [3], f"Expected [3] got {result}"
    assert (result := prime_factorization(4)) == [2, 2], f"Expected [2, 2] got {result}"
    assert (result := prime_factorization(9)) == (
        expected := [3, 3]
    ), f"Expected {expected} got {result}"
    assert (result := prime_factorization(25)) == (
        expected := [5, 5]
    ), f"Expected {expected} got {result}"
    assert (result := prime_factorization(200)) == (
        expected := [2, 2, 2, 5, 5]
    ), f"Expected {expected} got {result}"
