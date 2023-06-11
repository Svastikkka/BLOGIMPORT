# Special Sum of array

Published: 2021-04-13T15:47:00.002+05:30

Description: 
      <p><span face="Roboto, sans-serif" style="background-color: white;
      color: #565656; font-size: 14px; letter-spacing:
      0.3px;">Level&nbsp;EASY</span></p><p><span
      style="background-color: white; color: #565656; font-size: 14px; letter-spacing:
      0.3px;">Given an array of length N, which contains single digit elements at every index.
      You need to find and return the sum of all elements of the array. But the final sum should
      also be single digit.</span></p><div _ngcontent-uge-c119="" class="description
      ng-star-inserted" style="-webkit-font-smoothing: antialiased; background-color: white;
      font-family: Roboto, sans-serif; font-size: 16px; margin: 0px; padding: 0px;"><h4
      id="in-order-to-keep-the-output-single-digit-you-need-to-keep-adding-the-output-number-digits-till-single-digit-is-left"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">In order to
      keep the output single digit - you need to keep adding the output number digits till single
      digit is left.</h4><h5 id="input-format" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Input Format :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">Line 1 : An Integer N i.e. size of array
      Line 2 : N integers which are elements of the array, separated by spaces
      </code></pre><h5 id="output-format" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Output Format :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">Single digit sum
      </code></pre><h5 id="constraints" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Constraints :</h5><h4 id="1-lt-n-lt-10-6" style="-webkit-font-smoothing:
      antialiased; color: #565656; font-size: 14px; font-weight: 400; letter-spacing: 0.3px;
      line-height: 25px; margin: 0px; padding: 15px 0px 5px;"><em
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"><strong
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">1 &lt;= N
      &lt;= 10^6</strong></em></h4></div><div _ngcontent-uge-c119=""
      class="description ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: Roboto, sans-serif; font-size: 16px; margin: 0px;
      padding: 0px;"><h5 id="sample-input-1" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Sample Input 1 :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">3
      9 9 9
      </code></pre><h5 id="sample-output-1" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 1 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">9
      </code></pre><h5 id="sample-output-explanation" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output Explanation :</h5><h4 id="9-9-9-27"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">9 + 9 + 9 =
      27</h4><h4 id="2-7-9" style="-webkit-font-smoothing: antialiased; color: #565656;
      font-size: 14px; font-weight: 400; letter-spacing: 0.3px; line-height: 25px; margin: 0px;
      padding: 15px 0px 5px;">2 + 7 = 9</h4><h4 id="hence-ans-is-9"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Hence, ans
      is 9.</h4><h5 id="sample-input-2" style="-webkit-font-smoothing: antialiased; color:
      #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Sample Input 2 :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">5
      1 7 8 5 9
      </code></pre><h5 id="sample-output-1" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 1 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">3
      </code></pre><h5 id="sample-output-explanation" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output Explanation :</h5><h4 id="1-7-8-5-9-30"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">1 + 7 + 8 +
      5 + 9 = 30</h4><h4 id="3-0-3" style="-webkit-font-smoothing: antialiased; color:
      #565656; font-size: 14px; font-weight: 400; letter-spacing: 0.3px; line-height: 25px; margin:
      0px; padding: 15px 0px 5px;">3 + 0 = 3</h4><h4 id="hence-ans-is-3"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Hence, ans
      is 3</h4></div>
      <script
      src="https://gist.github.com/Svastikkka/06262bdc6046b9dcaa6ae1a1a791b504.js"></script>

Write your content here...