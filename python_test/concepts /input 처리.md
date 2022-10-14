# 파이썬 코딩 테스트 input 처리 방법

## input 처리

- 코딩 테스트의 경우 input값이 주어지는 경우가 있음
- 기존의 input 내장 함수를 쓰면 시간내에 프로그램이 수행되지 않으므로
  sys 모듈을 사용하여 코드 수행 시간을 단축 시킴.

## sys 모듈

- 파이썬 인터프리터에서 제공하는 변수, 함수 등을 사용(접근) 할 수 있게 해주는 모듈

```python
import sys
sys.path          # 디렉토리 경로 저장
sys.version       # 인터프리터 버전
sys.psl         # 프롬프트에 접근
```

## 기존의 input() 함수

- 파이썬의 빌트인 input의 처리 과정

```python
input()

'''
   1. input() 실행
   2. 입력값 한줄씩 읽음
   3. 개행(줄바꿈)을 지움
   4. 문자열로 변환
   5. return
'''
```

## sys.stdin.readline()

#### sys 모듈의 stdin 객체에 readline을 사용한다. return 값은 리스트

### stdin

- sys 모듈안에 있는 파일 개체
- 파이썬 인터프리터가 표준 입력에 사용하는 파일 객체

### readline()

- 파일의 한줄을 읽음
  (c.f) stdin.readlines의 경우 `컨트롤` + `z`를 입력해야 입력을 멈춤  
  백준에서는 입력값을 주어주고 `켠트롤` + `z`를 입력해주지 않으므로 쓸 수 없음

### strip()

sys.stdin.readline()은

- strip() : 왼쪽 오른쪽의 인자로 전달된 문자 제거
- lstrip() : 왼쪽의 인자로 전달된 문자 제거
- rstrip() : 오른쪽 인자로 전달된 문자 제거
