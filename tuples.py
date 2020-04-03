lax_coordinates = (33.9425, -118.408045)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
print(type(('Tokyo', 2003, 32450, 0.66, 8014)))
print(type(lax_coordinates))
traveler_ids = [('USA', '33434355'), ('BRA', 'CE3423444'), ('ESP', 'XDA3242344')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

print('*' * 40)

lax_coordinates = (33.9425, -118.408045)
latitude, longitude = lax_coordinates
print("Latitude: {}".format(latitude))
print("Longitude: {}".format(longitude))
latitude, longitude = longitude, latitude
print("Latitude: {}".format(latitude))
print("Longitude: {}".format(longitude))

print(divmod(20, 8))
t = (20, 8)
print(type(t))
print(divmod(*t))
quotient, remainder = divmod(*t)

print(('*' * 40))

a, b, *rest = range(5)
print(a)
print(b)
print((a, b, rest))

a, b, *body, c, d = range(5)
print((a, b, body, c, d))








