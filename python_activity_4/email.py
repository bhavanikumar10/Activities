import os
import csv

# setting the path for the csv file
filepath = os.path.join("employees.csv")

new_employee_data = []

# Read datat into a dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    #print(reader)
    for row in reader:
        #print(row)
        first_name = row["First Name"]
        last_name = row["Last Name"]
        email = first_name + "." + last_name + "@example.com"
        print(email)
        # option 2
        # email = f"{first_name}.{Last_name}@example.com"
        new_employee_data.append({
            "first_name": first_name,
            "last_name": last_name,
            "ssn": row["ssn"],
            "email":email
        })
print(new_employee_data)

# Grab the filename from the original path
print(filepath)
# _ means "I dont care about everything else, I just want the filename employee"
#_, filenamereaderath)
print(_)
print(filename)

csvpath = os.path.join( ".", "output", filename)
with open(csvpath, "w") as csvfile:
    field_names = ["First name", "Last name", "SSN", "email"]
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writheader()
    writer.writerow(new_employee_data)