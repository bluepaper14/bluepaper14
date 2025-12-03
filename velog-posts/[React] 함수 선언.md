---
title: "[React] 함수 선언"
date: Mon, 10 Nov 2025 04:31:36 GMT
categories: []
---

# [React] 함수 선언

<h3 id="react-함수의-기본형">React 함수의 기본형</h3>
<p>기본형은 다음과 같다.</p>
<pre><code class="language-javascript">function func1(str){    
    console.log(str);
}

func1(&quot;Hello, func1&quot;);</code></pre>
<p>이후 더욱 쉽게 표현하기 위해 표현식과 화살표 함수이다.</p>
<pre><code class="language-javascript">// func2: 함수 표현식으로 함수를 정의하고, 함수 호출하기
// 함수 표현식
const func2 = function(str){    
    console.log(str);
} 

func2(&quot;Hello, func2&quot;);


// func3: 화살표 함수로 함수를 정의하고, 함수 호출하기
// 화살표 함수
const func3 = (str) =&gt; {    
    console.log(str);
}

func3(&quot;Hello, func3&quot;);</code></pre>
<h3 id="함수-선언-예제">함수 선언 예제</h3>
<pre><code class="language-javascript">func4(&quot;Hello, func4&quot;);   // func4: 함수 선언문

function func4(str){
    console.log(str);
}</code></pre>
<p>이렇게 함수의 선언형이 주어질때 표현식과 화살표 함수로 수정하여 선언해보자.</p>
<pre><code class="language-javascript">//표현식
func4(&quot;Hello, func4&quot;);

const func4 = function(str) {
  console.log(str);
}

//화살표
func4(&quot;Hello, func4&quot;);

const func4 = (str) =&gt; {
  console.log(str);
}</code></pre>