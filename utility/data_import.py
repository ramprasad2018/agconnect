import pandas as pd
from sqlalchemy import create_engine

# Set up the database connection
engine = create_engine('sqlite:///../db.sqlite3')




# Read the Excel file into a Pandas dataframe
df = pd.read_excel('./crop.xlsx', sheet_name='Sheet1')

# Write the dataframe to a new table in the database
df.to_sql('crop1', con=engine, if_exists='replace', index=False)
