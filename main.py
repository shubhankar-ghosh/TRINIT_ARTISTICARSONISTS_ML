import rainfall_table as rt
import random_forest_regressor as rfr
import crop_rec as cr


def get_date():
    print("Enter a date (dd/mm/yyyy)")
    date = input()
    return date


def get_location():
    print("Enter a location name")
    location = input()
    location = location.upper()
    return location


# MAIN CODE
date = get_date()
location = get_location()

print("Your inputted date = ", date)
print("Your inputted location = ", location)

print("Annual rainfall of ", location, "is", rt.annual_rainfall(location))
print("Set of total rain data in a year -> ", rt.total_rainfall(location))

print(rfr.model([[i] for i in range(0, len(rt.total_rainfall(location)))], rt.total_rainfall(location)))
rain = rfr.model([[i] for i in range(0, len(rt.total_rainfall(location)))], rt.total_rainfall(location))

print("According to our ML prediction, the crops that can grow are -> ", cr.get_crop(rain))


