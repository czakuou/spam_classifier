import pandas as pd
import os

# list of files with names
filenames = next(os.walk('data/names'))[2]
name_dir = [next(os.walk('data/names'))[0] + '/' + filenames[i] for i in range(len(filenames))]

# dataframe with names of files
df = pd.read_csv(name_dir[0])
print(df)

