# Consecutive elements

Published: 2021-03-29T00:24:00.002+05:30

Description: 
      <p><span color="var(--text-general)" face="Muli, sans-serif"
      style="background-color: white; font-size: 14px; letter-spacing:
      0.3px;">Level&nbsp;MEDIUM</span></p><p><span
      color="var(--text-general)" face="Muli, sans-serif" style="background-color: white; font-size:
      14px; letter-spacing: 0.3px;">You are given an array arr of N non-negative integers, you
      need to return true if the array elements consist of consecutive numbers otherwise return
      false.</span></p><h4
      id="for-example-if-the-given-array-is-4-3-5-then-you-should-return-true-as-all-the-array-elements-are-in-consecutive-order"
      style="color: var(--text-general); font-family: Muli, sans-serif; font-size: 14px;
      letter-spacing: 0.3px; line-height: 22px; margin: 0px; padding: 0px 0px 15px;"><span
      style="background-color: white;">For Example: If the given array is [4,3,5] then you should
      return true as all the array elements are in consecutive
      order.</span></h4><div><div _ngcontent-serverapp-c167=""
      class="description" style="color: rgba(0, 0, 0, 0.87); font-family: Muli, sans-serif; margin:
      0px; padding: 30px 0px 0px;"><h5 id="input-format" style="color: var(--text-title);
      font-family: var(--app-font); font-size: 14px; line-height: 22px; margin: 0px; padding: 0px;
      text-transform: capitalize;">Input Format:</h5><pre style="border-radius: 5px;
      color: var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: var(--block-color); font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">The first line of
      input contains a single integer T, representing the number of test cases or queries to be run.
      Then the T test cases follow.

      The first line of each test case contains an integer 'N', representing the length of the
      array.

      The next line contains 'N' single space-separated integers representing elements of the array.
      </code></pre><h5 id="output-format" style="color: var(--text-title);
      font-family: var(--app-font); font-size: 14px; line-height: 22px; margin: 0px; padding: 0px;
      text-transform: capitalize;">Output Format :</h5><pre style="border-radius: 5px;
      color: var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: var(--block-color); font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">For each test case,
      print “True” or “False” in a separate line.
      </code></pre><h5 id="note" style="color: var(--text-title); font-family:
      var(--app-font); font-size: 14px; line-height: 22px; margin: 0px; padding: 0px;
      text-transform: capitalize;">Note:</h5><pre style="border-radius: 5px; color:
      var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: var(--block-color); font-size: 13px; font-weight: 400;
      letter-spacing: 0.23px; margin: 0px; padding: 0px;">You are not required to print the
      expected output, it has already been taken care of. Just implement the function.
      </code></pre><h5 id="constraints" style="color: var(--text-title); font-family:
      var(--app-font); font-size: 14px; line-height: 22px; margin: 0px; padding: 0px;
      text-transform: capitalize;">Constraints:</h5><pre style="border-radius: 5px;
      color: var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: var(--block-color); font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1 &lt;= T
      &lt;= 10
      1 &lt;= N &lt;= 10^5
      0 &lt;= arr[i] &lt;= 10^9

      Time Limit: 1 sec
      </code></pre></div><div _ngcontent-serverapp-c167="" class="description"
      style="color: rgba(0, 0, 0, 0.87); font-family: Muli, sans-serif; margin: 0px; padding: 30px
      0px 0px;"><h5 style="color: var(--text-title); font-family: var(--app-font); font-size:
      14px; line-height: 22px; margin: 0px; padding: 0px; text-transform: capitalize;">Sample
      Input 1:</h5><pre style="border-radius: 5px; color: var(--block-color); font-size:
      14px; font-weight: 600; line-height: 20px; margin-bottom: 20px; margin-top: 10px; max-width:
      866px; overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code
      style="color: var(--block-color); font-size: 13px; font-weight: 400; letter-spacing: 0.23px;
      margin: 0px; padding: 0px;">1
      4
      1 2 4 6
      </code></pre><h5 style="color: var(--text-title); font-family: var(--app-font);
      font-size: 14px; line-height: 22px; margin: 0px; padding: 0px; text-transform:
      capitalize;">Sample Output 1:</h5><pre style="border-radius: 5px; color:
      var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: var(--block-color); font-size: 13px; font-weight: 400;
      letter-spacing: 0.23px; margin: 0px; padding: 0px;">False
      </code></pre><h5 style="color: var(--text-title); font-family: var(--app-font);
      font-size: 14px; line-height: 22px; margin: 0px; padding: 0px; text-transform:
      capitalize;">Explanation For Input 1:</h5><pre style="border-radius: 5px; color:
      var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: var(--block-color); font-size: 13px; font-weight: 400;
      letter-spacing: 0.23px; margin: 0px; padding: 0px;">As 3 and 5 are not in the array. Thus,
      this makes the array non-consecutive.
      </code></pre><h5 style="color: var(--text-title); font-family: var(--app-font);
      font-size: 14px; line-height: 22px; margin: 0px; padding: 0px; text-transform:
      capitalize;">Sample Input 2:</h5><pre style="border-radius: 5px; color:
      var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: var(--block-color); font-size: 13px; font-weight: 400;
      letter-spacing: 0.23px; margin: 0px; padding: 0px;">1
      3
      7 9 8
      </code></pre><h5 style="color: var(--text-title); font-family: var(--app-font);
      font-size: 14px; line-height: 22px; margin: 0px; padding: 0px; text-transform:
      capitalize;">Sample Output 2:</h5><pre style="border-radius: 5px; color:
      var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: var(--block-color); font-size: 13px; font-weight: 400;
      letter-spacing: 0.23px; margin: 0px; padding:
      0px;">True</code></pre></div></div><div><span
      style="background-color: white;"><br /></span></div>
      <script
      src="https://gist.github.com/Svastikkka/3bb6417ec5ed8b5a8eae8167ad1407a8.js"></script>

Write your content here...