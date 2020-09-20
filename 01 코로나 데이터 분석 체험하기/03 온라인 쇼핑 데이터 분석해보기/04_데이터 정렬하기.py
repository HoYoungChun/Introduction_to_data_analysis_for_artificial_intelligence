# python 데이터 분석 라이브러리인 pandas를 불러오고, 이를 pd라는 이름으로 사용(앨리어스 지정)합니다.
import pandas as pd

# pd.read_csv() 명령어를 사용하여 csv 형태로 저장된 데이터를 불러올 수 있습니다.
shopping_data = pd.read_csv('./data/shopping_data.csv', index_col='상품군별')


# 계산된 YoY 데이터를 바탕으로 데이터를 정렬해봅시다.

# 2020년 6월의 YoY 데이터를 yoy_2006이라는 이름으로 저장합니다
yoy_2006 = (shopping_data['20-6'] - shopping_data['19-6']) / shopping_data['19-6'] * 100

# pandas 열 데이터에 .sort_values() 명령어(메서드)를 사용하면 데이터를 값 순서대로 간단히 정렬할 수 있습니다.
# 이 때 열의 데이터는 가급적 숫자들만으로 구성되어 있어야 합니다.
print('오름차순 정렬')
print(yoy_2006.sort_values())

# 실습: 데이터를 내림차순으로 정렬해봅니다.
# sort_values()에 ascending=False 옵션(파라미터)을 주면 내림차순으로 정렬됩니다.
# 명령어(메서드)의 옵션은 다음과 같이 사용합니다: sort_values(ascending=False)
print('\n내림차순 정렬')
print(yoy_2006.sort_values(ascending = False))
