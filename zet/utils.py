from copy import deepcopy


def overlay(a, **b):
  new = deepcopy(a)
  for k, v in b.items():
    new[k] = deepcopy(v)
  return new

def _to_int(n):
  try:
    return int(n)
  except ValueError as e:
    raise ValueError('must provide an integer when using -n') from e


