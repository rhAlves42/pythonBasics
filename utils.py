def checkType(value, type):
  try:
    type(value)
  except ValueError:
    return False
  else:
    return isinstance(type(value), type)
