# python 데이터 분석 라이브러리인 pandas를 불러오고, 이를 pd라는 이름으로 사용(별명 지정)합니다.
import pandas as pd

# pd.read_csv() 명령어를 사용하여 csv 형태로 저장된 데이터를 불러올 수 있습니다.
shopping_data = pd.read_csv('./data/shopping_data.csv', index_col='상품군별')

# 실습: 불러온 데이터를 확인해봅니다.
print(shopping_data)
