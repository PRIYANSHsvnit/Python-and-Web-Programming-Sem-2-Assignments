import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

supper = s.str.upper()
print("\nUpper case =\n\n", supper)

slower = s.str.lower()
print("\n\nLower case =\n\n", slower)

slength = s.str.len()
print("\n\nLength of each string =\n\n", slength)