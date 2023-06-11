# B. Restore the Permutation by Merger

Published: 2020-07-17T23:37:00.002+05:30

Description: 
      <div class="header" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;helvetica neue&quot;, helvetica, arial, sans-serif; font-size:
      14px; margin: 0px 0px 1em; padding: 0px; text-align: center; text-size-adjust:
      auto;"><div class="title" style="font-size: 21px; margin: 0px 0px 0.5em; padding:
      0px;">B. Restore the Permutation by Merger</div><div class="time-limit"
      style="margin: 0px auto; padding: 0px;"><div class="property-title" style="display:
      inline; margin: 0px; padding: 0px 4px 0px 0px;">time limit per test</div>1
      second</div><div class="memory-limit" style="margin: 0px auto; padding:
      0px;"><div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px
      0px 0px;">memory limit per test</div>256 megabytes</div><div
      class="input-file" style="margin: 0px auto; padding: 0px;"><div class="property-title"
      style="display: inline; margin: 0px; padding: 0px 4px 0px 0px;">input</div>standard
      input</div><div class="output-file" style="margin: 0px auto; padding:
      0px;"><div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px
      0px 0px;">output</div>standard output</div></div><div
      style="caret-color: rgb(34, 34, 34); margin: 0px; padding: 0px; text-size-adjust:
      auto;"><font color="#444444" face="arial"><br /><br />A permutation of
      length n is a sequence of integers from 1 to n of length n containing each number exactly
      once. For example, [1], [4,3,5,1,2], [3,2,1] are permutations, and [1,1], [0,1], [2,2,1,4] are
      not.<br /><br />There was a permutation p[1…n]. It was merged with itself. In
      other words, let's take two instances of p and insert elements of the second p into the first
      maintaining relative order of elements. The result is a sequence of the length 2n.<br
      /><br />For example, if p=[3,1,2] some possible results are: [3,1,2,3,1,2],
      [3,3,1,1,2,2], [3,1,3,1,2,2]. The following sequences are not possible results of a merging:
      [1,3,2,1,2,3], [3,1,2,3,2,1], [3,3,1,2,2,1].<br /><br />For example, if p=[2,1]
      the possible results are: [2,2,1,1], [2,1,2,1]. The following sequences are not possible
      results of a merging: [1,1,2,2], [2,1,1,2], [1,2,2,1].</font><p style="color:
      #222222; font-family: &quot;helvetica neue&quot;, helvetica, arial, sans-serif;
      line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;">Your task is to restore the
      permutation<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-28-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-244" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.539em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1000.54em, 2.92em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-245" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-246" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.861em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.282em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>by the given resulting
      sequence<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-29-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-247" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.539em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1000.48em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-248" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-249" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑎</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.718em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.068em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></span></span>.
      It is guaranteed that the answer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-bf"
      style="font-weight: bold;">exists and is unique</span>.</p><p style="color:
      #222222; font-family: &quot;helvetica neue&quot;, helvetica, arial, sans-serif;
      line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;">You have to answer<span
      class="Apple-converted-space">&nbsp;</span><font color="rgba(0, 0, 0,
      0)"><span class="MathJax_Preview" style="color:
      inherit;"></span></font><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-30-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-250" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.479em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.36em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.789em, 1000.3em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-251" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-252" style="border: 0px;
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
      class="Apple-converted-space">&nbsp;</span>independent test
      cases.</p></div><div class="input-specification" style="caret-color: rgb(34,
      34, 34); color: #222222; font-family: &quot;helvetica neue&quot;, helvetica, arial,
      sans-serif; font-size: 14px; margin: 0px; padding: 0px; text-size-adjust: auto;"><div
      class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px; padding:
      0px;">Input</div><p style="font-size: 1em; line-height: 1.4em; margin: 1.5em 0px
      0px; padding: 0px;">The first line of the input contains one integer<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-31-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-253" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.479em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.36em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.789em, 1000.3em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-254" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-255" style="border: 0px;
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
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;400&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-32-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-256" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.955em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 4.943em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.729em, 1004.94em, 2.86em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-257" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mn" id="MathJax-Span-258" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">1</span><span class="mo" id="MathJax-Span-259"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.301em; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">≤</span><span
      class="mi" id="MathJax-Span-260" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.301em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑡</span><span class="mo" id="MathJax-Span-261" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">≤</span><span class="mn" id="MathJax-Span-262"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.301em; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">400</span></span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 2.562em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 1.075em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.211em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>t</mi><mo>≤</mo><mn>400</mn></math></span></span>)
      — the number of test cases. Then<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-33-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-263" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.479em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.36em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.789em, 1000.3em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-264" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-265" style="border: 0px;
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
      style="font-size: 1em; line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;">The first
      line of the test case contains one integer<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-34-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-266" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.539em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1000.48em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-267" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-268" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑛</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.718em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.068em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>(<span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;50&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-35-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-269" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.598em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 4.646em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.67em, 1004.65em, 2.86em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-270" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mn" id="MathJax-Span-271" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">1</span><span class="mo" id="MathJax-Span-272"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.301em; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">≤</span><span
      class="mi" id="MathJax-Span-273" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.301em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑛</span><span class="mo" id="MathJax-Span-274" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">≤</span><span class="mn" id="MathJax-Span-275"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.301em; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">50</span></span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 2.562em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 1.075em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.211em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>50</mn></math></span></span>)
      — the length of permutation. The second line of the test case contains<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-36-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-276" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.253em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 1.015em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.729em, 1000.96em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-277" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mn" id="MathJax-Span-278" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">2</span><span class="mi" id="MathJax-Span-279"
      style="border: 0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑛</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.932em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.068em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>integers<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;&amp;#x2026;&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-37-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-280" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      6.967em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 5.777em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1005.78em, 2.92em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-281" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="msubsup" id="MathJax-Span-282" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.955em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.396em, 1000.48em, 4.17em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-283" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑎</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-284" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-285" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="msubsup" id="MathJax-Span-286" style="border: 0px; box-sizing: content-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.182em; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.955em;"><span style="border: 0px; box-sizing: content-box; clip: rect(3.396em,
      1000.48em, 4.17em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mi" id="MathJax-Span-287" style="border: 0px; box-sizing:
      content-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑎</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-288" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-289" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="mo" id="MathJax-Span-290" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.182em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">…</span><span class="mo" id="MathJax-Span-291" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.182em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">,</span><span class="msubsup" id="MathJax-Span-292"
      style="border: 0px; box-sizing: content-box; display: inline; line-height: normal; margin:
      0px; padding: 0px 0px 0px 0.182em; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 1.313em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.396em, 1000.48em, 4.17em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-293"
      style="border: 0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑎</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-294" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-295" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-296" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span class="mi" id="MathJax-Span-297" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; font-size:
      11.8776px; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none
      0s ease 0s; vertical-align: 0px;">𝑛</span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 2.562em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: content-box; display:
      inline-block; height: 0.861em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.282em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>…</mo><mo>,</mo><msub><mi>a</mi><mrow
      class="MJX-TeXAtom-ORD"><mn>2</mn><mi>n</mi></mrow></msub></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>(<span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-38-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-298" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.301em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 4.408em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.729em, 1004.35em, 2.92em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-299" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mn" id="MathJax-Span-300" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">1</span><span class="mo" id="MathJax-Span-301"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.301em; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">≤</span><span
      class="msubsup" id="MathJax-Span-302" style="border: 0px; box-sizing: content-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.777em;"><span style="border: 0px; box-sizing: content-box; clip: rect(3.396em,
      1000.48em, 4.17em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mi" id="MathJax-Span-303" style="border: 0px; box-sizing:
      content-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑎</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-304" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑖</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-305" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.301em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="mi" id="MathJax-Span-306" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">𝑛</span></span><span style="border: 0px;
      box-sizing: content-box; display: inline-block; height: 2.562em; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 1.146em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.282em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><msub><mi>a</mi><mi>i</mi></msub><mo>≤</mo><mi>n</mi></math></span></span>),
      where<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-39-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-307" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.015em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.836em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.61em, 1000.84em, 2.562em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.199em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-308" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="msubsup" id="MathJax-Span-309" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.777em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.396em, 1000.48em, 4.17em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-310" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑎</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-311" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑖</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 2.205em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: content-box; display:
      inline-block; height: 0.861em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.282em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>i</mi></msub></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>is the<span
      class="Apple-converted-space">&nbsp;</span><span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-40-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-312" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.479em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.36em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.789em, 1000.3em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-313" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-314" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑖</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.932em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.068em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></span></span>-th
      element of<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-41-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-315" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.539em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1000.48em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-316" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-317" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑎</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.718em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.068em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></span></span>.
      It is guaranteed that the array<span
      class="Apple-converted-space">&nbsp;</span><span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-42-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-318" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.539em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1000.48em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-319" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-320" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑎</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.718em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.068em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>represents the result of merging of
      some permutation<span class="Apple-converted-space">&nbsp;</span><span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-43-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-321" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.539em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1000.54em, 2.92em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-322" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-323" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.861em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.282em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>with the same permutation<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-44-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-324" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.539em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1000.54em, 2.92em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-325" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-326" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.861em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.282em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></span></span>.</p></div><div
      class="output-specification" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      &quot;helvetica neue&quot;, helvetica, arial, sans-serif; font-size: 14px; margin: 0px
      0px 1em; padding: 0px; text-size-adjust: auto;"><div class="section-title"
      style="font-size: 16.1px; font-weight: bold; margin: 0px; padding:
      0px;">Output</div><p style="font-size: 1em; line-height: 1.4em; margin: 1.5em 0px
      0px; padding: 0px;">For each test case, print the answer:<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-45-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-327" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.539em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1000.48em, 2.741em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-328" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-329" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑛</span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 2.562em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 0.718em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.068em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>integers<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;&amp;#x2026;&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-46-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-330" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      6.313em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 5.241em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.967em, 1005.24em, 2.92em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-331" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="msubsup" id="MathJax-Span-332" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.896em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-333" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-334" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-335" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="msubsup" id="MathJax-Span-336" style="border: 0px; box-sizing: content-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.182em; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.896em;"><span style="border: 0px; box-sizing: content-box; clip: rect(3.396em,
      1000.48em, 4.348em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mi" id="MathJax-Span-337" style="border: 0px; box-sizing:
      content-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑝</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-338" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-339" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="mo" id="MathJax-Span-340" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.182em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">…</span><span class="mo" id="MathJax-Span-341" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.182em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">,</span><span class="msubsup" id="MathJax-Span-342"
      style="border: 0px; box-sizing: content-box; display: inline; line-height: normal; margin:
      0px; padding: 0px 0px 0px 0.182em; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.896em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-343"
      style="border: 0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-344" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑛</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 2.562em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: content-box; display:
      inline-block; height: 0.861em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.282em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mn>1</mn></msub><mo>,</mo><msub><mi>p</mi><mn>2</mn></msub><mo>,</mo><mo>…</mo><mo>,</mo><msub><mi>p</mi><mi>n</mi></msub></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>(<span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-47-Frame" role="presentation" style="border: 0px; color: black; direction:
      ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-345" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.301em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 4.408em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.729em, 1004.35em, 2.92em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-346" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mn" id="MathJax-Span-347" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">1</span><span class="mo" id="MathJax-Span-348"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.301em; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">≤</span><span
      class="msubsup" id="MathJax-Span-349" style="border: 0px; box-sizing: content-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.777em;"><span style="border: 0px; box-sizing: content-box; clip: rect(3.396em,
      1000.48em, 4.348em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mi" id="MathJax-Span-350" style="border: 0px; box-sizing:
      content-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑝</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-351" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑖</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-352" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.301em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="mi" id="MathJax-Span-353" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">𝑛</span></span><span style="border: 0px;
      box-sizing: content-box; display: inline-block; height: 2.562em; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 1.146em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.282em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><msub><mi>p</mi><mi>i</mi></msub><mo>≤</mo><mi>n</mi></math></span></span>),
      representing the initial permutation. It is guaranteed that the answer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-bf"
      style="font-weight: bold;">exists and is unique</span>.</p></div><div
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
      data-clipboard-target="#id00019049528043945885" id="id008075398654659686" style="border: 1px
      solid rgb(185, 185, 185); color: #888888; cursor: pointer; float: right; font-size: 1.2rem;
      line-height: 1.1rem; margin: 1px; padding: 3px; text-transform: none;"
      title="Copy">Copy</div></div><pre id="id00019049528043945885"
      style="background-color: #efefef; color: #880000; font-family: consolas, &quot;lucida
      console&quot;, &quot;andale mono&quot;, &quot;bitstream vera sans
      mono&quot;, &quot;courier new&quot;, courier; font-size: 12.6px; line-height:
      1.25em; margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">5
      2
      1 1 2 2
      4
      1 3 1 4 3 4 2 2
      5
      1 2 1 2 3 4 3 5 4 5
      3
      1 2 3 1 2 3
      4
      2 3 2 4 1 3 4 1
      </pre></div><div class="output" style="border: 1px solid rgb(136, 136, 136);
      margin: 0px 0px 1em; padding: 0px; position: relative; top: -1px;"><div class="title"
      style="border-bottom: 1px solid rgb(136, 136, 136); font-size: 1.3em; font-weight: bold;
      margin: 0px; padding: 0.25em; text-transform: lowercase;">output<div
      class="input-output-copier" data-clipboard-target="#id003146957846983718"
      id="id003874032463216115" style="border: 1px solid rgb(185, 185, 185); color: #888888; cursor:
      pointer; float: right; font-size: 1.2rem; line-height: 1.1rem; margin: 1px; padding: 3px;
      text-transform: none;" title="Copy">Copy</div></div><pre
      id="id003146957846983718" style="background-color: #efefef; color: #880000; font-family:
      consolas, &quot;lucida console&quot;, &quot;andale mono&quot;,
      &quot;bitstream vera sans mono&quot;, &quot;courier new&quot;, courier;
      font-size: 12.6px; line-height: 1.25em; margin-bottom: 0px; margin-top: 0px; overflow-wrap:
      break-word; padding: 0.25em; white-space: pre-wrap;">1 2
      1 3 4 2
      1 2 3 4 5
      1 2 3
      2 3 4 1 </pre></div></div></div><div><br
      /></div><div><br /></div><div><br /></div>
      <script
      src="https://gist.github.com/Svastikkka/a6e62af2346815ca83c339b64912179f.js"></script>

Write your content here...