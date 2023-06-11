# Interview Shuriken 55: Missing Numbers

Published: 2020-08-03T04:22:00.002+05:30

Description: 
      <div _ngcontent-fsp-c152="" class="padding"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px 0px 15px;"><div
      _ngcontent-fsp-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;"><a _ngcontent-fsp-c152="" class="key" style="-webkit-font-smoothing: antialiased;
      color: #b3b3b3; font-size: 12px; letter-spacing: 0.27px; line-height: 30px; margin: 0px;
      padding: 0px;">Level</a><a _ngcontent-fsp-c152="" class="value"
      style="-webkit-font-smoothing: antialiased; color: #656565; font-size: 12px; font-weight: 700;
      letter-spacing: 0.27px; line-height: 30px; margin: 0px; padding: 0px 0px 0px
      8px;">&nbsp;EASY</a></div></div><div _ngcontent-fsp-c152=""
      class="description ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: roboto, sans-serif; font-size: 16px; margin: 0px;
      padding: 0px;"><h4
      id="given-an-unsorted-array-of-integers-of-size-n-having-elements-ranging-from-1-to-n-number-of-elements-the-array-may-have-repetitive-elements-hence-some-numbers-in-the-range-are-missing-from-the-array-find-and-print-those-numbers"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Given an
      unsorted array of integers of size n, having elements ranging from 1 to n (number of
      elements). The array may have repetitive elements, hence some numbers in the range are missing
      from the array. Find and print those numbers.</h4><h5 id="input-format"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">Input Format:</h5><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;open
      sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">The first line of
      input contains an integer,</code></pre><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">that denotes the value of n.
      The following line contains n space separated integers, </code></pre><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;open
      sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">that denote the
      array elements.
      </code></pre><h5 id="constraints" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Constraints:</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">1 &lt;= number of elements, element values &lt;= 10,000,000
      Time Limit: 1 second
      </code></pre><h5 id="output-format" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Output Format:</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">The first and only line of output contains elements that are not found in the array.
      </code></pre></div><div _ngcontent-fsp-c152="" class="description
      ng-star-inserted" style="-webkit-font-smoothing: antialiased; background-color: white;
      font-family: roboto, sans-serif; font-size: 16px; margin: 0px; padding: 0px;"><h5
      id="sample-input-1" style="-webkit-font-smoothing: antialiased; color: #353535; font-size:
      14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">Sample Input
      1:</h5><pre style="-webkit-font-smoothing: antialiased; background-image:
      linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family:
      &quot;open sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      20px; max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">7
      4 2 7 1 1 3 7
      </code></pre><h5 id="sample-output-1" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 1:</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">5 6
      </code></pre><h5 id="explanation" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Explanation:</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: scroll; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">Missing numbers between range of 1 to 7 are 5 and
      6.</code></pre></div>
      <script
      src="https://gist.github.com/Svastikkka/98553bc0ba418c77129131a586411c38.js"></script>

Write your content here...