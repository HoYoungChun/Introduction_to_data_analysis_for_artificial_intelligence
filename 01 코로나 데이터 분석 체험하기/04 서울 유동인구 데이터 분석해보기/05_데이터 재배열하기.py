import pandas as pd

movement_data = pd.read_csv('./data/movement_skt.csv')

# --- 주차별 성별 유동인구수 변동 추이 분석하기 --- #
# 행(index)는 '주차'로, 열(columns)은 '성별'로 설정하였습니다.
# 결과값으로 보기를 원하는 것은 총 유동인구수이므로, 결과값(values)에는 '유동인구수'를 설정하였습니다.
# 또한 주차별 합계를 보기를 원하므로, 연산값(aggfunc)에는 'sum'(합계)을 설정하였습니다.
print('주차/성별 총 유동인구수 변동 추이')
result_1 = movement_data.pivot_table(index='주차', columns='성별', values='유동인구수', aggfunc='sum')
print(result_1)

# --- 지역별 성별 유동인구수 변동 추이 분석하기 --- #
# 행(index)는 '지역'으로, 열(columns)은 '성별'로 설정하였습니다.
# 결과값으로 보기를 원하는 것은 총 유동인구수이므로, 결과값(values)에는 '유동인구수'를 설정하였습니다.
# 또한 주차별 합계를 보기를 원하므로, 연산값(aggfunc)에는 'sum'(합계)을 설정하였습니다.
print('\n 전체 기간 내 지역/성별 총 유동인구수')
result_2 = movement_data.pivot_table(index='지역', columns='성별', values='유동인구수', aggfunc='sum')
print(result_2)

# 실습 - 주차별 연령대별 유동인구수 변화 추이를 구해봅니다.
print('\n 연령대별 총 유동인구수 변화 추이')
result_3 = movement_data.pivot_table(index='주차', columns='연령대', values='유동인구수', aggfunc='sum')
print(result_3)
