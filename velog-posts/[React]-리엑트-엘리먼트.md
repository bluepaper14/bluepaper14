# [React] 리엑트 엘리먼트

Parsed from [Velog](https://velog.io/@bluepaper14/React-%EB%A6%AC%EC%97%91%ED%8A%B8-%EC%97%98%EB%A6%AC%EB%A8%BC%ED%8A%B8)

Date: Sun, 16 Nov 2025 11:49:24 GMT

---

<h3 id="리엑트-앨리먼트">리엑트 앨리먼트</h3>
<p>엘리먼트는 리액트 앱을 구성하는 가장 작은 단위를 의미한다. 예를 들어보자.</p>
<h3 id="리엑트-엘리먼트-생성---문자열">리엑트 엘리먼트 생성 - 문자열</h3>
<pre><code class="language-javascript">const addr = React.createElement(
    &quot;section&quot;, 
    {id: &quot;address&quot;},
    React.createElement(
        &quot;ul&quot;,
        {className: &quot;contents&quot;},</code></pre>
<p>가장먼저 section이라는 독립된 공간을 만들었다. 이에 대한 이름표로 address라는 이름표를 붙었다.
다음은 그 안에 ul 이라는 방을 만들고 이름을 contents로 지었다. </p>
<pre><code class="language-javascript">const addr = React.createElement(
    &quot;section&quot;, 
    {id: &quot;address&quot;},
    React.createElement(
        &quot;ul&quot;,
        {className: &quot;contents&quot;},
        React.createElement(&quot;li&quot;, null, &quot;Division of Computer Engineering&quot;),
        React.createElement(&quot;li&quot;, null, &quot;Hansung University&quot;),
        React.createElement(&quot;li&quot;, null, &quot;116&quot;),
        React.createElement(&quot;li&quot;, null, &quot;Samseongyo-ro&quot;),
        React.createElement(&quot;li&quot;, null, &quot;16-gil&quot;),
        React.createElement(&quot;li&quot;, null, &quot;Seongbuk-gu&quot;),
        React.createElement(&quot;li&quot;, null, &quot;Seoul&quot;),
        React.createElement(&quot;li&quot;, null, &quot;02876&quot;),
        React.createElement(&quot;li&quot;, null, &quot;South Korea&quot;)
    )
);</code></pre>
<p>최종적으론 ul 내부에 한줄씩 작성하였다. section을 만드는 설계도였던 것이다.</p>
<h3 id="리엑트-엘리먼트-생성---배열">리엑트 엘리먼트 생성 - 배열</h3>
<p>이전코드는 일일히 해당 내용을 입력했지만 따로 배열을 만들어 코드를 가독성 있게 만들어보자.</p>
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

// 실습19-2-r16: 리액트 엘리먼트 생성 - Array 활용
const addr = React.createElement(
    &quot;section&quot;, 
    {id: &quot;address&quot;},
    React.createElement(
        &quot;ul&quot;,
        {className: &quot;contents&quot;},
        React.createElement(&quot;li&quot;, null, address[0]),
        React.createElement(&quot;li&quot;, null, address[1]),
        React.createElement(&quot;li&quot;, null, address[2]),
        React.createElement(&quot;li&quot;, null, address[3]),
        React.createElement(&quot;li&quot;, null, address[4]),
        React.createElement(&quot;li&quot;, null, address[5]),
        React.createElement(&quot;li&quot;, null, address[6]),
        React.createElement(&quot;li&quot;, null, address[7]),
        React.createElement(&quot;li&quot;, null, address[8])
    )
);

ReactDOM.render( //r-16
    addr,
    document.getElementById('root')
)

const root = ReactDOM.createRoot(document.getElementById('root')); //r-18
root.render(addr);

console.log('addr:', addr);</code></pre>
<h3 id="리엑트-엘리먼트-생성---map-활용">리엑트 엘리먼트 생성 - map() 활용</h3>
<p>코드를 더 가독성있게 만들기 위해서 map()함수를 사용해보자.</p>
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

// 실습20-r16: 리액트 엘리먼트 생성 - Array.map() 활용
const addr = React.createElement(
    &quot;section&quot;, 
    {id: &quot;address&quot;},
    React.createElement(
        &quot;ul&quot;,
        {className: &quot;contents&quot;},
        address.map( (addr, i) =&gt; React.createElement(&quot;li&quot;, {key: i}, addr ))
    )
);

ReactDOM.render(
    addr,
    document.getElementById('root')
)

console.log('addr:', addr);</code></pre>
<p>다시 map() 함수를 복습해보자. 기본형이다.</p>
<pre><code class="language-javascript">const newArray = array.map((currentValue, index, array) =&gt; {
    // currentValue: 현재 처리 중인 배열의 요소
    // index (선택): 현재 요소의 인덱스(순서)
    // array (선택): map()이 호출된 배열 자체

    return /* 변형된 새로운 값 */;
});

address.map( (addr, i) =&gt; React.createElement(&quot;li&quot;, {key: i}, addr ))</code></pre>
<blockquote>
<p>currentValue = addr
index = i
해당 리턴값은 React.createElement(&quot;li&quot;, {key: i}, addr )이다.</p>
</blockquote>
<h3 id="리엑트-엘리먼트-vs-리엑트-컴포넌트">리엑트 엘리먼트 vs 리엑트 컴포넌트</h3>
<p>지금까지는 엘리먼트로 구성해서 출력했다. 이제는 객체가 아닌 컴포넌트로 함수 또는 클래스를 만들어 관리할 수 있도록 할거다.</p>
<pre><code class="language-javascript">const Address = function(props){
    return React.createElement(
        &quot;ul&quot;,
        {className: &quot;address&quot;},
        props.data.map( (addr, i) =&gt; React.createElement(&quot;li&quot;, {key: i}, addr) )
    );
}</code></pre>
<p>Address가 함수형 컴포넌트이다. 현재 실행될때마다 새로운 엘리먼트 객체를 반환한다. 이를 JSX로 바꾸면</p>
<pre><code class="language-javascript">function Address(props) {
  return (
    &lt;ul className=&quot;address&quot;&gt;
      {props.data.map((addr, i) =&gt; (
        &lt;li key={i}&gt;{addr}&lt;/li&gt;
      ))}
    &lt;/ul&gt;
  );
}</code></pre>
<p>렌더링하는 부분이 중요한데 </p>
<h4 id="r16버전">r16버전</h4>
<pre><code class="language-javascript">ReactDOM.render(
    React.createElement(Address, {data: address}, null),
    document.getElementById('root')
);

console.log('Address:', Address({data: address}));</code></pre>
<h4 id="r18버전">r18버전</h4>
<pre><code class="language-javascript">const root = ReactDOM.createRoot(document.getElementById('root'));
root.render( Address({data: address}) );

console.log('Address:', Address({data: address}));</code></pre>