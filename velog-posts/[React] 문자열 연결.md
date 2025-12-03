---
title: "[React] 문자열 연결"
date: Mon, 10 Nov 2025 04:17:06 GMT
categories: []
---

# [React] 문자열 연결

<h3 id="js-방식의-기본적인-문자열-연결">JS 방식의 기본적인 문자열 연결</h3>
<p>아래 코드와 같다.</p>
<pre><code class="language-javascript">let i1 = 10;
let i2 = 20;
let i3 = 30;

// 출력 예:
// 10 + 20 + 30 = 60
// 10, 20, 30을 모두 더하면 60입니다.

// 일반 문자열로 조합하여 출력

let sum = i1 + i2 + i3;
console.log(i1 + &quot; + &quot; + i2 + &quot; + &quot; + i3 + &quot; = &quot; + sum);
console.log(i1 + &quot;,&quot; + i2 + &quot;,&quot; + i3 + &quot;을 모두 더하면 &quot; + sum + &quot;입니다.&quot;);</code></pre>
<p>이런식으로 문자열은 큰 따옴표 안으로 처리하여 출력가능하다. 불편하니 이번에 템플릿 문자열로 출력해보자.</p>
<pre><code class="language-javascript">let i1 = 10;
let i2 = 20;
let i3 = 30;

let sum = i1 + i2 + i3;
// 출력 예:
// 10 + 20 + 30 = 60
// 10, 20, 30을 모두 더하면 60입니다.

// 템플릿 문자열 활용
console.log(`${i1} + ${i2} + ${i3} = ${sum}`);
console.log(`${i1}, ${i2}, ${i3}을 모두 더하면 ${sum}입니다.`);</code></pre>
<p>위와 같이 `(백틱)으로 감싸서 문자열 안에 변수나 표혁식을 ${} 형태로 넣을 수 있다.</p>