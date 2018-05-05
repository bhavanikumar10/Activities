prices = ["24", "13", "16000", "1400"]
price_nums = [int(price) for price in prices]
print(prices)
print(price_nums)

dog = "poodle"
letters = [letter for letter in dog]
print(letters)
print(f"We iterate over a string into a list: {letters}")

capital_letters = [letter.upper() for letter in letters]
# another way of doing the same thing as in line 11 is below in line 13,14,15
capital_letters = []
for letter in letters:
    capital_letters.append(letter.upper())
print(capital_letters)

no_o = [letter for letter in letters if letter != 'o']
print(no_o)

# another way of doing the same thing as line 17 is below
no_o = []
for letter in letters:
    if letter != 'o':
        no_o.append(letter)

june_temperature = [72,65,59,87]
july_temperature = [87,85,92,79]
august_temperature = [88,77,66,100]
temperature = [june_temperature, july_temperature, august_temperature]
# to find the lowest temperature
#short hand
lowest_summer_temperature = [min(temps) for temps in temperature]
maximum_summer_temperature = [max(temps) for temps in temperature]
print(lowest_summer_temperature[0])
print(lowest_summer_temperature[1])
print(lowest_summer_temperature[2])
print("=" * 30)

# another way of doing the same finding lowest temperature is as below
#long hand
lowest_summer_temperature = []
for temps in temperature:
    lowest_summer_temperature.append(min(temps))

print(sum(lowest_summer_temperature)/len(lowest_summer_temperature))
print(sum(maximum_summer_temperature)/len(maximum_summer_temperature))
print(lowest_summer_temperature[0])
print(lowest_summer_temperature[1])
print(lowest_summer_temperature[2])


# functions
def name(parameter):
    return "Hello " + parameter
print (name("loc"))

def average(data):
    return (sum(data1)/len(data1)) + (sum(data2)/len(data2))
# the below code will print "=" 40 times
print("=" * 40)
print(average([1,2,3,4,5],[2,3,4,5,6]))

# another way of doing it is
a = average([1,2,3,4,5],[2,3,4,5,6])
print(a)

def multiple3(a):
    if(a % 3 == 0):
        return True
    else:
        return False
print(multiple3(4))



