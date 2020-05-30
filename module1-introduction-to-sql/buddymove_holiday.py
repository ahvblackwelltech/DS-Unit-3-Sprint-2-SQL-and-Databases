import pandas as pd 
import sqlite3

# Read Data
df = pd.read_csv('buddymove_holidayiq.csv')

print(df.shape)
print(df.head(5))

con = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('review', con)