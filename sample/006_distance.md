# 006. Distance

Published: 2020-08-20T13:30:00.001+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div class="header" style="margin: 0px 0px 1em; padding: 0px; text-align: center;">
      <div class="title" style="font-family: &quot;Helvetica Neue&quot;, Helvetica,
      Arial, sans-serif; font-size: 21px; margin: 0px 0px 0.5em; padding: 0px;">
      006. Distance</div>
      <div class="time-limit" style="margin: 0px auto; padding: 0px;">
      <div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px 0px
      0px;">
      time limit per test</div>
      1 second</div>
      <div class="memory-limit" style="margin: 0px auto; padding: 0px;">
      <div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px 0px
      0px;">
      memory limit per test</div>
      256 megabytes</div>
      <div class="input-file" style="margin: 0px auto; padding: 0px;">
      <div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px 0px
      0px;">
      input</div>
      standard input</div>
      <div class="output-file" style="margin: 0px auto; padding: 0px;">
      <div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px 0px
      0px;">
      output</div>
      standard output</div>
      </div>
      <div style="margin: 0px; padding: 0px;">
      <div style="font-size: 1em; line-height: 1.4em; margin-bottom: 1em !important; padding:
      0px;">
      Find the distance between two 2D points. Remember that the distance formula is<span
      class="Apple-converted-space">&nbsp;</span></div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      <span class="MathJax_Preview" style="color: inherit;"></span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;d&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;msqrt&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msup&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;y&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;y&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msup&gt;&lt;/msqrt&gt;&lt;/math&gt;"
      id="MathJax-Element-1-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-1" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      14.824em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 12.324em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.491em, 1012.32em, 3.039em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-2" style="border: 0px; box-sizing: content-box; display: inline; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-3" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑑</span><span class="mo" id="MathJax-Span-4" style="border:
      0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">=</span><span class="msqrt" id="MathJax-Span-5"
      style="border: 0px; box-sizing: content-box; display: inline; line-height: normal; margin:
      0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 10.479em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.039em, 1009.53em, 4.348em, -999.997em); left:
      0.955em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-6" style="border: 0px; box-sizing: content-box; display: inline; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mo" id="MathJax-Span-7" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">(</span><span class="msubsup" id="MathJax-Span-8"
      style="border: 0px; box-sizing: content-box; display: inline; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0.955em;"><span style="border: 0px; box-sizing:
      content-box; clip: rect(3.396em, 1000.54em, 4.17em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-9" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑥</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.539em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-10" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-11" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-12" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-13" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.241em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">−</span><span class="msubsup" id="MathJax-Span-14" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.241em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.955em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.396em, 1000.54em, 4.17em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-15" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑥</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.539em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-16" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-17" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-18" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="msubsup"
      id="MathJax-Span-19" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.777em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.158em, 1000.3em, 4.348em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-20"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">)</span><span style="border:
      0px; box-sizing: content-box; display: inline-block; height: 3.991em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span><span style="border: 0px; box-sizing:
      content-box; left: 0.36em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -4.283em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-21" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-22" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.241em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">+</span><span class="mo" id="MathJax-Span-23" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.241em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">(</span><span class="msubsup" id="MathJax-Span-24"
      style="border: 0px; box-sizing: content-box; display: inline; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0.955em;"><span style="border: 0px; box-sizing:
      content-box; clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-25" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑦</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-26" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-27" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-28" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-29" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.241em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">−</span><span class="msubsup" id="MathJax-Span-30" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.241em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.955em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-31" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑦</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-32" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-33" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-34" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="msubsup"
      id="MathJax-Span-35" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.777em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.158em, 1000.3em, 4.348em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-36"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">)</span><span style="border:
      0px; box-sizing: content-box; display: inline-block; height: 3.991em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span><span style="border: 0px; box-sizing:
      content-box; left: 0.36em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -4.283em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-37" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: content-box; clip: rect(2.979em, 1009.53em, 3.396em, -999.997em); left: 0.955em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.104em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      9.527em;"><span style="border: 0px; box-sizing: content-box; font-family:
      STIXGeneral-Regular; left: 0em; line-height: normal; margin: 0px; padding: 0px; position:
      absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align: 0px;">‾<span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: content-box; font-family: STIXGeneral-Regular; left: 9.051em; line-height: normal;
      margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;">‾<span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 0.42em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 0.896em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 1.313em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 1.789em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 2.265em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 2.682em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 3.158em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 3.574em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 4.051em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 4.527em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 4.943em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 5.42em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 5.836em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 6.313em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 6.789em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 7.205em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 7.682em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 8.098em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 8.574em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: content-box; clip: rect(2.86em, 1000.96em, 4.408em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.926em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;">√</span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 2.562em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border-left-style: solid; border-width: 0px; box-sizing: content-box; display:
      inline-block; height: 1.646em; line-height: normal; margin: 0px; overflow: hidden; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: -0.425em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px !important; left: 0px; line-height: normal; margin: 0px;
      overflow: hidden !important; padding: 0px; position: static; top: 0px; transition: none 0s
      ease 0s; user-select: none; vertical-align: 0px; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><msqrt><mo
      stretchy="false">(</mo><msub><mi>x</mi><mrow
      class="MJX-TeXAtom-ORD"><mn>2</mn></mrow></msub><mo>−</mo><msub><mi>x</mi><mrow
      class="MJX-TeXAtom-ORD"><mn>1</mn></mrow></msub><msup><mo
      stretchy="false">)</mo><mn>2</mn></msup><mo>+</mo><mo
      stretchy="false">(</mo><msub><mi>y</mi><mrow
      class="MJX-TeXAtom-ORD"><mn>2</mn></mrow></msub><mo>−</mo><msub><mi>y</mi><mrow
      class="MJX-TeXAtom-ORD"><mn>1</mn></mrow></msub><msup><mo
      stretchy="false">)</mo><mn>2</mn></msup></msqrt></math></span></span></div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      <span class="tex-font-style-tt" style="font-family: &quot;courier new&quot;,
      monospace; font-size: 15.399999618530273px;">math.sqrt</span><span
      class="Apple-converted-space">&nbsp;</span>will calculate the square root of a
      number. Also, you also have to add the line<span
      class="Apple-converted-space">&nbsp;</span><span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot;, monospace; font-size:
      15.399999618530273px;">import math</span><span
      class="Apple-converted-space">&nbsp;</span>at the top of the program.</div>
      </div>
      <div class="input-specification" style="margin: 0px; padding: 0px;">
      <div class="section-title" style="font-family: &quot;Helvetica Neue&quot;,
      Helvetica, Arial, sans-serif; font-size: 16.100000381469727px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Input</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      The first two lines contain the X and Y coordinates of the first point respectively. The
      second two lines contain the X and Y coordinates of the second point respectively. Each
      coordinate will have an integer value between -1000 and 1000, inclusive.</div>
      </div>
      <div class="output-specification" style="margin: 0px 0px 1em; padding: 0px;">
      <div class="section-title" style="font-family: &quot;Helvetica Neue&quot;,
      Helvetica, Arial, sans-serif; font-size: 16.100000381469727px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Output</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      A double N representing the distance between the two points</div>
      </div>
      <div class="sample-tests" style="font-family: Consolas, &quot;Lucida Console&quot;,
      &quot;Andale Mono&quot;, &quot;Bitstream Vera Sans Mono&quot;,
      &quot;Courier New&quot;, Courier; font-size: 0.9em; margin: 0px; padding: 0px;">
      <div class="section-title" style="font-family: &quot;Helvetica Neue&quot;,
      Helvetica, Arial, sans-serif; font-size: 14.489999771118164px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Examples</div>
      <div class="sample-test" style="margin: 0px; padding: 0px;">
      <div class="input" style="border: 1px solid rgb(136, 136, 136); margin: 0px; padding:
      0px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      input<div class="input-output-copier" data-clipboard-target="#id0013881207373777238"
      id="id005225929021055822" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id0013881207373777238" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">1
      1
      2
      2
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<div class="input-output-copier" data-clipboard-target="#id003079497463202031"
      id="id00787140440118651" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id003079497463202031" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">1.4142135623730951
      </pre>
      </div>
      <div class="input" style="border: 1px solid rgb(136, 136, 136); margin: 0px; padding:
      0px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      input<div class="input-output-copier" data-clipboard-target="#id007142858162412373"
      id="id001567491601794564" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id007142858162412373" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">1
      1
      1
      1
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<div class="input-output-copier" data-clipboard-target="#id0015745315934968573"
      id="id0011117081651610217" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id0015745315934968573" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">0.0</pre>
      </div>
      </div>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/eb6bc80e5af7a4f7c32aeabe67802a59.js"></script>

Write your content here...