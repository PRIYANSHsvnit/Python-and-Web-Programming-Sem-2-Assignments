import numpy as np

arr = np.array(["Jay", "Veeru", "Gabbar", "Thakur", "RamLal"])

centered = np.char.center(arr, 15, fillchar='_')
left_justified = np.char.ljust(arr, 15, fillchar='_')
right_justified = np.char.rjust(arr, 15, fillchar='_')

print("Original Array = ")
print(arr)

print("\nCentered = ")
print(centered)

print("\nLeft-Justified = ")
print(left_justified)

print("\nRight-Justified = ")
print(right_justified)