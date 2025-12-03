---
title: [React] JSX 사용하기
date: Sun, 16 Nov 2025 13:11:04 GMT
link: https://velog.io/@bluepaper14/React-JSX-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
---

<h3 id="예제1">예제1</h3>
<pre><code class="language-javascript">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;meta name=&quot;babel-sourcemap&quot; content=&quot;false&quot; /&gt;
    &lt;meta charset=&quot;utf-8&quot;&gt;
    &lt;title&gt;Rendering React Element&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;

&lt;!-- Root element --&gt;
&lt;div id=&quot;root&quot;&gt;&lt;/div&gt;

&lt;script src=&quot;https://unpkg.com/@babel/standalone/babel.min.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/babel&quot; data-type=&quot;module&quot;&gt;

import React from &quot;https://cdn.jsdelivr.net/npm/react@19/+esm&quot;;
import { createRoot } from &quot;https://cdn.jsdelivr.net/npm/react-dom@19/client/+esm&quot;;

const user = {
    firstname: &quot;Kim&quot;,
    lastname: &quot;Yuna&quot;
}

const getUser = user =&gt; `${user.lastname}, ${user.firstname}`;

const element = React.createElement(
    &quot;h1&quot;, 
    null, 
    &quot;Hello, &quot;, getUser(user), &quot;!&quot;
);

const root = createRoot(document.getElementById('root'));
root.render(element);

&lt;/script&gt;

&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>div id=&quot;root&quot;엘리먼트 하위에 자식 노드로 h1 엘리먼트를 생성하였다.   </p>
<h4 id="jsx-사용한-리액트-엘리먼트">JSX 사용한 리액트 엘리먼트</h4>
<pre><code class="language-javascript">const user = {
    firstname: &quot;Kim&quot;,
    lastname: &quot;Yuna&quot;
}

const getUser = user =&gt; `${user.lastname}, ${user.firstname}`;

const element1 = (
    &lt;h1&gt;
        Hello, {getUser(user)}!
    &lt;/h1&gt;
);

const element2 = &lt;h1&gt;Hello, {getUser(user)}!&lt;/h1&gt;;

const root = createRoot(document.getElementById('root'));
root.render(element1);</code></pre>
<h4 id="배열-활용--map함수">배열 활용 + map()함수</h4>
<pre><code class="language-javascript">const majors = (
    &lt;ul&gt;
        &lt;li&gt;{data[0]}&lt;/li&gt;
        &lt;li&gt;{data[1]}&lt;/li&gt;
        &lt;li&gt;{data[2]}&lt;/li&gt;
        &lt;li&gt;{data[3]}&lt;/li&gt;
    &lt;/ul&gt;
);

root.render(majors);</code></pre>
<p>해당 배열을 아래 map()함수를 이용하여 변경하였다.</p>
<pre><code class="language-javascript">const majors = (
    &lt;ul&gt;
        {
            data.map( (major, i) =&gt; (
                &lt;li key={i}&gt;{major}&lt;/li&gt;
            ))
        }
    &lt;/ul&gt;
);

root.render(majors);</code></pre>
<h4 id="컴포넌트-생성">컴포넌트 생성</h4>
<pre><code class="language-javascript">const MajorList = function(){
    return (
        &lt;ul&gt;
            {data.map( (major, i) =&gt; (
                &lt;li key={i}&gt;{major}&lt;/li&gt;
            ))}
        &lt;/ul&gt;
    );
}

root.render( &lt;MajorList /&gt; );</code></pre>