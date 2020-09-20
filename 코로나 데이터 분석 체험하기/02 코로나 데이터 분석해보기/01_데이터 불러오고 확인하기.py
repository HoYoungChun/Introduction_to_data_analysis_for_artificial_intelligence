# pandas는 파이썬의 대표적인 데이터 분석 라이브러리(툴)이며, 다음과 같이 사용할 수 있습니다.
import pandas as pd


# pd.read_excel()를 사용하면 xlsx 형태로 저장된 데이터 파일을 읽을 수 있습니다.
# 본 예제에서는 데이터셋을 불러온 다음 corona_data라는 이름으로 데이터를 저장하겠습니다.
corona_data = pd.read_excel('./data/corona_data.xlsx', index_col='날짜')


# print() 명령어를 사용하면 불러온 데이터를 출력(확인)할 수 있습니다.
print(corona_data)


