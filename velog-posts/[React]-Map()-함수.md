# [React] Map() 함수

Parsed from [Velog](https://velog.io/@bluepaper14/React-Map-%ED%95%A8%EC%88%98)

Date: Sat, 15 Nov 2025 16:29:19 GMT

---

<h3 id="map-함수-발단">Map() 함수 발단</h3>
<p>기본적으로 javascript에서 배열은 여러 데이터를 순서대로 모아놓는다. 그래서 일반적으로 배열에 대한 데이터를 하나씩 처리하려면 for문을 사용한다.</p>
<pre><code class="language-javascript">
const fruits = [&quot;apple&quot;, &quot;banana&quot;, &quot;orange&quot;];
for (let i = 0; i &lt; fruits.length; i++) {
    console.log(fruits[i]);
}</code></pre>
<p>이를 더 간결하게 나타내고자 Map() 함수가 등장하였다.</p>
<h3 id="map-함수">Map() 함수</h3>
<p>map() 함수는 배열의 각 요소를 가공하여 새로운 배열로 반환하는 함수이다.
<u>기존 배열은 변경되지 않고 새배열을 반환한다. 또한 콜벡함수</u></p>
<pre><code class="language-javascript">const numbers = [1, 2, 3];
const doubled = numbers.map(num =&gt; num * 2);

console.log(doubled); // [2, 4, 6]
console.log(numbers); // [1, 2, 3] 기존 배열은 그대로
</code></pre>
<p>객체 변환할때에는</p>
<pre><code class="language-javascript">const fruits = [&quot;apple&quot;, &quot;banana&quot;];
const objFruits = fruits.map(fruit =&gt; ({ name: fruit }));

console.log(objFruits);
// [{name: &quot;apple&quot;}, {name: &quot;banana&quot;}]</code></pre>
<h3 id="예제1">예제1</h3>
<h4 id="문자열-길이-배열">문자열 길이 배열</h4>
<pre><code class="language-javascript">const fruits = [&quot;apple&quot;, &quot;banana&quot;, &quot;orange&quot;];
// 각 과일 이름의 길이를 배열로
const lengths = fruits.map(fruit =&gt; fruit.length);

console.log(lengths); // [5, 6, 6]</code></pre>
<p>fruit.length로 길이를 배열로 출력했다. </p>
<h4 id="객체-배열-특정-값-추출">객체 배열 특정 값 추출</h4>
<pre><code class="language-javascript">const users = [
  { name: &quot;Alice&quot;, age: 25 },
  { name: &quot;Bob&quot;, age: 30 },
  { name: &quot;Charlie&quot;, age: 35 }
];

// 이름만 뽑아서 새 배열 생성
const names = users.map(user =&gt; user.name);
// const sameUsers = users.map(user =&gt; user); 그대로 객체 배열 출력
console.log(names); // [&quot;Alice&quot;, &quot;Bob&quot;, &quot;Charlie&quot;]
</code></pre>
<p>user.name으로  순서대로 이름만 뽑아서 새 배열을 생성하였다. </p>