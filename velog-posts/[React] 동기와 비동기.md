---
title: [React] 동기와 비동기
date: Sat, 15 Nov 2025 05:36:30 GMT
link: https://velog.io/@bluepaper14/React-%EB%8F%99%EA%B8%B0%EC%99%80-%EB%B9%84%EB%8F%99%EA%B8%B0
---

<h3 id="동기와-비동기">동기와 비동기</h3>
<ul>
<li>동기</li>
</ul>
<blockquote>
<p>동기는 하나의 작업이 완료될때까지 다음 작업이 <u>대기한다</u>.</p>
</blockquote>
<ul>
<li>비동기</li>
</ul>
<blockquote>
<p>비동기는 하나의 작업의 <u>완료를 기다리지 않고</u> 바로 다음 작업으로 간다. </p>
</blockquote>
<p>바로 예제 코드를 보자. </p>
<pre><code class="language-javascript">const fs = require('fs'); //node.js 모듈 불러오기

fs.readFile('./data/readme1.txt', (err, data) =&gt; {
    if (err) {
        console.error(err);
    }
    else {
        console.log('1st reading:', data.toString());
    }
});
</code></pre>
<p>fs.readFile을 호출했다. 그렇다면 해당 함수의 의미를 알아보자.</p>
<h3 id="fsreadfile">fs.readFile()</h3>
<p><img alt="" src="https://velog.velcdn.com/images/bluepaper14/post/9f26c184-c702-41f7-9ef4-bd44282872b2/image.png" /></p>
<p>결론은 파일을 비동기(ASYNCHRONOUS) 방식으로 읽는 함수이다.파일 읽기 작업이 완료될 까지 다른 코드를 계속 실행할 수 있게 한다.</p>
<pre><code class="language-javascript">import { readFile } from 'node:fs';

readFile('/etc/passwd', (err, data) =&gt; {
  if (err) throw err;
  console.log(data);
});</code></pre>
<p>여기서 '/etc/passwd'는  읽어올 파일의 경로이고 중요한 점은 </p>
<pre><code class="language-javascript">(err, data) =&gt; { ... }</code></pre>
<p>콜벡함수 파일 읽기 작업이 끝나면 해당 함수가 실행되는데 두개의 인자가 보인다.</p>
<p>err : 에러가 발생하면 들어오는 값
data : 파일 읽기 성공시 파일 내용들</p>
<p>위 코드가 비동기 함수랑 관련이 있을까?</p>
<p>다른 예제를 보자.</p>
<h3 id="예제2">예제2</h3>
<pre><code class="language-javascript">const fs = require('fs');

fs.readFile('./data/readme1.txt', (err, data) =&gt; {
    if (err) {
        console.error(err);
    }
    else {
        console.log('1st reading:', data.toString());
    }
});</code></pre>
<p>결과를 실행해보면 </p>
<pre><code>1st reading: This file contains sample text #1.</code></pre><p>이렇게 출력된다. 이를 일반적으로 3개의 함수를 연달아 작성하면 </p>
<pre><code>/**
 * ex07-1.js
 * ref: ch02/05/01/01-async.js
 */

const fs = require('fs');

console.log('start');
fs.readFile('./data/readme1.txt', (err, data) =&gt; {
    if (err) {
        console.error(err);
    }
    else {
        console.log('1st reading:', data.toString());
    }
});

fs.readFile('./data/readme2.txt', (err, data) =&gt; {
    if (err) {
        console.error(err);
    }
    else {
        console.log('2nd reading:', data.toString());
    }
});

fs.readFile('./data/readme3.txt', (err, data) =&gt; {
    if (err) {
        console.error(err);
    }
    else {
        console.log('3rd reading:', data.toString());
    }    
});

console.log('end');</code></pre><p>즉 이렇게 되면 비동기함수이기에 어떤 파일이 먼저 읽고 완료되는지 모른다.(즉 랜덤) </p>
<pre><code>start
1st reading: This file contains sample text #1.
2st reading: This file contains sample text #2.
3st reading: This file contains sample text #3.
end</code></pre><p>이렇게 만들기 위해선 어떻게 위 코드를 변형해야할까.</p>
<pre><code class="language-javascript">const fs = require('fs');

console.log('start');
fs.readFile('./data/readme1.txt', (err, data) =&gt; {
    if (err) {
        console.error(err);
    }
    else {
        console.log('1st reading:', data.toString());
    }
});

fs.readFile('./data/readme2.txt', (err, data) =&gt; {
    if (err) {
        console.error(err);
    }
    else {
        console.log('2nd reading:', data.toString());
    }
});

fs.readFile('./data/readme3.txt', (err, data) =&gt; {
    if (err) {
        console.error(err);
    }
    else {
        console.log('3rd reading:', data.toString());
    }    
});

console.log('end');</code></pre>
<p>1번안이다. 이렇게 하면 출력은 이렇다.</p>
<p>결론적은 console.log는 동기이고 아래 배웠던 readFile은 비동기 함수이기 떄문에 <u>fs는 요청만 던져놓고 다음줄인 end를 출력한 것이다.</u> 또한 세 파일의 결과 순서도 보장되지 않는다. OS의 상황에 따라 다르다. 그렇다면 다음 2번안이다.</p>
<pre><code class="language-javascript">const fs = require('fs');

console.log(`start`);
fs.readFile('./data/readme1.txt', (err, data) =&gt; {
    if (err) {
        console.error(err);
    }
    else {
        console.log('1st reading:', data.toString());
        fs.readFile('./data/readme2.txt', (err, data) =&gt; {
            if (err) {
                console.error(err);
            }
            else {
                console.log('2nd reading:', data.toString());
                fs.readFile('./data/readme3.txt', (err, data) =&gt; {
                    if (err) {
                        console.error(err);
                    }
                    else {
                        console.log('3rd reading:', data.toString());
                    }                    
                    console.log(`end`);
                });
            }
        });
    }
});</code></pre>
<p>이번엔 비동기 파일을 중첩하였다. 해당 첫번째 파일이 성공적으로 읽으면 그 안에서 두번째 파일을  읽도록 하였다. 이렇게 실행순서를 보장해주고 있지만 너무 복잡하다. 그래서 다음엔 해결책으로 Promise에 대해 살펴보자.</p>