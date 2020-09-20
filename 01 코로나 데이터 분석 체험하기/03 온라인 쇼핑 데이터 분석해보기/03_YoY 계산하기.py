# python 데이터 분석 라이브러리인 pandas를 불러오고, 이를 pd라는 이름으로 사용(앨리어스 지정)합니다.
import pandas as pd

# pd.read_csv() 명령어를 사용하여 csv 형태로 저장된 데이터를 불러올 수 있습니다.
shopping_data = pd.read_csv('./data/shopping_data.csv', index_col='상품군별')


# pandas의 열 계산 실습 1
print('20년 6월 데이터와 19년 6월 데이터의 차이')
print(shopping_data['20-6'] - shopping_data['19-6'])

# pandas의 열 계산 실습 2
# 참고 - YoY 계산식: ((기준년도 데이터 - 직전년도 데이터) / 직전년도 데이터) X 100
# 참고 - 연산자: python에서는 곱하기를 *로, 나누기를 /로 사용합니다.
print('\n20년 6월 데이터 및 19년 6월 데이터의 YoY')
print((shopping_data['20-6'] - shopping_data['19-6']) / shopping_data['19-6'] * 100) 

# 실습: 20년 2월의 YoY를 계산해봅니다
print('\n20년 2월 데이터 YoY')
print((shopping_data['20-2'] - shopping_data['19-2']) / shopping_data['19-2'] * 100)
