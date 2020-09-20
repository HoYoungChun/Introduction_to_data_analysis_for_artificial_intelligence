# 라이브러리를 사용하기 위해서는 다음처럼 pandas 라이브러리를 임포트(불러오기)해야 합니다.
# (as pd는 pandas를 pd라는 짧은 이름으로 사용하겠다는 뜻입니다)
import pandas as pd

# <pd.명령어>와 같은 형태로 라이브러리의 기능을 사용할 수 있습니다.
# 예컨대 pd.read_csv()는 pandas(pd)의 csv 파일 불러오기 기능을 사용하겠다는 뜻입니다.

# 다음 코드를 실행해 데이터를 어떻게 불러오는지 직접 확인해봅시다.
my_data = pd.read_csv('./data/shopping_data.csv')
print(my_data)
