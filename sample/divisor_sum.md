# Divisor sum

Published: 2020-07-16T17:47:00.002+05:30

Description: 
      <codezen-problem-description _ngcontent-ctc-c161="" _nghost-ctc-c152=""
      style="-webkit-font-smoothing: antialiased; display: block; font-family: Roboto, sans-serif;
      font-size: 16px; margin: 0px; padding: 0px; width: 775.594px;"><div
      _ngcontent-ctc-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;"><div _ngcontent-ctc-c152="" class="padding" style="-webkit-font-smoothing:
      antialiased; margin: 0px; padding: 0px 0px 15px;"><div _ngcontent-ctc-c152=""
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"><a
      _ngcontent-ctc-c152="" class="key" style="-webkit-font-smoothing: antialiased; color: #b3b3b3;
      font-size: 12px; letter-spacing: 0.27px; line-height: 30px; margin: 0px; padding:
      0px;">Level</a><a _ngcontent-ctc-c152="" class="value"
      style="-webkit-font-smoothing: antialiased; color: #656565; font-size: 12px; font-weight: 700;
      letter-spacing: 0.27px; line-height: 30px; margin: 0px; padding: 0px 0px 0px
      8px;">&nbsp;EASY</a></div></div><div _ngcontent-ctc-c152=""
      class="description ng-star-inserted" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;"><h4
      id="given-an-integer-n-calculate-the-sum-of-all-possible-proper-divisors-of-n"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Given an
      integer n, calculate the sum of all possible proper divisors of n.</h4><h4
      id="proper-divisor-of-a-natural-number-is-the-divisor-that-is-strictly-less-than-the-number"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Proper
      divisor of a natural number, is the divisor that is strictly less than the
      number.</h4><h5 id="note-you-have-to-return-the-sum" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Note : You have to return the sum.</h5><p
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.3px; line-height: 25px; margin: 0px; padding: 0px 0px 5px;"><code
      style="-webkit-font-smoothing: antialiased; background-color: #f9f2f4; border-radius: 4px;
      color: #c7254e; line-height: 25px; margin: 0px; padding: 2px 4px;">Input Format : Integer
      n.</code></p><p style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 0px 0px
      5px;"><code style="-webkit-font-smoothing: antialiased; background-color: #f9f2f4;
      border-radius: 4px; color: #c7254e; line-height: 25px; margin: 0px; padding: 2px
      4px;">Output Format : Integer answer</code></p></div><div
      _ngcontent-ctc-c152="" class="description ng-star-inserted" style="-webkit-font-smoothing:
      antialiased; margin: 0px; padding: 0px;"><h5 id="sample-input-1"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">Sample Input 1 :</h5><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">20
      </code></pre><h5 id="sample-output-1" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 1 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">22
      </code></pre><h5 id="sample-input-2" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Input 2 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">10
      </code></pre><h5 id="sample-output-2" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 2 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">8
      </code></pre><h5 id="sample-output-1-explanation"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">Sample Output 1 Explanation :</h5><h5
      id="20-has-5-proper-divisors-1-2-4-5-10-and-the-divisor-summation-is-1-2-4-5-10-22"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">20 has 5 proper divisors: 1, 2, 4, 5, 10, and
      the divisor summation is: 1 + 2 + 4 + 5 + 10 =
      22</h5></div></div></codezen-problem-description><div
      _ngcontent-ctc-c161="" class="ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      font-family: Roboto, sans-serif; font-size: 16px; margin: 0px; padding: 0px;"><div
      _ngcontent-ctc-c161="" class="ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      margin: 0px; padding: 0px;"><codezen-code-problem _ngcontent-ctc-c161=""
      _nghost-ctc-c153="" style="-webkit-font-smoothing: antialiased; display: block; margin: auto;
      padding: 30px 0px 0px; width: 775.594px;"><div _ngcontent-ctc-c153=""
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"><div
      _ngcontent-ctc-c153="" style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;"></div></div></codezen-code-problem></div></div>
      <script
      src="https://gist.github.com/Svastikkka/4c3dd90765b87dd9f1ce81eb041a5c13.js"></script>

Write your content here...