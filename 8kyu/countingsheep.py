from functools import reduce

def count_sheeps(sheep):
  # TODO May the force be with you
  return reduce(lambda x, y: x+1 if y else x, sheep, 0)