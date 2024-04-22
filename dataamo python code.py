import statistics
import pandas

df = pandas.read_csv('myfile3.csv')
amount1 = df['amount1']
print (amount1)

amount2 = df['amount2']
print (amount2)

amount3 = df['amount3']
print (amount3)
mean_value = round(statistics.mean(amount1),2)
print (mean_value)