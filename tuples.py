from collections import namedtuple

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

print(('*' * 40))

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))

print('*' * 40)
print('Namedtuples Example')

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key, value, in delhi._asdict().items():
    print(key + ':', value)

l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)


l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
tuple1 = (1, 2, 3)
print(id(tuple1))
tuple1 *= 2
print(tuple1)
print(id(tuple1))























