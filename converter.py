def kg_to_pounds(kg):
    return round(kg * 2.20462, 2)

def pounds_to_kg(lb):
    return round(lb / 2.20462, 2)

print("10 kg =", kg_to_pounds(10), "lb")
print("22 lb =", pounds_to_kg(22), "kg")

def km_to_miles(km):
    return round(km * 0.621371, 2)

def miles_to_km(miles):
    return round(miles / 0.621371, 2)

print("5 km =", km_to_miles(5), "miles")
print("3 miles =", miles_to_km(3), "km")
