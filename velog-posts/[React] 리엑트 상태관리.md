---
title: "[React] 리엑트 상태관리"
date: Mon, 17 Nov 2025 03:51:09 GMT
categories: []
---

# [React] 리엑트 상태관리

**bluepaper14** · *Mon, 17 Nov 2025 03:51:09 GMT*



---
<br/>

<p>컴포넌트 동작에는 2가지가 있다. 바로 State와 Props이다.</p>
<h3 id="state상태">State(상태)</h3>
<p>컴포넌트 내부에서 변경될 수 있는 데이터를 의미한다. 컴포넌트 안에서 만들어지고 값이 변경될 수 있고 값이 바뀌면 컴포넌트가 자동으로 다시 렌더링한다. <u>상태가 바뀌면 다시 화면을 그린다</u></p>
<p>state는 컴포넌트가 스스로 기억해야 하는 값이라고 생각하자.(변할 수 있는값)</p>
<h3 id="state-사용">State 사용</h3>
<p>useState()를 사용한다. 아래와 같은 구조를 가진다.</p>
<pre><code class="language-javascript">[ currentState, setterFunction ] = useState(initState);
[현재 상태값,상태를 변경하는 함수] = useState(최초 초기값);</code></pre>
<h3 id="예제1">예제1</h3>
<pre><code class="language-javascript">import React, {useState} from &quot;react&quot;;
import Star from &quot;./Star&quot;;

const createArray = length =&gt; [...Array(length)];

const StarRating = function( { totalStars = 5 } ){
    const [selectedStars] = useState(3);

    return (
        &lt;&gt;
            {createArray(totalStars).map( (n, i) =&gt; 
                    &lt;Star key={i} selected={selectedStars &gt; i} /&gt; )}
            &lt;p&gt;
                {selectedStars} of {totalStars} stars
            &lt;/p&gt;
        &lt;/&gt;
    );
};

export default StarRating;</code></pre>
<pre><code class="language-javascript">const [selectedStars] = useState(3);</code></pre>
<p>현재 selectedStars는 현재 상태값을 의미하는데 현재 선택된 별 개수(state값) 이다.
여기서 state값을 3으로 설정하였다. 아직 별 개수를 변경하지 않는 정적 예제라 setter함수는 필요없다.</p>
<pre><code class="language-javascript">{createArray(totalStars).map((n, i) =&gt;
    &lt;Star key={i} selected={selectedStars &gt; i} /&gt;
)}</code></pre>
<p>그리고 totalStars 개수만큼 Star컴포넌트를 반복생성하고 있다. 이제 Setter를 포함버전으로 다시 코드를 작성해보자.</p>
<h4 id="starjs">Star.js</h4>
<pre><code class="language-javascript">const Star = ({ selected = false, onSelect = f =&gt; f }) =&gt; (
  &lt;FaStar
    color={selected ? &quot;red&quot; : &quot;grey&quot;}
    onClick={onSelect}
  /&gt;
);</code></pre>
<p>Star.js는 slected가 true면 빨강 false면 회색이다. 클릭하면 onSelect()함수가 실행된다.</p>
<h4 id="starratingjs">StarRating.js</h4>
<pre><code class="language-javascript">const StarRating = ({ totalStars = 5 }) =&gt; {
  const [selectedStars, setSelectedStars] = useState(3);

  return (
    &lt;&gt;
      {createArray(totalStars).map((n, i) =&gt; (
        &lt;Star
          key={i}
          selected={selectedStars &gt; i}
          onSelect={() =&gt; setSelectedStars(i + 1)}
        /&gt;
      ))}
      &lt;p&gt;
        {selectedStars} of {totalStars} stars
      &lt;/p&gt;
    &lt;/&gt;
  );
};
</code></pre>
<h4 id="1단계--초기-렌더링">1단계 : 초기 렌더링</h4>
<pre><code>const [selectedStars, setSelectedStars] = useState(3);</code></pre><h4 id="2단계--별-클릭-이벤트">2단계 : 별 클릭 이벤트</h4>
<pre><code>onSelect={() =&gt; setSelectedStars(i + 1)}
              → setSelectedStars(3 + 1)
              → setSelectedStars(4)</code></pre><p>4번째 별을 클릭하여 selectedStar = 4로 변경했음.</p>
<h3 id="props속성">Props(속성)</h3>
<p>부모 컴포넌트가 자식 컴포넌트에게 전달하는 외부 데이터이다. 중요한건 자식 컴포넌트에서는 props를 절대 수정하지 않는다. 컴포넌트는 외부 데이터를 절대 변경해선 안된다.</p>
<p>props는 부모가 관리하고 자식은 받기만 한다.(읽기 전용)</p>
<h3 id="props-사용">Props 사용</h3>
<pre><code class="language-javascript">function Greeting({ name }) {
  return &lt;h1&gt;안녕하세요 {name}!&lt;/h1&gt;;
}

&lt;Greeting name=&quot;지현&quot; /&gt;</code></pre>