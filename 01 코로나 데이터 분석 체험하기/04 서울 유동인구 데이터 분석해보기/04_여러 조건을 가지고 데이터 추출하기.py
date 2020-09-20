import pandas as pd

movement_data = pd.read_csv('./data/movement_skt.csv')

# '서울 강남구'에 살면서 20대인 데이터만 추출합니다.
# 힌트1: pandas에서 여러 조건을 사용할 때는 각 조건을 ()(괄호)로 묶습니다.
# 힌트2: python에서 텍스트(문자열) 값이 아닐 때는 ''(따옴표)를 사용하지 않습니다.
print('서울 강남구 20대 데이터')
print(movement_data[(movement_data['지역'] == '서울 강남구') & (movement_data['연령대'] == 20)])

# '19-16'주차의 남성 데이터
print('\n19년 16주차 남성 유동인구 데이터')
print(movement_data[(movement_data['주차'] == '19-16') & (movement_data['성별'] == '남성')])

# 서울 강남구 또는 서울 강북구 데이터
print('\n강북구 or 강남구 데이터')
print(movement_data[(movement_data['지역'] == '서울 강남구') | (movement_data['지역'] == '서울 강북구')])

# 실습: 성별이 '남성'이면서 연령대가 50인 데이터를 추출해보세요
print('\n50대 남성 데이터')
print(movement_data[(movement_data['성별'] == '남성') & (movement_data['연령대'] == 50)])
