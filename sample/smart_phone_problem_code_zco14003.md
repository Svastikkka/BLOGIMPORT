# Smart Phone Problem Code: ZCO14003

Published: 2020-07-06T13:15:00.003+05:30

Description: 
      <h2 class="mathjax-support" style="box-sizing: border-box; color:
      #222222; font-family: arial, sans-serif; font-size: 2.3125rem; font-weight: 400; line-height:
      1.4; margin: 0.2rem 0px 0.5rem; padding: 0px; text-rendering: optimizelegibility;">Zonal
      Computing Olympiad 2014, 30 Nov 2013</h2><br class="mathjax-support"
      style="box-sizing: border-box;" /><p class="mathjax-support" style="box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 15px; font-stretch:
      normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px; text-rendering:
      optimizelegibility;">You are developing a smartphone app. You have a list of potential
      customers for your app. Each customer has a budget and will buy the app at your declared price
      if and only if the price is less than or equal to the customer's budget.</p><br
      class="mathjax-support" style="box-sizing: border-box;" /><p class="mathjax-support"
      style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      15px; font-stretch: normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px;
      text-rendering: optimizelegibility;">You want to fix a price so that the revenue you earn
      from the app is maximized. Find this maximum possible revenue.</p><br
      class="mathjax-support" style="box-sizing: border-box;" /><p class="mathjax-support"
      style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      15px; font-stretch: normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px;
      text-rendering: optimizelegibility;">For instance, suppose you have 4 potential customers
      and their budgets are 30, 20, 53 and 14. In this case, the maximum revenue you can get is
      60.</p><br class="mathjax-support" style="box-sizing: border-box;" /><h3
      class="mathjax-support" style="border-top-style: solid; border-top-width: 1px; box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 18px; font-stretch:
      normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering:
      optimizelegibility;">Input format</h3><p class="mathjax-support"
      style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      15px; font-stretch: normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px;
      text-rendering: optimizelegibility;">Line 1 :<span
      class="Apple-converted-space">&nbsp;</span><em class="mathjax-support"
      style="box-sizing: border-box; line-height: inherit;">N</em>, the total number of
      potential customers.</p><p class="mathjax-support" style="box-sizing: border-box;
      color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 15px; font-stretch: normal;
      line-height: 1.7; margin: 0px 0px 20px; padding: 0px; text-rendering:
      optimizelegibility;">Lines 2 to<span
      class="Apple-converted-space">&nbsp;</span><em class="mathjax-support"
      style="box-sizing: border-box; line-height: inherit;">N</em>+1: Each line has the
      budget of a potential customer.</p><br class="mathjax-support" style="box-sizing:
      border-box;" /><h3 class="mathjax-support" style="border-top-style: solid;
      border-top-width: 1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica,
      sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem;
      padding: 10px 0px 0px; text-rendering: optimizelegibility;">Output format</h3><p
      class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica,
      sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px 0px 20px;
      padding: 0px; text-rendering: optimizelegibility;">The output consists of a single integer,
      the maximum possible revenue you can earn from selling your app.</p><br
      class="mathjax-support" style="box-sizing: border-box;" /><h3 class="mathjax-support"
      style="border-top-style: solid; border-top-width: 1px; box-sizing: border-box; color: #4a4a4a;
      font-family: helvetica, sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6;
      margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering: optimizelegibility;">Sample
      Input 1</h3><pre class="mathjax-support" style="box-sizing: border-box;
      margin-bottom: 20px; margin-top: 0px; padding: 0px; white-space: pre-wrap;">4
      30
      20
      53
      14
      </pre><br class="mathjax-support" style="box-sizing: border-box;" /><h3
      class="mathjax-support" style="border-top-style: solid; border-top-width: 1px; box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 18px; font-stretch:
      normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering:
      optimizelegibility;">Sample Output 1</h3><pre class="mathjax-support"
      style="box-sizing: border-box; margin-bottom: 20px; margin-top: 0px; padding: 0px;
      white-space: pre-wrap;">60
      </pre><br class="mathjax-support" style="box-sizing: border-box;" /><h3
      class="mathjax-support" style="border-top-style: solid; border-top-width: 1px; box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 18px; font-stretch:
      normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering:
      optimizelegibility;">Sample Input 2</h3><pre class="mathjax-support"
      style="box-sizing: border-box; margin-bottom: 20px; margin-top: 0px; padding: 0px;
      white-space: pre-wrap;">5
      40
      3
      65
      33
      21
      </pre><br class="mathjax-support" style="box-sizing: border-box;" /><h3
      class="mathjax-support" style="border-top-style: solid; border-top-width: 1px; box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 18px; font-stretch:
      normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering:
      optimizelegibility;">Sample Output 2</h3><pre class="mathjax-support"
      style="box-sizing: border-box; margin-bottom: 20px; margin-top: 0px; padding: 0px;
      white-space: pre-wrap;">99
      </pre><br class="mathjax-support" style="box-sizing: border-box;" /><h3
      class="mathjax-support" style="border-top-style: solid; border-top-width: 1px; box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 18px; font-stretch:
      normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering:
      optimizelegibility;">Test data</h3><p class="mathjax-support" style="box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 15px; font-stretch:
      normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px; text-rendering:
      optimizelegibility;">Each customers' budget is between 1 and 10<sup
      class="mathjax-support" style="box-sizing: border-box;">8</sup>,
      inclusive.</p><br class="mathjax-support" style="box-sizing: border-box;" /><p
      class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica,
      sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px 0px 20px;
      padding: 0px; text-rendering: optimizelegibility;"><span class="mathjax-support"
      style="box-sizing: border-box; font-weight: 700; line-height: inherit;">Subtask 1 (30
      marks)</span><span class="Apple-converted-space">&nbsp;</span>: 1
      ≤<span class="Apple-converted-space">&nbsp;</span><em
      class="mathjax-support" style="box-sizing: border-box; line-height:
      inherit;">N</em><span class="Apple-converted-space">&nbsp;</span>≤
      5000.</p><p class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a;
      font-family: helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7;
      margin: 0px 0px 20px; padding: 0px; text-rendering: optimizelegibility;"><span
      class="mathjax-support" style="box-sizing: border-box; font-weight: 700; line-height:
      inherit;">Subtask 2 (70 marks)</span><span
      class="Apple-converted-space">&nbsp;</span>: 1 ≤<span
      class="Apple-converted-space">&nbsp;</span><em class="mathjax-support"
      style="box-sizing: border-box; line-height: inherit;">N</em><span
      class="Apple-converted-space">&nbsp;</span>≤ 5×10<sup class="mathjax-support"
      style="box-sizing: border-box;">5</sup>.</p><br class="mathjax-support"
      style="box-sizing: border-box;" /><h3 class="mathjax-support" style="border-top-style:
      solid; border-top-width: 1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica,
      sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem;
      padding: 10px 0px 0px; text-rendering: optimizelegibility;">Live evaluation
      data</h3><p class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a;
      font-family: helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7;
      margin: 0px 0px 20px; padding: 0px; text-rendering: optimizelegibility;">There are 15 test
      inputs on the server during the exam. The grouping into subtasks is as follows.</p><p
      class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica,
      sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px 0px 20px;
      padding: 0px; text-rendering: optimizelegibility;">•<span
      class="Apple-converted-space">&nbsp;</span><span class="mathjax-support"
      style="box-sizing: border-box; font-weight: 700; line-height: inherit;">Subtask
      1:</span><span class="Apple-converted-space">&nbsp;</span>Test inputs
      0,…,5</p><p class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a;
      font-family: helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7;
      margin: 0px 0px 20px; padding: 0px; text-rendering: optimizelegibility;">•<span
      class="Apple-converted-space">&nbsp;</span><span class="mathjax-support"
      style="box-sizing: border-box; font-weight: 700; line-height: inherit;">Subtask
      2:</span><span class="Apple-converted-space">&nbsp;</span>Test inputs
      6,…,14</p><br class="mathjax-support" style="box-sizing: border-box;" /><br
      class="mathjax-support" style="box-sizing: border-box;" /><h3 class="mathjax-support"
      style="border-top-style: solid; border-top-width: 1px; box-sizing: border-box; color: #4a4a4a;
      font-family: helvetica, sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6;
      margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering:
      optimizelegibility;">Note</h3><p class="mathjax-support" style="box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 15px; font-stretch:
      normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px; text-rendering:
      optimizelegibility;">The answer might not fit in a variable of type<span
      class="Apple-converted-space">&nbsp;</span><tt class="mathjax-support"
      style="box-sizing: border-box;">int</tt>. We recommend that you use variables of
      type<span class="Apple-converted-space">&nbsp;</span><tt
      class="mathjax-support" style="box-sizing:
      border-box;">long&nbsp;long</tt><span
      class="Apple-converted-space">&nbsp;</span>to read the input and compute the
      answer. If you use<span class="Apple-converted-space">&nbsp;</span><tt
      class="mathjax-support" style="box-sizing: border-box;">printf</tt><span
      class="Apple-converted-space">&nbsp;</span>and<span
      class="Apple-converted-space">&nbsp;</span><tt class="mathjax-support"
      style="box-sizing: border-box;">scanf</tt>, you can use<span
      class="Apple-converted-space">&nbsp;</span><tt class="mathjax-support"
      style="box-sizing: border-box;">%lld</tt><span
      class="Apple-converted-space">&nbsp;</span>for<span
      class="Apple-converted-space">&nbsp;</span><tt class="mathjax-support"
      style="box-sizing: border-box;">long&nbsp;long</tt>.<span
      class="Apple-converted-space">&nbsp;</span></p><div
      _ngcontent-wnf-c152="" class="description ng-star-inserted" style="-webkit-font-smoothing:
      antialiased; background-color: white; color: #757575; font-family: Roboto, sans-serif;
      font-size: 16px; margin: 0px; padding: 0px;">Explanation:-&nbsp;<a
      href="https://stackoverflow.com/questions/58274817/smart-phone-codechef-problem-logic-confusion"
      style="background: transparent; color: #2196f3; text-decoration-line:
      none;">https://stackoverflow.com/questions/58274817/smart-phone-codechef-problem-logic-confusion</a></div>
      <script
      src="https://gist.github.com/Svastikkka/d6ef2d4c8156ce6337f991532d7cceef.js"></script>

Write your content here...