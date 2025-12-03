---
title: [React] 배열을 문자열로 출력
date: Sat, 15 Nov 2025 13:26:03 GMT
link: https://velog.io/@bluepaper14/React-%EB%B0%B0%EC%97%B4%EC%9D%84-%EB%AC%B8%EC%9E%90%EC%97%B4%EB%A1%9C-%EC%B6%9C%EB%A0%A5
---

<h3 id="예제1">예제1</h3>
<pre><code class="language-javascript">const address = [
    &quot;Division of Computer Engineering&quot;,
    &quot;Hansung University&quot;,
    &quot;116&quot;,
    &quot;Samseongyo-ro&quot;,
    &quot;16-gil&quot;,
    &quot;Seongbuk-gu&quot;,
    &quot;Seoul&quot;,
    &quot;02876&quot;,
    &quot;South Korea&quot;
];

console.log(address);
console.log(address.join(&quot;, &quot;));</code></pre>
<p>배열이 아닌 문자열로 출력할 때는 join(&quot;,&quot;)으로 배열의 모든 요소를 &quot;,&quot;로 연결해서 하나의 긴 문자열로 만든다.</p>
<h3 id="예제2">예제2</h3>
<pre><code class="language-javascript">const address = [
    &quot;Division of Computer Engineering&quot;,
    &quot;Hansung University&quot;,
    &quot;116&quot;,
    &quot;Samseongyo-ro&quot;,
    &quot;16-gil&quot;,
    &quot;Seongbuk-gu&quot;,
    &quot;Seoul&quot;,
    &quot;02876&quot;,
    &quot;South Korea&quot;
];

console.log(address);
const addr = address.filter(el =&gt; el[0] === &quot;S&quot;);
console.log(addr);</code></pre>
<p>이번엔 배열의 요소중 첫 글자가 S인 요소만 출력시킨다.</p>
<h3 id="예제3">예제3</h3>
<pre><code class="language-javascript">const address = [
    &quot;Division of Computer Engineering&quot;,
    &quot;Hansung University&quot;,
    &quot;116&quot;,
    &quot;Samseongyo-ro&quot;,
    &quot;16-gil&quot;,
    &quot;Seongbuk-gu&quot;,
    &quot;Seoul&quot;,
    &quot;02876&quot;,
    &quot;South Korea&quot;
];

console.log(address);
const newFilter = (list, cond) =&gt; list.filter(el =&gt; el[0] !== cond);
console.log(newFilter(address, 'S'));</code></pre>
<p>이번엔 요소중 첫 글자가 S가 아닌 요소만 출력시킨다.</p>