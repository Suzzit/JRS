import pandas as pd
from gensim.models import Word2Vec

# Replace 'your_large_file.csv' with the actual path to your CSV file
input_file_path = '../data/traindata.csv'
output_file_path = '../data/traindata_cleaned.csv'

# # Specify the qualifications you're interested in
target_qualifications = ['BCA', 'M.Tech', 'MCA', 'M.Com', 'B.Com', 'B.Tech', 'BBA']

# Specify the columns you want to extract
columns_to_extract = ['Job Description', 'Qualifications']

# Use the 'usecols' parameter to specify the columns you want to read
df = pd.read_csv(input_file_path)

# Filter the DataFrame based on the specified qualifications
filtered_df = df[df['Qualifications'].isin(target_qualifications)]

qualificationsList = filtered_df['Qualifications'].to_list()
experienceList = filtered_df['Experience'].to_list()
salaryList = filtered_df['Salary Range'].to_list()
countryList = filtered_df['Country'].to_list()
workTypelList = filtered_df['Work Type'].to_list()
rolesList = filtered_df['Role'].to_list()
skillsList = filtered_df['skills'].to_list()

concaneted = zip(qualificationsList, experienceList, salaryList, countryList, workTypelList, rolesList, skillsList)
sentences = []

for sentencesArr in concaneted:
    sentences.append(' '.join(sentencesArr))

print(sentences[0])
model = Word2Vec(sentences, vector_size=50, window=50, min_count=1, workers=4)

for snt in sentences:
    word_vectors = [model.wv[word] for word in snt if word in model.wv]
    print(word_vectors)

model.save("word2vec_model.bin")

# for q,e,s,c,w,r,s in concaneted:
#     print(q)

# # Save the extracted columns to a new CSV file
# filtered_df.to_csv(output_file_path, index=False)
