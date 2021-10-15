from sklearn.feature_extraction.text import TfidfVectorizer

str_list = ["find what you love", "do what you love", "don't do what you hate"]

tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(str_list)

str_distances = tfidf_matrix * tfidf_matrix.T

shape = str_distances.get_shape()
print(f"유사도 분석을 위한 {shape[0]}x{shape[1]} 매트릭스")
print(str_distances.toarray())
