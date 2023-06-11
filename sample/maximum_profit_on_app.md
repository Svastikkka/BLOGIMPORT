# Maximum Profit on App

Published: 2020-07-06T13:11:00.000+05:30

Description: 
      <div _ngcontent-wnf-c152="" class="padding"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px 0px 15px;"><div
      _ngcontent-wnf-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;"><a _ngcontent-wnf-c152="" class="key" style="-webkit-font-smoothing: antialiased;
      color: #b3b3b3; font-size: 12px; letter-spacing: 0.27px; line-height: 30px; margin: 0px;
      padding: 0px;">Level</a><a _ngcontent-wnf-c152="" class="value"
      style="-webkit-font-smoothing: antialiased; color: #656565; font-size: 12px; font-weight: 700;
      letter-spacing: 0.27px; line-height: 30px; margin: 0px; padding: 0px 0px 0px
      8px;">&nbsp;MEDIUM</a></div></div><div _ngcontent-wnf-c152=""
      class="description ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: Roboto, sans-serif; font-size: 16px; margin: 0px;
      padding: 0px;"><h4
      id="you-have-made-a-smartphone-app-and-want-to-set-its-price-such-that-the-profit-earned-is-maximised-there-are-certain-buyers-who-will-buy-your-app-only-if-their-budget-is-greater-than-or-equal-to-your-price"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">You have
      made a smartphone app and want to set its price such that the profit earned is maximised.
      There are certain buyers who will buy your app only if their budget is greater than or equal
      to your price.</h4><h4
      id="you-will-be-provided-with-a-list-of-size-n-having-budgets-of-buyers-and-you-need-to-return-the-maximum-profit-that-you-can-earn"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">You will be
      provided with a list of size N having budgets of buyers and you need to return the maximum
      profit that you can earn.</h4><h4
      id="lets-say-you-decide-that-price-of-your-app-is-rs-x-and-there-are-n-number-of-buyers-so-maximum-profit-you-can-earn-is"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Lets say you
      decide that price of your app is Rs. x and there are N number of buyers. So maximum profit you
      can earn is :</h4><pre style="-webkit-font-smoothing: antialiased; background-image:
      linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family:
      &quot;Open Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      20px; max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"> m * x
      </code></pre><h4
      id="where-m-is-total-number-of-buyers-whose-budget-is-greater-than-or-equal-to-x"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">where m is
      total number of buyers whose budget is greater than or equal to x.</h4><h5
      id="input-format" style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px;
      letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">Input format
      :</h5><pre style="-webkit-font-smoothing: antialiased; background-image:
      linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family:
      &quot;Open Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      20px; max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">Line 1 : N (No. of
      buyers)
      Line 2 : Budget of buyers (separated by space)
      </code></pre><h5 id="output-format" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Output Format :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">
      Maximum profit
      </code></pre><h5 id="constraints" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Constraints :</h5><h4 id="1-lt-n-lt-10-6" style="-webkit-font-smoothing:
      antialiased; color: #565656; font-size: 14px; font-weight: 400; letter-spacing: 0.3px;
      line-height: 25px; margin: 0px; padding: 15px 0px 5px;">1 &lt;= N &lt;=
      10^6</h4></div><div _ngcontent-wnf-c152="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px;"><h5 id="sample-input-1"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">Sample Input 1 :</h5><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">4
      30 20 53 14
      </code></pre><h5 id="sample-output-1" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 1 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">60
      </code></pre><h5 id="sample-output-1-explanation"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">Sample Output 1 Explanation :</h5><h4
      id="price-of-your-app-should-be-rs-20-or-rs-30-for-both-prices-you-can-get-the-profit-rs-60"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Price of
      your app should be Rs. 20 or Rs. 30. For both prices, you can get the profit Rs.
      60.</h4><h5 id="sample-input-2" style="-webkit-font-smoothing: antialiased; color:
      #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Sample Input 2 :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">5
      34 78 90 15 67
      </code></pre><h5 id="sample-output-2" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 2 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">201
      </code></pre><h5 id="sample-output-2-explanation"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">Sample Output 2 Explanation :</h5><h4
      id="price-of-your-app-should-be-rs-67-you-can-get-the-profit-rs-201-i-e-3-67"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Price of
      your app should be Rs. 67. You can get the profit Rs. 201 (i.e. 3 *
      67).</h4><div>Explanation:-&nbsp;<a
      href="https://stackoverflow.com/questions/58274817/smart-phone-codechef-problem-logic-confusion">https://stackoverflow.com/questions/58274817/smart-phone-codechef-problem-logic-confusion</a></div></div>
      <script
      src="https://gist.github.com/Svastikkka/15b948c00c8535d7576cc5b073536771.js"></script>

Write your content here...