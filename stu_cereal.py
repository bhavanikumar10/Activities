import os
import csv

# setting the path for the csv file
cereal_csv_path = os.path.join(".","Resource","cereal.csv")

# opening the file cereal.csv, space as a newline delimiter
with open(cereal_csv_path, newline = "") as csvfile:

    #  reading through the cereal.csv filer
        csv_reader = csv.reader(csvfile, delimiter = ",")
        for row in csv_reader:
            if(float(row[7]) >= 5):
                print(row)






