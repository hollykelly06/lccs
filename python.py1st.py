import csv 
csvfile = open("myfile.csv","x")
print("file created")

csvwriter = csv.writer(csvfile)
csvwriter.writerow(["Name","Age", "city"])
print("columes created")

csvwriter.writerow(["alice","25","New York"])
print("data created")

csvfile.close()
print("closed")