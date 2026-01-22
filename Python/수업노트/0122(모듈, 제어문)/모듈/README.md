# 파이썬 표준 라이브러리(PSL)
파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

## 모듈
* 하나의 파일로 묶인 변수와 함수의 모음
* 특정한 기능알 하는 코드가 작성된 파이썬 파일(.py)

### 모듈 예시
**math 내장 모듈**
파이썬이 미리 작성해둔 수학 관련 변수와 함수가 작성된 모듈

```python
print(math.pi) # 3.141592 ...
print(math.sqrt(4)) # 2.0 -> sqrt = 제곱근
```
#### import 문 사용
* 같은 이름의 함수가 여러 모듈에 있을 때 충돌을 방지할 수 있음
* dot 연산자 - 점의 오른쪽을 찾아라
* 코드가 길어질 수 있음
```python
print(math.pi) # 모듈명. 변수명
print(math.sqrt(4)) # 모듈명. 함수명
```
#### from 절 사용
* 코드가 짧고 간결해짐
* 정의된 모듈의 위치를 알기 어려워 명시적이지 않을 수 있음
* 사용자가 선언한 변수 또는 함수와 겹칠 수 있음
```python
from math import pi, sqrt

print(pi) # 변수명
print(sqrt(4)) # 함수명
```
* 서로 다른 모듈에서 import된 변수나 함수의 이름이 같은 경우 이름 충돌 발생
* 마지막에 import된 것이 이전 것을 덮어쓰기 때문에, 나중에 import된 것만 유효함
```python
from math import sqrt    # math.sqrt가 먼저 import됨
from my_math import sqrt # my_math.sqrt가 math.sqrt를 덮어씀

result = sqrt(9) # math.sqrt가 아닌 my_math.sqrt가 사용됨
```
* 모든 요소를 한 번에 import하는 *표기는 권장하지 않음
```python
from math import *
from my_math import sqrt, tangent  # 어느 함수가 math 모듈과 중복되는지 모름

# 아래는 사용자가 임의로 정의한 변수들
a = 100
c = 200
e = 300 # math 모듈의 자연상수 e를 사용할 수 없게 됨
```
#### 'as'키워드
as 키워드를 사용하여 별칭을 부여
* 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결
* import되는 함수나 변수명이 너무 길거나 자주 사용해야 할 경우 'as'키워드로 별칭을 정의해 쉽게 사용

### 사용자 정의 모듈
#### 직접 정의한 모듈 사용하기
* my_math.py를 생성하여 두 수의 합을 구하는 add 함수를 작성
```python
def add(x, y):
    return x + y


def sqrt(x):
    return x**0.5
```
* 같은 위치에 sample.py 파일을 생성하고 my_math 모듈의 add 함수 import 후 add 함수 호출
```python
## 사용자 정의 모듈
import my_math

# from my_math import add

print(my_math.add(1, 2))
# print(add(1, 2))

```
---
## 패키지
연관된 모듈들을 하나의 디렉토리에 모아 놓은 것

### 패키지 만들기
```python
from my_package.math import my_math # my_package -> math -> my_math.py
from my_package.statistics import tools # my_package -> statistics -> tools.py

print(my_math.add(1, 2))
print(tools.mod(1, 2))
```
**Tip**
* 너무 많은 기능이 한 파일에 몰려 있으면 사용자가 헷갈릴 수 있다.
* 비슷한 기능은 묶고, 관련없는 것은 나누는 것이 사용하기 편하다.
* 폴어/파일명은 소문자 + 언더스코어(_)를 쓰는 것이 깔끔하고 표준적이다.

### 패키지의 종류

#### 파이썬 표준 라이브러리 (PSL, Python Standard Library)

* 파이썬을 설치하면 자동으로 사용할 수 있는 기본 라이브러리

* 다양한 기능이 내장되어 있어 복잡한 작업도 쉽게 처리할 수 있음

* math, random, sys (모듈) 및 json, email (패키지) 등 다양한 모듈과 패키지가 포함됨

* 별도 설치 없이 바로 import 해서 사용 가능

#### 파이썬 외부 패키지 (Third-party Packages)

* 필요한 기능을 사용하기 위해 직접 설치해서 쓰는 패키지

* 전 세계 개발자들이 만든 다양한 패키지들이 존재

  예시) 엑셀 파일 조작(pandas, openpyxl) / 데이터 시각화(matplotlib) / 웹 데이터 수집(requests) 등

* 사용할 패키지를 설치할 때는 pip 명령어를 사용

### requests 외부 패키지 설치 및 사용 예시
* requests 외부 패키지 : 파이썬에서 웹에 요청을 보내고 응답을 받는 걸 아주 쉽게 만들어주는 외부 패키지
* pip을 통해 requests 패키지를 설치
터미널에 입력 : $ pip install requests
python requests 검색 후 공식 문서를 먼저 확인하자..!

**패키지 사용 목적**
* 모듈들의 이름공간을 구분하여 충돌을 방지
* 모듈들을 효율적으로 관리하고 할 수 있도록 돕는 역할