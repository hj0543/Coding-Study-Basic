### 1. 파일 생성하기 (open)
파일을 생성하기 위해 파이썬 내장 함수 open을 사용합니다.
```Python
# newfile.py
f = open("새파일.txt", 'w')
f.close()
```
| 파일열기모드 | 설명 |
| :---: | :--- |
| **r** | **읽기 모드**: 파일을 읽기만 할 때 사용 |
| **w** | **쓰기 모드**: 파일에 내용을 쓸 때 사용 (기존 내용 삭제됨) |
| **a** | **추가 모드**: 파일의 마지막에 새로운 내용을 추가할 때 사용 |

#### Tip: 파일 경로와 슬래시(/)역슬래시(\) 사용 시 이스케이프 문자로 오인될 수 있으므로, 슬래시(/)를 사용하거나 Raw String(r"...")을 사용합니다.  
#### 예: f = open("C:/doit/새파일.txt", 'w')
---
### 2. 파일에 내용 쓰기 (write)
print 함수 대신 파일 객체의 write 함수를 사용하여 파일에 데이터를 직접 쓸 수 있습니다.
```Python
# write_data.py
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```
---
### 3. 파일을 읽는 여러 가지 방법
1) readline 함수 이용하기파일의 가장 첫 번째 줄만 읽어옵니다. 반복문을 이용해 모든 줄을 읽을 수 있습니다.
```Python
# readline_all.py
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break  # 더 이상 읽을 줄이 없으면 종료
    print(line)
f.close()
```
3) readlines 함수 이용하기
파일의 모든 줄을 읽어서 각 줄을 요소로 갖는 리스트로 반환합니다.
```Python
# readlines.py
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈(\n) 제거
    print(line)
f.close()
```
5) read 함수 이용하기
파일의 내용 전체를 하나의 문자열로 반환합니다.
```Python
# read.py
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()
```
---
### 4. 파일에 새로운 내용 추가하기
(a)기존 파일의 내용을 유지하면서 뒤에 새로운 값을 추가할 때는 **추가 모드('a')**를 사용합니다.
```Python
# add_data.py
f = open("C:/doit/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```
### 5. with 문과 함께 사용하기
파일을 열고(open) 닫는(close) 것을 자동으로 처리하기 위해 with 문을 사용합니다. 
with 블록을 벗어나면 파일 객체 f가 자동으로 닫힙니다.
```Python# file_with.py
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
```
파일 처리 시 주의사항 (인코딩)한글이 포함된 파일을 다룰 때는 encoding="utf-8"을 명시하는 것이 좋습니다.
```Python
with open("한글파일.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬!")
```
