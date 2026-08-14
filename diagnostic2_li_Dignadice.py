def calculate_fuel(cargo_weight):
    base_weight= 50000
    total_weight = base_weight + cargo_weight 
    fuel_needed = 3 * total_weight
    return fuel_needed 
total_cargo_weight = 0
print("Philsa Cargo Loader")
print("Items available: satellite, rover, supplies.")
while True:
    item = input("Enter cargo item to load.")
    if item == "launch":
        break
    elif item == "satellite":
        weight = 1000
        total_cargo_weight += weight
        print("Satellite added to cargo(", weight ,"kg).")
        print("Total cargo weight:", total_cargo_weight,"kg")
    elif item == "rover":
        weight = 2500
        total_cargo_weight += weight
        print("Rover added to cargo(", weight ,"kg).")
        print("Total cargo weight:", total_cargo_weight,"kg")
    elif item == "supplies":
        weight = 500
        total_cargo_weight += weight
        print("Supplies added to cargo(", weight ,"kg).")
        print("Total cargo weight:", total_cargo_weight,"kg")
    else:
        print("ITEM NOT APPROVED")
    if total_cargo_weight > 10000:
        print("MAX WEIGHT REACHED")
        break

print("MISSION SUMMARY")
print("Total cargo load:", total_cargo_weight, "kg")

required_fuel = calculate_fuel(total_cargo_weight)
print("Required fuel", required_fuel, "gal")