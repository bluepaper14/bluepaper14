---
title: "[React] 순수함수"
date: Sat, 15 Nov 2025 13:13:18 GMT
categories: []
---

# [React] 순수함수

**bluepaper14** · *Sat, 15 Nov 2025 13:13:18 GMT*



---
<br/>

<h3 id="순수함수">순수함수</h3>
<p>순수함수는 같은 입력이면 항상 같은 출력을 반환하고 외부 상태를 변경하지 않으며 외부 상태에 의존하지 않는 함수다.</p>
<h3 id="예제1">예제1</h3>
<pre><code class="language-javascript">let frederick = {
  name: &quot;Frederick Douglass&quot;,
  canRead: false,
  canWrite: false
};

// 비순수 함수
function selfEducate() {
  frederick.canRead = true;
  frederick.canWrite = true;
}

console.log(frederick);

selfEducate();

console.log(frederick);
</code></pre>
<p>여기서 selfEducate는 비순수 함수다. 왜냐하면</p>
<ol>
<li>인자가 없다. -&gt; 입력값으로 출력이 결정 x</li>
<li>return이 없다 -&gt; 내부에서 무언갈 바꿔버린다</li>
<li>외부변수 frederick을 직접 변경시킴</li>
</ol>
<p>이런 함수는 예측불가하기에 사이드이팩트가 발생</p>
<blockquote>
<p>사이드이팩트 : 함수가 자기 스코프 밖의 상태를 변경하거나 외부 세계와 상호작용하는 것</p>
</blockquote>
<h3 id="예제2">예제2</h3>
<pre><code class="language-javascript">let frederick = {
    name: &quot;Frederick Douglass&quot;,
    canRead: false,
    canWrite: false
};

// 스프레드 연산자로 순수함수 만들기
const selfEducate = person =&gt;
    ({
        ...person,
        canRead: true,
        canWrite: true
    })

console.log(frederick);

console.log(selfEducate(frederick));

console.log(frederick);
</code></pre>
<p>스프레드 연산자를 사용해서 person 객체를 복사한 새 객체를 만들어서 반환한다.</p>