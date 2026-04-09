---
title: "[프로젝트]API 명세서 작성"
date: Thu, 09 Apr 2026 07:40:11 GMT
url: "https://velog.io/@bluepaper14_/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8API-%EB%AA%85%EC%84%B8%EC%84%9C-%EC%9E%91%EC%84%B1%EB%B2%95"
tags: [velog, backup]
---

# [[프로젝트]API 명세서 작성](https://velog.io/@bluepaper14_/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8API-%EB%AA%85%EC%84%B8%EC%84%9C-%EC%9E%91%EC%84%B1%EB%B2%95)

### 들어가기 이전

이 페이지에 들어온 것은 어느정도 벡엔드 서버 구축와 프론트 목업디자인이 완성된 상태일 것이다. 하지만 우리는 클라이언트를 향한 API를
만들어주고 데이터들을 보내주는 통로를 만들어줘야하기 때문에 가장 기초적인 API 명세서에 대해서 알아보자.

### API정의

프론트 = 손님 벡엔드 = 주방 API = 웨이터

이렇게 손님이 어떠한 데이터를 요청하면 웨이터가 주방에게 전달하고 주방에서 만들 결과물을 쏴주는 것이다.

### API 명세

우리는 메뉴판을 만들기 위해 웨이터가 어떻게 주문을 받을지 메뉴얼을 만든다.
![](https://velog.velcdn.com/images/bluepaper14_/post/0ea027f9-d1f3-4625-95b8-c71cad79b012/image.svg)

### 프론트엔드 화면을 보고 API 목록 뽑기

기본적으로 화면에서 데이터를 주고받는 순간은 2가지이다.

**사용자가 무언가 제출해야할때** -> 서버로 데이터를 보내는 API(**POST**) **화면에 데이터가 표시되어야할때** -> 서버로
데이터를 가져오는 API(**GET**)

이것이 기본적인 것이고 API URL을 만들때는 **RESTful** 규칙을 따른다. 모든 자원은 고유한 URL로 만들기 위해서다.

Method | 역할 (Action) | 의미 및 설명  
---|---|---  
**GET** | 조회 (Read) | 서버로부터 특정 자원을 가져올 때 사용  
**POST** | 생성 (Create) | 서버에 새로운 자원을 등록할 때 사용  
**PUT** | 수정 (Update) | 자원 전체를 새로운 내용으로 덮어쓸 때 사용  
**PATCH** | 수정 (Update) | 자원의 일부 내용만 변경할 때 사용  
**DELETE** | 삭제 (Delete) | 특정 자원을 삭제할 때 사용  
  
이제 명세화 이전의 목록을 만들어보자.

화면 / 기능 | 주요 동작 및 내용 | 필요한 API  
---|---|---  
로그인 | 로그인 시도 및 JWT 토큰 발급 (이후 모든 요청 헤더에 포함) | POST /api/auth/login  
전체 공통 (내 정보) | 현재 로그인한 사용자 정보 조회 (우측 상단 아바타 표시용) | GET /api/auth/me  
홈 / 사이드바 공통 | 로그인 계정이 소유한 시뮬레이션 목록 불러오기 | GET /api/simulations  
시뮬레이션 초기 설정 | 시뮬레이션 생성 및 ID 발급 (URL, 페르소나 설정 등 전송) | POST /api/simulations  
진행 화면 | 시뮬레이션 진행률 및 상태 조회 (폴링 방식) | GET /api/simulations/{id}/status  
결과 전체 공통 | 시뮬레이션 제목, 생성일, 상태 등 기본 정보 조회 | GET /api/simulations/{id}  
결과 페이지 공통 | 방문한 페이지 목록 및 스크린샷 URL 조회 | GET /api/simulations/{id}/pages  
개요 | 전환율, AI 사용자 수, 평균 완료 시간 등 요약 데이터 표시 | GET /api/simulations/{id}/overview  
주요 이슈 | 페이지별 카테고리 분포 및 상세 이슈 목록 조회 | GET /api/simulations/{id}/pages/{pageId}/issues  
히트맵 | 연령대 필터링이 적용된 집계 클릭 좌표 및 오류 오버레이 표시 | GET /api/simulations/{id}/pages/{pageId}/heatmap  
WCAG | 웹 콘텐츠 접근성 준수 점수, 통과 테스트 수, 위반 목록 조회 | GET /api/simulations/{id}/pages/{pageId}/wcag  
AI 수정 | 이슈별 Before/After 코드 및 영향도 설명 조회 | GET /api/simulations/{id}/pages/{pageId}/aifix


