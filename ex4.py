# cars available
cars = 100
# spaces in each car
space_in_a_car = 4
# Drivers available
drivers = 30
# Passengers requiring transport
passengers = 90
# Cars that won't be available
cars_not_driven = cars - drivers
# Cars available
cars_driven = drivers
# total capacity
carpool_capacity = cars_driven * space_in_a_car
# average of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")