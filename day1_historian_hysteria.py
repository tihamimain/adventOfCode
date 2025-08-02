from collections import Counter
# Day 1: Historian Hysteria

# The problem involves sorting two lists.
# The lists are of length 6, which is relatively small.
# For sorting, we can use Merge Sort with a time complexity of O(n log n).
# Alternatively, Python's built-in sort function (Timsort) can be used. 
# Timsort combines Insertion Sort and Merge Sort, and has a best-case time complexity of O(n) 
# when the list is already sorted or nearly sorted, 
# and a worst-case time complexity of O(n log n).

filenames = "puzzle_input.txt"
with open(filenames, "r") as file:
    data = [line.strip().split() for line in file.readlines()]

collumn1 = [int(item[0]) for item in data]
collumn2 = [int(item[1]) for item in data]

collumn1.sort()
collumn2.sort()


total_distance = sum(abs(a-b) for a, b in zip(collumn1, collumn2))
print("total distance", total_distance)
# total distance 1666427

#--- Part Two ---

counter = Counter(collumn2)     #count frequency of each number 
similarity_score = sum(x * counter[x] for x in collumn1)
print("similarity score", similarity_score)
# similarity score 24316233