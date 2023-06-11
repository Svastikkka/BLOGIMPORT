# How Many Different Ways Of Swapping Two Numbers

Published: 2020-08-10T11:44:00.008+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      Well the first thing comes in our mind when we are a beginner is how many ways we can swap two
      variable but honestly, there are multiple ways of doing it. Generally, for swapping two
      variables we use a temporary third variable, but there are various other ways where we do not
      even require the help of any third variable.<br />
      <div>
      So let's see</div>
      <div>
      <br /></div>
      <b>Method 1:- The simple method using a third variable</b><br />
      <b><br /></b>
      <div>
      <span style="color: red;"><span style="font-family: courier;">1.# method 1 <br
      /> 2.a=50 <br /> 3.b=5 <br /> 4.temp=a <br /> 5.a=b <br /> 5.b=temp
      <br /> 6.print(a,b)</span></span></div><div><b
      style="font-family: menlo;"><br /></b></div><div><b
      style="font-family: menlo;">Method 2:- Using arithmetic operators + and
      -</b><div>
      <b><br /></b></div>
      <div>
      <span style="color: red; font-family: courier;">1.#method 2<br /> 2.a=50<br
      /> 3.b=5<br /> 4.a = a + b<br /> 5.b = a - b<br /> 6.a = a - b<br
      /> 7.print(a,b)</span></div><div><span style="color: red; font-family:
      courier;"><br /></span>
      <b>Method 3:- Using arithmetic operators * and
      /</b></div><div><b><br /></b></div>
      <span style="color: red; font-family: courier;">1.#method 3<br /> 2.a=50<br
      /> 3.b=5<br /> 4.a = a * b<br /> 5.b = a // b<br /> 6.a = a // b<br
      /> 7.print(a,b)</span></div><div><span style="color: red; font-family:
      courier;"><br />
      </span><div>
      <div>
      <b>Method 4:- Using bitwise XOR operator ^</b><br />
      <br />
      <span style="color: red; font-family: courier;">1.#method 4<br /> 2.a=50<br
      /> 3.b=5<br /> 4.a = a ^ b<br /> 5.b = a ^ b<br /> 6.a = a ^ b<br
      /> 7.print(a,b)</span></div><div><b style="font-family:
      times;"><br /></b></div><div><b style="font-family:
      times;">It can also be written in a more compact manner like
      this:</b></div><div><pre><span style="color: red; font-family:
      courier;">1.a=50 <br />2.b=5 <br />3.a ^= b <br />4.b ^= a <br
      />5.a ^= b <br />6.print(a,b)</span></pre><pre><b
      style="font-family: menlo;">Method 5:- The simple method using two
      variables</b></pre></div><div><b><br
      /></b></div>
      <span style="color: red; font-family: courier;">1.# method 5<br /> 2.a=50<br
      /> 3.b=5<br /> 4.a,b=b,a<br /> 5.print(a,b)</span><br />
      </div>
      </div>
      </div>


Write your content here...