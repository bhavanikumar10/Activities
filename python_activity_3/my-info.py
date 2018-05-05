bhavani = {
    "name": "Bhavani",
    "age": "16",
    "hobbies": ["reading","music","research"],
    "wake_up": {"Mon": "5:00", "Tues": 5, "Sat":7}
}
print(bhavani)
print("Hello I am " + bhavani["name"]+ "my age is "+ bhavani["age"])

for hobby in bhavani["hobbies"]:
    print(hobby)


for time in bhavani["wake_up"].values():
    #print(time+" "+str(bhavani["wake_up"][time]))
    print(time)
for key,values in bhavani["wake_up"].items():
    print(key)
    print(values)
