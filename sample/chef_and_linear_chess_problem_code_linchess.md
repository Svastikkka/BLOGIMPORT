# Chef and Linear Chess Problem Code: LINCHESS

Published: 2020-08-07T20:35:00.006+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <br />
      <h3 class="mathjax-support"
      id="readproblemstatementsinhindihttpwwwcodechefcomdownloadtranslatedaug20hindilinchesspdfbengalihttpwwwcodechefcomdownloadtranslatedaug20bengalilinchesspdfmandarinchinesehttpwwwcodechefcomdownloadtranslatedaug20mandarinlinchesspdfrussianhttpwwwcodechefcomdownloadtranslatedaug20russianlinchesspdfandvietnamesehttpwwwcodechefcomdownloadtranslatedaug20vietnameselinchesspdfaswell"
      style="border-top-style: solid; border-top-width: 1px; box-sizing: border-box; color: #4a4a4a;
      font-family: helvetica, sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6;
      margin: 15px 0px 0.5rem; padding: 10px 0px 0px; text-rendering: optimizelegibility;">
      Read problem statements in<span
      class="Apple-converted-space">&nbsp;</span><a class="mathjax-support"
      href="http://www.codechef.com/download/translated/AUG20/hindi/LINCHESS.pdf" style="box-sizing:
      border-box; color: #3b5998; line-height: inherit; transition: all 0.15s ease-in
      0s;">Hindi</a>,<span class="Apple-converted-space">&nbsp;</span><a
      class="mathjax-support"
      href="http://www.codechef.com/download/translated/AUG20/bengali/LINCHESS.pdf"
      style="box-sizing: border-box; color: #3b5998; line-height: inherit; transition: all 0.15s
      ease-in 0s;">Bengali</a>,<span
      class="Apple-converted-space">&nbsp;</span><a class="mathjax-support"
      href="http://www.codechef.com/download/translated/AUG20/mandarin/LINCHESS.pdf"
      style="box-sizing: border-box; color: #3b5998; line-height: inherit; transition: all 0.15s
      ease-in 0s;">Mandarin Chinese</a>,<span
      class="Apple-converted-space">&nbsp;</span><a class="mathjax-support"
      href="http://www.codechef.com/download/translated/AUG20/russian/LINCHESS.pdf"
      style="box-sizing: border-box; color: #3b5998; line-height: inherit; transition: all 0.15s
      ease-in 0s;">Russian</a>, and<span
      class="Apple-converted-space">&nbsp;</span><a class="mathjax-support"
      href="http://www.codechef.com/download/translated/AUG20/vietnamese/LINCHESS.pdf"
      style="box-sizing: border-box; color: #3b5998; line-height: inherit; transition: all 0.15s
      ease-in 0s;">Vietnamese</a><span
      class="Apple-converted-space">&nbsp;</span>as well.</h3>
      <div class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px
      0px 20px; padding: 0px; text-rendering: optimizelegibility;">
      Chef wants to play a game of<span
      class="Apple-converted-space">&nbsp;</span><em class="mathjax-support"
      style="box-sizing: border-box; line-height: inherit;">linear chess</em><span
      class="Apple-converted-space">&nbsp;</span>on a one-dimensional board ― an
      infinite row of squares numbered by positive integers. In this game, he has a pawn, which is
      initially at a square<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-29-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-108" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.932em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.768em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.77em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-109" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-110" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">K<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.516em; line-height: normal; margin:
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span>.
      There are also<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-30-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-111" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.932em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.768em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.77em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-112" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-113" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">N<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.516em; line-height: normal; margin:
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
      class="Apple-converted-space">&nbsp;</span>other people (numbered<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-31-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-114" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.38em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-115" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-116" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>through<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-32-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-117" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.932em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.768em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.77em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-118" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-119" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">N<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.516em; line-height: normal; margin:
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span>);
      Chef can choose one of them to play against. For each valid<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-33-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-120" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.44em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.331em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.33em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-121" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-122" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">i</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
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
      the<span class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-34-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-123" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.44em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.331em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.33em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-124" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-125" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">i</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span>-th
      player would play in the following way:</div>
      <ul class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7;
      list-style-position: outside; margin: 0px 0px 20px 25px; padding: 0px;">
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;">Take a pawn and place it on a square<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-35-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-126" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.096em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.877em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.314em,
      1000.88em, 2.462em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.128em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-127" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="msubsup"
      id="MathJax-Span-128" style="border: 0px; box-sizing: border-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.877em;"><span style="border:
      0px; box-sizing: border-box; clip: rect(3.172em, 1000.6em, 4.156em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.986em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-129"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">P</span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-130" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">i</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.134em;
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
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi></mi><mi></mi></msub></math></span></span>.</li>
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;">Repeat the following move any number of times: move the pawn from its current
      square<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-36-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-131" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.096em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.877em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.314em,
      1000.88em, 2.462em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.128em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-132" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="msubsup"
      id="MathJax-Span-133" style="border: 0px; box-sizing: border-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.877em;"><span style="border:
      0px; box-sizing: border-box; clip: rect(3.172em, 1000.6em, 4.156em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.986em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-134"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">P</span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-135" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">i</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.134em;
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
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi></mi><mi></mi></msub></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>squares forward, i.e. from a
      square<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-37-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-136" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.549em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.44em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.915em,
      1000.44em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-137" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-138" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">s</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.67em; line-height:
      normal; margin: 0px; overflow: hidden; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span>,
      this player's pawn is moved to the square<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-38-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-139" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 3.172em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.571em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1002.57em, 2.844em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-140" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-141" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">s</span><span
      class="mo" id="MathJax-Span-142" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.276em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">+</span><span class="msubsup" id="MathJax-Span-143" style="border: 0px;
      box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.276em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.877em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.172em, 1000.6em, 4.156em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.986em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-144" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">P</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-145" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">i</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.516em;
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi><mo></mo><msub><mi></mi><mi></mi></msub></math></span></span>.</li>
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;">If this player moves their pawn to the square with Chef's pawn, then Chef's pawn
      is<span class="Apple-converted-space">&nbsp;</span><em
      class="mathjax-support" style="box-sizing: border-box; line-height:
      inherit;">captured</em><span
      class="Apple-converted-space">&nbsp;</span>and he loses the game.</li>
      </ul>
      <div class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px
      0px 20px; padding: 0px; text-rendering: optimizelegibility;">
      Unfortunately, Chef cannot move his pawn during the game, making him an easy target for other
      players. Given the starting positions of all<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-39-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-146" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 3.172em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      2.571em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1002.46em, 2.735em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-147" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-148" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">N<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span><span class="mo" id="MathJax-Span-149"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.276em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">+</span><span class="mn"
      id="MathJax-Span-150" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.276em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.003em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.13em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi><mo></mo><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>players, find a player who can capture
      Chef's pawn in the smallest number of moves or determine that no player can capture his
      pawn.</div>
      <h3 class="mathjax-support" id="input" style="border-top-style: solid; border-top-width:
      1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px;
      text-rendering: optimizelegibility;">
      Input</h3>
      <ul class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7;
      list-style-position: outside; margin: 0px 0px 20px 25px; padding: 0px;">
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;">The first line of the input contains a single integer<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-40-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-151" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.822em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.66em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-152" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-153" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">T<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.516em; line-height: normal; margin:
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
      class="Apple-converted-space">&nbsp;</span>denoting the number of test cases. The
      description of<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-41-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-154" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.822em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.658em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.66em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-155" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-156" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">T<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.516em; line-height: normal; margin:
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
      class="Apple-converted-space">&nbsp;</span>test cases follows.</li>
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;">The first line of each test case contains two space-separated integers<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-42-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-157" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.932em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.768em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.77em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-158" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-159" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">N<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.516em; line-height: normal; margin:
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
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-43-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-160" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.932em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.768em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.77em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-161" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-162" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">K<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.516em; line-height: normal; margin:
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span>.</li>
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;">The second line contains<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-44-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-163" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.932em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.768em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.77em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-164" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-165" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">N<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span></span><span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 2.516em; line-height: normal; margin:
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
      class="Apple-converted-space">&nbsp;</span>space-separated integers<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;&amp;#x2026;&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-45-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-166" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 7.107em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.795em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1005.79em, 2.844em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-167" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="msubsup"
      id="MathJax-Span-168" style="border: 0px; box-sizing: border-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 1.041em;"><span style="border:
      0px; box-sizing: border-box; clip: rect(3.172em, 1000.6em, 4.156em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.986em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-169"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">P</span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-170" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-171" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="msubsup" id="MathJax-Span-172" style="border: 0px; box-sizing: border-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.167em; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.041em;"><span style="border: 0px; box-sizing: border-box; clip: rect(3.172em,
      1000.6em, 4.156em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -3.986em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mi" id="MathJax-Span-173" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">P</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-174" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-175" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="mo" id="MathJax-Span-176" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.167em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">…</span><span class="mo" id="MathJax-Span-177" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.167em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">,</span><span class="msubsup" id="MathJax-Span-178"
      style="border: 0px; box-sizing: border-box; display: inline; line-height: normal; margin: 0px;
      padding: 0px 0px 0px 0.167em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 1.205em;"><span style="border: 0px; box-sizing:
      border-box; clip: rect(3.172em, 1000.6em, 4.156em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.986em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-179" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">P</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-180" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">N<span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px; width:
      0.057em;"></span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.516em;
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
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi></mi><mn></mn></msub><mo></mo><msub><mi></mi><mn></mn></msub><mo></mo><mo></mo><mo></mo><msub><mi></mi><mi></mi></msub></math></span></span>.</li>
      </ul>
      <h3 class="mathjax-support" id="output" style="border-top-style: solid; border-top-width:
      1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px;
      text-rendering: optimizelegibility;">
      Output</h3>
      <div class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px
      0px 20px; padding: 0px; text-rendering: optimizelegibility;">
      For each test case, print a single line containing one integer ― the starting square of one
      player that can beat Chef in the smallest number of turns, or<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-46-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-181" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.478em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.205em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1001.1em, 2.844em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-182" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo"
      id="MathJax-Span-183" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">−</span><span
      class="mn" id="MathJax-Span-184" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
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
      class="Apple-converted-space">&nbsp;</span>if no player can beat him.</div>
      <div class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px
      0px 20px; padding: 0px; text-rendering: optimizelegibility;">
      If there are multiple solutions, you may find any one.</div>
      <h3 class="mathjax-support" id="constraints" style="border-top-style: solid;
      border-top-width: 1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica,
      sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem;
      padding: 10px 0px 0px; text-rendering: optimizelegibility;">
      Constraints</h3>
      <ul class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7;
      list-style-position: outside; margin: 0px 0px 20px 25px; padding: 0px;">
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;"><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;100&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-47-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-185" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 6.669em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.467em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1005.47em, 2.79em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-186" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-187" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mo" id="MathJax-Span-188" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.331em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="mi" id="MathJax-Span-189" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px 0px 0px 0.331em; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">T<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.057em;"></span></span><span class="mo" id="MathJax-Span-190"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.331em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">≤</span><span class="mn"
      id="MathJax-Span-191" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.331em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">100</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.07em; line-height:
      normal; margin: 0px; overflow: hidden; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: -0.197em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mo></mo><mi></mi><mo></mo><mn></mn></math></span></span></li>
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;"><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;000&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-48-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-192" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 7.926em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      6.505em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1006.5em, 2.844em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-193" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-194" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mo" id="MathJax-Span-195" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.331em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="mi" id="MathJax-Span-196" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px 0px 0px 0.331em; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">N<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.057em;"></span></span><span class="mo" id="MathJax-Span-197"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.331em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">≤</span><span class="mn"
      id="MathJax-Span-198" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.331em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span><span class="mo" id="MathJax-Span-199" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">,</span><span class="mn" id="MathJax-Span-200"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.167em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">000</span></span><span style="border:
      0px; box-sizing: border-box; display: inline-block; height: 2.516em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span></span><span style="border-left-style:
      solid; border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.137em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.263em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mo></mo><mi></mi><mo></mo><mn></mn><mo></mo><mn></mn></math></span></span></li>
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;"><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;9&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-49-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-201" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 6.669em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.467em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.478em,
      1005.47em, 2.79em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-202" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-203" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mo" id="MathJax-Span-204" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.331em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="mi" id="MathJax-Span-205" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px 0px 0px 0.331em; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">K<span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.057em;"></span></span><span class="mo" id="MathJax-Span-206"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.331em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;">≤</span><span class="msubsup"
      id="MathJax-Span-207" style="border: 0px; box-sizing: border-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px 0px 0px 0.331em; position: static; transition:
      none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 1.423em;"><span
      style="border: 0px; box-sizing: border-box; clip: rect(3.172em, 1000.99em, 4.156em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -3.986em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-208" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">10</span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 3.992em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: border-box; left: 0.986em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -4.369em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mn" id="MathJax-Span-209" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Regular; font-size: 12.9381px; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">9</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.516em;
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mo></mo><mi></mi><mo></mo><msup><mn></mn><mn></mn></msup></math></span></span></li>
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;"><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;9&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-50-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-210" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 6.833em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.577em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.478em,
      1005.58em, 2.844em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-211" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-212" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">1</span><span
      class="mo" id="MathJax-Span-213" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.331em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="msubsup" id="MathJax-Span-214" style="border: 0px;
      box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.331em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.877em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.172em, 1000.6em, 4.156em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.986em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-215" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">P</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-216" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">i</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-217" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.331em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">≤</span><span class="msubsup" id="MathJax-Span-218" style="border: 0px;
      box-sizing: border-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.331em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 1.423em;"><span style="border: 0px; box-sizing: border-box;
      clip: rect(3.172em, 1000.99em, 4.156em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.986em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mn" id="MathJax-Span-219" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">10</span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.986em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.369em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-220" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">9</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.516em;
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn><mo></mo><msub><mi></mi><mi></mi></msub><mo></mo><msup><mn></mn><mn></mn></msup></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>for each valid<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-51-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-221" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.44em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.331em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.33em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-222" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-223" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">i</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi></math></span></span></li>
      <li class="mathjax-support" style="box-sizing: border-box; margin: 0px; padding:
      0px;"><span class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;&amp;#x2026;&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;P&lt;/mi&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-52-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-224" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 8.473em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      6.943em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1006.94em, 2.844em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-225" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-226" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">K<span style="border: 0px;
      box-sizing: border-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.057em;"></span></span><span class="mo" id="MathJax-Span-227"
      style="border: 0px; box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">,</span><span class="msubsup" id="MathJax-Span-228"
      style="border: 0px; box-sizing: border-box; display: inline; line-height: normal; margin: 0px;
      padding: 0px 0px 0px 0.167em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 1.041em;"><span style="border: 0px; box-sizing:
      border-box; clip: rect(3.172em, 1000.6em, 4.156em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.986em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-229" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">P</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-230" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-231" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="msubsup" id="MathJax-Span-232" style="border: 0px; box-sizing: border-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.167em; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      border-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      1.041em;"><span style="border: 0px; box-sizing: border-box; clip: rect(3.172em,
      1000.6em, 4.156em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -3.986em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mi" id="MathJax-Span-233" style="border: 0px; box-sizing: border-box;
      display: inline; font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">P</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-234" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-235" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">,</span><span
      class="mo" id="MathJax-Span-236" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.167em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">…</span><span class="mo" id="MathJax-Span-237" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.167em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">,</span><span class="msubsup" id="MathJax-Span-238"
      style="border: 0px; box-sizing: border-box; display: inline; line-height: normal; margin: 0px;
      padding: 0px 0px 0px 0.167em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 1.205em;"><span style="border: 0px; box-sizing:
      border-box; clip: rect(3.172em, 1000.6em, 4.156em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.986em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-239" style="border: 0px;
      box-sizing: border-box; display: inline; font-family: STIXGeneral-Italic; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">P</span><span style="border: 0px; box-sizing: border-box; display:
      inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: border-box; left:
      0.604em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.822em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-240" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 12.9381px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">N<span style="border: 0px; box-sizing: border-box; display: inline-block; height:
      1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px; width:
      0.057em;"></span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 3.992em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: border-box; display: inline-block; height: 2.516em;
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mi></mi><mo></mo><msub><mi></mi><mn></mn></msub><mo></mo><msub><mi></mi><mn></mn></msub><mo></mo><mo></mo><mo></mo><msub><mi></mi><mi></mi></msub></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>are pairwise distinct</li>
      </ul>
      <h3 class="mathjax-support" id="subtasks" style="border-top-style: solid; border-top-width:
      1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica, sans-serif; font-size:
      18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem; padding: 10px 0px 0px;
      text-rendering: optimizelegibility;">
      Subtasks</h3>
      <div class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px
      0px 20px; padding: 0px; text-rendering: optimizelegibility;">
      <span class="mathjax-support" style="box-sizing: border-box; font-weight: 700; line-height:
      inherit;">Subtask #1 (100 points):</span><span
      class="Apple-converted-space">&nbsp;</span>original constraints</div>
      <h3 class="mathjax-support" id="exampleinput" style="border-top-style: solid;
      border-top-width: 1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica,
      sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem;
      padding: 10px 0px 0px; text-rendering: optimizelegibility;">
      Example Input</h3>
      <pre class="mathjax-support" style="box-sizing: border-box; margin-bottom: 20px;
      margin-top: 0px; padding: 0px; white-space: pre-wrap;"><code class="mathjax-support"
      style="background-position: 0px 0px; border: none; box-sizing: border-box; color: #333333;
      font-family: consolas, &quot;liberation mono&quot;, courier, monospace; line-height:
      1.3; padding: 0px;">2
      4 6
      4 3 2 8
      4 7
      4 3 2 8
      </code></pre>
      <h3 class="mathjax-support" id="exampleoutput" style="border-top-style: solid;
      border-top-width: 1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica,
      sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem;
      padding: 10px 0px 0px; text-rendering: optimizelegibility;">
      Example Output</h3>
      <pre class="mathjax-support" style="box-sizing: border-box; margin-bottom: 20px;
      margin-top: 0px; padding: 0px; white-space: pre-wrap;"><code class="mathjax-support"
      style="background-position: 0px 0px; border: none; box-sizing: border-box; color: #333333;
      font-family: consolas, &quot;liberation mono&quot;, courier, monospace; line-height:
      1.3; padding: 0px;">3
      -1
      </code></pre>
      <h3 class="mathjax-support" id="explanation" style="border-top-style: solid;
      border-top-width: 1px; box-sizing: border-box; color: #4a4a4a; font-family: helvetica,
      sans-serif; font-size: 18px; font-stretch: normal; line-height: 1.6; margin: 15px 0px 0.5rem;
      padding: 10px 0px 0px; text-rendering: optimizelegibility;">
      Explanation</h3>
      <div class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px
      0px 20px; padding: 0px; text-rendering: optimizelegibility;">
      <span class="mathjax-support" style="box-sizing: border-box; font-weight: 700; line-height:
      inherit;">Example case 1:</span><span
      class="Apple-converted-space">&nbsp;</span>The player who starts at the
      position<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-53-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-241" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.5em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-242" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-243" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>can move to square<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;4&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-54-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-244" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.5em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-245" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-246" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">4</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span>and
      then to square<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;6&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-55-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-247" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.642em,
      1000.44em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-248" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-249" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">6</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.003em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span>.
      The player who starts at the position<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;3&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-56-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-250" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.44em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-251" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-252" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">3</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.003em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>can move to square<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;6&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-57-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-253" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.642em,
      1000.44em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-254" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-255" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">6</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.003em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span>.
      The player at position<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-58-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-256" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.5em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-257" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-258" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>can capture Chef's pawn in<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-59-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-259" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.5em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-260" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-261" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>turns, whereas the player at
      position<span class="Apple-converted-space">&nbsp;</span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;3&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-60-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-262" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.44em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-263" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-264" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">3</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.003em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>can capture Chef's pawn in<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-61-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-265" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.38em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-266" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-267" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 0.937em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>turn. Therefore, the answer is<span
      class="Apple-converted-space">&nbsp;</span><span class="MathJax"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;3&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-62-Frame" role="presentation" style="border: 0px; box-sizing: border-box;
      direction: ltr; display: inline; float: none; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; box-sizing: border-box; line-height: normal; margin:
      0px; max-height: 5000em; max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="math"
      id="MathJax-Span-268" style="border: 0px; box-sizing: border-box; display: inline-block;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.604em;"><span style="border: 0px; box-sizing: border-box;
      display: inline-block; font-size: 18.3px; height: 0px; line-height: normal; margin: 0px;
      padding: 0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.495em;"><span style="border: 0px; box-sizing: border-box; clip: rect(1.697em,
      1000.44em, 2.68em, -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px;
      position: absolute; top: -2.511em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-269" style="border: 0px; box-sizing:
      border-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-270" style="border: 0px; box-sizing: border-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align:
      0px;">3</span></span><span style="border: 0px; box-sizing: border-box;
      display: inline-block; height: 2.516em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: border-box; display: inline-block; height: 1.003em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.063em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: border-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px; left: 0px; line-height: normal; margin: 0px; overflow:
      hidden; padding: 0px; position: static; top: 0px; transition: none 0s ease 0s; user-select:
      none; vertical-align: 0px; width: 1px;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn></mn></math></span></span>.</div>
      <div class="mathjax-support" style="box-sizing: border-box; color: #4a4a4a; font-family:
      helvetica, sans-serif; font-size: 15px; font-stretch: normal; line-height: 1.7; margin: 0px
      0px 20px; padding: 0px; text-rendering: optimizelegibility;">
      <span class="mathjax-support" style="box-sizing: border-box; font-weight: 700; line-height:
      inherit;">Example case 2:</span><span
      class="Apple-converted-space">&nbsp;</span>No player can capture Chef's
      pawn.</div>
      <pre style="background-color: white; font-family: menlo; font-size: 9pt;"></pre>
      <pre style="background-color: white; font-family: menlo; font-size: 9pt;"></pre>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/32e802541a0218c2a23b54ff9a4d9689.js"></script>


Write your content here...