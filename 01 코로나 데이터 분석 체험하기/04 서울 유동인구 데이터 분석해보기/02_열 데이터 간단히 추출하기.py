import pandas as pd

movement_data = pd.read_csv('./data/movement_skt.csv')
# 기존까지는 특정한 행/열 데이터를 추출할 때는 다음과 같이 .loc() 메서드를 사용했습니다
print('지역 데이터만 출력하기')
print(movement_data.loc[:, '지역'])

# 만약 특정한 열의 데이터만 뽑는다면, 이를 다음과 같이 간단히 사용할 수 있습니다.
print('\n지역 데이터만 출력하기(간단 버전)')
print(movement_data['지역'])

# 여러 열의 데이터를 추출할 때는 데이터들을 ['a', 'b', 'c']와 같이 넣어주면 됩니다
# [](대괄호)가 2번 사용되는 것에 유의하세요!
print('\n성별, 연령, 유동인구수 데이터 추출')
print(movement_data[['성별', '연령대', '유동인구수']])

# 실습: 데이터셋으로부터 지역과 유동인구수 열을 출력해보세요
print('\n지역, 유동인구수 데이터 추출')
print(movement_data[['지역','유동인구수']])
