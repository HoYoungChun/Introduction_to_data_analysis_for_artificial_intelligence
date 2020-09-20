from elice_utils import EliceUtils
elice_utils = EliceUtils()
import matplotlib.pyplot as plt
import pandas as pd


def main():
	# 코로나 데이터셋을 불러옵니다
    corona_data = pd.read_excel('./data/corona_data.xlsx', index_col='날짜')
    
    
    # 작성된 이미지를 제출합니다
    draw_image(corona_data)


# 데이터를 다루고 이미지를 그리는 부분입니다
def draw_image(corona_data):
    
    # 이미지 형태를 만들고 사용될 한글 글꼴을 설정합니다.
    plt.figure(figsize=(10,10))
    plt.rc('font', family='NanumBarunGothic')
    
    
    # 확진자 데이터를 시각화합니다
    corona_data['확진자'].plot()
    
    
    # 누적 검사 수 데이터를 시각화합니다
    corona_data['누적검사'].plot(secondary_y=True)
    
    
    # 차트 제목을 붙입니다
    plt.title('확진자 및 누적검사 추이')
    
    
    # 이미지 데이터를 만듭니다
    plt.savefig('corona.png')
    elice_utils.send_image('corona.png')

if __name__ == "__main__":
    main()
