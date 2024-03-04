import pandas as pd
from gensim.models import Word2Vec
import numpy as np
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import json

# Replace 'your_large_file.csv' with the actual path to your CSV file
input_file_path = '../data/traindata.csv'

# Use the 'usecols' parameter to specify the columns you want to read
df = pd.read_csv(input_file_path)

qualificationsList = df['Qualifications'].to_list()
experienceList = df['Experience'].to_list()
salaryList = df['Salary Range'].to_list()
countryList = df['Country'].to_list()
workTypelList = df['Work Type'].to_list()
rolesList = df['Role'].to_list()
skillsList = df['skills'].to_list()

text_tuple = zip(qualificationsList, experienceList, salaryList, countryList, workTypelList, rolesList, skillsList)