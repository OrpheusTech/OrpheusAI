import csv


"""This Function returns a list of all data from specified column"""
def getuniquevalues(filename,datatype):
  values = []
  with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # This assumes the first row contains headers
    for row in reader:
        if row[datatype] not in values: #This makes sure that there are no duplicates
          values.append(row[datatype])
    return values
  
