#If you just want to give filename, this script file and the filename you give must be in the same directory.

file_path = str(input("From which file do you want to load this information? ")) #take file path from user
print("Data loaded.")
print("Data sorted.")
f = open(file_path, "r") #open this file to read
datas = f.readlines() #read all lines
cars_list_dict = [] #created it to save all dict and sort
for lines in range (3, len(datas), 6):
    if datas[lines].startswith('Car'):
        car = {}
        car["Make"] = datas[lines+1].split()[1]
        car["Model"] = datas[lines+2].split()[1]
        car["Year"] = datas[lines+3].split()[1]
        car["License"] =  datas[lines+4].split()[1]
        cars_list_dict.append(car)

sorted_cars_list_dict = sorted(cars_list_dict, key=lambda k: k['Year']) #sort cars
sorted_list_with_string = []
for b in sorted_cars_list_dict: #string format
    string = b["Year"] + " " + b["Make"] + " " + b["Model"] + " " + b["License"]
    sorted_list_with_string.append(string)
print("ArrayList: ", sorted_list_with_string)
