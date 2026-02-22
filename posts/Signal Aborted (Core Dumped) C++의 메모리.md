---
title: "Signal: Aborted (Core Dumped) C++의 메모리"
date: Sun, 22 Feb 2026 06:47:06 GMT
url: "https://velog.io/@bluepaper14_/Signal-Aborted-Core-Dumped-C%EC%9D%98-%EB%A9%94%EB%AA%A8%EB%A6%AC"
tags: [velog, backup]
---

# [Signal: Aborted (Core Dumped) C++의 메모리](https://velog.io/@bluepaper14_/Signal-Aborted-Core-Dumped-C%EC%9D%98-%EB%A9%94%EB%AA%A8%EB%A6%AC)

### 에러처리

![](https://velog.velcdn.com/images/bluepaper14_/post/a84ae729-fac7-4600-b88f-7fa61f4dccc9/image.png)

문제에 대하여 코드를 작성하다가 에러가 발생하였다. _signal: aborted (core dumped)_ 는 강제로 프로그램이
종료되었다는 건데..무슨 원인이길래 찾아보자.

### Core Dumped

쉽게 말해 프로그램이 죽기직전의 메모리 상태를 블랙박스처럼 남겼다는 것이다. Core는 메모리를 의미하고 Dumped는 쏟아냈다라는
의미다._*_프로그램이 허용하지 않은 메모리에 접근하거나 처리할 수 없는 예외사항이 있을때 OS가 개입하여 프로그램을 강제종료한 것이다.
*__

### 흔한 원인은 무엇일까

코딩테스트 한정해서 에러처리를 해결하는 것이기에 문제를 찾는건 다소 쉽다.

#### 배열 벡터 인덱스 초과

의도하지 않은 배열의 범위를 초과해 런타임체크를 실패해 abort를 호출할 수 있다. 이외에 여러 원인들이 있다만 대게 _잘못된 메모리
접근, 범위/조건 위배_ 가 가장 유력한 에러사항이다.

이번엔 에러 문제를 확인하러 가보자.

### 에러처리 예제

아래 코드는 특정 범위의 문자열을 잘라 숫자로 변환한 뒤 k와 비교하는 로직이다.

    
    
    #include <string>
    #include <vector>
    
    using namespace std;
    
    vector<int> solution(vector<string> intStrs, int k, int s, int l) {
        vector<int> answer;
    
        for(int j = 0; j < intStrs.size(); j++) {
            string x = intStrs[j];
            string temp = "";
            for(int i = s; i < s + l; i++) {
                temp += x[i];
            }
            if(stoi(temp) > k) {
                answer.push_back(stoi(temp));
            }
    }
        return answer;
    }
    

문제는 간단하다. s와 l 사이의 특정 부분 수를 k와 비교하는 것이다. 그런데 에러가된 부분을 알려면 먼저 디버깅을 해보자(프로그래머스라
디버깅 안하고 바로 코드 작성함..)

짧게 설명하자면 확인하는 벡터 배열을 순회. 그리고 s부터 s + l 까지의 특정 부분을 temp라는 임시 문자열에 넣어 이를 k와
비교했다. 오류를 찾으셨나요?

    
    
    string temp = "";

temp 변수가 루프 밖에서 선언되어 있다.이로 인해 이전 루프의 문자열이 사라지지 않고 계속 누적된다.

첫 번째 루프: "123"

두 번째 루프: "123456"

N 번째 루프: "123456...789" (엄청나게 긴 문자열)

요약해서 _** temp가 루프를 돌수록 기하급수적으로 크기가 커졌기에 예외를 던진 것이다._ **

![](https://velog.velcdn.com/images/bluepaper14_/post/79860c89-053a-4d3f-80b7-9c617ed74e54/image.png)

아래가 완성된 코드다.

    
    
    #include <string>
    #include <vector>
    
    using namespace std;
    
    vector<int> solution(vector<string> intStrs, int k, int s, int l) {
        vector<int> answer;
    
        for(int j = 0; j < intStrs.size(); j++) {
            string x = intStrs[j];
            string temp = "";
            for(int i = s; i < s + l; i++) {
                temp += x[i];
            }
            if(stoi(temp) > k) {
                answer.push_back(stoi(temp));
            }
    }
        return answer;
    }


