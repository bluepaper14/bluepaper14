# [React] 고차함수 예제

Parsed from [Velog](https://velog.io/@bluepaper14/React-%EA%B3%A0%EC%B0%A8%ED%95%A8%EC%88%98-%EC%98%88%EC%A0%9C)

Date: Sat, 15 Nov 2025 17:08:16 GMT

---

<p>이전에 1급 함수가 있었는데 이는 고차함수이다. 1급 객체의 조건은 다음과 같았다.</p>
<ul>
<li>변수에 할당이 가능</li>
<li>매개변수로 전달 가능</li>
<li>함수에서 반환 가능</li>
</ul>
<p>즉 함수가 값처럼 취급될 수 있으면 1급 함수이다.</p>
<p>고차함수는 1급함수를 전제로 작동한다. 하지만 변수에 할당만 해도 1급함수이지만 고차함수가 되기 위해선 리턴이 있어야한다. </p>
<pre><code class="language-javascript">const invokeIf = (condition, fnTrue, fnFalse) =&gt; 
    (condition) ? fnTrue() : fnFalse();

const showWelcome = () =&gt; console.log(&quot;Welcome!!!&quot;);
const showUnauthorized = () =&gt; console.log(&quot;Unauthorized!!!&quot;);

invokeIf(true, showWelcome, showUnauthorized)
invokeIf(false, showWelcome, showUnauthorized)
</code></pre>
<p>invokeIF는 고차함수이다. condition이 true이면 fnTrue()호출 false이면 fnFalse()를 호출한다.</p>
<pre><code class="language-javascript">const userLogs = userName =&gt; message =&gt; console.log(`${userName} -&gt; ${message}`);
const log = userLogs(&quot;grandpa23&quot;);

log(&quot;attempted to load 20 fake members&quot;);
</code></pre>
<p>userLogs는 화살표함수이다. userName을 받아 새로운 함수를 반환하고 있다. </p>
<pre><code class="language-javascript">message =&gt; console.log(`${userName} -&gt; ${message}`)</code></pre>
<p>매개변수 message를 받아 로그를 출력한다. 이를 커링이라고 한다.</p>
<blockquote>
<p>커링 : 한 번에 여러 매개변수를 받지 않고 단계별로 함수가 반환되는 패턴</p>
</blockquote>