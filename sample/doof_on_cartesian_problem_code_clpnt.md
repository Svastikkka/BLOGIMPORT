# Doof on Cartesian Problem Code: CLPNT

Published: 2020-07-16T11:49:00.004+05:30

Description: 
      <p class="mathjax-support" style="box-sizing: border-box; color:
      #4a4a4a; font-family: helvetica, sans-serif; font-size: 15px; font-stretch: normal;
      line-height: 1.7; margin: 0px 0px 20px; padding: 0px; text-rendering:
      optimizelegibility;">You may have helped Chef and prevented Doof from destroying the even
      numbers. But, it has only angered Dr Doof even further. However, for his next plan, he needs
      some time. Therefore, Doof has built<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-1-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-1" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.947em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.781em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1000.78em, 2.669em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-2" style="border: 0px; box-sizing: border-box;
      display: inline; line-height: normal; margin: 0px; padding: 0px; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-3"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">N<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.058em;"></span></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>walls to prevent Chef from
      interrupting him. You have to help Chef by telling him the number of walls he needs to destroy
      in order to reach Dr Doof.</p><p class="mathjax-support" style="box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 15px; font-stretch:
      normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px; text-rendering:
      optimizelegibility;">Formally, the whole area can be represented as the first quadrant with
      the origin at the bottom-left corner. Dr. Doof is located at the origin<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-2-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-4" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 2.558em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.114em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.06em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-5" style="border: 0px; box-sizing: border-box;
      display: inline; line-height: normal; margin: 0px; padding: 0px; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-6"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">(</span><span class="mn" id="MathJax-Span-7" style="border:
      0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">0</span><span class="mo" id="MathJax-Span-8" style="border:
      0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">,</span><span class="mn" id="MathJax-Span-9" style="border:
      0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.169em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">0</span><span class="mo" id="MathJax-Span-10"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">)</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><mn></mn><mo></mo><mn></mn><mo
      stretchy="false"></mo></math></span></span>. There are<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-3-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-11" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.947em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.781em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1000.78em, 2.669em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-12" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-13"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">N<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.058em;"></span></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>walls, the i-th wall is a straight
      line segment joining the points<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-4-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-14" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 2.892em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.392em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.34em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-15" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-16"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">(</span><span class="msubsup" id="MathJax-Span-17"
      style="border: 0px; box-sizing: border-box; display: inline; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.781em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.392em, 1000.5em, 4.169em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-18" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">a</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.503em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-19"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      font-size: 12.726px; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">i</span><span style="border:
      0px; box-sizing: border-box; display: inline-block; height: 4.003em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-20" style="border: 0px; box-sizing: border-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">,</span><span class="mn"
      id="MathJax-Span-21" style="border: 0px; box-sizing: border-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.169em; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">0</span><span
      class="mo" id="MathJax-Span-22" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">)</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><msub><mi></mi><mi></mi></msub><mo></mo><mn></mn><mo
      stretchy="false"></mo></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>and<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-5-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-23" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 2.892em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.392em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.34em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-24" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-25"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">(</span><span class="mn" id="MathJax-Span-26" style="border:
      0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">0</span><span class="mo" id="MathJax-Span-27" style="border:
      0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">,</span><span class="msubsup" id="MathJax-Span-28"
      style="border: 0px; box-sizing: border-box; display: inline; line-height: normal; margin: 0px;
      padding: 0px 0px 0px 0.169em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0.781em;"><span style="border: 0px; box-sizing:
      border-box; clip: rect(3.392em, 1000.5em, 4.169em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-29" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">a</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.503em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-30"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      font-size: 12.726px; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">i</span><span style="border:
      0px; box-sizing: border-box; display: inline-block; height: 4.003em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-31" style="border: 0px; box-sizing: border-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">)</span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.503em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.137em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><mn></mn><mo></mo><msub><mi></mi><mi></mi></msub><mo
      stretchy="false"></mo></math></span></span>. For every initial
      position of Chef<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mi&gt;j&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;y&lt;/mi&gt;&lt;mi&gt;j&lt;/mi&gt;&lt;/msub&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-6-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-32" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 3.114em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.558em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.5em, 2.947em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-33" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-34"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">(</span><span class="msubsup" id="MathJax-Span-35"
      style="border: 0px; box-sizing: border-box; display: inline; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.725em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.392em, 1000.45em, 4.169em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-36" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">x<span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px; width:
      0.003em;"></span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.447em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-37"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      font-size: 12.726px; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">j<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-38" style="border: 0px; box-sizing: border-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">,</span><span class="msubsup"
      id="MathJax-Span-39" style="border: 0px; box-sizing: border-box; display: inline; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.169em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.725em;"><span style="border:
      0px; box-sizing: border-box; clip: rect(3.392em, 1000.45em, 4.392em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-40"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">y</span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.447em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-41"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      font-size: 12.726px; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">j<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-42" style="border: 0px; box-sizing: border-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">)</span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.503em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.337em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.397em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><msub><mi></mi><mi></mi></msub><mo></mo><msub><mi></mi><mi></mi></msub><mo
      stretchy="false"></mo></math></span></span>, find the number of
      walls he needs to break before reaching Doof. Obviously, chef can't start from a point on the
      wall. Therefore, if<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mi&gt;j&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;y&lt;/mi&gt;&lt;mi&gt;j&lt;/mi&gt;&lt;/msub&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-7-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-43" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 3.114em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.558em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.5em, 2.947em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-44" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-45"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">(</span><span class="msubsup" id="MathJax-Span-46"
      style="border: 0px; box-sizing: border-box; display: inline; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.725em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.392em, 1000.45em, 4.169em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-47" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">x<span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px; width:
      0.003em;"></span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.447em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-48"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      font-size: 12.726px; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">j<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-49" style="border: 0px; box-sizing: border-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">,</span><span class="msubsup"
      id="MathJax-Span-50" style="border: 0px; box-sizing: border-box; display: inline; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.169em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.725em;"><span style="border:
      0px; box-sizing: border-box; clip: rect(3.392em, 1000.45em, 4.392em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-51"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">y</span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.447em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-52"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      font-size: 12.726px; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">j<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-53" style="border: 0px; box-sizing: border-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">)</span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.503em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.337em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.397em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><msub><mi></mi><mi></mi></msub><mo></mo><msub><mi></mi><mi></mi></msub><mo
      stretchy="false"></mo></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>lies on any of the given walls,
      print<span class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-8-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-54" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.503em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.225em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1001.11em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-55" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-56"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">−</span><span class="mn" id="MathJax-Span-57" style="border:
      0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">1</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo></mo><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>in a new line.</p><h3
      class="mathjax-support" id="input" style="border-top-style: solid; border-top-width: 1px;
      box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 18px;
      font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px;
      text-rendering: optimizelegibility;">Input</h3><ul class="mathjax-support"
      style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      15px; font-stretch: normal; line-height: 1.7; list-style-position: outside; margin: 0px 0px
      20px 25px; padding: 0px;"><li class="mathjax-support" style="box-sizing: border-box;
      margin: 0px; padding: 0px;">First line contains<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-9-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-58" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.836em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.669em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1000.67em, 2.669em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-59" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-60"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">T<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.058em;"></span></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span>,
      denoting the number of testcases.</li><li class="mathjax-support" style="box-sizing:
      border-box; margin: 0px; padding: 0px;">The first line of every test case contains a single
      integer<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-10-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-61" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.947em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.781em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1000.78em, 2.669em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-62" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-63"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">N<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.058em;"></span></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>denoting the number of walls Dr Doof
      has built.</li><li class="mathjax-support" style="box-sizing: border-box; margin:
      0px; padding: 0px;">The next line contains<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-11-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-64" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.947em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.781em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1000.78em, 2.669em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-65" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-66"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">N<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.058em;"></span></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>space separated distinct integers each
      denoting<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-12-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-67" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.003em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.836em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.558em,
      1000.84em, 2.503em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.164em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-68" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="msubsup"
      id="MathJax-Span-69" style="border: 0px; box-sizing: border-box; display: inline; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.781em;"><span style="border:
      0px; box-sizing: border-box; clip: rect(3.392em, 1000.5em, 4.169em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-70"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">a</span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.503em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-71"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      font-size: 12.726px; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">i</span><span style="border:
      0px; box-sizing: border-box; display: inline-block; height: 4.003em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.169em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 0.87em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi></mi><mi></mi></msub></math></span></span>.</li><li
      class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding: 0px;">The next
      line contains a single integer<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;Q&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-13-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-72" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.892em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.725em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1000.73em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-73" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-74"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">Q</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>denoting the number of times Chef asks
      for your help.</li><li class="mathjax-support" style="box-sizing: border-box; margin:
      0px; padding: 0px;">The next<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;Q&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-14-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-75" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.892em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.725em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1000.73em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-76" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-77"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">Q</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>lines contains two space separated
      integers<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mi&gt;j&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-15-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-78" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.947em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.781em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.558em,
      1000.78em, 2.614em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.164em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-79" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="msubsup"
      id="MathJax-Span-80" style="border: 0px; box-sizing: border-box; display: inline; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.725em;"><span style="border:
      0px; box-sizing: border-box; clip: rect(3.392em, 1000.45em, 4.169em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-81"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">x<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.003em;"></span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.447em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-82"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      font-size: 12.726px; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">j<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.169em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.003em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.397em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi></mi><mi></mi></msub></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>and<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;y&lt;/mi&gt;&lt;mi&gt;j&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-16-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-83" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.947em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.781em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.558em,
      1000.78em, 2.614em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.164em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-84" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="msubsup"
      id="MathJax-Span-85" style="border: 0px; box-sizing: border-box; display: inline; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.725em;"><span style="border:
      0px; box-sizing: border-box; clip: rect(3.392em, 1000.45em, 4.392em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-86"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">y</span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.447em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-87"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      font-size: 12.726px; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">j<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.169em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.003em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.397em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi></mi><mi></mi></msub></math></span></span>,
      each denoting the co-ordinates of the starting point of Chef.</li></ul><h3
      class="mathjax-support" id="output" style="border-top-style: solid; border-top-width: 1px;
      box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 18px;
      font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px;
      text-rendering: optimizelegibility;">Output</h3><p class="mathjax-support"
      style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      15px; font-stretch: normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px;
      text-rendering: optimizelegibility;">For each query, print the number of walls Chef needs
      to break in order to reach Dr Doof in a separate line. If Chef tries to start from a point on
      any of the walls, print<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-17-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-88" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.503em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.225em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1001.11em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-89" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-90"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">−</span><span class="mn" id="MathJax-Span-91" style="border:
      0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">1</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo></mo><mn></mn></math></span></span>.</p><h3
      class="mathjax-support" id="constraints" style="border-top-style: solid; border-top-width:
      1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px;
      text-rendering: optimizelegibility;">Constraints</h3><ul class="mathjax-support"
      style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      15px; font-stretch: normal; line-height: 1.7; list-style-position: outside; margin: 0px 0px
      20px 25px; padding: 0px;"><li class="mathjax-support" style="box-sizing: border-box;
      margin: 0px; padding: 0px;"><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;&amp;#x2217;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-18-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-92" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 8.281em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      6.892em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.447em,
      1006.89em, 2.781em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-93" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn" id="MathJax-Span-94"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">1</span><span class="mo" id="MathJax-Span-95" style="border:
      0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.336em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">≤</span><span class="mi" id="MathJax-Span-96"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.336em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">T<span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0.058em;"></span></span><span class="mo" id="MathJax-Span-97"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.336em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">≤</span><span class="mn"
      id="MathJax-Span-98" style="border: 0px; box-sizing: border-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.336em; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">2</span><span
      class="mo" id="MathJax-Span-99" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.281em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">∗</span><span class="msubsup" id="MathJax-Span-100" style="border: 0px;
      box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.281em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.447em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.169em, 1001em, 4.169em, -999.997em); left: 0em; line-height: normal; margin: 0px;
      padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mn" id="MathJax-Span-101" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">10</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      1.003em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.386em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-102" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.503em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.337em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.197em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mo></mo><mi></mi><mo></mo><mn></mn><mo></mo><msup><mn></mn><mn></mn></msup></math></span></span></li><li
      class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding: 0px;"><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mi&gt;Q&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;&amp;#x2217;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;5&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-19-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-103" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 9.781em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      8.114em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.447em,
      1008.11em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-104" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-105" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mo" id="MathJax-Span-106" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="mi" id="MathJax-Span-107" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px 0px 0px 0.336em; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">N<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.058em;"></span></span><span class="mo" id="MathJax-Span-108"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">,</span><span class="mi" id="MathJax-Span-109"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.169em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">Q</span><span class="mo"
      id="MathJax-Span-110" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="mn" id="MathJax-Span-111" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.336em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">2</span><span class="mo" id="MathJax-Span-112"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.281em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">∗</span><span class="msubsup"
      id="MathJax-Span-113" style="border: 0px; box-sizing: border-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.281em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 1.447em;"><span
      style="border: 0px; box-sizing: border-box; clip: rect(3.169em, 1001em, 4.169em, -999.997em);
      left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-114" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">10</span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 4.003em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: border-box; left: 1.003em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -4.386em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mn" id="MathJax-Span-115" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Regular; font-size: 12.726px; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">5</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.503em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.403em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mo></mo><mi></mi><mo></mo><mi></mi><mo></mo><mn></mn><mo></mo><msup><mn></mn><mn></mn></msup></math></span></span></li><li
      class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding: 0px;"><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;9&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-20-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-116" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 6.558em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.447em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.447em,
      1005.45em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-117" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-118" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mo" id="MathJax-Span-119" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="msubsup" id="MathJax-Span-120" style="border: 0px;
      box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.336em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.781em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.392em, 1000.5em, 4.169em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-121" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">a</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.503em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-122" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">i</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-123" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="msubsup" id="MathJax-Span-124" style="border: 0px;
      box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.336em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.447em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.169em, 1001em, 4.169em, -999.997em); left: 0em; line-height: normal; margin: 0px;
      padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mn" id="MathJax-Span-125" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">10</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      1.003em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.386em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-126" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">9</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.503em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.403em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mo></mo><msub><mi></mi><mi></mi></msub><mo></mo><msup><mn></mn><mn></mn></msup></math></span></span></li><li
      class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding: 0px;"><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mi&gt;j&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;y&lt;/mi&gt;&lt;mi&gt;j&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;9&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-21-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-127" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 7.892em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      6.558em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.447em,
      1006.56em, 2.947em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-128" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-129" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">0</span><span
      class="mo" id="MathJax-Span-130" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="msubsup" id="MathJax-Span-131" style="border: 0px;
      box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.336em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.725em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.392em, 1000.45em, 4.169em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-132" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">x<span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px; width:
      0.003em;"></span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.447em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-133" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">j<span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px; width:
      0.003em;"></span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-134" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="msubsup" id="MathJax-Span-135" style="border: 0px; box-sizing: border-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.169em; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.725em;"><span style="border: 0px; box-sizing: border-box; clip: rect(3.392em,
      1000.45em, 4.392em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -3.997em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mi" id="MathJax-Span-136" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">y</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.447em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-137" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">j<span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px; width:
      0.003em;"></span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-138" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="msubsup" id="MathJax-Span-139" style="border: 0px;
      box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.336em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.447em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.169em, 1001em, 4.169em, -999.997em); left: 0em; line-height: normal; margin: 0px;
      padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mn" id="MathJax-Span-140" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">10</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      1.003em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.386em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-141" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">9</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.503em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.537em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.397em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mo></mo><msub><mi></mi><mi></mi></msub><mo></mo><msub><mi></mi><mi></mi></msub><mo></mo><msup><mn></mn><mn></mn></msup></math></span></span></li><li
      class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding: 0px;"><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;&amp;lt;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;&amp;lt;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mn&gt;3&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;&amp;lt;&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;&amp;lt;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-22-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-142" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 12.503em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      10.392em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.781em,
      1010.39em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-143" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="msubsup"
      id="MathJax-Span-144" style="border: 0px; box-sizing: border-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.947em;"><span style="border:
      0px; box-sizing: border-box; clip: rect(3.392em, 1000.5em, 4.169em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-145"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">a</span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.503em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-146" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-147" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">&lt;</span><span class="msubsup" id="MathJax-Span-148" style="border:
      0px; box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px
      0px 0px 0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0.947em;"><span style="border: 0px; box-sizing:
      border-box; clip: rect(3.392em, 1000.5em, 4.169em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-149" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">a</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.503em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-150" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-151" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">&lt;</span><span class="msubsup" id="MathJax-Span-152" style="border:
      0px; box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px
      0px 0px 0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0.947em;"><span style="border: 0px; box-sizing:
      border-box; clip: rect(3.392em, 1000.5em, 4.169em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-153" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">a</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.503em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.831em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-154" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">3</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-155" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.336em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">&lt;</span><span class="mo" id="MathJax-Span-156" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">.</span><span class="mo" id="MathJax-Span-157"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.169em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">.</span><span class="mo"
      id="MathJax-Span-158" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.169em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">.</span><span class="mo" id="MathJax-Span-159" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.169em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">.</span><span class="mo" id="MathJax-Span-160"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.169em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">&lt;</span><span class="msubsup"
      id="MathJax-Span-161" style="border: 0px; box-sizing: border-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.336em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 1.114em;"><span
      style="border: 0px; box-sizing: border-box; clip: rect(3.392em, 1000.5em, 4.169em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -3.997em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-162" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">a</span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 4.003em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: border-box; left: 0.503em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -3.831em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mi" id="MathJax-Span-163" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Italic; font-size: 12.726px; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">N<span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px; width:
      0.058em;"></span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.503em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.003em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi></mi><mn></mn></msub><mo></mo><msub><mi></mi><mn></mn></msub><mo></mo><msub><mi></mi><mn></mn></msub><mo></mo><mo></mo><mo></mo><mo></mo><mo></mo><mo></mo><msub><mi></mi><mi></mi></msub></math></span></span></li><li
      class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding: 0px;">Sum
      of<span class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-23-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-164" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.947em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.781em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1000.78em, 2.669em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-165" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-166" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">N<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.058em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.503em; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>and<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;Q&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-24-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-167" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.892em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.725em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1000.73em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-168" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-169" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">Q</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>over all testcases for a particular
      test file does not exceed<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;&amp;#x2217;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;5&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-25-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-170" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 3.669em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      3.058em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.447em,
      1003.06em, 2.669em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-171" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-172" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">2</span><span
      class="mo" id="MathJax-Span-173" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.281em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">∗</span><span class="msubsup" id="MathJax-Span-174" style="border: 0px;
      box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.281em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.447em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.169em, 1001em, 4.169em, -999.997em); left: 0em; line-height: normal; margin: 0px;
      padding: 0px; position: absolute; top: -3.997em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mn" id="MathJax-Span-175" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">10</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      1.003em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.386em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-176" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.726px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">5</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 4.003em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.503em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: border-box; display:
      inline-block; height: 1.203em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mo></mo><msup><mn></mn><mn></mn></msup></math></span></span></li></ul><h3
      class="mathjax-support" id="sampleinput" style="border-top-style: solid; border-top-width:
      1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px;
      text-rendering: optimizelegibility;">Sample Input</h3><pre class="mathjax-support"
      style="box-sizing: border-box; margin-bottom: 20px; margin-top: 0px; padding: 0px;
      white-space: pre-wrap;"><code class="mathjax-support" style="background-position: 0px
      0px; border: none; box-sizing: border-box; color: #333333; font-family: consolas,
      &quot;liberation mono&quot;, courier, monospace; line-height: 1.3; padding: 0px;">1
      2
      1 3
      5
      0 0
      2 0
      0 4
      1 1
      1 2
      </code></pre><h3 class="mathjax-support" id="sampleoutput"
      style="border-top-style: solid; border-top-width: 1px; box-sizing: border-box; color: #4a4a4a;
      font-family: helvetica, sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6;
      margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering: optimizelegibility;">Sample
      Output</h3><pre class="mathjax-support" style="box-sizing: border-box; margin-bottom:
      20px; margin-top: 0px; padding: 0px; white-space: pre-wrap;"><code
      class="mathjax-support" style="background-position: 0px 0px; border: none; box-sizing:
      border-box; color: #333333; font-family: consolas, &quot;liberation mono&quot;,
      courier, monospace; line-height: 1.3; padding: 0px;">0
      1
      2
      1
      -1
      </code></pre><h3 class="mathjax-support" id="explanation"
      style="border-top-style: solid; border-top-width: 1px; box-sizing: border-box; color: #4a4a4a;
      font-family: helvetica, sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6;
      margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering:
      optimizelegibility;">Explanation</h3><p class="mathjax-support" style="box-sizing:
      border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size: 15px; font-stretch:
      normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px; text-rendering:
      optimizelegibility;">The sample input can be represented by the graph given
      below:</p><p class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a;
      font-family: helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7;
      margin: 0px 0px 20px; padding: 0px; text-rendering: optimizelegibility;"><img alt="test
      case 1" class="mathjax-support" height="300"
      src="https://codechef_shared.s3.amazonaws.com/download/HYC/External_contest_images/COLE2020/image5.png"
      style="box-sizing: border-box; display: inline-block; height: auto; max-width: 100%;
      vertical-align: middle;" width="300" /></p><p class="mathjax-support"
      style="box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      15px; font-stretch: normal; line-height: 1.7; margin: 0px 0px 20px; padding: 0px;
      text-rendering: optimizelegibility;">If Chef starts from<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-26-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-177" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 2.558em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.114em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.06em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-178" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo"
      id="MathJax-Span-179" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">(</span><span
      class="mn" id="MathJax-Span-180" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">0</span><span
      class="mo" id="MathJax-Span-181" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="mn" id="MathJax-Span-182" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.169em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">0</span><span class="mo" id="MathJax-Span-183" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">)</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><mn></mn><mo></mo><mn></mn><mo
      stretchy="false"></mo></math></span></span>, he can reach Dr Doof
      without destroying any wall.<br class="mathjax-support" style="box-sizing: border-box;"
      />If Chef starts from<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-27-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-184" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 2.558em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.114em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.06em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-185" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo"
      id="MathJax-Span-186" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">(</span><span
      class="mn" id="MathJax-Span-187" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">2</span><span
      class="mo" id="MathJax-Span-188" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="mn" id="MathJax-Span-189" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.169em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">0</span><span class="mo" id="MathJax-Span-190" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">)</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><mn></mn><mo></mo><mn></mn><mo
      stretchy="false"></mo></math></span></span>, he has to destroy
      the<span class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-28-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-191" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.503em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.225em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1001.23em, 2.669em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-192" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-193" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mi" id="MathJax-Span-194" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">s</span><span
      class="mi" id="MathJax-Span-195" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">t<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.503em; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mi></mi><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>wall.<br class="mathjax-support"
      style="box-sizing: border-box;" />If Chef starts from<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;4&lt;/mn&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-29-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-196" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 2.558em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.114em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.06em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-197" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo"
      id="MathJax-Span-198" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">(</span><span
      class="mn" id="MathJax-Span-199" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">0</span><span
      class="mo" id="MathJax-Span-200" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="mn" id="MathJax-Span-201" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.169em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">4</span><span class="mo" id="MathJax-Span-202" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">)</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><mn></mn><mo></mo><mn></mn><mo
      stretchy="false"></mo></math></span></span>, he has to destroy both
      the walls.<br class="mathjax-support" style="box-sizing: border-box;" />If Chef starts
      from<span class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-30-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-203" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 2.558em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.114em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.06em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-204" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo"
      id="MathJax-Span-205" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">(</span><span
      class="mn" id="MathJax-Span-206" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mo" id="MathJax-Span-207" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="mn" id="MathJax-Span-208" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.169em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span><span class="mo" id="MathJax-Span-209" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">)</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><mn></mn><mo></mo><mn></mn><mo
      stretchy="false"></mo></math></span></span>, he has to destroy
      the<span class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-31-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-210" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.503em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.225em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1001.23em, 2.669em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-211" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-212" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mi" id="MathJax-Span-213" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">s</span><span
      class="mi" id="MathJax-Span-214" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">t<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.503em; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mi></mi><mi></mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>wall.<br class="mathjax-support"
      style="box-sizing: border-box;" />As<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-32-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-215" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 2.558em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.114em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1002.06em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-216" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo"
      id="MathJax-Span-217" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">(</span><span
      class="mn" id="MathJax-Span-218" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mo" id="MathJax-Span-219" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="mn" id="MathJax-Span-220" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.169em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span class="mo" id="MathJax-Span-221" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">)</span></span><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo
      stretchy="false"></mo><mn></mn><mo></mo><mn></mn><mo
      stretchy="false"></mo></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>lies on the second wall, the answer
      is<span class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-33-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-222" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.503em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.225em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.669em,
      1001.11em, 2.836em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.497em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-223" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo"
      id="MathJax-Span-224" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">−</span><span
      class="mn" id="MathJax-Span-225" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.503em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo></mo><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>for the last query.</p>
      <script
      src="https://gist.github.com/Svastikkka/3d2d77e72c781da9fbec41d5402a57d5.js"></script>

Write your content here...