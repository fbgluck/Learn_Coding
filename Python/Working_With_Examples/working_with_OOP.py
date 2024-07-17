# print ("Everything is Python is an Object that was created from a class")
# print(f"None: {type(None)}")
# print(f"Bool :{type(True)}")
# print(f"Integer :{type(5)}")
# print(f"Float :{type(5.5)}")
# print(f"String :{type('WooHoo')}")
# print(f"List: {type([1,2,3])}")
# print(type(
#   {
#   'letters':('a','b','c')
#   }))
# print(f"Set: {type({'value',6,7})}")
print (30*'-')
# #Classes are named using Camelback notation
class SRTCTeacher: # Create the class
  ## Code for the class goes here
  pass
## ---------------------
# Create the object called obj_MrGluck from the class called SRTCTeacher
# # Instantiate the class to create an object
# obj_MrGluck = SRTCTeacher()
# print(f"obj_MrGluck: {type(obj_MrGluck)}")
# # # Create more objects from this class
# obj_MrJones = SRTCTeacher()
# obj_MsWilliams = SRTCTeacher()
# print(45*'-')


# ### More Details about how to create classes and objects

class DeliveryDroneTypeA: 
   # def in a class is used to create a method
   # the __init__ method (a dunder method) is called as soon as the class is used to instantiate an object. It is often called a "constructor" method.
   # self refers to the class itself. It is always the first parameter when defining a method
   ## Define the method called __init__
  # Note default value for drone_speed
  # This is the constructor. Good practice is to check to see if all the correct parameter were passed.
  def __init__ (self,flight_id,drone_speed=4):
    # give the object some properties (attributes)
    # These are dynamic attributes. They can be changed
    self.flight_id = flight_id
    self.drone_speed = drone_speed
  #define a property of the object that can not be changed
  fuel_type="JetA" 
  # Define a method called drone_launch
  def drone_launch(self):
    if self.drone_speed >3:
      self.fly_time_minutes = 5
    elif self.drone_speed == 3:
      self.fly_time_minutes=10
    else:
      self.fly_time_minutes=20
    print(f"Launching {self.flight_id} flying at {self.drone_speed} MPH.\nEstimated fly time is {self.fly_time_minutes} minutes")
    print (45*'-')
    return self.fly_time_minutes
# # ###############
# # Show information on this object
# help(DeliveryDroneTypeA)
print (45*'-')

# ### The Program really begins here....

# Set current fuel cost
fuel_cost=.342
#Create four new drones and launch them
drone0 = DeliveryDroneTypeA('a12345',5)
drone1 = DeliveryDroneTypeA('x43312',3)
drone2 = DeliveryDroneTypeA('Y77834',2)
drone3 = DeliveryDroneTypeA('Z66555')
## Show some info about the objects just instantiated
# print("\n")
# print (drone0)
# print (drone1)
# print (drone2)
# print (drone3)
# print (45*'-')
# print("\n")

# Launch four drones and get total fly times
fly_time_0=drone0.drone_launch()
fly_time_1=drone1.drone_launch()
fly_time_2=drone2.drone_launch()
fly_time_3=drone3.drone_launch()
print(f"Drone flight {drone0.flight_id} is using {drone1.fuel_type}")
print(f"Drone flight {drone1.flight_id} is using {drone1.fuel_type}")
print(f"Drone flight {drone2.flight_id} is using {drone2.fuel_type}")
print(f"Drone flight {drone3.flight_id} is using {drone3.fuel_type}")
total_fly_time = fly_time_0 + fly_time_1 + fly_time_2 + fly_time_3
total_fuel_cost = total_fly_time * fuel_cost
#Print total fly time
print(f"Drone launch is complete.\nTotal mission time is {total_fly_time} minutes")
print(f"Estimated fuel cost is {total_fuel_cost}")
