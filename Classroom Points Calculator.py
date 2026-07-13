team1 = 120
team2 = 85
team3 = 150
team4 = 95
team5 = 110

total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("Total points      :", total)
print("Average points    :", average)

stars = total

boxes = stars // 25
leftover = stars % 25

print("Reward stars      :", stars)
print("Full boxes packed :", boxes)
print("Leftover stars    :", leftover)

last_week = 500

print("Better than last week? :", total > last_week)
print("Same as last week?     :", total == last_week)
print("At least as good?      :", total >= last_week)

total += 50
print("After bonus points :", total)

total -= 20
print("After deduction    :", total)