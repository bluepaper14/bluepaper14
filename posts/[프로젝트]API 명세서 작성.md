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

# | HTTP | 엔드포인트 | 설명 | 주요 기능  
---|---|---|---|---  
1 | **POST** | `/api/simulations` | 시뮬레이션 생성 | `SimulationCreateRequest` 기반으로 DB 저장, `pending` 상태로 반환  
2 | **GET** | `/api/simulations` | 시뮬레이션 목록 조회(사이드바) | 사용자별 시뮬레이션 목록, 최신순 정렬  
3 | **GET** | `/api/simulations/{id}/overview` | 개요 탭 데이터 | **Mock** : 전체 성공률, funnel 패널, 연령대별 통계  
4 | **GET** | `/api/simulations/{id}/issues` | 주요 이슈 탭 | **Mock** : 페이지별 이슈 목록, 심각도, 영향 사용자 수  
5 | **GET** | `/api/simulations/{id}/ai-fix` | AI 수정 제안 탭 | **Mock** : Before/After 코드, 영향도 설명  
6 | **GET** | `/api/simulations/{id}/heatmap` | 히트맵 탭 | **Mock** : 좌표 기반 오류 집계, 연령대 필터  
7 | **GET** | `/api/simulations/{id}/wcag` | WCAG 접근성 탭 | **Mock** : 규정 준수 점수, Critical/Moderate/Minor 분류


