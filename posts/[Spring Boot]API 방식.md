---
title: "[Spring Boot]API 방식"
date: Sun, 05 Apr 2026 15:51:38 GMT
url: "https://velog.io/@bluepaper14_/Spring-BootAPI-%EB%B0%A9%EC%8B%9D"
tags: [velog, backup]
---

# [[Spring Boot]API 방식](https://velog.io/@bluepaper14_/Spring-BootAPI-%EB%B0%A9%EC%8B%9D)

### API

> **API:** 서로 다른 소프트웨어가 기능이나 데이터를 주고받을 수 있도록 정해놓은 인터페이스

바로 코드를 확인해보자.

### 예제

    
    
    package hello.hello_spring.controller;
    
    import org.springframework.stereotype.Controller;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestParam;
    import org.springframework.web.bind.annotation.ResponseBody;
    
    @Controller
    public class HelloController {
    
        @GetMapping("hello-api")
        @ResponseBody 
        public Hello helloApi(@RequestParam("name") String name) {
            Hello hello = new Hello();
            hello.setName(name); 
            return hello; 
        }
    
        static class Hello {
            private String name;
            public String getName() {
                return name;
            }
            public void setName(String name) {
                this.name = name;
            }
        }
    }

> @GetMapping :웹 브라우저에서 '/hello-api'요청이 들어오면 메서드 실행
    
    
    @GetMapping("hello-api")

> @ResponseBody : HTTP의 BODY에 이 데이터를 직접 넣겠다는 선언
    
    
    @ResponseBody

> ?name=spring이라고 입력하면, Spring이 URL을 확인하고 spring이라는 글자를 추출해서 name이라는 변수에 넣는다.
> 데이터를 담을 Hello 객체를 하나 만듭니다. 그리고 아까 받은 name("spring")을 상자 안에 예쁘게
> 넣습니다(setName). 이를 리턴한다.
    
    
    public Hello helloApi(@RequestParam("name") String name) {
            Hello hello = new Hello();
            hello.setName(name); 
            return hello; 
        }

** 1. HTTP 요청 ** 웹 브라우저나 클라이언트가 URL을 통해 서버에 요청을 보낸다.

예시: /hello-api?name=spring -> 데이터가 전달

**2\. 컨트롤러 매핑 및 파라미터 바인딩** 해당 URL을 처리할 컨트롤러(HelloController)를 찾는다. -> controll
먼저

**@RequestParam**("name")에 의해 URL의 spring이라는 문자열이 자바 변수 String name에 할당

**3\. @ResponseBody와 컨버터 작동** 메서드가 hello 객체를 리턴하면, Spring은 @ResponseBody
어노테이션을 확인

ViewResolver 대신 **HttpMessageConverter가 선택**

리턴 타입이 객체이므로, **JSON 변환기인 MappingJackson2HttpMessageConverter** 가 동작

*_5\. JSON 응답 *_ 변환기가 자바 객체를 JSON 문자열로 바꾼 뒤, HTTP 응답 바디에 담아 클라이언트에 보냄

최종 결과값: {"name":"spring"}

### Getter/Setter

private String name;만 쓰는것이 아니다. 왜냐하면 데이터를 넣고 뺄 수 있는 공식적인 통로가 필요하다.API 방식(JSON
변환)이 작동하려면 이 구조가 필수다.

    
    
    static class Hello {
            private String name;
            public String getName() {
                return name;
            }
            public void setName(String name) {
                this.name = name;
            }
        }

스프링이 객체를 JSON으로 바꿀 때 쓰는 도구다. 객체의 변수(name)를 직접 보는 게 아니라, getName()이라는 메서드 이름을
보고 "아, 이 객체에는 name이라는 데이터가 있구나!"라고 판단한다

    
    
    @Controller // 스프링이 시작될 때 이 클래스를 '컨트롤러(서버 입구)'로 자동 등록합니다.
    public class HelloController {
    
        @GetMapping("hello-api") // 사용자가 주소창에 /hello-api 라고 치고 들어오면 아래 메서드를 실행합니다.
        @ResponseBody // 중요! 이 메서드의 결과물을 HTML 파일에서 찾는 게 아니라, HTTP 응답의 바디(Body)에 직접 넣어서 보내겠다는 뜻입니다.
        public Hello helloApi(@RequestParam("name") String name) { 
            // @RequestParam("name"): 주소창의 ?name=spring 부분에서 'spring'을 꺼내서 자바 변수 'name'에 저장합니다.
            // Hello helloApi(...): 이 메서드는 최종적으로 'Hello'라는 객체(데이터 상자)를 밖으로 내보냅니다.
    
            Hello hello = new Hello(); // 데이터를 담기 위해 위에서 정의한 'Hello'라는 이름의 빈 상자(객체)를 하나 새로 만듭니다.
            hello.setName(name); // 사용자가 보내준 'spring'이라는 이름을 그 상자 안에 집어넣습니다.
    
            return hello; // 상자(객체)를 그대로 반환합니다. @ResponseBody가 붙어있으므로, 스프링이 이 상자를 JSON(문자 데이터)으로 자동 변환해서 사용자에게 쏩니다.
        }
    
        // 데이터를 담는 전용 상자의 설계도입니다.
        static class Hello {
            private String name; // 이름 데이터를 저장할 공간입니다. 'private'은 외부에서 이 변수를 직접 만지지 못하게 잠가둔 것입니다.
    
            // 상자 안의 이름을 밖으로 꺼내주는 통로(Getter)입니다. 스프링(Jackson 라이브러리)이 이 메서드를 호출해서 JSON을 만듭니다.
            public String getName() {
                return name;
            }
    
            // 상자 안에 이름을 새로 저장하거나 바꿀 때 쓰는 통로(Setter)입니다.
            public void setName(String name) {
                this.name = name; // 여기서 'this.name'은 위에서 선언한 변수이고, 'name'은 밖에서 전달받은 새로운 이름입니다.
            }
        }
    }


