# --- python 데이터 분석 세계에 입문하신 것을 진심으로 환영합니다! --- #

# pandas는 파이썬의 대표적인 데이터 분석 라이브러리(툴)이며, 다음과 같이 사용할 수 있습니다.
import pandas as pd
corona_data = pd.read_excel('./data/corona_data.xlsx', index_col='날짜')


# 코로나 데이터셋에는 4개의 열(속성이라고도 합니다)이 있으며,
# 각각 '격리해제', '사망자', '확진자', '누적검사'입니다.

# corona_data가 갖고 있는 열(칼럼)들이 무엇인지 출력하여 확인해봅니다..
print(corona_data.columns)


# corona_data에서 특정 열 데이터만 출력해보도록 하겠습니다.
# 데이터셋['열 이름'] 형태로 코드를 작성하면 특정 열의 데이터만 확인할 수 있습니다.
# 열 이름은 '(따옴표)를 사용해야 한다는 점에 주의해주세요
print(corona_data['격리해제'])


# 아래에 corona_data가 갖고 있는 열 중, '격리해제' 대신 '확진자' 등의 다른 열을 입력하여 확인해보세요
print(corona_data['확진자'])


