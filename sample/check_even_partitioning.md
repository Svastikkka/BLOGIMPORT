# Check Even Partitioning

Published: 2020-07-27T12:34:00.001+05:30

Description: 
      <codezen-problem-description _ngcontent-dwb-c161="" _nghost-dwb-c152=""
      style="-webkit-font-smoothing: antialiased; display: block; font-family: roboto, sans-serif;
      font-size: 16px; margin: 0px; padding: 0px; width: 775.594px;"><div
      _ngcontent-dwb-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;"><div _ngcontent-dwb-c152="" class="padding" style="-webkit-font-smoothing:
      antialiased; margin: 0px; padding: 0px 0px 15px;"><div _ngcontent-dwb-c152=""
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"><a
      _ngcontent-dwb-c152="" class="key" style="-webkit-font-smoothing: antialiased; color: #b3b3b3;
      font-size: 12px; letter-spacing: 0.27px; line-height: 30px; margin: 0px; padding:
      0px;">Level</a><a _ngcontent-dwb-c152="" class="value"
      style="-webkit-font-smoothing: antialiased; color: #656565; font-size: 12px; font-weight: 700;
      letter-spacing: 0.27px; line-height: 30px; margin: 0px; padding: 0px 0px 0px
      8px;">&nbsp;EASY</a></div></div><div _ngcontent-dwb-c152=""
      class="description ng-star-inserted" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;"><h4
      id="given-a-number-n-check-whether-the-number-can-be-sum-of-two-even-numbers-or-not-return-true-if-it-can-be-return-false-otherwise"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Given a
      number n, check whether the number can be the sum of two even numbers or not. Return true if
      it can be, return false otherwise.</h4><h4 id="constraints"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Constraints
      :</h4><h5 id="1-lt-n-lt-100000" style="-webkit-font-smoothing: antialiased; color:
      #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;"><em style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">**
      1 &lt;= n &lt;= 100000**</em></h5><p style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.3px; line-height: 25px;
      margin: 0px; padding: 0px 0px 5px;"><code style="-webkit-font-smoothing: antialiased;
      background-color: #f9f2f4; border-radius: 4px; color: #c7254e; line-height: 25px; margin: 0px;
      padding: 2px 4px;">Input Format : Integer n</code></p><p
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.3px; line-height: 25px; margin: 0px; padding: 0px 0px 5px;"><code
      style="-webkit-font-smoothing: antialiased; background-color: #f9f2f4; border-radius: 4px;
      color: #c7254e; line-height: 25px; margin: 0px; padding: 2px 4px;">Output Format : YES or
      NO</code></p></div><div _ngcontent-dwb-c152="" class="description
      ng-star-inserted" style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;"><h5 id="sample-input-1" style="-webkit-font-smoothing: antialiased; color:
      #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Sample Input 1 :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">8
      </code></pre><h5 id="sample-output-1" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 1 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">YES
      </code></pre><h5 id="sample-input-2" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Input 2 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">9
      </code></pre><h5 id="sample-output2" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output2 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">NO
      </code></pre></div></div></codezen-problem-description><div
      _ngcontent-dwb-c161="" class="ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      font-family: roboto, sans-serif; font-size: 16px; margin: 0px; padding: 0px;"><div
      _ngcontent-dwb-c161="" class="ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      margin: 0px; padding: 0px;"><codezen-code-problem _ngcontent-dwb-c161=""
      _nghost-dwb-c153="" style="-webkit-font-smoothing: antialiased; display: block; margin: auto;
      padding: 30px 0px 0px; width: 775.594px;"><div _ngcontent-dwb-c153=""
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"><div
      _ngcontent-dwb-c153="" style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;"></div></div></codezen-code-problem></div></div>
      <script
      src="https://gist.github.com/Svastikkka/a9e8e69bed4d50f936dd26f266b8ae9e.js"></script>

Write your content here...