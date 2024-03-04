import pickle
from gensim.models import Word2Vec

testData = ('PhD', '4 to 9 Years', '$59K-$107K', 'Iceland', 'Full-Time', 'Automation Test Engineer', 'Test automation Test framework development Continuous integration Scripting languages (e.g., Python) Test reporting Code review')
testDataSentence = ' '.join(testData)

model = Word2Vec.load('model.bin')

# words_vec = [model.wv[word] for word in testData if word in model.wv]
# sentence_vec = sum(words_vec) / len(words_vec)

print(model.wv[testData])

# print('from model.bin', sentence_vec)

# with open('dict_sentences_vector.pkl', 'rb') as f:
#     dict_sentences_vector = pickle.load(f)

# print('from dict sentences', dict_sentences_vector[testData])

# print(dict_sentences_vector)
# for keys in dict_sentences_vector:
#     print(dict_sentences_vector[testData])

# [-2.7024404e-03  1.8877003e-03  8.2334504e-04  1.8014765e-03
#  -2.3706691e-05 -1.7443011e-03  1.8570070e-03  3.8855884e-03
#  -3.4311397e-03 -2.4841626e-03  1.3187079e-03 -1.4194023e-03
#  -1.0636441e-03  7.3787145e-04  1.0650801e-03 -6.6522788e-04
#   3.0069477e-03  1.5391913e-03 -3.3109898e-03 -4.5029698e-03
#   2.8807973e-04 -6.1083445e-04  5.3874901e-03 -6.5058976e-04
#   9.4739144e-04  2.1130795e-04 -6.9947838e-04  2.4225935e-03
#  -2.6541245e-03  1.6661873e-03  2.1484613e-03 -1.6230507e-03
#   8.3880511e-04 -2.9822828e-03 -3.4159367e-04  1.0837240e-03
#   2.0816580e-03  1.9932810e-04 -9.7261858e-05  2.6788321e-04
#   6.1583525e-04 -5.5920152e-04 -3.3494278e-03  4.4791223e-04
#   1.0954138e-03  2.3517500e-04 -4.2594620e-04  8.8486192e-04
#   5.1767169e-04  1.1624321e-03  4.5458312e-04 -1.6608611e-03
#  -1.2112027e-03 -9.1819983e-04 -1.5937412e-03 -1.2328814e-03
#   9.0981775e-04 -1.3933383e-03 -8.9618278e-04  7.3047500e-04
#  -2.9821292e-04 -3.9339633e-04  2.7367303e-03 -1.5863939e-03
#  -1.3696417e-03  2.5728089e-03  1.6780989e-03  2.6489892e-03
#  -2.4946912e-03  3.4494500e-04  9.7315590e-04  2.7600219e-03
#   1.1373147e-03  1.6635319e-03  5.8557541e-04  8.4697828e-04
#   6.2160537e-04  9.3928521e-04 -3.9174507e-04 -2.4380628e-03
#  -1.8554183e-03 -6.9124548e-04  1.3391454e-03  1.0731554e-03
#  -1.3336851e-03 -2.5599978e-03  2.3458283e-03 -1.5153501e-03
#   2.3867535e-04 -2.4496030e-05  3.0827840e-04  9.1218634e-04
#   1.1470286e-03 -1.5728157e-03  4.5758449e-03  1.1289666e-03
#   1.5744311e-03 -2.5538534e-03  6.6234247e-04  3.3601694e-04]


