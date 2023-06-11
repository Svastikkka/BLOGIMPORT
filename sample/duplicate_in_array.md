# Duplicate in array

Published: 2020-07-06T14:53:00.001+05:30

Description: 
      <div _ngcontent-rpa-c152="" class="padding"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px 0px 15px;"><div
      _ngcontent-rpa-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;"><a _ngcontent-rpa-c152="" class="key" style="-webkit-font-smoothing: antialiased;
      color: #b3b3b3; font-size: 12px; letter-spacing: 0.27px; line-height: 30px; margin: 0px;
      padding: 0px;">Level</a><a _ngcontent-rpa-c152="" class="value"
      style="-webkit-font-smoothing: antialiased; color: #656565; font-size: 12px; font-weight: 700;
      letter-spacing: 0.27px; line-height: 30px; margin: 0px; padding: 0px 0px 0px
      8px;">&nbsp;EASY</a></div></div><div _ngcontent-rpa-c152=""
      class="description ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: Roboto, sans-serif; font-size: 16px; margin: 0px;
      padding: 0px;"><h4
      id="given-an-array-of-integers-of-size-n-which-contains-numbers-from-0-to-n-2-each-number-is-present-at-least-once-that-is-if-n-5-numbers-from-0-to-3-is-present-in-the-given-array-at-least-once-and-one-number-is-present-twice-you-need-to-find-and-return-that-duplicate-number-present-in-the-array"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Given an
      array of integers of size n which contains numbers from 0 to n - 2. Each number is present at
      least once. That is, if n = 5, numbers from 0 to 3 is present in the given array at least once
      and one number is present twice. You need to find and return that duplicate number present in
      the array.</h4><h4 id="assume-duplicate-number-is-always-present-in-the-array"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Assume,
      duplicate number is always present in the array.</h4><h5 id="input-format"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">Input format :</h5><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">Line 1 : Size of
      input array
      Line 2 : Array elements (separated by space)
      </code></pre><h5 id="output-format" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Output Format :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">Duplicate element
      </code></pre><h5 id="constraints" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Constraints :</h5><h4 id="1-lt-n-lt-10-6" style="-webkit-font-smoothing:
      antialiased; color: #565656; font-size: 14px; font-weight: 400; letter-spacing: 0.3px;
      line-height: 25px; margin: 0px; padding: 15px 0px 5px;">1 &lt;= n &lt;=
      10^6</h4></div><div _ngcontent-rpa-c152="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px;"><h5 id="sample-input"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">Sample Input:</h5><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">9
      0 7 2 5 4 7 1 3 6
      </code></pre><h5 id="sample-output" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Sample Output:</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: scroll; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">7</code></pre></div>
      <script
      src="https://gist.github.com/Svastikkka/7c8873914e75510f0d303d2fd865b36d.js"></script>

Write your content here...