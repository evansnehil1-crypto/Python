print("=======================================")
print("       Welcome To Ride Builder!        ")
print("=======================================")


print("Step 1:Pick your vehicle")
print(" 1 - Bike")
print(" 2 - Car")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2: Pick your bike type")
    print(" 1 - Scooty")
    print(" 2 - Mountain Bike")
    print()

    bike_type = int(input("Enter 1 or 2: "))

    if bike_type == 1:
        print("You picked : Scooty")
        print("Top speed : 80 km/h")
        print("Best for : City roads")
    else:
        print("You picked : Mountain Bike")
        print("Top speed : 40 km/h")
        print("Best for : off-road trails")
        
elif choice == 2:

    print("Step 2: Pick your car type")
    print(" 1 - Sedan")
    print(" 2 - Suv")
    print()

    car_type = int(input("Enter 1 or 2: "))

    if car_type == 1:
        print("You picked : Sedan")
        print("Seats : 5 passengers")
        print("Best for : Famaly trips")
    else:
        print("You picked : Suv")
        print("Seats : 7 passengers")
        print("Best for : off-road adventures")
else:
    print("Thats not a valid choice.")
    print(" Please enter 1 for Bike or 2 for a Car.")

print()
print("=======================================")
print("      Your custom ride is ready!       ")
print("      Enjoy the journey!               ")
print("=======================================")
