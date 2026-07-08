field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest      :", total, "kg")
print("Average per field  :", average, "kg")

price_per_kg = 15
earnings = total * price_per_kg

print("Total earnings     :RS.", earnings)

bags = total // 25
leftover = total % 25

print("Full bags packed   :", bags)
print("Leftover grain     :", leftover, "kg")

last_year = 500

print("Better that last year?  :", total > last_year)
print("Same as last year?      :", total == last_year)
print("At least as good?       :", total >= last_year)

print("After bonus crop   :", total, "kg")

print("After seed reserve :", total, "kg")

print("Final bags packed  :", bags)
