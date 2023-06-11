# Interview Shuriken 53: Find the Missing Number

Published: 2020-08-03T13:07:00.002+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <codezen-problem-description _ngcontent-yip-c161="" _nghost-yip-c152=""
      style="-webkit-font-smoothing: antialiased; display: block; font-family: Roboto, sans-serif;
      font-size: 16px; margin: 0px; padding: 0px; width:
      775.594px;"></codezen-problem-description><br />
      <div _ngcontent-yip-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">
      <div _ngcontent-yip-c152="" class="padding" style="-webkit-font-smoothing: antialiased;
      margin: 0px; padding: 0px 0px 15px;">
      <div _ngcontent-yip-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">
      <a _ngcontent-yip-c152="" class="key" href="https://www.blogger.com/null"
      style="-webkit-font-smoothing: antialiased; color: #b3b3b3; font-size: 12px; letter-spacing:
      0.27px; line-height: 30px; margin: 0px; padding: 0px;">Level</a><a
      _ngcontent-yip-c152="" class="value" href="https://www.blogger.com/null"
      style="-webkit-font-smoothing: antialiased; color: #656565; font-size: 12px; font-weight: 700;
      letter-spacing: 0.27px; line-height: 30px; margin: 0px; padding: 0px 0px 0px
      8px;">&nbsp;EASY</a></div>
      </div>
      <div _ngcontent-yip-c152="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">
      <h4
      id="you-are-given-an-array-containing-n-distinct-numbers-taken-from-the-range-0-n-since-the-array-contains-only-n-numbers-and-count-of-numbers-from-0-to-n-is-n-1-so-you-have-to-find-the-missing-number"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">
      You are given an array containing ‘n’ distinct numbers taken from the range: [0, n]. Since the
      array contains only ‘n’ numbers and count of numbers from 0 to n is ‘n+1’, so, you have to
      find the missing number.</h4>
      <h4 id="example-1" style="-webkit-font-smoothing: antialiased; color: #565656; font-size:
      14px; font-weight: 400; letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px
      0px 5px;">
      Example 1:</h4>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">Input: [4, 0, 3, 1]
      Output: 2
      </code></pre>
      <h4 id="example-2" style="-webkit-font-smoothing: antialiased; color: #565656; font-size:
      14px; font-weight: 400; letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px
      0px 5px;">
      Example 2:</h4>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">Input: [8, 3, 5, 2,
      4, 6, 0, 1]
      Output: 7
      </code></pre>
      <h5 id="input-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Input Format:</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">The first line of
      input contains an integer, that denotes the value of n. The following line contains n space
      separated integers, that denotes the value of array elements.
      </code></pre>
      <h5 id="constraints" style="-webkit-font-smoothing: antialiased; color: #353535; font-size:
      14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Constraints:</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">1 &lt;= N
      &lt;= 100000
      0 &lt;= A[i] &lt;= N
      Time Limit: 0.5 seconds.
      </code></pre>
      <h5 id="output-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Output Format:</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">The first and only
      line of output contains the missing number, as described in the task.
      </code></pre>
      </div>
      <div _ngcontent-yip-c152="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">
      <h5 id="sample-input-1" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Input 1:</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">6
      1 5 6 0 3 2
      </code></pre>
      <h5 id="sample-output-1" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Output 1:</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">4
      </code></pre>
      </div>
      </div>
      <br />
      <div _ngcontent-yip-c161="" class="ng-star-inserted" style="-webkit-font-smoothing:
      antialiased; font-family: Roboto, sans-serif; font-size: 16px; margin: 0px; padding: 0px;">
      <div _ngcontent-yip-c161="" class="ng-star-inserted" style="-webkit-font-smoothing:
      antialiased; margin: 0px; padding: 0px;">
      <codezen-code-problem _ngcontent-yip-c161="" _nghost-yip-c153=""
      style="-webkit-font-smoothing: antialiased; display: block; margin: auto; padding: 30px 0px
      0px; width: 775.594px;"></codezen-code-problem><br />
      <div _ngcontent-yip-c153="" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">
      <div _ngcontent-yip-c153="" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">
      </div>
      </div>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/679b7d32f166e909af65685f79da5ae3.js"></script></div>


Write your content here...