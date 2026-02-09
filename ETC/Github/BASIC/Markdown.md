# 1. 마크다운의 장-단점
## 장점
    * 간결하다.
    * 별도의 도구없이 작성가능하다.
    * 다양한 형태로 변환이 가능하다.
    * 텍스트(Text)로 저장되기 때문에 용량이 적어 보관이 용이하다.
    * 텍스트파일이기 때문에 버전관리시스템을 이용하여 변경이력을 관리할 수 있다.
    * 지원하는 프로그램과 플랫폼이 다양하다.

## 단점
    * 표준이 없다.
    * 표준이 없기 때문에 도구에 따라서 변환방식이나 생성물이 다르다.
    * 모든 HTML 마크업을 대신하지 못한다.

# 2. 마크다운 사용법 ★★★★★

## 1. 헤더 (Headers)

제목은 `#`의 개수로 크기를 조절합니다 (1~6단계).

# H1: 가장 큰 제목 `#`
## H2: 두 번째 큰 제목 `##`
### H3: 세 번째 큰 제목 `###`
#### H4: 네 번째 큰 제목 `####`
##### H5: 다섯 번째 큰 제목 `#####`
###### H6: 가장 작은 제목 `######`

Alternatively, for H1 and H2, an underline style can be used:

Alt-H1 `======`
======

Alt-H2`------`
------

## 2. 인용문 (BlockQuote)

이메일 인용처럼 `>` 기호를 사용합니다. 중첩도 가능합니다.

> This is a first blockquote.
> > This is a second blockquote.
> > > This is a third blockquote.

## 3. 목록 (Lists)

### 순서 있는 목록 (Ordered List)
숫자와 점을 사용합니다. 숫자가 틀려도 렌더링 시에는 순서대로 보정됩니다.

1. 첫번째
2. 두번째
3. 세번째

### 순서 없는 목록 (Unordered List)
`*`, `+`, `-` 기호를 혼용하여 사용할 수 있습니다. 들여쓰기를 통해 중첩이 가능합니다.

* 1단계 `*`
  - 2단계 `-`
    + 3단계 `+`
      + 4단계 `+`

## 4. 코드 (Code)

### 인라인 코드 (Inline Code)
문장 중간에 코드를 넣을 때는 백틱(`)을 사용합니다.
예: `String args` 값을 입력하세요.

### 코드 블럭 (Code Blocks)
GitHub에서는 **백틱 3개(```)**를 사용하는 방식을 가장 많이 씁니다. 언어를 지정하면 문법 강조(Syntax Highlighting)가 적용됩니다.
```백틱 3개 + 언어명```
```java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}

```

## 5. 수평선 (Horizontal Rule)

문단을 나눌 때 사용합니다.`---`

---

---



## 6. 링크 (Links)

### 기본 링크
```[Google](https://google.com)```
[Google](https://google.com)

### 참조 링크 (Reference Links)

링크가 많을 때 문서 가독성을 위해 본문 하단에 주소를 정의할 수 있습니다.
```[Google](https://www.google.com/search?q=%5Bhttps://google.com%5D(https://google.com))```
[Google](https://www.google.com/search?q=%5Bhttps://google.com%5D(https://google.com))

### 자동 링크
```
[http://example.com/](http://example.com/)
[address@example.com](mailto:address@example.com)
```
[http://example.com/](http://example.com/)
[address@example.com](mailto:address@example.com)

## 7. 강조 (Emphasis)

* *기울임* ```*기울임*```
* **굵게** ```**굵게**```
* ~~취소선~~ ```~~(취소선)~~```

문장 중간에 사용할 경우 **띄어쓰기**를 하는 것이 안전합니다.

## 8. 이미지 (Images)

이미지는 링크 문법 앞에 `!`만 붙이면 됩니다.

> **Note:** GitHub 마크다운은 이미지 크기 조절 문법을 기본 지원하지 않습니다. 크기를 조절하려면 아래와 같이 HTML 태그를 사용해야 합니다.

<img src="https://www.google.com/search?q=/path/to/img.jpg" width="400px" height="300px" title="크기 설정" alt="설명">

## 9. 줄바꿈 (Line Breaks)

마크다운에서 줄을 바꾸려면 문장 끝에 **공백(Space)을 2칸 이상** 입력하고 엔터를 쳐야 합니다.

또는 명시적으로 `<br/>` 태그를 사용할 수 있습니다.

첫 번째 줄입니다. (공백 2칸 없음)
두 번째 줄입니다. (줄바꿈 안됨)

첫 번째 줄입니다. (공백 2칸 있음)

두 번째 줄입니다. (줄바꿈 됨)



---

### 💡 GitHub 마크다운 작성 팁

GitHub에 올리실 때 추가적으로 알면 좋은 기능들입니다:

1.  **체크리스트 (Task Lists):**
    ```markdown
    - [x] 완료된 작업
    - [ ] 해야 할 작업
    ```
2.  **표 (Tables):**
    ```markdown
    | 제목1 | 제목2 |
    | --- | --- |
    | 내용1 | 내용2 |
    ```
    | 제목1 | 제목2 |
    | --- | --- |
    | 내용1 | 내용2 |