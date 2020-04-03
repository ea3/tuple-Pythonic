lax_coordinates = (33.9425, -118.408045)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '33434355'), ('BRA', 'CE3423444'), ('ESP', 'XDA3242344')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)




