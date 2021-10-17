from newspaper import Article
from konlpy.tag import Kkma
from sklearn.feature_extraction.text import TfidfVectorizer


url_list = [
    'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=025&aid=0003142996', 
    'https://www.edaily.co.kr/news/read?newsId=01879446629213904&mediaCodeNo=257&OutLnkChk=Y', 
    'https://imnews.imbc.com/news/2021/society/article/6307742_34873.html',
    'https://biz.chosun.com/it-science/bio-science/2021/10/17/XH7WMEGW6ZHJHITW2NLCWHOP3Y/?utm_source=naver&utm_medium=original&utm_campaign=biz',
]

kkma = Kkma()
doc_list = []

for url in url_list:
    article = Article(url, language='ko')
    article.download()
    article.parse()
    doc_list.append(' '.join(kkma.nouns(article.title)) + ' '.join(kkma.nouns(article.text)))

tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(doc_list)

str_distances = tfidf_matrix * tfidf_matrix.T

shape = str_distances.get_shape()
print(f"유사도 분석을 위한 {shape[0]}x{shape[1]} 매트릭스")
print(str_distances.toarray())
