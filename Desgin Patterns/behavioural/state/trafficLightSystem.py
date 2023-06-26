class TrafficLightState:
    def go(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()

    def caution(self):
        raise NotImplementedError()


class RedLightState(TrafficLightState):
    def go(self):
        print("Can't go now, the light is red.")

    def stop(self):
        print("Already stopped at the red light.")

    def caution(self):
        print("Changing from red to green.")
        # Change state to GreenLightState


class GreenLightState(TrafficLightState):
    def go(self):
        print("You can proceed.")

    def stop(self):
        print("Stopping at the green light.")

    def caution(self):
        print("Can't change directly from green to yellow.")


class YellowLightState(TrafficLightState):
    def go(self):
        print("Can't go now, the light is yellow.")

    def stop(self):
        print("Stopping at the yellow light.")

    def caution(self):
        print("Changing from yellow to red.")
        # Change state to RedLightState


class TrafficLight:
    def __init__(self):
        self.state = RedLightState()

    def change_state(self, state):
        self.state = state

    def go(self):
        self.state.go()

    def stop(self):
        self.state.stop()

    def caution(self):
        self.state.caution()


# Usage
traffic_light = TrafficLight()

traffic_light.stop()
# Output: Already stopped at the red light.

traffic_light.go()
# Output: Can't go now, the light is red.

traffic_light.caution()
# Output: Changing from red to green.

traffic_light.go()
# Output: You can proceed.

traffic_light.stop()
# Output: Stopping at the green light.

traffic_light.caution()
# Output: Can't change directly from green to yellow.
