class Vehicle:
    def __init__(self, speed):
        if speed > 240:
            raise Exception("Not Allowed")
        self.speed = speed
    
    def __del__(self):
        print("Release resources")
        
# creating an object
car = Vehicle(250)
# to delete the object explicitly
del car