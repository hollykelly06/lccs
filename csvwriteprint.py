import csv
import pandas as pd

with open('myfile3.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(['Noise', 'Temp'])  
	writer.writerow([25, 10])  
	writer.writerow([24, 12])  

with open('myfile3.csv', 'r', newline='') as file:
	reader = csv.reader(file)
	for row in reader:
		print(row)


with open('myfile3.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([12, 9]) 
	writer.writerow([33, 77]) 


data = pd.read_csv('myfile3.csv')
print("\nStatistics:")
print(data.describe())
