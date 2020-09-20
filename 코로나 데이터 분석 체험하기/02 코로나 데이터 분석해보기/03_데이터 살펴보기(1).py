# pandas 라이브러리 및 데이터 불러오기
import pandas as pd
corona_data = pd.read_excel('./data/corona_data.xlsx', index_col='날짜')


# loc를 이용하여 7월 31일의 검사 수를 출력합니다.
print(corona_data.loc['2020-07-31', '누적검사'])


# 실습: loc에 행과 열을 입력하여, 다른 데이터들도 출력해보세요.
print(corona_data.loc['2020-07-30', '누적검사'])
