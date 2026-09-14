box1 = {"chips", "apple", "sandwich", "juice", "chips"}
box2 = {"juice", "sandwich", "cookie", "water", "cookie"}

print("Snack box 1: ", box1)
print("Snack box 2: ", box2)

box1.add("banna")
print("Snack box 1 after adding banna: ", box1)

shared_snacks = box1.intersection(box2)
print("Snacks in both boxes: ", shared_snacks)

import array as arr
snack_counts = arr.array('i', [3, 5, 2, 4])

print("Snack counts array: ", snack_counts)

snack_counts.insert(0, 1)
snack_counts.append(6)

print("Snack counts after adding items: ", snack_counts)

count_of_5 = snack_counts.count(5)
print("Number of times 5 appears: ", count_of_5)

snack_counts.reverse()
print("Reversed snack counts array:", snack_counts)

print("")
print("===== SCHOOL SNACK COUNTER =====")
print("Snack Box 1:", box1)
print("Snack Box 2:", box2)
print("Shared snacks:", shared_snacks)
print("Snack counts:", snack_counts)
print("================================")