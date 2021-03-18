import pandas as pd
import os
import nltk
from nltk.tokenize import word_tokenize

# list of files with names
filenames = next(os.walk('data/names'))[2]
name_dir = [next(os.walk('data/names'))[0] + '/' + filenames[i] for i in range(len(filenames))]

# dataframe with names of files
df = pd.read_csv(name_dir[0])
# get file name
fil = df['easy_ham_2'][0]

# read file
data = open(f'data/{df.columns[0]}/{fil}', "r")
text = data.readlines()

# get the context of an email
words = []
with open(f'data/{df.columns[0]}/{fil}', "r") as myFile:
    for num, line in enumerate(myFile, 1):
        # print(line[0:1].strip().lower())
        if not line.strip():
            data_f = text[num:-7]
            for i in data_f:
                # print(i)
                words.append(i.split())

# tokenize words
merged_words = []
for w in words:
    merged_words += w
    
print(merged_words)
