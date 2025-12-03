---
title: [React] 구조분해 할당
date: Sat, 15 Nov 2025 06:57:19 GMT
link: https://velog.io/@bluepaper14/React-%EA%B5%AC%EC%A1%B0%EB%B6%84%ED%95%B4-%ED%95%A0%EB%8B%B9
---

<h3 id="구조분해할당">구조분해할당</h3>
<p>객체나 배열 안에 있는 값을 꺼내서 변수에 쉽게 담는 문법이다.</p>
<pre><code class="language-javascript">var bread = sandwich.bread;
var meat = sandwich.meat;</code></pre>
<p>기존 방식은 sandwich객체를 작성해서 호출한다. 이를</p>
<pre><code class="language-javascript">var { bread, meat } = sandwich;</code></pre>
<p>이렇게 동일한 이름의 변수로 집어넣을 수 있다. 예를 들어보자.</p>
<pre><code class="language-javascript">&lt;script type=&quot;module&quot;&gt;

// 객체 구조분해
var sandwich =  {
  bread: &quot;더치-크런치&quot;,
  meat: &quot;참치&quot;,
  cheese: &quot;스위스&quot;,
  toppings: [&quot;상추&quot;, &quot;토마토&quot;, &quot;머스타드&quot;]
}

// 구조분해 할당
var {bread, meat} = sandwich
console.log(bread, meat) //1

// 새로운 값 대입
bread = &quot;마늘&quot;
meat = &quot;칠면조&quot;

console.log(bread, meat)
console.log(sandwich.bread, sandwich.meat)

&lt;/script&gt;
</code></pre>
<p>sandwich라는 한 객체를 구조분해했다. 여기서 </p>
<pre><code class="language-javascript">var {bread, meat} = sandwich</code></pre>
<p>이런식으로 구조분해할당을 하였다. 객체 안의 있는 값을 그대로 담았다. </p>
<pre><code class="language-javascript">console.log(bread, meat) //1</code></pre>
<p>해당 출력의 결과는 구조분해할당한 값에 들어가 다음과 같이 출력된다.</p>
<pre><code>더치-크런치 참치</code></pre><p>하지만 여기서 새로운 값을 대입하고 console.log를 확인해보자.</p>
<pre><code class="language-javascript">console.log(bread, meat)
console.log(sandwich.bread, sandwich.meat)</code></pre>
<p>두번째 console은 값이 바뀌었으니 출력값이</p>
<pre><code>마늘 칠면조</code></pre><p>하지만 세번째 console은 객체 내부 데이터가 바뀌지 않았기에 그대로이다.</p>
<h3 id="객체의-구조분해할당">객체의 구조분해할당</h3>
<pre><code class="language-javascript">const lordify = regularPerson =&gt; {
  console.log(`캔터베리의 ${regularPerson.firstname}`)
}

const regularPerson = {
  firstname: &quot;현석&quot;,
  lastname: &quot;오&quot;
}

lordify(regularPerson)
</code></pre>
<pre><code>캔터베리의 현석</code></pre><p>현재 상황은 lordify가 regularPerson 전체 객체를 인자로 받는다. 그래서 해당 함수 내부에서 .으로 접근해야한다. 
이를 구조분해할당해보자.</p>
<pre><code class="language-javascript">const lordify = ({ firstname }) =&gt;
  console.log(`캔터베리의 ${firstname}`)

const regularPerson = {
  firstname: &quot;현석&quot;,
  lastname: &quot;오&quot;
}

lordify(regularPerson)</code></pre>
<p>이런식으로 함수 인자 괄호안에 {firstname} 이렇게 작성하면 regularPerson 객체에서 firstname 속성만 바로 꺼내서 변수 firstname으로 바로 사용이 가능하다. </p>
<h3 id="배열의-구조분해할당">배열의 구조분해할당</h3>
<pre><code class="language-javascript">const [firstResort] = [&quot;용평&quot;,&quot;평창&quot;,&quot;강촌&quot;];
console.log(firstResort); // 용평</code></pre>
<pre><code>용평</code></pre><p>배열 요소의 순서에서 첫번째 배열을 가리켜 출련된다.</p>
<pre><code class="language-javascript">const array = [&quot;용평&quot;,&quot;평창&quot;,&quot;강촌&quot;];
const [,,thirdResort] = array;
console.log(thirdResort); // 강촌
</code></pre>
<p>이번엔 ,,를 이용해서 해당 위치의 요소를 건너뛰고 3번째 요소만 thirdResort에 할당하여 출력하였다. 즉 필요한 값을 바로 가져올수 있다.</p>