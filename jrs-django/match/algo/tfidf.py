import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv('../data/dice_com-job_us_sample.csv')
df1.head()
df1.info()
df1=df1.dropna()
df1.shape
df1['jobdescription'].head()

from sklearn.feature_extraction.text import TfidfVectorizer

df1['combined_text'] = df1['employmenttype_jobstatus'] + ' ' + df1['jobdescription'] + ' ' + df1['joblocation_address'] + df1['shift'] + ' ' + df1['skills']
tdif=TfidfVectorizer(stop_words='english')
df1['combined_text']=df1['combined_text'].fillna('')

tdif_matrix=tdif.fit_transform(df1['combined_text'])
tdif_matrix.shape

from sklearn.metrics.pairwise import linear_kernel

cosine_sim=linear_kernel(tdif_matrix,tdif_matrix)
indices=pd.Series(df1.index, index=df1['jobtitle']).drop_duplicates()

dd = []
def get_recommendation(title, skills=[], cosine_sim=cosine_sim):
    # Concatenate title and description
    input_text = title + ' ' + ' '.join(skills)

    # Transform input text using the TF-IDF vectorizer
    input_matrix = tdif.transform([input_text])

    # Compute cosine similarity between input and all other job descriptions
    cosine_similarities = linear_kernel(input_matrix, tdif_matrix).flatten()

    # Get indices of similar job descriptions
    similar_indices = cosine_similarities.argsort()[:-16:-1]  # Top 15 similar indices

    # Return the titles of similar jobs
    dd = df1.iloc[similar_indices].to_dict()

    return dd

recommended = get_recommendation('python', ['Javascript', 'Java', 'css'])

data = []
for key in recommended['jobtitle'].keys():
    data.append([recommended['jobtitle'][key], recommended['joblocation_address'][key], recommended['skills'][key]])

for jobs in data:
    print(jobs)