import re

_int_re = re.compile(r'-?\d+')


def extract_ints(s: str) -> list[int]:
  """
  >>> extract_ints("Button A: X+94, Y+34")
  [94, 34]
  >>> extract_ints("Prize: X=8400, Y=5400")
  [8400, 5400]
  >>> extract_ints("p=6,3 v=-1,-3")
  [6, 3, -1, -3]
  """
  return [int(m) for m in _int_re.findall(s)]


if __name__ == '__main__':
  import doctest
  doctest.testmod()
