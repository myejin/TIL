import numpy as np
from matplotlib import pyplot as plt 
from newspaper import Article
from khaiii import KhaiiiApi, KhaiiiExcept
from sklearn.feature_extraction.text import TfidfVectorizer

url_list = [
    'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=015&aid=0004618208',
    'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=018&aid=0005063885',
    'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=008&aid=0004658737',
    'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=005&aid=0001477986',
    'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=022&aid=0003629602',
    'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=020&aid=0003388201',
    'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=119&aid=0002539489',
    'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=025&aid=0003143581',
]

api = KhaiiiApi()

doc_list = []
for i, url in enumerate(url_list):
    article = Article(url, language="ko")
    article.download()
    article.parse()
    doc = ''
    try:
        if not article.title:
            continue
        for word in api.analyze(article.title):
            for morph in word.morphs:
                if morph.tag in ('NNG', 'NNP', 'NP', 'VV', 'SN', 'SL'):
                    doc += morph.lex + ' '
        
        if not article.text:
            continue
        for word in api.analyze(article.text):
            for morph in word.morphs:
                if morph.tag in ('NNG', 'NNP', 'NP', 'VV', 'SN', 'SL'):
                    doc += morph.lex + ' '
        doc_list.append(doc)

    except KhaiiiExcept as khaiii_except:
        print('hi', str(khaiii_except))

tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(doc_list)

str_distances = tfidf_matrix * tfidf_matrix.T
shape = str_distances.get_shape()
# print(f"유사도 분석을 위한 {shape[0]}x{shape[1]} 매트릭스")
res_matrix = str_distances.toarray()
# print(res_matrix)

print(f"총 {shape[0]}개의 유사데이터 비교")
data = np.ravel(res_matrix)
plt.hist(data, bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
plt.show()
