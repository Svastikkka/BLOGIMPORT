# Array Insert

Published: 2020-09-15T14:59:00.002+05:30

Description: 
      <p><span style="background-color: white; caret-color: rgb(37, 44,
      51); color: #252c33; font-family: &quot;Open Sans&quot;, sans-serif; font-size: 14px;
      word-spacing: 1px;">Gary likes to solve problems of array, but he doesn't like problems
      that involve queries. His school teacher gave him an assignment full of problems but one of
      them involve queries. Can you help Gary in solving that problem so that he can go and play
      with his friends? The problem is :</span></p><div class="starwars-lab"
      style="background-color: white; caret-color: rgb(37, 44, 51); color: #252c33; font-family:
      &quot;Open Sans&quot;, sans-serif; font-size: 14px; text-size-adjust: auto;
      word-spacing: 1px;"><p>Given an Array A consisting of N positive integers, you have
      to answer Q queries on it. Queries can be of the two types: * 1 X Y - Update X at location Y
      in the array. * 2 L R - Print the sum of range [L, R], i.e. Both L and R are
      inclusive.</p><pre class="prettyprint prettyprinted" style="background-color:
      #f8f8f8; border: 1px solid rgb(204, 204, 204); overflow-x: auto; padding: 10px; white-space:
      pre-wrap; word-spacing: 0px; word-wrap: break-word;"><code style="margin-right: 1px;
      padding: 0px;"><span class="typ" style="color: #660066;">Note</span><span
      class="pun" style="color: #666600;">:-</span><span class="pln">
      </span><span class="typ" style="color: #660066;">Array</span><span
      class="pln"> indexing </span><span class="kwd" style="color:
      #000088;">is</span><span class="pln"> </span><span class="kwd"
      style="color: #000088;">from</span><span class="pln"> </span><span
      class="lit" style="color:
      #006666;">0.</span></code></pre><p><span style="font-weight:
      600;">Input</span>:</p><pre class="prettyprint prettyprinted"
      style="background-color: #f8f8f8; border: 1px solid rgb(204, 204, 204); overflow-x: auto;
      padding: 10px; white-space: pre-wrap; word-spacing: 0px; word-wrap: break-word;"><code
      style="margin-right: 1px; padding: 0px;"><span class="pln"> </span><span
      class="typ" style="color: #660066;">The</span><span class="pln"> first line
      contains two space separated integers N</span><span class="pun" style="color:
      #666600;">(</span><span class="typ" style="color:
      #660066;">Length</span><span class="pln"> of </span><span class="typ"
      style="color: #660066;">Array</span><span class="pun" style="color:
      #666600;">)</span><span class="pln"> </span><span class="kwd"
      style="color: #000088;">and</span><span class="pln"> Q</span><span
      class="pun" style="color: #666600;">(</span><span class="typ" style="color:
      #660066;">Queries</span><span class="pun" style="color:
      #666600;">).</span><span class="pln">
      </span><span class="typ" style="color: #660066;">Next</span><span
      class="pln"> </span><span class="typ" style="color:
      #660066;">Line</span><span class="pln"> contains N space separated integers
      denoting array A</span><span class="pun" style="color:
      #666600;">.</span><span class="pln">
      </span><span class="typ" style="color: #660066;">Next</span><span
      class="pln"> Q </span><span class="typ" style="color:
      #660066;">Line</span><span class="pln"> contains </span><span
      class="lit" style="color: #006666;">3</span><span class="pln"> space separated
      integers </span><span class="kwd" style="color: #000088;">for</span><span
      class="pln"> each line</span><span class="pun" style="color:
      #666600;">,</span><span class="pln"> </span><span class="kwd"
      style="color: #000088;">as</span><span class="pln"> described
      above</span></code></pre><p><span style="font-weight:
      600;">Output</span>: Answer to the each query of type 2 in a new line, only when
      range is valid, otherwise ouput `-1`</p><p><span style="font-weight:
      600;">Constraints:</span><span
      class="Apple-converted-space">&nbsp;</span>1 &lt;= N &lt;= 10^9 1
      &lt;= Q &lt;= 10^5 1 &lt;= A[i], X, Y, L, R &lt;=
      10^5</p></div><div class="less-margin-2 input-output-container"
      style="background-color: white; border-radius: 3px; border: 1px solid rgb(229, 231, 232);
      caret-color: rgb(37, 44, 51); color: #252c33; font-family: &quot;Open Sans&quot;,
      sans-serif; font-size: 14px; line-height: 21px; margin: 10px 0px 0px; text-size-adjust: auto;
      word-spacing: 1px;"><div class="input-output right-border" style="border-right-color:
      rgb(229, 231, 232); border-right-style: solid; border-right-width: 1px; box-sizing:
      border-box; float: left; overflow-x: auto; white-space: nowrap; width: 307px;"><div
      class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); padding: 6px
      10px;"><div class="weight-600 less-margin-right light float-left small" style="color:
      #9ca3a8; float: left; font-size: 12px; font-weight: 600; margin-right: 5px;">SAMPLE
      INPUT</div><div class="input-output-opt float-right" style="float: right;"><a
      class="track-problem-sample-input tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/breakfast-challenge/problems/ee3de7568a-sample-input-ee3d805.txt?Signature=XdkCqZGBHkWnxVnfFvUk0HY8kIE%3D&amp;Expires=1600165005&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
      style="color: #4c9cdf; cursor: pointer; font-size: 16px; margin: 0px 5px;
      text-decoration-line: none;" target="_blank"><span class="fa fa-link"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; line-height: 1; text-rendering:
      auto;"></span></a><span
      class="Apple-converted-space">&nbsp;</span><a
      class="track-problem-sample-input-copy input-output-copy tool-tip" style="color: #4c9cdf;
      cursor: pointer; font-size: 16px; margin: 0px 5px;"><span class="fa fa-files-o"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; line-height: 1; text-rendering:
      auto;"></span></a></div><div class="clear" style="clear:
      both;"></div></div><div class="dark" style="color: #46535e;"><pre
      class="word-spacing-0" style="margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word;
      overflow-x: auto; padding: 10px; white-space: pre-wrap; word-spacing: 0px;">5 5
      2 3 4 8 9
      1 0 3
      2 0 1
      2 0 4
      1 2 5
      2 0 3</pre></div></div><div class="input-output" style="box-sizing:
      border-box; float: left; overflow-x: auto; white-space: nowrap; width: 307px;"><div
      class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); padding: 6px
      10px;"><div class="weight-600 float-left less-margin-right light small" style="color:
      #9ca3a8; float: left; font-size: 12px; font-weight: 600; margin-right: 5px;">SAMPLE
      OUTPUT</div><div class="input-output-opt float-right" style="float: right;"><a
      class="track-problem-sample-output tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/breakfast-challenge/problems/d6eb642e8a-sample-output-d6eafca.txt?Signature=tbH9cUvN7tb8z4SRD7OssZY1qwU%3D&amp;Expires=1600165005&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
      style="color: #4c9cdf; cursor: pointer; font-size: 16px; margin: 0px 5px;
      text-decoration-line: none;" target="_blank"><span class="fa fa-link"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; line-height: 1; text-rendering:
      auto;"></span></a><span
      class="Apple-converted-space">&nbsp;</span><a
      class="track-problem-sample-output-copy input-output-copy tool-tip" style="color: #4c9cdf;
      cursor: pointer; font-size: 16px; margin: 0px 5px;"><span class="fa fa-files-o"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; line-height: 1; text-rendering:
      auto;"></span></a></div><div class="clear" style="clear:
      both;"></div></div><div class="dark" style="color: #46535e;"><pre
      class="word-spacing-0" style="margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word;
      overflow-x: auto; padding: 10px; white-space: pre-wrap; word-spacing: 0px;">6
      27
      19</pre></div></div><div class="clear" style="clear:
      both;"></div></div><div class="standard-margin" style="background-color:
      white; caret-color: rgb(37, 44, 51); color: #252c33; font-family: &quot;Open
      Sans&quot;, sans-serif; font-size: 14px; margin: 30px 0px 0px; text-size-adjust: auto;
      word-spacing: 1px;"><span class="weight-600 form-label" style="font-weight:
      600;">Explanation</span><div class="less-margin" style="margin: 5px 0px
      0px;"><pre class="prettyprint prettyprinted" style="background-color: #f8f8f8; border:
      1px solid rgb(204, 204, 204); overflow-x: auto; padding: 10px; white-space: pre-wrap;
      word-spacing: 0px; word-wrap: break-word;"><code style="margin-right: 1px; padding:
      0px;"><span class="pln">

      </span><span class="typ" style="color: #660066;">After</span><span
      class="pln"> </span><span class="typ" style="color:
      #660066;">First</span><span class="pln"> query</span><span class="pun"
      style="color: #666600;">:</span><span class="pln">

      </span><span class="typ" style="color: #660066;">Array</span><span
      class="pln"> becomes </span><span class="lit" style="color:
      #006666;">3</span><span class="pln"> </span><span class="lit"
      style="color: #006666;">3</span><span class="pln"> </span><span
      class="lit" style="color: #006666;">4</span><span class="pln">
      </span><span class="lit" style="color: #006666;">8</span><span
      class="pln"> </span><span class="lit" style="color:
      #006666;">9</span><span class="pln">

      </span><span class="typ" style="color: #660066;">After</span><span
      class="pln"> </span><span class="typ" style="color:
      #660066;">Second</span><span class="pln"> query</span><span
      class="pun" style="color: #666600;">:</span><span class="pln">
      </span><span class="typ" style="color: #660066;">Sum</span><span
      class="pln"> of range </span><span class="pun" style="color:
      #666600;">[</span><span class="lit" style="color:
      #006666;">0</span><span class="pun" style="color:
      #666600;">,</span><span class="pln"> </span><span class="lit"
      style="color: #006666;">1</span><span class="pun" style="color:
      #666600;">]</span><span class="pln"> i</span><span class="pun"
      style="color: #666600;">.</span><span class="pln">e</span><span
      class="pun" style="color: #666600;">.</span><span class="pln">
      A</span><span class="pun" style="color: #666600;">[</span><span
      class="lit" style="color: #006666;">0</span><span class="pun" style="color:
      #666600;">]+</span><span class="pln">A</span><span class="pun"
      style="color: #666600;">[</span><span class="lit" style="color:
      #006666;">1</span><span class="pun" style="color:
      #666600;">]</span><span class="pln"> </span><span class="kwd"
      style="color: #000088;">is</span><span class="pln"> </span><span
      class="lit" style="color: #006666;">6</span><span class="pln">
      </span><span class="typ" style="color: #660066;">After</span><span
      class="pln"> </span><span class="typ" style="color:
      #660066;">Third</span><span class="pln"> query

      </span><span class="typ" style="color: #660066;">Sum</span><span
      class="pln"> of range </span><span class="pun" style="color:
      #666600;">[</span><span class="lit" style="color:
      #006666;">0</span><span class="pun" style="color:
      #666600;">,</span><span class="pln"> </span><span class="lit"
      style="color: #006666;">4</span><span class="pun" style="color:
      #666600;">]</span><span class="pln"> </span><span class="kwd"
      style="color: #000088;">is</span><span class="pln"> </span><span
      class="lit" style="color: #006666;">27</span><span class="pln">
      </span><span class="typ" style="color: #660066;">After</span><span
      class="pln"> </span><span class="typ" style="color:
      #660066;">Fourth</span><span class="pln"> query

      </span><span class="typ" style="color: #660066;">Array</span><span
      class="pln"> becomes </span><span class="lit" style="color:
      #006666;">3</span><span class="pln"> </span><span class="lit"
      style="color: #006666;">3</span><span class="pln"> </span><span
      class="lit" style="color: #006666;">5</span><span class="pln">
      </span><span class="lit" style="color: #006666;">8</span><span
      class="pln"> </span><span class="lit" style="color:
      #006666;">9</span><span class="pln">

      </span><span class="typ" style="color: #660066;">After</span><span
      class="pln"> </span><span class="typ" style="color:
      #660066;">Fifth</span><span class="pln"> query

      </span><span class="typ" style="color: #660066;">Sum</span><span
      class="pln"> of range </span><span class="pun" style="color:
      #666600;">[</span><span class="lit" style="color:
      #006666;">0</span><span class="pun" style="color:
      #666600;">,</span><span class="pln"> </span><span class="lit"
      style="color: #006666;">3</span><span class="pun" style="color:
      #666600;">]</span><span class="pln"> </span><span class="kwd"
      style="color: #000088;">is</span><span class="pln"> </span><span
      class="lit" style="color:
      #006666;">19</span></code></pre></div></div>
      <script
      src="https://gist.github.com/Svastikkka/6a5dbe12e97f6ce1b6464ea871a22675.js"></script>

Write your content here...