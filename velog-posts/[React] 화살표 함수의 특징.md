---
title: [React] 화살표 함수의 특징
date: Mon, 10 Nov 2025 04:53:20 GMT
link: https://velog.io/@bluepaper14/React-%ED%99%94%EC%82%B4%ED%91%9C-%ED%95%A8%EC%88%98%EC%9D%98-%ED%8A%B9%EC%A7%95
---

<h3 id="화살표-함수의-특징">화살표 함수의 특징</h3>
<p>다시 기본형을 짚고 넘어가자</p>
<pre><code class="language-javascript">const fun4 = (str) =&gt; {
  console.log(str);
}

fun4(&quot;Hello, fun4&quot;);</code></pre>
<h3 id="매개변수-작성">매개변수 작성</h3>
<p>위 코드처럼 매개변수는 () 괄호를 통해 작성하고 있다. </p>
<pre><code class="language-javascript">const aFunc2 = () =&gt; 100 + 200; //필수
const aFunc3 = val =&gt; val + 200; //선택
const aFunc1 = (val1, val2) =&gt; val1 + val2; //필수</code></pre>
<table>
<thead>
<tr>
<th>경우</th>
<th>문법</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td>매개변수가 <strong>없을 때</strong></td>
<td><code>()</code> 필수</td>
<td><code>const f = () =&gt; {...}</code></td>
</tr>
<tr>
<td>매개변수가 <strong>1개일 때</strong></td>
<td><code>()</code> 생략 가능</td>
<td><code>const f = x =&gt; x + 1</code></td>
</tr>
<tr>
<td>매개변수가 <strong>2개 이상일 때</strong></td>
<td><code>()</code> 필수</td>
<td><code>const f = (x, y) =&gt; x + y</code></td>
</tr>
<tr>
<td>매개변수가 1개일때 괄호가 생략 가능하다는 점을 유의하자.</td>
<td></td>
<td></td>
</tr>
</tbody></table>
<h3 id="함수-본문body-작성-규칙">함수 본문(body) 작성 규칙</h3>
<p>화살표 함수를 사용하면 꽤나 코드를 줄일 수 있다. </p>
<pre><code class="language-javascript">const aFunc4a = val =&gt; { return val + 200; };
const aFunc4b = val =&gt; val + 200;</code></pre>
<table>
<thead>
<tr>
<th>경우</th>
<th>문법</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>여러 문장일 때</td>
<td><code>{}</code> 필수, <code>return</code> 필요</td>
<td><code>js const f = x =&gt; { let y = x+1; return y; }</code></td>
</tr>
<tr>
<td>한 줄로 반환 시</td>
<td><code>{}</code> 생략 + <code>return</code> 생략 가능</td>
<td><code>js const f = x =&gt; x + 1;</code></td>
</tr>
<tr>
<td>이와 같이 한줄로 반환한는 간단한 함수라면 return 그리고 {}가 생략 가능하다.</td>
<td></td>
<td></td>
</tr>
</tbody></table>
<h3 id="호이스팅-여부">호이스팅 여부</h3>
<p>화살표함수는 호이스팅이 되지 않는다. 즉 정의하기전에 호출하면 오류가 발생한다.</p>
<pre><code>console.log(aFunc5(100)); // ❌ ReferenceError
const aFunc5 = val =&gt; val + 200;</code></pre><h3 id="this-바인딩-여부">this 바인딩 여부</h3>
<p>화살표 함수는 자신만의 this를 가지지 않는다. 즉 상위 스코프의 this를 그대로 사용한다. </p>
<pre><code class="language-javascript">function Counter() {
  this.count = 0;
  setInterval(() =&gt; {  // 화살표 함수
    this.count++;
    console.log(this.count); // this는 Counter 객체
  }, 1000);
}
</code></pre>