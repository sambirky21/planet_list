planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(1,"Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

print(planet_list)

# sliceObject = slice(0, 1, 2, 3)
# rocky_planets = planet_list[sliceObject]

# for rp in range(0,5):
#     if rp in planet_list:
#         slice(planet_list) == rocky_planets

rocky_planets = planet_list[0:4]

del planet_list[8]