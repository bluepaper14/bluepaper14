---
title: "Python 문자열 파싱: 예외 처리를 고려한 비밀번호 생성기"
date: Sat, 14 Feb 2026 08:19:11 GMT
url: "https://velog.io/@bluepaper14_/Python-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8C%8C%EC%8B%B1-%EC%98%88%EC%99%B8-%EC%B2%98%EB%A6%AC%EB%A5%BC-%EA%B3%A0%EB%A0%A4%ED%95%9C-%EA%B2%AC%EA%B3%A0%ED%95%9C-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%83%9D%EC%84%B1%EA%B8%B0"
tags: [velog, backup]
---

# [Python 문자열 파싱: 예외 처리를 고려한 비밀번호 생성기](https://velog.io/@bluepaper14_/Python-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8C%8C%EC%8B%B1-%EC%98%88%EC%99%B8-%EC%B2%98%EB%A6%AC%EB%A5%BC-%EA%B3%A0%EB%A0%A4%ED%95%9C-%EA%B2%AC%EA%B3%A0%ED%95%9C-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%83%9D%EC%84%B1%EA%B8%B0)

### 문자열처리를 가지고 비밀번호 만들어보자.

파이썬 문자열 처리를 학습하다가 사이트의 이름을 가지고 비밀번호가 생성되도록 만들어보자. 규칙은 간단하여 아래와 같이 코드를 작성할 수
있다.

> 규칙1. http:// 부분은 제외한다. 규칙2. 처음 만나는 점(.) 이후 부분은 제외한다. 규칙3. 남은 글자중 처음 세자리 + 글자
> 갯수 + 글자 내 'e'개수 + "!"로 구성
    
    
    site = input("사이트를 입력하시오: ")
    rule1 = site.replace("http://", "") 
    rule1 = rule1[:rule1.index(".")]
    password = str(rule1[0:3]) + str(len(rule1)) + str(rule1.count('e')) + '!'
    print("{0} 의 비밀번호는 {1} 입니다.".format(site, password))
    
    
    > python .\practice.py
    사이트를 입력하시오: http://naver.com
    http://naver.com 의 비밀번호는 nav51! 입니다.

이런식으로 비밀번호를 만들었다. 하지만 위 문제는 여러 예외사항을 고려하지 않고 무작정 만들었기 때문에 여러 규칙들을 더 추가해서 그럴듯한
프로그램을 만들어보자.

### http https등 여러 경우들..

> "naver.com" → # 프로토콜 입력이 없을때 "[https://naver.com"](https://naver.com")
> "[ftp://naver.com"](ftp://naver.com") → # 새로운 통신 프로토콜일때
> "http://////naver.com" → #슬래시를 중복으로 입력받을때.

먼저 통신 프로토콜 부분이다. 초기 코드는 http범위만 상정하여 코드를 작성했기에 s를 추가하여 사이트를 입력한다면

    
    
    사이트를 입력하시오: https://naver.com
    https://naver.com 의 비밀번호는 htt131! 입니다.

이렇게 출력된다. replace의 문자열 리터럴이 동일하지 않으면 제외하지 않고 그대로 출력한다. 그럼 여러 프로토콜 그리고 잘못 입력한
경우가 있다면 어떻게 처리할까.

    
    
    if site[4] == 's' :
        rule1 = site.replace("https://", "") 
    else :
        rules = site.replace("http://", "")

이렇게 분기를 나누면 좋긴하지만 더 가독성 있는 코드가 있는지 살펴보았다. 바로 splite이다. 어차피 제외할거면 굳이 분기로 코드를 길게
할 필요가 없다.

    
    
    rule1 = site.split("//")[-1]

만약 단순히 [1]을 사용해도 정상 동작한다. 하지만 [-1]을 사용하는 이유는 입력값이 다양하기에 이렇게 하였다.

이처럼 슬래시가 다수 존재하든 존재하지 않든 항상 마지막 요소가 도메인 부분이 되도록 설계했다._항상 마지막 결과를 사용한다_

### (.)점이 중복되서 나온다면?

    
    
    rule1 = rule1[:rule1.index(".")]

이제는 .을 해결할 차례다. 슬라이싱과 index를 이용해서 .com을 제거하였다. 하지만 .이 2개 이상 포함될 수 있다.

> blog.naver.com → 점이 중복되어 위 코드대로 한다면 blog문자열만 추출된다.

이를 어떻게 해결할까 생각했는데 애초에 .이 없을수도 있지 않은가..비밀번호를 생성할때 naver 문자열만 사용한다고 가정할때 이것도
split을 이용하는게 가장 깔끔하다.

    
    
    rule2 = split(".")[-2]

![](https://velog.velcdn.com/images/bluepaper14_/post/a221ac0c-e3bf-48bb-
ba69-83d47f0810d0/image.png)

하지만 (.)점이 없는 경우도 생각하면 [-2]를 작성시 정상적으로 가져오지 못한다. 이는 분기를 나눠보자.

    
    
    parts = rule1.split(".")
    if len(parts) >= 2: #parts의 리스트 개수가 2개 이상이면 .이 한개는 있는거다.
        rule1 = parts[-2]
    else:
        rule1 = parts[0]

이렇게 리스트의 개수가 2개 이상은 .이 최소 한개는 있는 것이고 없다면 리스트를 바로 출력하도록 하였다.

최종 코드이다

    
    
    site = input("사이트를 입력하시오: ")
    rule1 = site.split("//")[-1]
    
    parts = rule1.split(".")
    if len(parts) >= 2: #parts의 리스트 개수가 2개 이상이면 .이 한개는 있는거다.
        rule1 = parts[-2]
    else:
        rule1 = parts[0]
    
    password = str(rule1[0:3]) + str(len(rule1)) + str(rule1.count('e')) + '!'
    print("{0} 의 비밀번호는 {1} 입니다.".format(site, password))

여러 문제들을 작성하고 풀때 스스로 예외처리를 고려해서 설계하는 습관을 잘 기르도록 하자.


