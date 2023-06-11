# Fibonacci Member

Published: 2020-06-21T19:21:00.003+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div _ngcontent-pmn-c147="" class="padding" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: Roboto, sans-serif; font-size: 16px; margin: 0px;
      padding: 0px 0px 15px;">
      <div _ngcontent-pmn-c147="" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">
      Level&nbsp;EASY</div>
      </div>
      <div _ngcontent-pmn-c147="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px;">
      <h4
      id="given-a-number-n-figure-out-if-it-is-a-member-of-fibonacci-series-or-not-return-true-if-the-number-is-member-of-fibonacci-series-else-false"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">
      Given a number N, figure out if it is a member of fibonacci series or not. Return true if the
      number is member of fibonacci series else false.</h4>
      <h4 id="fibonacci-series-is-defined-by-the-recurrence" style="-webkit-font-smoothing:
      antialiased; color: #565656; font-size: 14px; font-weight: 400; letter-spacing: 0.3px;
      line-height: 25px; margin: 0px; padding: 15px 0px 5px;">
      Fibonacci Series is defined by the recurrence</h4>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"> F(n) = F(n-1) +
      F(n-2)
      </code></pre>
      <h4 id="where-f-0-0-and-f-1-1" style="-webkit-font-smoothing: antialiased; color: #565656;
      font-size: 14px; font-weight: 400; letter-spacing: 0.3px; line-height: 25px; margin: 0px;
      padding: 15px 0px 5px;">
      where F(0) = 0 and F(1) = 1</h4>
      <div style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px;
      letter-spacing: 0.3px; line-height: 25px; padding: 0px 0px 5px;">
      <br style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"
      /></div>
      <h5 id="input-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Input Format :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">Integer N
      </code></pre>
      <h5 id="output-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Output Format :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">true or false
      </code></pre>
      <h5 id="constraints" style="-webkit-font-smoothing: antialiased; color: #353535; font-size:
      14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Constraints :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">0 &lt;= n
      &lt;= 10^4
      </code></pre>
      </div>
      <div _ngcontent-pmn-c147="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px;">
      <h5 id="sample-input-1" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Input 1 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">5
      </code></pre>
      <h5 id="sample-output-1" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Output 1 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">true
      </code></pre>
      <h5 id="sample-input-2" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Input 2 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">14
      </code></pre>
      <h5 id="sample-output-2" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Output 2 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: scroll; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">false
      </code></pre>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/5ad2ae870d23f7c22ed89b46a58d23b6.js"></script>
      </div>


Write your content here...