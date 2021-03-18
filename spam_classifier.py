import pandas as pd
import os

# list of files with names
filenames = next(os.walk('data/names'))[2]
name_dir = [next(os.walk('data/names'))[0] + '/' + filenames[i] for i in range(len(filenames))]

# dataframe with names of files
df = pd.read_csv(name_dir[0])
# get file name
fil = df['easy_ham_2'][0]

# read file
data = open(f'data/{df.columns[0]}/{fil}', "r")
print(data.read())
