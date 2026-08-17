def total(bill, tip):
    total = bill * (1 + 0.01 * tip)
    total = round(total, 2)
    print(f"Please pay ${total}")

def seating(x):
    """This is a recrusive function for seating arrangements"""
    if x == 0 or x == 1:
        return 1
    else:
        return x * seating(x -1)

total(150, 20)

print(seating.__doc__)
print("Seating arrangements:", seating(5))