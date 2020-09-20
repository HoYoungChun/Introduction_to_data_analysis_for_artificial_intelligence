import pandas as pd

# 데이터셋으로부터 유동인구 데이터를 불러와 movement_data라는 이름으로 저장합니다.
movement_data = pd.read_csv('./data/movement_skt.csv')
print('서울 유동인구 데이터 출력')
print(movement_data)

# 불러온 데이터셋에 어떠한 지역들이 있는지 확인합니다.
# .unique() 명령어(메서드)를 사용하면 해당 데이터셋의 열에서 유일한 값들만 확인할 수 있습니다.
print('\n지역의 유일한 값 찾기')
print(movement_data.loc[:, '지역'].unique())

# 실습: unique() 명령어를 사용하여 연령대가 어떻게 구성되어 있는지 확인해봅니다.
print('\n연령대의 유일한 값 찾기')
print(movement_data.loc[:, '연령대'].unique())
