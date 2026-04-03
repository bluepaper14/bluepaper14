---
title: "[Spring Boot]MVC"
date: Fri, 03 Apr 2026 07:41:08 GMT
url: "https://velog.io/@bluepaper14_/Spring-BootMVC"
tags: [velog, backup]
---

# [[Spring Boot]MVC](https://velog.io/@bluepaper14_/Spring-BootMVC)

### MVC

> **MVC**(Model, View, Controller) : 데이터, 화면, 제어 로직을 분리하여 각자의 역할에만 집중하게 만드는
> 소프트웨어 설계 방식

바로 코드로 확인해보자.

### 예제코드

초기 설정으로는 현재 controller패키지 안에 HelloController 그리고 templates내부에 hello.html이
존재한다.

    
    
    package hello.hello_spring.controller;
    
    import org.springframework.ui.Model;
    import org.springframework.stereotype.Controller;
    import org.springframework.web.bind.annotation.GetMapping;
    
    @Controller
    public class HelloController {
        @GetMapping("hello")
        public String hello(Model model) {
            model.addAttribute("data", "spring!!");
            return "hello";
        }
    }

> @Controller: 이 클래스가 스프링 MVC의 컨트롤러임을 선언하고 있다. 스프링 컨테이너가 실행될 때 이 애노테이션(라벨)을 보고
> 객체를 생성하여 관리한다.
    
    
    @Controller

> @GetMapping : 웹 브라우저에서 '/hello'라는 경로로 _GET_ 방식의 요청이 들어오면 이 메서드를 실행합니다.
    
    
    @GetMapping("hello")

GET은 서버로부터 정보를 조회하기 위한 요청 방식이다. POST는 서버의 리소스를 생성하거나 데이터를 제출하기 위한 방식이다.

정리하면 서버는 주소창에 hello라고 치고 들어온 GET요청은 이 메서드에서 처리하자! 라는 의미.

> Model 객체 : 데이터를 담아서 뷰로 전달하는 바구니 역할이다. key는 data value는 spring!!으로 설정하여 모델에
> 담았다. View Resolver : 컨트롤러에서 문자열을 반환하면 뷰 리졸버가 해당 이름의 파일을 찼는다. 기본적으로
> 'resources/templates/hello.html' 파일을 찾아 렌더링한다.
    
    
    public String hello(Model model) {
            model.addAttribute("data", "spring!!");
            return "hello";
        }
    
    
    <!DOCTYPE HTML>
    <html xmlns:th="http://www.thymeleaf.org">
    <head>
        <title>Hello</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    </head>
    <body>
    <p th:text="'안녕하세요. ' + ${data}" >안녕하세요. 손님</p>
    </body>
    </html>

정리하면 프로그램 순서는 이러하다.

  1. 사용자 요청(localhost:8080/hello)
  2. Controller Mapping(GET요청 인식하고 메서드 실행)
  3. Model 준비(Model 객체에 값 담아 준비)
  4. View 찾기(파일 찾아 랜더링 할준비함)
  5. 응답(${data}부분을 추적하여 값으로 치환)


