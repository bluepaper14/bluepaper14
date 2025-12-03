---
title: "[React] Promise 객체"
date: Sat, 15 Nov 2025 05:59:23 GMT
categories: []
---

# [React] Promise 객체

<h3 id="promise-객체">promise 객체</h3>
<p>Promise는 미래에 완료될 작업을 약속하는 객체다.</p>
<p>이전에는 파일 읽기 같은 비동기 작업을 콜백 함수로만 처리하다 보니,
비동기 안에 비동기가 들어가는 이중 if문 + 콜백 지옥(callback hell) 구조가 자주 나타났다.</p>
<h3 id="예제">예제</h3>
<pre><code class="language-javascript">console.log('start');

const promise = new Promise((resolve, reject) =&gt; {
  fs.readFile('./readme1.txt', (err, data1) =&gt; {
    if (!err) resolve(data1);
    else reject(err);
  });
});

promise
  .then(data1 =&gt; {
    console.log('1st reading:', data1.toString());
    return new Promise((resolve, reject) =&gt; {
      fs.readFile('./readme2.txt', (err, data2) =&gt; {
        if (!err) resolve(data2);
        else reject(err);
      });
    });
  })
  .catch(err =&gt; console.error(err.message))
  .finally(() =&gt; console.log('end'));
</code></pre>
<p>위 코드를 요약하면 txt1 -&gt; txt2 순서대로 읽고 실패하면 catch로 이동. 마지막 end가 출력되며 코드가 종료된다.</p>
<pre><code class="language-javascript">.then(data1 =&gt; {
  console.log(&quot;1st reading:&quot;, data1.toString());
  return new Promise(...)
})
</code></pre>
<p>여기서 then은 다음 작업이 완료되면(resolve) 다음 then을 실행하라는 의미이다. 이후 2번째 파일에 대한 새로운 promise 객체를 다시 생성하고 있다. </p>
<blockquote>
<p>then 안에서 return한 Promise는 다음 then 실행 전까지 기다려라</p>
</blockquote>
<p>esolve(value)
→ 성공 상태(fulfilled)가 되어 다음 then으로 value 전달</p>
<p>reject(error)
→ 실패 상태(rejected)가 되어 가장 가까운 catch로 error 전달</p>
<h3 id="fspromises-모듈">fs.promises 모듈</h3>
<p>이번엔 promise를 직접 new로 만들지 않고 promise 기반 fs.readFile을 사용하는 방식이다.</p>
<pre><code class="language-javascript">const fs = require('fs');
const fsPromises = fs.promises;

console.log('start');
fsPromises.readFile('./data/readme1.txt')
.then(data1 =&gt; {
    // fsPromise-then for data1 from readme1.txt
    console.log('1st reading:', data1.toString());
    return fsPromises.readFile('./data/readme2.txt')
})
.then(data2 =&gt; {
    // fsPromise-then for data2 from readme2.txt
    console.log('2nd reading:', data2.toString());
    return fsPromises.readFile('./data/readme3.txt')
})
.then(data3 =&gt; console.log('3rd reading:', data3.toString()))
.catch(err =&gt; console.error(err.message))
.finally(() =&gt; console.log('end'))</code></pre>
<p>fs.promises.readFile()은 자동으로 Promise를 반환한다.</p>
<h3 id="asyncawait-구문-활용">async/await 구문 활용</h3>
<p>이번 async 함수가 최종적으로 promise보다 더 쉽게 작성할수 있다.
async는 자동으로 promise 함수를 반환하는 함수로 알면된다.</p>
<pre><code class="language-javascript">async function run() {
  try {
    const a = await work1();  // work1 끝날 때까지 기다림
    const b = await work2();  // work2 끝날 때까지 기다림
    return b;                 // 이 함수 전체는 Promise 반환
  } catch (err) {
    console.error(err);
  }
}
run();</code></pre>
<pre><code class="language-javascript">(async () =&gt; {
  try {
    // 1) 파일1 읽기 (Promise가 끝날 때까지 기다림)
    let data1 = await fsPromises.readFile(filename1);
    console.log(data1);

    // 2) 파일2 읽기
    let data2 = await fsPromises.readFile(filename2);
    console.log(data2);

    // 3) 파일3 읽기
    let data3 = await fsPromises.readFile(filename3);
    console.log(data3);
  }
  catch (err) {
    // 하나라도 에러가 나면 여기 실행
    console.error(err);
  }
  finally {
    // 성공/실패 관계없이 마지막에 실행
    console.log('end');
  }
})();</code></pre>