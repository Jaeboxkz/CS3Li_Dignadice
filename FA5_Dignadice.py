class Vehicle:
    def __init__(self, plate_number, model):
        self.plate_number = plate_number
        self.model = model

class Driver:
    def __init__(self, name):
        self.name = name
        self.assigned_vehicle = None

    def assign_vehicle(self, vehicle):
        self.assigned_vehicle = vehicle

vehicle1 = Vehicle("ABC 1234", "Toyata Vios")
driver1 = Driver("Mr. Santos")

driver1.assign_vehicle(vehicle1)

print("Driver:", driver1.name)
print("Plate Number:", driver1.assigned_vehicle.plate_number)
print("Vehicle Model:", driver1.assigned_vehicle.model)