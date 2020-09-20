import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from elice_utils import EliceUtils
elice_utils = EliceUtils()

movement_data = pd.read_csv('./data/movement_skt.csv')

# 연령대별 총 유동인구수 변화 추이를 계산합니다
age_1 = 40   # 연령대
age_2 = 50   # 비교하고자 하는 연령대
pivot_table = movement_data.pivot_table(index='주차', columns='연령대', values='유동인구수', aggfunc='sum')

# 한국어를 보기 좋게 표시할 수 있도록 폰트를 설정합니다.
font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
plt.rc('font', family=font.get_name())

# 데이터 시각화 코드입니다
pivot_table[[40, 50]].plot(figsize=(8,4))
plt.title('서울 내 연령대별 총 유동인구수 변화 추이')
plt.savefig("plot.png")
elice_utils.send_image("plot.png")
