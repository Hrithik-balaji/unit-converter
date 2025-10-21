def kg_to_pounds(kg):
    return round(kg * 2.20462, 2)

def pounds_to_kg(lb):
    return round(lb / 2.20462, 2)

print("10 kg =", kg_to_pounds(10), "lb")
print("22 lb =", pounds_to_kg(22), "kg")
