
try:
    raise MemoryError('memory exception')
except MemoryError as e:
    print(e)