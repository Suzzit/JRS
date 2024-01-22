from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import pandas as pd
from nltk import word_tokenize
import nltk
nltk.download('punkt')

input_file_path = '../data/traindata.csv'
df = pd.read_csv(input_file_path)
sentences = df['Job Description'].tolist()
sentencesArr = []
for sentence in sentences:
    sentencesArr.append([sentence.split()])

tokenized_sentences = [word_tokenize(description.lower()) for description in sentences]

#Create Word2Vec model
model = Word2Vec(tokenized_sentences, vector_size=10, window=50, min_count=1, workers=4)


model.save("word2vec_model.bin")