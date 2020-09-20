import pandas as pd

movement_data = pd.read_csv('./data/movement_skt.csv')

# '주차' 열의 값 조건이 '19-08'인 데이터만 선택합니다.
# 참고: A와 B의 값이 같다는 것은 '=='로 표현합니다.
print('19년 8주차 데이터')
print(movement_data[movement_data['주차']=='19-08'])

# '지역'열의 값 조건이 '서울 노원구'인 데이터만 선택합니다.
print('\n서울 노원구 데이터')
print(movement_data[movement_data['지역']=='서울 노원구'])

# 실습: 성별이 '여성'인 데이터만 추출해보세요
print('\n성별이 여성인 데이터')
print(movement_data[movement_data['성별']=='여성'])
