import pandas as pd
import os

# get file names and export it to csv files
for r, d, f in os.walk('data'):
    for dirs in d:
        data = pd.DataFrame()
        data[dirs] = pd.Series(next(os.walk(f'..\data\{dirs}'))[2])
        data[:-1].to_csv(f'{dirs}_names.csv', sep=';', encoding='utf-8', index=False)
        