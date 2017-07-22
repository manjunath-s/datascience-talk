import re, math
from collections import Counter
from nltk.corpus import stopwords

WORD = re.compile(r'\w+')
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # remove it if you need punctuation
print(len(stop_words))

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     #print(WORD)
     words = WORD.findall(str(text))
     list_of_words = [i.lower() for i in words if i.lower() not in stop_words]
    # print("words ",len(words))
    # print("after stop",len(list_of_words))
     return Counter(words)

def readfile(filename):
    #https://stackoverflow.com/questions/16528468/while-reading-file-on-python-i-faced-the-error-that-said-unicodedecodeerror-wh
    enc ='utf-8' #iso-8859-15 #cp437
    with open(filename, 'r', encoding=enc) as f:
        content = f.readlines()
        return content
    #content = [x.strip() for x in content]

def jaccard(word_list1, word_list2):
    set_1 = set(word_list1)
    set_2 = set(word_list2)
    n = len(set_1.intersection(set_2))
    sim = n / float(len(set_2.difference(set_1))) #union , difference show example.
    return  sim




file1 = "../data/news-sample/xiaomi1.txt"
file2 = "../data/news-sample/xiaomi2.txt"
#file3 = "../data/news-sample/news3.txt"

content1 = readfile(file1)
content2 = readfile(file2)
#content3 = readfile(file3)


vector1 = text_to_vector(content1)
vector2 = text_to_vector(content2)



cosine1 = get_cosine(vector1, vector2)
jaccard = jaccard(vector1,vector2)

print ('Cosine1:', cosine1)
print('Jaccard:',jaccard)





