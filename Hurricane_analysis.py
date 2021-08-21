# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def convert_damage(damage):
  new_damage =[]
  for i in damage:
    if i != "Damages not recorded":
      new_i = i[:-1]
      unit_i = i[-1]
      new_i =float(new_i)*conversion.get(unit_i)
      new_damage.append(new_i)
    else:
      new_damage.append(i)
  return new_damage
new_damages= convert_damage(damages)

# 2 
# Create a Table
keys =["Name", "Month", "Year", "Max Sustained Wind", "Areas Affected", "Damage", "Death"]
# Create and view the hurricanes dictionary
def hurricane_inf(name):
  idx = names.index(name)
  values =[name, months[idx], years[idx],max_sustained_winds[idx],areas_affected[idx], new_damages[idx], deaths[idx] ]
  dict_values = dict(zip(keys, values))
  return dict_values


# 3
# Organizing by Year
unique_years = list(set(years))
# create a new dictionary of hurricanes with year and key
def hurricane_year(year):
  idxs = [index for index, value in enumerate(years) if value==year]
  hurricane_in_year = []
  for i in idxs:
    hurricane_in_year.append(hurricane_inf(names[i]))
  return hurricane_in_year



# 4
# Counting Damaged Areas
from collections import Counter
def union_list(list_x):
  final_list=[]
  for x in list_x:
    final_list +=x
  final_list = dict(Counter(final_list))
  sorted_final_list = dict(sorted(final_list.items(), key=lambda x: x[1], reverse=True))
  return sorted_final_list
# create dictionary of areas to store the number of hurricanes involved in


# 5 
# Calculating Maximum Hurricane Count
hurricane_count = union_list(areas_affected)
# find most frequently affected area and the number of hurricanes involved in
area, times_affected = list(hurricane_count.items())[0]
print('The area of {0} was the most frequently affected {1} times'.format(area, times_affected))

# 6
# Calculating the Deadliest Hurricane
import numpy as np
def stat_func(metric,bins):
  metric_array = np.array([float(i) for i in metric if not isinstance(i, str)])
  indx_max = np.argmax(metric_array)
# find highest mortality hurricane and the number of deaths
  highest_value_hurricane = names[indx_max]
  max_value = metric_array[indx_max]
  # 7
  # Rating Hurricanes by Mortality
  scale = list(range(len(bins)+1))
  values = [ [] for _ in range(len(bins)+1) ]
  hurricane_scale_metric = dict(zip(scale,values))
  # categorize hurricanes in new dictionary with mortality severity as key
  for i in range(len(metric_array)):
     
    metric_value = metric_array[i]
    metric_scale = np.digitize(metric_value, bins)
    hurricane_scale_metric.get(metric_scale).append(names[i])
  return highest_value_hurricane,max_value,hurricane_scale_metric


bins_death = np.array([0,100,500,1000,10000])

stat_death = stat_func(deaths, bins_death)
print("the deadliest hurricane is {0} with {1} deaths".format(stat_death[0], stat_death[1]))

print("the death rating is as blw \n{0} ".format(stat_death[-1]))
# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
bins_damage = np.array([i for i in damage_scale.values()])
stat_damage = stat_func(new_damages, bins_damage)
# categorize hurricanes in new dictionary with damage severity as key
print("the highest damage hurricane is {0} with {1} deaths".format(stat_damage[0], stat_damage[1]))

print("the damage rating is as blw \n{0} ".format(stat_damage[-1]))