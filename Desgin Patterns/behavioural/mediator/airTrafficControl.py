"""In an air traffic control system, the Mediator pattern can be used to coordinate the communication between various
aircraft and the control tower. The mediator acts as the central authority that receives information from aircraft
and provides instructions and updates to them. """


class ControlTowerMediator:
    def __init__(self):
        self.aircrafts = []

    def register_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def receive_location_update(self, aircraft, location):
        # Process location update and provide instructions if necessary
        # ...
        pass


class Aircraft:
    def __init__(self, identifier, control_tower):
        self.identifier = identifier
        self.control_tower = control_tower

    def send_location_update(self, location):
        self.control_tower.receive_location_update(self, location)


# Usage
control_tower = ControlTowerMediator()

aircraft1 = Aircraft("Flight 123", control_tower)
aircraft2 = Aircraft("Flight 456", control_tower)
aircraft3 = Aircraft("Flight 789", control_tower)

control_tower.register_aircraft(aircraft1)
control_tower.register_aircraft(aircraft2)
control_tower.register_aircraft(aircraft3)

aircraft1.send_location_update("Latitude: 40.7128, Longitude: -74.0060")
