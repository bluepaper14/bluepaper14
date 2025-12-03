---
title: [React] script 타입의 종류
date: Sat, 15 Nov 2025 05:20:50 GMT
link: https://velog.io/@bluepaper14/React-script-%ED%83%80%EC%9E%85%EC%9D%98-%EC%A2%85%EB%A5%98
---

<h3 id="script-type-속성">script type 속성</h3>
<p>같은 코드인데도 script의 type 속성에 따라 동작이 달라진다.</p>
<h3 id="typemodule">type=&quot;module&quot;</h3>
<pre><code class="language-script">&lt;script type=&quot;module&quot;&gt;
  a = 5;
  console.log(a);
  console.log(this);
&lt;/script&gt;</code></pre>
<p>a가 전역변수로 보이지만 결과적으로 전역으로 올라가지 않는다. console.log(a)는 잘 출력되지만 모듈 안에서 this는 undefined가 출력된다. <u>스크립트 전체가 독립된 모든 공간에서 실행된다</u></p>
<h3 id="typetextbabel">type=&quot;text/babel&quot;</h3>
<pre><code class="language-script">&lt;script type=&quot;text/babel&quot;&gt;
  a = 5;
  console.log(a);
  console.log(this);
&lt;/script&gt;</code></pre>
<p>Babel은 module과 다르게 결과적으로 전역 스크립트에서 실행된다. 즉 this값이 잘 출력된다.</p>
<h3 id="typetextjavascript">type=&quot;text/javascript&quot;</h3>
<pre><code class="language-script">&lt;script type=&quot;text/javascript&quot;&gt;
  a = 5;
  console.log(a);
  console.log(this);
&lt;/script&gt;</code></pre>
<p>스크립트도 상황은 babel과 동일하다. </p>
<p>요약해서 module은 완전한 독립공간이다. 전역에 영향을 주지 않는다. 반대로 babel과 javascript는 전역스코프로 작동된다. window에 변수가 바인딩된다. 즉 암묵적 전역변수로 사용가능하다. </p>