# [React] 일반 함수 vs 화살표 함수

Parsed from [Velog](https://velog.io/@bluepaper14/React-%EC%9D%BC%EB%B0%98-%ED%95%A8%EC%88%98-vs-%ED%99%94%EC%82%B4%ED%91%9C-%ED%95%A8%EC%88%98)

Date: Mon, 10 Nov 2025 06:32:13 GMT

---

<h3 id="예제1">예제1</h3>
<p>this를 통해 객체 흐름을 살펴보고 일반 함수와 화살표 함수의 차이를 알아보자.</p>
<pre><code class="language-javascript">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width&quot;/&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;object and this&lt;/title&gt;
  &lt;script src=&quot;https://unpkg.com/babel-standalone@6.15.0/babel.min.js&quot;&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Arrow Functions&lt;/h1&gt;
&lt;p&gt;Open the console&lt;/p&gt;
&lt;script type=&quot;module&quot;&gt;

// 1. 전역 scope에서 this 값 확인
console.log(this);          // this === undefined

// 2. obj 객체 생성
const obj = {

  // 3. 속성 obj_this에 'str1' 값 할당
  obj_this: 'str1',         // obj_this === 'str1'

    // 4. 메서드 func1() 정의
    func1(){

      // 5. this가 참조하는 값 콘솔에 출력
      console.log(this);      // this === obj

      // 6. 함수 표현식으로 5를 구현하는 함수 funcFunc1()를 구현하고 호출
      const funcFunc1 = function(){
        console.log(this);    // this === undefined
      };
      funcFunc1();

    // 7. 화살표 함수로 5를 구현하는 함수 funcFunc2()를 구현하고 호출
    const funcFunc2 = () =&gt; {
      console.log(this);    // this === obj
    };
    funcFunc2();

    // 8. 함수 표현식으로 5를 구현하는 함수 funcFunc3()를 구현하되,
    // obj을 바인딩하고, 호출
    const funcFunc3 = function(){
      console.log(this);    // this === obj
    }.bind(obj);
    funcFunc3();    

    // 9. setTimeout()의 callback에서 this 값 확인
    // callback은 함수 선언문으로 구현하고, timeout은 0으로 지정
    setTimeout(function(){
      console.log(this);    // this === Window
    }, 0);

    // 10. setTimeout()의 callback에서 this 값 확인
    // callback은 화살표 함수로 구현하고, timeout은 0으로 지정
    setTimeout(() =&gt; {
      console.log(this);    // this === objx
    }, 0);
  },  
};

obj.func1();

&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code></pre>
<h3 id="해석">해석</h3>
<pre><code class="language-javascript">console.log(this);          // this === undefined</code></pre>
<p>this는 클래스형 컴포넌트 인스턴스를 가리키는데 사용된다. 일반적으로 react에서 모듈 최상위 스코프에서 this는 undefined로 고정된다. 즉 가리킬 객체가 없으니 말이다. </p>
<pre><code class="language-javascript">const obj = {
  obj_this: 'str1',         // obj_this === 'str1'

  func1(){

    console.log(this);      // this === obj</code></pre>
<p>func1() 호출을 설명하기전 일단 func1()이 어떻게 호출을 했는지 확인해야 한다. 객체 하단에</p>
<pre><code class="language-javascript">obj.func1();</code></pre>
<p>이렇게 객체의 프로퍼티인 함수를 점을 통해 호출하면 그 객체가 곧 this가 된다. 그래서 func1()을 보면 객체를 출력하는 것이다.</p>
<pre><code class="language-javascript">func1() {
  ..
      const funcFunc1 = function(){
        console.log(this);    // this === undefined
      };
      funcFunc1()
  ..
}</code></pre>
<p>func1() 메서드 안에 선언된 <u>함수 표현식</u>이다. <u>중요한 점은 funFunc1은 객체의 메서드가 아닌 단순히 변수에 담긴 함수라는 것을 알아야 한다.</u></p>
<p>그래서 해당 funFunc1() 안의 console.log의 this를 찍어보면 undefined가 출력됨을 알 수 있다.</p>
<pre><code class="language-javascript">func1() {
  ..
    const funcFunc2 = () =&gt; {
      console.log(this);    // this === obj
    };
    funcFunc2();
  ..
}</code></pre>
<p>화살표 함수는 자신만의 this를 만들지 않고 선언된 상위 스코프의 this를 그대로 사용한다.
여기서 funcFunc2는 func1 안에서 선언되었고 func1은 obj의 메서드로 호출되므로 funcFunc2의 this도 obj를 가리킨다.</p>
<pre><code class="language-javascript">func1() {
  ..
    const funcFunc3 = function(){
      console.log(this);    // this === obj
    }.bind(obj);
    funcFunc3(); 
  ..
}</code></pre>
<p>함수 표현식은 호출 방식에 따라 this가 정해진다고 말했다. 아까 위에서도 func1() 내부에 funFunc1으로 단순히 변수에 담긴 함수이기에 undefined가 출력되었다. 하지만 .bind(바인딩)을 이용하면 상황은 달라진다.</p>
<blockquote>
<p>바인딩 : bind는 함수의 this를 강제로 특정 객체로 고정하는 메서드</p>
</blockquote>
<p>.bind() 메서드를 사용하면, 함수의 this를 특정 객체로 강제로 고정할 수 있다.
따라서 funcFunc3 = funcFunc.bind(obj)처럼 바인딩하면, 호출 방식과 상관없이 항상 this === obj가 된다.</p>
<h3 id="예제2">예제2</h3>
<p>이제 this를 이용해 객체를 가리킨다는 것을 알았으니 또 다른 예제를 보자. </p>
<pre><code class="language-javascript">
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width&quot;/&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;object and this&lt;/title&gt;
  &lt;script src=&quot;https://unpkg.com/babel-standalone@6.15.0/babel.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Arrow Functions&lt;/h1&gt;
&lt;p&gt;Open the console&lt;/p&gt;
&lt;script type=&quot;module&quot;&gt;

/**
 * ex05-2.html
 * this
 */

// 1. 전역 scope에서 this 값 확인
console.log(this);          // this === undefined

// 2. obj 객체 생성
const obj = {

  // 3. 속성 obj_this에 'str1' 값 할당
  obj_this: 'str1',         // obj_this === 'str1'

  // 4. 메서드 func1() 정의
  func2: () =&gt; {

    // 5. this가 참조하는 값 콘솔에 출력
    console.log(this);      // this === undefined

    // 6. 함수 표현식으로 5를 구현하는 함수 funcFunc1()를 구현하고 호출
    const funcFunc1 = function(){
      console.log(this);    // this === undefined
    };
    funcFunc1();

    // 7. 화살표 함수로 5를 구현하는 함수 funcFunc2()를 구현하고 호출
    const funcFunc2 = () =&gt; {
      console.log(this);    // this === undefined
    };
    funcFunc2();

    // 8. 함수 표현식으로 5를 구현하는 함수 funcFunc3()를 구현하되,
    // obj을 바인딩하고, 호출
    const funcFunc3 = function(){
      console.log(this);    // this === obj
    }.bind(obj);
    funcFunc3();    

    // 9. setTimeout()의 callback에서 this 값 확인
    // callback은 함수 선언문으로 구현하고, timeout은 0으로 지정
    setTimeout(function(){
      console.log(this);    // this === Window
    }, 0);

    // 10. setTimeout()의 callback에서 this 값 확인
    // callback은 화살표 함수로 구현하고, timeout은 0으로 지정
    setTimeout(() =&gt; {
      console.log(this);    // this === undefined
    }, 0);
  },  
};

obj.func2();

&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<pre><code class="language-javascript">func1() {
..
}

func2:() {
..
}</code></pre>
<p>1, 2번 코드를 비교해보면 객체 안의 메서드 선언 방식이 다르다. 1번 코드는 일반 함수 선언으로 메서드를 정의했지만 2번 코드는 화살표 함수로 메서드를 정의했다. 화살표 함수는 자신만의 this를 가지지 않고 선언된 상위 스코프의 this를 그대로 사용한다.</p>
<p>따라서 obj.func2()처럼 객체에 붙여 호출하더라도 화살표 함수로 정의된 메서드 안에서는 this가 객체를 가리키지 않고 undefined가 된다.</p>