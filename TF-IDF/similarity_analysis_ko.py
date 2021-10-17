from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()

sentence = "영희와 철수는 뭉치를 산책시키기 위해 동락공원에 갔다. 그곳에서 뭉치는 다른 강아지들과 즐거운 시간을 보냈다."

print(f"형태소 : {kkma.morphs(sentence)}")
print(f"명사 : {kkma.nouns(sentence)}")  # 문장에서 조사를 떼어내고, 명사만 활용해 분석하기
print(f"품사 : {kkma.pos(sentence)}")
