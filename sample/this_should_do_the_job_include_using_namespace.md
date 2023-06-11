# This should do the job:

      #include
      using namespace ...

Published: 2021-12-06T23:34:12.435+05:30

Description: This should do the job:<br /><br />#include<br />using
      namespace std;<br /><br />int main()<br />{<br /> int
      S,E,W,i,cd;<br /> cin&gt;&gt;S;<br /> cin&gt;&gt;E;<br />
      cin&gt;&gt;W;<br /> while (((S&gt;=0)&amp;&amp;(S&lt;=80))
      &amp;&amp; ((E&gt;=S)&amp;&amp;(S&lt;=900)) &amp;&amp;
      ((W&gt;=0)&amp;&amp;(W&lt;=40)))<br /> {<br />
      while(S&lt;=E)<br /> {<br /> for(i=S;i&lt;=E;i+=W)<br /> {<br
      /> cd=(i-32)/1.8;<br />
      cout&lt;&lt;i&lt;&lt;&quot;\t&quot;&lt;&lt;cd&lt;&lt;&quot;\n&quot;;<br
      /> S+=W;<br /> }<br /> }<br /> }<br />}

Write your content here...