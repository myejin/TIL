from newspaper import Article
from khaiii import KhaiiiApi, KhaiiiExcept
from sklearn.feature_extraction.text import TfidfVectorizer

# 네이버 오픈 API 활용, '삼성전자' 키워드로 약 30개 추출
url_list = [
    "https://www.businesspost.co.kr/BP?command=article_view&num=255096",
    "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=101&oid=032&aid=0003104484",
    "https://www.idaegu.co.kr/news/articleView.html?idxno=361226",
    "https://www.siminilbo.co.kr/news/newsview.php?ncode=1065616363675493",
    "http://www.econonews.co.kr/news/articleView.html?idxno=221166",
    "http://www.sentv.co.kr/news/view/602988",
    "http://www.kihoilbo.co.kr/news/articleView.html?idxno=950107",
    "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=102&oid=008&aid=0004658190",
    "http://www.kihoilbo.co.kr/news/articleView.html?idxno=950020",
    "http://www.koit.co.kr/news/articleView.html?idxno=89902",
    "http://www.kyeongin.com/main/view.php?key=20211018010002903",
    "http://www.g-enews.com/ko-kr/news/article/news_all/20211018203103734a01bf698f_1/article.html",
    "http://www.newstnt.com/news/articleView.html?idxno=107643",
    "https://www.insight.co.kr/news/363680",
    "http://www.wsobi.com/news/articleView.html?idxno=141965",
    "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=100&oid=008&aid=0004658183",
    "http://www.nbntv.co.kr/news/articleView.html?idxno=937157",
    "http://www.sentv.co.kr/news/view/602982",
    "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=105&oid=469&aid=0000635730",
    "https://www.hellot.net/news/article.html?no=62647",
    "http://www.youthdaily.co.kr/news/article.html?no=83595",
    "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=105&oid=029&aid=0002701496",
    "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=101&oid=029&aid=0002701479",
    "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=100&oid=052&aid=0001653896",
    "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=105&oid=018&aid=0005063238",
    "http://www.ggilbo.com/news/articleView.html?idxno=874091",
    "http://it.chosun.com/site/data/html_dir/2021/10/18/2021101801557.html",
    "http://www.insightkorea.co.kr/news/articleView.html?idxno=92723",
    "http://www.iminju.net/news/articleView.html?idxno=75722",
    "https://www.dnews.co.kr/uhtml/view.jsp?idxno=202110181834054740942",
    "http://www.gwangnam.co.kr/read.php3?aid=1634551153399107010",
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
print(f"유사도 분석을 위한 {shape[0]}x{shape[1]} 매트릭스")
print(str_distances.toarray())
