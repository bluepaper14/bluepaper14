# [React] 불변성

Parsed from [Velog](https://velog.io/@bluepaper14/React-%EB%B6%88%EB%B3%80%EC%84%B1)

Date: Sat, 15 Nov 2025 12:54:09 GMT

---

<h3 id="불변성">불변성</h3>
<p>객체의 불변성은 원본을 직접 수정하지 않는다.  즉 변경이 필요하면 새로운 복사본을 만들어 그 복사본을 수정한다.</p>
<h3 id="objectassign">Object.assign()</h3>
<pre><code class="language-javascript">var rateColor = function(obj, rating) {
  return Object.assign({}, obj, { rating: rating });
};</code></pre>
<p>첫번째 인자 {} 에 모든 obj의 속성을 복사하고 rating에 대한 것만 덮어쓰기한다. 즉 새 객체가 만들어지면 원본 걱정이 없다.</p>
<h3 id="스프레드-연산자">스프레드 연산자</h3>
<pre><code class="language-javascript">const rateColor = (obj, rating) =&gt; ({
  ...obj,
  rating
});</code></pre>
<p>아니면 스프레드 연산자를 사용해 모든 key-value를 복사시킨다. </p>