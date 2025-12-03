---
title: "[React] 함수를 매개변수로 활용"
date: Sat, 15 Nov 2025 12:40:08 GMT
categories: []
---

# [React] 함수를 매개변수로 활용

<h3 id="1급-객체">1급 객체</h3>
<p>1급 객체는 값처럼 자유롭게 다룰 수 있는 데이터를 말한다. 함수를 변수에 담고, 다른 함수에 전달하고, 반환하고, 배열/객체 안에 넣는 것 모두 가능</p>
<h3 id="예제1">예제1</h3>
<pre><code class="language-javascript">const insideFn = logger =&gt; logger(&quot;함수를 다른 함수에 매개변수로 전달&quot;);
insideFn(message =&gt; console.log(message));</code></pre>
<p>insideFn은 logger라는 이름을 함수를 받음. 그리고 바로 실행.</p>
<ol>
<li>insideFn은 logger를 받음</li>
<li>indiseFn은 내부에서 logger를 실행</li>
</ol>
<h3 id="예제2">예제2</h3>
<pre><code class="language-javascript">const createScream = logger =&gt; message =&gt; logger(message.toUpperCase() + &quot;!!!&quot;);

const scream = createScream(message =&gt; console.log(message));
scream('function can return other functions');</code></pre>
<p>차라리 생략된 괄호나 인자를 더 붙어서 쉽게 돌아가보자.</p>
<pre><code class="language-javascript">const createScream = (logger) =&gt; {
    return (message) =&gt; {
        const newMessage = message.toUpperCase() + &quot;!!!&quot;;
        logger(newMessage);
    };
};

const scream = createScream((message) =&gt; {
    console.log(message);
});

scream(&quot;function can return other functions&quot;);</code></pre>
<p>1.createScream(console.log를 실행하는 함수)를 호출
2.내부에서 message → logger(newMessage) 하는 함수를 만들어 반환
3.scream은 그 만들어진 함수
4.scream(&quot;text&quot;) 호출 시 메시지를 대문자 + !!!로 바꿔서 출력</p>