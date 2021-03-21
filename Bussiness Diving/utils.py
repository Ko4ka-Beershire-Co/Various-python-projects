import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

stopwords = stopwords.words("english")

h = ['Had', 'the', 'game', 'before', 'and', 'loved', 'it', 'but', 'after', 'the', 'last', 'update', 'the', 'game',
     'will', 'not', 'load.', 'It', 'starts', 'and', 'at', 'the', 'Niantic', 'screen', 'it', 'force', 'closes', 'and',
     'I', 'had', 'get', 'sent', 'back', 'to', 'my', 'home', 'screen.', 'Samsung', 'note', '4",']

words_to_ignore = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during',
                   'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
                   'such', 'into', 'of',
                   'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
                   'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me',
                   'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both',
                   'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and',
                   'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
                   'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where',
                   'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 'it', 'being', 'if',
                   'theirs',
                   'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

j = len(h)
i = 0
while i < j:
    z = h[i]
    if z.lower() in words_to_ignore:
        print(z)
        h.pop(i)
        j -= 1
    else:
        i += 1

print(h)

def corpus_counter(corpus_file, top):
    with open(corpus_file, 'r+', encoding='utf-8') as c:
        data_set = c.read()
        split_it = data_set.split()

        # input values and their respective counts.
        most_occur = Counter(split_it).most_common(top)

        print(most_occur)
