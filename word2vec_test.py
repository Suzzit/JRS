import matplotlib.pyplot as plt
from gensim.models import Word2Vec

#testing

# Load the trained Word2Vec model from the binary file
model = Word2Vec.load("word2vec_model.bin")

# Example words
wordArr = ['html', 'css', 'javascript', 'accountants', 'computer', 'networks']
vecArr = []

# Extract vectors for the words
for words in wordArr:
    vecArr.append((words, model.wv[words]))

plt.figure(figsize=(8, 6))
for word, vec in vecArr:
    plt.scatter(vec[0], vec[1], color='red', label=word)
    plt.annotate(word, (vec[0], vec[1]))

# Set axis labels and legend
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.legend()

# Show the plot
plt.show()
