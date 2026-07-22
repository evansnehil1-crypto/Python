print("=======================================")
print("      Welcome To Holiday Planner!      ")
print("=======================================")

print("Step 1: Pick your destination")
print(" 1 - Beach")
print(" 2 - Mountains")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2: Pick your activity")
    print(" 1 - Swimming")
    print(" 2 - Boat Ride")
    print()

    activity = int(input("Enter 1 or 2: "))

    if activity == 1:
        print("You picked : Swimming")
        print("Duration : 2 hours")
        print("Best for : Relaxation and fun")
    else:
        print("You picked : Boat Ride")
        print("Duration : 1 hour")
        print("Best for : Sightseeing")

elif choice == 2:
    print("Step 2: Pick your activity")
    print(" 1 - Hiking")
    print(" 2 - Camping")
    print()

    activity = int(input("Enter 1 or 2: "))

    if activity == 1:
        print("You picked : Hiking")
        print("Duration : 4 hours")
        print("Best for : Adventure")
    else:
        print("You picked : Camping")
        print("Duration : Overnight")
        print("Best for : Nature lovers")

else:
    print("That's not a valid choice.")
    print("Please enter 1 for Beach or 2 for Mountains.")

print()
print("=======================================")
print("     Your holiday plan is ready!       ")
print("          Have a great trip!           ")
print("=======================================")