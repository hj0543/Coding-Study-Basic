# CLI

### GUI (Graphic User Interface)

그래픽을 통해 사용자와 컴퓨터가 상호작용

- 사진이 있는 메뉴판을 보고 손가락으로 주문하는 방식
- 쉽고 직관적
- 예) 윈도우 화면

### CLI (Command Line Interface)

명령어를 통해 사용자와 컴퓨터가 상호작용

- 주방자에게 직접 말로 주문하는 방식
- 원하는 대로 정확하고, 세밀하며, 빠르게 요청할 수 있음
- 예) 터미널 또는 cmd

### Why CLI?

- 효율성 : 키보드만으로 모든 작업을 빠르고 가볍게 수행할 수 있음
- 정밀한 제어 : 그래픽 화면에 보이지 않는 숨겨진 설정까지 정밀하게 제어할 수 있음
- 강력한 자동화 : 단순하고 반복적인 작업을 명령어 한 줄로 자동화 할 수 있음
- 표준 환경 : 서버, 클라우드 등 그래픽이 없는 개발 환경의 필수 도구

### 문법 및 활용 - 한글 파일명 비추천

- touch : touch sample.txt > sample.txt 생성
- mkdir : mkdir menu >menu 폴더 생성
- ls : 현재 폴더에 있는 것들을 나타냄.
- clear : 정리 > Ctrl + L
- cd(chance directory) : 폴더를 바꾼다 (cd .. > 상위 폴더로 이동 / . > 현재 폴)
- ls -a :
- start ‘파일명’ : 폴더 또는 파일 실행 (파일 실행 시 확장자 이름 붙이기)
- rm : 삭제
- rm -r : 폴더 삭제 (복구 불가)
- rmdir : 비어있는 폴더만 삭제함
- PWD(Print Walk Directory) : 현재폴더 경로 출력

directory = folder

### 경로

- CLI에서 가장 중요한 것. 내가 어디 있는지 알아야 한다.
- ‘주소’를 이해하는 것이 CLI의 첫 걸음

**루트 디렉토리(/)**

- 건물의 정문 또는 1층 로비 모든 주소의 시작점

**홈 디렉토리 (~)**

- 나의 집 또는 개인 사무실. 터미널을 처음ㅋ 켰ㅇ,ㄹ 때 시작하는 나의 기본 공간

### 절대 경로

정문(루트, root, /)부터 목적지까지의 전체 주소

누가 어디서 보든 항상 똑같은 주소

/C/Users/ssafy/

### 상대 경로

‘현재 내 위치’를 기준으로 한 주소

저 방으로 가(Desktop/) 또는 이전 방(..)으로 가 와 같음

ls -1 도 해ㅔ보기

# Git → 프로그램

### Wroking directory

실제 작업 중인 파일들이 위치하는 영역

### Staging directory

Wroking directory에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

### Repository

버전 이력과 파일들이 영구적으로 저장되는 영역

모든 버전과 변경 이력이 기록

### Commit → 버전

변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 스냅샷이라고도 함.

### Git의 동작

git init

git add

git commit

### remote repository

온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간

원격 저장소 **‘서비스’** git lab, git hub, bitbucket

Git(프로그램) ↔ GitLab, GitHub(서비스) 차이가 있다.

## FLOW


git init -> git add . -> git commit -m “여기에 버전 수정사항” -> git remote add origin ‘여기에 url’ -> git remote -v -> git push origin master

#### SSAFY 과제제출
* 과제 파일 받기 : git clone '여기에 레포 URL'
* 과제 파일 제출 : git add . -> git commit -m “여기에 버전 수정사항” -> git push origin master

git pull origin master


