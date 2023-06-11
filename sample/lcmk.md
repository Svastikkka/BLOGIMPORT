# LCM^k

Published: 2020-07-26T23:42:00.001+05:30

Description: 
      <div class="starwars-lab" style="background-color: white; caret-color:
      rgb(37, 44, 51); color: #252c33; font-family: &quot;Open Sans&quot;, sans-serif;
      font-size: 14px; text-size-adjust: auto; word-spacing: 1px;"><p>Given three
      integers<span class="Apple-converted-space">&nbsp;</span><em><span
      style="font-weight: 600;">N,M,K</span></em>&nbsp;and array of
      integers<span class="Apple-converted-space">&nbsp;</span><em><span
      style="font-weight:
      600;">a<sub>1</sub>,a<sub>2</sub>,...,a<sub>n</sub></span></em>.<br
      />Find the value of<span
      class="Apple-converted-space">&nbsp;</span><em>LCM</em><span
      style="font-weight:
      600;"><em>(a<sub>1</sub><sup>k</sup>,a<sub>2</sub><sup>k</sup>,...,a<sub>n</sub><sup>k</sup>)<span
      class="Apple-converted-space">&nbsp;</span></em></span><em>mod<span
      class="Apple-converted-space">&nbsp;</span></em><span
      style="font-weight: 600;"><em>M</em></span>, where<span
      class="Apple-converted-space">&nbsp;</span><em>LCM</em><span
      class="Apple-converted-space">&nbsp;</span>means<span
      class="Apple-converted-space">&nbsp;</span><em>Least Common
      Multiple</em>.</p><p><span style="font-weight:
      600;"><em>Input</em></span></p><p>The first line of the input
      contains a single integer<span
      class="Apple-converted-space">&nbsp;</span><em><span style="font-weight:
      600;">T</span></em><span
      class="Apple-converted-space">&nbsp;</span>denoting the number of test cases(1
      ≤&nbsp;<span style="font-weight: 600;"><em>T</em></span><span
      class="Apple-converted-space">&nbsp;</span>≤&nbsp;10).&nbsp;<br
      />The description of<span
      class="Apple-converted-space">&nbsp;</span><span style="font-weight:
      600;"><em>T</em></span><span
      class="Apple-converted-space">&nbsp;</span>test cases follows.<br />First
      line contains three positive integers<span
      class="Apple-converted-space">&nbsp;</span><span style="font-weight:
      600;"><em>N, M, K</em></span>(1 ≤<span
      class="Apple-converted-space">&nbsp;</span><span style="font-weight:
      600;"><em>N</em></span>&nbsp;≤&nbsp;3 *
      10<sup>5</sup>, 1 ≤<span
      class="Apple-converted-space">&nbsp;</span><em><span style="font-weight:
      600;">M</span></em>,<span
      class="Apple-converted-space">&nbsp;</span><span style="font-weight:
      600;"><em>K</em></span>&nbsp;≤&nbsp;10<sup>9</sup>).<br
      />The second line contains<span
      class="Apple-converted-space">&nbsp;</span><em><span style="font-weight:
      600;">N</span></em><span
      class="Apple-converted-space">&nbsp;</span>space-separated integers<span
      class="Apple-converted-space">&nbsp;</span><span style="font-weight:
      600;"><em>a<sub>1</sub>,a<sub>2</sub>,...,a<sub>n</sub></em></span>.(1
      ≤ a<sub>i</sub><span
      class="Apple-converted-space">&nbsp;</span>≤&nbsp;10<sup>6</sup>,1
      ≤<span class="Apple-converted-space">&nbsp;</span><em><span
      style="font-weight: 600;">i</span></em><span
      class="Apple-converted-space">&nbsp;</span>≤<span
      class="Apple-converted-space">&nbsp;</span><span style="font-weight:
      600;"><em>N</em></span>).</p><p><em><span
      style="font-weight: 600;">Output</span></em><br />For each test case
      print the value of<span
      class="Apple-converted-space">&nbsp;</span><em>LCM</em><span
      style="font-weight:
      600;"><em>(a<sub>1</sub><sup>k</sup>,a<sub>2</sub><sup>k</sup>,...,a<sub>n</sub><sup>k</sup>)<span
      class="Apple-converted-space">&nbsp;</span></em></span><em>mod<span
      class="Apple-converted-space">&nbsp;</span></em><span
      style="font-weight: 600;"><em>M</em></span>.</p></div><div
      class="less-margin-2 input-output-container" style="background-color: white; border-radius:
      3px; border: 1px solid rgb(229, 231, 232); caret-color: rgb(37, 44, 51); color: #252c33;
      font-family: &quot;Open Sans&quot;, sans-serif; font-size: 14px; line-height: 21px;
      margin: 10px 0px 0px; text-size-adjust: auto; word-spacing: 1px;"><div
      class="input-output right-border" style="border-right-color: rgb(229, 231, 232);
      border-right-style: solid; border-right-width: 1px; box-sizing: border-box; float: left;
      overflow-x: auto; white-space: nowrap; width: 330.5px;"><div class="form-label"
      style="border-bottom: 1px solid rgb(229, 231, 232); padding: 6px 10px;"><div
      class="weight-600 less-margin-right light float-left small" style="color: #9ca3a8; float:
      left; font-size: 12px; font-weight: 600; margin-right: 5px;">SAMPLE
      INPUT</div><div class="input-output-opt float-right" style="float: right;"><a
      class="track-problem-sample-input tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/july-circuits-20/problems/b904998ec74d11ea.txt?Signature=zvfVEFGz3aK8%2BBeE1zPcGzH1Fy4%3D&amp;Expires=1595790580&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
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
      overflow-x: auto; padding: 10px; white-space: pre-wrap; word-spacing: 0px;">1
      5 20 3
      17 2 9 4 12
      </pre></div></div><div class="input-output" style="box-sizing:
      border-box; float: left; overflow-x: auto; white-space: nowrap; width: 330.5px;"><div
      class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); padding: 6px
      10px;"><div class="weight-600 float-left less-margin-right light small" style="color:
      #9ca3a8; float: left; font-size: 12px; font-weight: 600; margin-right: 5px;">SAMPLE
      OUTPUT</div><div class="input-output-opt float-right" style="float: right;"><a
      class="track-problem-sample-output tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/july-circuits-20/problems/b9022122c74d11ea.txt?Signature=C9o9oYIq3G4z549GmcaP7awdPjg%3D&amp;Expires=1595790580&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
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
      overflow-x: auto; padding: 10px; white-space: pre-wrap; word-spacing:
      0px;">8</pre></div></div><div class="clear" style="clear:
      both;"></div></div><div class="standard-margin" style="background-color:
      white; caret-color: rgb(37, 44, 51); color: #252c33; font-family: &quot;Open
      Sans&quot;, sans-serif; font-size: 14px; margin: 30px 0px 0px; text-size-adjust: auto;
      word-spacing: 1px;"><span class="weight-600 form-label" style="font-weight:
      600;">Explanation</span><div class="less-margin" style="margin: 5px 0px
      0px;"><p>In the test
      LCM(17<sup>3</sup>,2<sup>3</sup>,9<sup>3</sup>,4<sup>3</sup>,12<sup>3</sup>)
      =&nbsp;229220928,&nbsp;229220928 mod 20 = 8.</p><p>Note:- Time Extended
      Problem Occur</p></div></div>
      <script
      src="https://gist.github.com/Svastikkka/889c305050c00d577c15dce77ec85cdb.js"></script>

Write your content here...