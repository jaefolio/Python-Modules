
def ft_water_reminder():
    last_water = input("Day since last watering: ")
    if (int(last_water) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
