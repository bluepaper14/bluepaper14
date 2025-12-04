# [React] 객체 리터럴

Parsed from [Velog](https://velog.io/@bluepaper14/React-%EA%B0%9D%EC%B2%B4-%EB%A6%AC%ED%84%B0%EB%9F%B4)

Date: Sat, 15 Nov 2025 07:36:18 GMT

---

<h3 id="객체-리터럴">객체 리터럴</h3>
<p>구조분해할당의 연장선이다. 리터럴이라는 말은 말 그대로 그 자체로 값을 나타내는 표기법이다. 그럼 객체 리터럴은</p>
<pre><code class="language-javascript">const person = {
  name: &quot;Alice&quot;,
  age: 25
};</code></pre>
<p>이런식으로 Person이라는 객체 안에 이름 - 값 쌓으로 모아놓은 것을 객체 리터럴이라고 부른다.</p>
<h3 id="객체-리터럴의-개선">객체 리터럴의 개선</h3>
<pre><code class="language-javascript">var name = &quot;Tallac&quot;;
var elevation = 9738;

var funHike = {
  name: name,
  elevation: elevation,
  print: function() {
    console.log(this.name + &quot; 산의 높이는 &quot; + this.elevation + &quot;피트입니다.&quot;);
  }
};

funHike.print();
// Tallac 산의 높이는 9738피트입니다.</code></pre>
<p>변수 이름과 객체속성에 대한 이름이 같더라도 반복해서 작성해야한다. 함수선언도 정의할때 function 키워드를 작성해야한다. </p>
<pre><code class="language-javascript">const name = &quot;Tallac&quot;;
const elevation = 9738;

const funHike = {
  name,            // 변수 이름과 속성 이름 동일 → 생략 가능
  elevation,
  print() {        // function 키워드 생략
    console.log(`${this.name} 산의 높이는 ${this.elevation}피트입니다.`);
  }
};

funHike.print();
// Tallac 산의 높이는 9738피트입니다.</code></pre>
<p>개선되어 변수 이름과 객체 속성이 이름이 같다면 한번만 작성해도된다.</p>
<h3 id="스프레드-연산자">스프레드 연산자</h3>
<p>스프레드(...) = 객체/배열을 얕게 복사해서 새로운 객체를 만드는 문법</p>
<h4 id="배열-합치기">배열 합치기</h4>
<pre><code class="language-javascript">var peaks = [&quot;대청봉&quot;, &quot;중청봉&quot;, &quot;소청봉&quot;];
var canyons = [&quot;천불동계곡&quot;, &quot;가야동계곡&quot;];
var seoraksan = [...peaks, ...canyons];

console.log(seoraksan.join(', '));</code></pre>
<p>...은 스프레드 연산자로 배열의 객체를 요소로 풀어서 나열한다.</p>
<h4 id="배열-뒤집기">배열 뒤집기</h4>
<pre><code class="language-javascript">var peaks = [&quot;대청봉&quot;, &quot;중청봉&quot;, &quot;소청봉&quot;];
var [last] = peaks.reverse();

console.log(last);
console.log(peaks.join(', '));
console.log(peaks);</code></pre>
<p>배열 순서를 뒤집었다. 구조분해할당으로 배열의 첫값을 last에 담았다.</p>
<h4 id="배열-복사후-뒤집기">배열 복사후 뒤집기</h4>
<pre><code class="language-javascript">var peaks = [&quot;대청봉&quot;, &quot;중청봉&quot;, &quot;소청봉&quot;];
var [last] = [...peaks].reverse();

console.log(last); // 소청봉
console.log(peaks.join(', '));</code></pre>
<p>peaks로 배열의 복사후 뒤집었으므로 원본 배열에 영향을 받지 않는다.</p>
<pre><code class="language-javascript">function directions(...args) {
  const [start, ...remaining] = args
  const [finish, ...stops] = remaining.reverse()

  console.log(`${args.length} 도시를 운행합니다.`)
  console.log(`${start}에서 출발합니다.`)
  console.log(`목적지는 ${finish}입니다.`)
  console.log(`중간에 ${stops.length}군데 들립니다.`)
}

directions(&quot;서울&quot;,&quot;수원&quot;,&quot;천안&quot;,&quot;대전&quot;,&quot;대구&quot;,&quot;부산&quot;)</code></pre>
<pre><code class="language-javascript">
``` javascript
const morning = {
  breakfast: &quot;미역국&quot;,
  lunch: &quot;삼치구이와 보리밥&quot;
}
const dinner = &quot;스테이크 정식&quot;
const backpackingMeals = {
  ...morning,   // morning 과 비교
  dinner
}

console.log(backpackingMeals)</code></pre>