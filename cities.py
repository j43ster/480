#!/usr/bin/python3

class City(object):
   name = ""
   state = ""
   pop_est = 0
   census = 0
   population_change = ""
   area = ""
   population_density = ""
   location = ""

   def __init__(self, name, state, pop_est, census, population_change, area, population_density, location):
      self.name = name
      self.state = state
      self.pop_est = pop_est
      self.census = census
      self.population_change = population_change
      self.area = area
      self.population_density = population_density
      self.location = location 

def make_city(name, state, pop_est, census, population_change, area, population_density, location):
   city = City(name, state, pop_est, census, population_change, area, population_density, location)
   return city

Cities = {}
#Cities["New York"] = make_city(name, state, pop_est, census, population_change, area, population_density, location):
Cities["New York"] = make_city("New York", "New York", 8405837, 8175133, "+2.82%", "302.6 sq mi", "27,012 per sq mi", "40.6643°N 73.9385°W")
Cities["Los Angeles"] = make_city("Los Angeles", "California", 3884307, 3792621, "+2.42%", "468.7 sq mi", "11,842 per sq mi", "34.0194°N 118.4108°W")
Cities["Chicago"] = make_city("Chicago", "Illinois", 2718782, 2695598, "+0.86%", "227.6 sq mi", "11,842 per sq mi", "41.8376°N 87.6818°W")
Cities["Houston"] = make_city("Houston", "Texas", 2195914, 2100263, "+4.55%", "599.6 sq mi", "3,501 per sq mi", "29.7805°N 95.3863°W")
Cities["Philadelphia"] = make_city("Philadelphia", "Pennsylvania", 1553165, 1526006, "+1.78%", "134.1 sq mi", "11,379 per sq mi", "40.0094°N 75.1333°W")
Cities["Phoenix"] = make_city("Phoenix", "Arizona", 1513367, 1445632, "+4.69%", "516.7 sq mi", "2,798 per sq mi", "33.5722°N 112.0880°W")
Cities["San Antonio"] = make_city("San Antonio", "Texas", 1409019, 1327407, "+6.15%", "460.9 sq mi", "2,880 per sq mi", "29.4724°N 98.5251°W")
Cities["San Diego"] = make_city("San Diego", "California", 1355896, 1307402, "+3.71%", "325.2 sq mi", "4,020 per sq mi", "32.8153°N 117.1350°W")
Cities["Dallas"] = make_city("Dallas", "Texas", 1257676, 1197816, "+5.00%", "340.5 sq mi", "3,518 per sq mi", "32.7757°N 96.7967°W")
Cities["San Jose"] = make_city("San Jose", "California", 998537, 945942, "+5.56%", "176.5 sq mi", "5,359 per sq mi", "37.2969°N 121.8193°W")

print("|     City     |    State     | 2013 estimate | 2010 Census | Change | 2013 land area | 2013 population densisty |      Location        |")

for name in sorted(Cities, key= lambda name: Cities[name].pop_est, reverse = True):
   city = Cities[name]
   print("| " + name.rjust(12) + " | " + city.state.rjust(12) + " |    " + str(city.pop_est).rjust(7) + "    |   " + str(city.census).rjust(7) + "   | " + city.population_change + " |  " + city.area + "   |     " + city.population_density.rjust(16) + "     | " + city.location.ljust(20) + " |")
