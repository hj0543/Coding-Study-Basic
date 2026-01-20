### 1. 코드 레이아웃 (Code Layout)코드의 전체적인 모양과 구조에 대한 규칙입니다.
* 들여쓰기 (Indentation):  
  * 공백(Space) 4칸을 사용합니다.  
  * 탭(Tab)은 사용하지 않습니다. (Python 3에서는 탭과 공백 혼용이 금지됨)  
* 한 줄 길이 제한 (Maximum Line Length):  
  * 한 줄은 최대 79자로 제한합니다.  
  * Docstrings(문서화 주석)나 주석은 72자로 제한합니다.  
* 빈 줄 (Blank Lines):  
  * 최상위 함수와 클래스 정의 사이에는 2줄을 비웁니다.  
  * 클래스 내부의 메서드 정의 사이에는 1줄을 비웁니다.  
---
### 2. 임포트 (Imports)라이브러리를 불러오는 규칙입니다.
#### 한 줄에 하나씩:
```Python
# 좋음 (Good)
import os
import sys

# 나쁨 (Bad)
import sys, os
```

* 순서 (그룹화): 다음 순서대로 그룹을 지어 작성하며, 각 그룹 사이에는 빈 줄을 넣습니다.
  * 표준 라이브러리 (Standard library imports)
  * 서드파티 라이브러리 (Related third party imports)
  * 로컬 어플리케이션/라이브러리 (Local application/library specific imports)
---
### 3. 공백 문자 (Whitespace)
수식이나 괄호 주변의 공백 규칙입니다.  
#### 피해야 할 공백 (Pet Peeves)
* 괄호, 대괄호, 중괄호 안쪽 바로 옆  
```Python
# 좋음
spam(ham[1], {eggs: 2})

# 나쁨
spam( ham[ 1 ], { eggs: 2 } )
```
* 쉼표(,), 세미콜론(;), 콜론(:) 바로 앞
```Python
# 좋음
if x == 4: print(x, y)

# 나쁨
if x == 4 : print(x , y)
```
#### 연산자 주변
* 할당(=), 비교(==, <, >), 논리(and, or) 연산자 앞뒤에는 공백을 하나씩 넣습니다.  
* 단, 우선순위가 다른 연산자가 섞여 있을 때는 우선순위가 낮은 연산자 주변에만 공백을 넣는 것이 좋을 때도 있습니다.
```Python
# 좋음
x = x*2 - 1
hypot2 = x*x + y*y
```
---
4. 이름 짓기 규칙 (Naming Conventions)
#### 가장 중요하고 자주 참조되는 부분입니다.  
> 변수 -> (Variable)소문자 + 밑줄 (snake_case)my_variable, count  
> 함수 -> (Function)소문자 + 밑줄 (snake_case)calculate_total(), run()  
> 클래스 -> (Class)각 단어 첫 글자 대문자 (CapWords)MyClass, UserProfile  
> 상수 -> (Constant)전체 대문자 + 밑줄MAX_OVERFLOW, TOTAL  
> 모듈 -> (Module)짧은 소문자 (밑줄 가능)mymodule.py  
> 패키지 -> (Package)짧은 소문자 (밑줄 지양)mypackage  

#### 참고:
* l (소문자 엘), O (대문자 오), I (대문자 아이) 한 글자 변수명은 숫자 1, 0과 헷갈리므로 피해야 합니다.
* _variable (앞에 밑줄): 내부적으로만 사용되는 변수/함수임을 암시합니다.

### 5. 프로그래밍 권장 사항 (Programming Recommendations)
* None 비교:None과 비교할 때는 항상 is나 is not을 사용합니다.
``` Python
# 좋음
if foo is None:

# 나쁨
if foo == None:
```
#### Boolean 비교:True, False와 직접 비교하지 않습니다.
```Python
# 좋음
if greeting:

# 나쁨
if greeting == True:
```
#### 타입 검사:객체의 타입을 검사할 때는 type() 대신 isinstance()를 사용합니다.
```Python
# 좋음
if isinstance(obj, int):

# 나쁨
if type(obj) is int:
```
