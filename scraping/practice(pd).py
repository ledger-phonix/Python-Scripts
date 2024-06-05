import pandas as pd
from rich import print

file = pd.read_csv('Data/saxo-books.csv')

# print(file.info())

# print(file.head())
# print(file.tail())

# print(file[file['Rank']< 10])

# print(file[file['Rating'] == 5.0])
authors = ['Emilie Melgaard Jacobsen', 'Preben Kirkegaard Hansen', 'Naleea Landmann']
# print(file[file['AuthorName'].isin(authors)] )

print(file.set_index('Language'))