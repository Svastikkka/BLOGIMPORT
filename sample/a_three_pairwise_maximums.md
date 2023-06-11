# A. Three Pairwise Maximums

Published: 2020-07-17T23:28:00.005+05:30

Description: 
      <div><div class="header" style="caret-color: rgb(34, 34, 34);
      color: #222222; font-family: &quot;helvetica neue&quot;, helvetica, arial, sans-serif;
      font-size: 14px; margin: 0px 0px 1em; padding: 0px; text-align: center; text-size-adjust:
      auto;"><div class="title" style="font-size: 21px; margin: 0px 0px 0.5em; padding:
      0px;">A. Three Pairwise Maximums</div><div class="time-limit" style="margin: 0px
      auto; padding: 0px;"><div class="property-title" style="display: inline; margin: 0px;
      padding: 0px 4px 0px 0px;">time limit per test</div>1 second</div><div
      class="memory-limit" style="margin: 0px auto; padding: 0px;"><div class="property-title"
      style="display: inline; margin: 0px; padding: 0px 4px 0px 0px;">memory limit per
      test</div>256 megabytes</div><div class="input-file" style="margin: 0px auto;
      padding: 0px;"><div class="property-title" style="display: inline; margin: 0px; padding:
      0px 4px 0px 0px;">input</div>standard input</div><div class="output-file"
      style="margin: 0px auto; padding: 0px;"><div class="property-title" style="display:
      inline; margin: 0px; padding: 0px 4px 0px 0px;">output</div>standard
      output</div></div><font color="#444444" face="arial"><br /><br
      />You are given three positive (i.e. strictly greater than zero) integers x, y and z.<br
      /><br />Your task is to find positive integers a, b and c such that x=max(a,b),
      y=max(a,c) and z=max(b,c), or determine that it is impossible to find such a, b and c.<br
      /><br />You have to answer t independent test cases. Print required a, b and c in any
      (arbitrary) order.</font></div><div><b style="color: #444444;
      font-family: arial;">Input</b></div><div><div
      class="input-specification" style="caret-color: rgb(34, 34, 34); margin: 0px; padding: 0px;
      text-size-adjust: auto;"><p style="color: #222222; font-family: &quot;helvetica
      neue&quot;, helvetica, arial, sans-serif; font-size: 1em; line-height: 1.4em; margin:
      1.5em 0px 0px; padding: 0px;">The first line of the input contains one integer<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-17-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-70" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.479em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.36em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.789em, 1000.3em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-71" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-72" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑡</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.861em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.068em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>(<span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;&amp;#x22C5;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;4&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-18-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-73" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      7.384em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 6.134em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.491em, 1006.13em, 2.86em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-74" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mn" id="MathJax-Span-75" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">1</span><span class="mo" id="MathJax-Span-76" style="border:
      0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">≤</span><span class="mi" id="MathJax-Span-77"
      style="border: 0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">𝑡</span><span class="mo"
      id="MathJax-Span-78" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.301em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="mn" id="MathJax-Span-79" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">2</span><span class="mo" id="MathJax-Span-80"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.241em; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">⋅</span><span
      class="msubsup" id="MathJax-Span-81" style="border: 0px; box-sizing: content-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.241em; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.432em;"><span style="border: 0px; box-sizing: content-box; clip: rect(3.158em,
      1000.96em, 4.17em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mn" id="MathJax-Span-82" style="border: 0px; box-sizing: content-box;
      display: inline; font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">10</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      1.015em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.402em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn" id="MathJax-Span-83"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;">4</span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 2.562em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: content-box; display:
      inline-block; height: 1.361em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.211em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>t</mi><mo>≤</mo><mn>2</mn><mo>⋅</mo><msup><mn>10</mn><mn>4</mn></msup></math></span></span>)
      — the number of test cases. Then<span
      class="Apple-converted-space">&nbsp;</span><span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-19-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-84" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.479em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.36em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.789em, 1000.3em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-85" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-86" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑡</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.861em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.068em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>test cases follow.</p><p
      style="line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;"><font color="#444444"
      face="arial">The only line of the test case contains three integers x, y, and z
      (1≤x,y,z≤109).<br /></font><span style="color: #222222; font-family:
      &quot;helvetica neue&quot;, helvetica, arial, sans-serif; font-size: 16.1px;
      font-weight: bold;">Output</span></p></div><div
      class="output-specification" style="caret-color: rgb(34, 34, 34); margin: 0px 0px 1em;
      padding: 0px; text-size-adjust: auto;"><font face="arial"><br /><br
      /><font color="#444444">For each test case, print the answer:<br
      /></font><ul style="text-align: left;"><li><font color="#444444"
      face="arial">"NO" in the only line of the output if a solution doesn't
      exist;</font></li><li><font color="#444444">or "YES" in the first line
      <b>and</b> any valid triple of positive integers a, b and c (1≤a,b,c≤109) in the
      second line. You can print a, band c <b>in any
      order.</b></font></li></ul></font></div><div
      class="sample-tests" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      consolas, &quot;lucida console&quot;, &quot;andale mono&quot;,
      &quot;bitstream vera sans mono&quot;, &quot;courier new&quot;, courier;
      font-size: 0.9em; margin: 0px; padding: 0px; text-size-adjust: auto;"><div
      class="section-title" style="font-family: &quot;helvetica neue&quot;, helvetica,
      arial, sans-serif; font-size: 14.49px; font-weight: bold; margin: 0px; padding:
      0px;">Example</div><div class="sample-test" style="margin: 0px; padding:
      0px;"><div class="input" style="border: 1px solid rgb(136, 136, 136); margin: 0px;
      padding: 0px;"><div class="title" style="border-bottom: 1px solid rgb(136, 136, 136);
      font-size: 1.3em; font-weight: bold; margin: 0px; padding: 0.25em; text-transform:
      lowercase;">input<div class="input-output-copier"
      data-clipboard-target="#id00043962096895745706" id="id006722418236732743" style="border: 1px
      solid rgb(185, 185, 185); color: #888888; cursor: pointer; float: right; font-size: 1.2rem;
      line-height: 1.1rem; margin: 1px; padding: 3px; text-transform: none;"
      title="Copy">Copy</div></div><pre id="id00043962096895745706"
      style="background-color: #efefef; color: #880000; font-family: consolas, &quot;lucida
      console&quot;, &quot;andale mono&quot;, &quot;bitstream vera sans
      mono&quot;, &quot;courier new&quot;, courier; font-size: 12.6px; line-height:
      1.25em; margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">5
      3 2 3
      100 100 100
      50 49 49
      10 30 20
      1 1000000000 1000000000
      </pre></div><div class="output" style="border: 1px solid rgb(136, 136, 136);
      margin: 0px 0px 1em; padding: 0px; position: relative; top: -1px;"><div class="title"
      style="border-bottom: 1px solid rgb(136, 136, 136); font-size: 1.3em; font-weight: bold;
      margin: 0px; padding: 0.25em; text-transform: lowercase;">output<div
      class="input-output-copier" data-clipboard-target="#id004617242441168725"
      id="id009904508028277501" style="border: 1px solid rgb(185, 185, 185); color: #888888; cursor:
      pointer; float: right; font-size: 1.2rem; line-height: 1.1rem; margin: 1px; padding: 3px;
      text-transform: none;" title="Copy">Copy</div></div><pre
      id="id004617242441168725" style="background-color: #efefef; color: #880000; font-family:
      consolas, &quot;lucida console&quot;, &quot;andale mono&quot;,
      &quot;bitstream vera sans mono&quot;, &quot;courier new&quot;, courier;
      font-size: 12.6px; line-height: 1.25em; margin-bottom: 0px; margin-top: 0px; overflow-wrap:
      break-word; padding: 0.25em; white-space: pre-wrap;">YES
      3 2 1
      YES
      100 100 100
      NO
      NO
      YES
      1 1 1000000000</pre></div></div></div></div><div><br
      /></div><div><br /></div><div><br /></div>
      <script
      src="https://gist.github.com/Svastikkka/1b5904c528e394de9ac2b3ed5c04cc27.js"></script>

Write your content here...