import json #importing json library

with open('countries.json') as file:
    data = json.load(file)
    print(data)
    del data['USD']

with open('updated_countries', 'w') as file2:
    newdata = json.dump(data, file2, indent=2)
    print(newdata)

# Also we can remove the whole key value pair from the entire Json file 

with open('countries.json') as newfile:
    olddata = json.load(newfile)
    print(olddata)
    
for i in olddata:
    del olddata[i]['code']

with open('without_codefile.json', 'w') as newfile2:
    newdata = json.dump(olddata, newfile, indent=2)
    print(newdata)