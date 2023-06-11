# 008. N-Dimensional Distance

Published: 2020-08-20T13:39:00.000+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div class="header" style="margin: 0px 0px 1em; padding: 0px; text-align: center;">
      <div class="title" style="font-family: &quot;Helvetica Neue&quot;, Helvetica,
      Arial, sans-serif; font-size: 21px; margin: 0px 0px 0.5em; padding: 0px;">
      008. N-Dimensional Distance</div>
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
      Calculate the distance between two points of a specified dimension. The common distance
      formula still applies to higher dimensional points with a small modification. You will input
      two points and display the distance between them as you normally would with the distance
      formula.</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      The n-dimensional distance formula can be expressed as</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      <span class="MathJax_Preview" style="color: inherit;"></span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;d&lt;/mi&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mi&gt;q&lt;/mi&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;msqrt&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;q&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msup&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;q&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msup&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;q&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;msup&gt;&lt;mo
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
      25.122em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 20.896em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.491em, 1020.9em, 3.039em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-2" style="border: 0px; box-sizing: content-box; display: inline; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-3" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑑</span><span class="mo" id="MathJax-Span-4" style="border:
      0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">(</span><span class="mi" id="MathJax-Span-5" style="border:
      0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span><span class="mo" id="MathJax-Span-6" style="border:
      0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">,</span><span class="mi" id="MathJax-Span-7" style="border:
      0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.182em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">𝑞<span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.003em;"></span></span><span class="mo" id="MathJax-Span-8" style="border:
      0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">)</span><span class="mo" id="MathJax-Span-9" style="border:
      0px; box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">=</span><span class="msqrt" id="MathJax-Span-10"
      style="border: 0px; box-sizing: content-box; display: inline; line-height: normal; margin:
      0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 16.967em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.039em, 1016.01em, 4.348em, -999.997em); left:
      0.955em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-11" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mo" id="MathJax-Span-12" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">(</span><span class="msubsup" id="MathJax-Span-13"
      style="border: 0px; box-sizing: content-box; display: inline; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0.896em;"><span style="border: 0px; box-sizing:
      content-box; clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-14" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑞<span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.003em;"></span></span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-15" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-16" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-17" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-18" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.241em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">−</span><span class="msubsup" id="MathJax-Span-19" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.241em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.896em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-20" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-21" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-22" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-23" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="msubsup"
      id="MathJax-Span-24" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.777em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.158em, 1000.3em, 4.348em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-25"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">)</span><span style="border:
      0px; box-sizing: content-box; display: inline-block; height: 3.991em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span><span style="border: 0px; box-sizing:
      content-box; left: 0.36em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -4.283em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-26" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-27" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.241em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">+</span><span class="mo" id="MathJax-Span-28" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.241em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">(</span><span class="msubsup" id="MathJax-Span-29"
      style="border: 0px; box-sizing: content-box; display: inline; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      0px; line-height: normal; margin: 0px; padding: 0px; position: relative; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0.896em;"><span style="border: 0px; box-sizing:
      content-box; clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease
      0s; vertical-align: 0px;"><span class="mi" id="MathJax-Span-30" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑞<span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 1px; line-height: normal; margin: 0px; overflow: hidden; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0.003em;"></span></span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-31" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-32" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-33" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-34" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.241em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">−</span><span class="msubsup" id="MathJax-Span-35" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.241em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.896em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-36" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-37" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-38" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-39" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="msubsup"
      id="MathJax-Span-40" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.777em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.158em, 1000.3em, 4.348em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-41"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">)</span><span style="border:
      0px; box-sizing: content-box; display: inline-block; height: 3.991em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span><span style="border: 0px; box-sizing:
      content-box; left: 0.36em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -4.283em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-42" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-43" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">+</span><span
      class="mo" id="MathJax-Span-44" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">.</span><span
      class="mo" id="MathJax-Span-45" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.182em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">.</span><span class="mo" id="MathJax-Span-46" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Regular; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.182em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">.</span><span class="mo" id="MathJax-Span-47"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px 0.182em; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">+</span><span
      class="mo" id="MathJax-Span-48" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">(</span><span
      class="msubsup" id="MathJax-Span-49" style="border: 0px; box-sizing: content-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.896em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(3.396em, 1000.48em, 4.348em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -3.985em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-50" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">𝑞<span style="border: 0px;
      box-sizing: content-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-51" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-52" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-53" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑛</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-54" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.241em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">−</span><span class="msubsup" id="MathJax-Span-55" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.241em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.896em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-56" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-57" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-58" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-59" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑛</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="msubsup"
      id="MathJax-Span-60" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.777em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.158em, 1000.3em, 4.348em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-61"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">)</span><span style="border:
      0px; box-sizing: content-box; display: inline-block; height: 3.991em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span><span style="border: 0px; box-sizing:
      content-box; left: 0.36em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -4.283em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-62" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: content-box; clip: rect(2.979em, 1016.07em, 3.396em, -999.997em); left: 0.955em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.104em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      16.074em;"><span style="border: 0px; box-sizing: content-box; font-family:
      STIXGeneral-Regular; left: 0em; line-height: normal; margin: 0px; padding: 0px; position:
      absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align: 0px;">‾<span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: content-box; font-family: STIXGeneral-Regular; left: 15.539em; line-height:
      normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease
      0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing: content-box; display:
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
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 1.729em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 2.205em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 2.622em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 3.098em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 3.515em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 3.991em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 4.408em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 4.884em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 5.301em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 5.777em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 6.193em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 6.67em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 7.086em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 7.562em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 7.979em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 8.455em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 8.872em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 9.348em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 9.765em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 10.241em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 10.658em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 11.074em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 11.551em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 11.967em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 12.443em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 12.86em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 13.336em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 13.753em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 14.229em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 14.646em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span><span
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 15.122em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; clip:
      rect(2.86em, 1000.96em, 4.408em, -999.997em); left: 0em; line-height: normal; margin: 0px;
      padding: 0px; position: absolute; top: -3.926em; transition: none 0s ease 0s; vertical-align:
      0px;"><span style="border: 0px; box-sizing: content-box; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">√</span><span style="border:
      0px; box-sizing: content-box; display: inline-block; height: 3.991em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span></span></span></span><span
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo
      stretchy="false">(</mo><mi>p</mi><mo>,</mo><mi>q</mi><mo
      stretchy="false">)</mo><mo>=</mo><msqrt><mo
      stretchy="false">(</mo><msub><mi>q</mi><mrow
      class="MJX-TeXAtom-ORD"><mn>1</mn></mrow></msub><mo>−</mo><msub><mi>p</mi><mrow
      class="MJX-TeXAtom-ORD"><mn>1</mn></mrow></msub><msup><mo
      stretchy="false">)</mo><mn>2</mn></msup><mo>+</mo><mo
      stretchy="false">(</mo><msub><mi>q</mi><mrow
      class="MJX-TeXAtom-ORD"><mn>2</mn></mrow></msub><mo>−</mo><msub><mi>p</mi><mrow
      class="MJX-TeXAtom-ORD"><mn>2</mn></mrow></msub><msup><mo
      stretchy="false">)</mo><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mo
      stretchy="false">(</mo><msub><mi>q</mi><mrow
      class="MJX-TeXAtom-ORD"><mi>n</mi></mrow></msub><mo>−</mo><msub><mi>p</mi><mrow
      class="MJX-TeXAtom-ORD"><mi>n</mi></mrow></msub><msup><mo
      stretchy="false">)</mo><mn>2</mn></msup></msqrt></math></span></span></div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      or in other terms:</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      <span class="MathJax_Preview" style="color: inherit;"></span><span
      class="MathJax" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msqrt&gt;&lt;munderover&gt;&lt;mo&gt;&amp;#x2211;&lt;/mo&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/mrow&gt;&lt;/munderover&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;q&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/mrow&gt;&lt;/msub&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msup&gt;&lt;/msqrt&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mi&gt;d&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-2-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height: none;
      max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><nobr
      aria-hidden="true" style="border: 0px; line-height: normal; margin: 0px; max-height: 5000em;
      max-width: 5000em; min-height: 0px; min-width: 0px; padding: 0px; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="math" id="MathJax-Span-63" style="border: 0px;
      box-sizing: content-box; display: inline-block; line-height: normal; margin: 0px; padding:
      0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      10.539em;"><span style="border: 0px; box-sizing: content-box; display: inline-block;
      font-size: 16.8px; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 8.753em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(1.193em, 1008.75em, 3.396em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -2.557em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-64" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="msqrt" id="MathJax-Span-65" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 6.908em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.039em, 1005.84em, 4.467em, -999.997em); left: 1.074em; line-height: normal;
      margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-66" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      class="munderover" id="MathJax-Span-67" style="border: 0px; box-sizing: content-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 2.027em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(3.039em, 1000.84em, 4.408em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -3.985em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mo"
      id="MathJax-Span-68" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0.003em;">∑</span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: content-box; clip: rect(3.515em, 1000.42em, 4.17em, -999.997em); left: 0.896em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.461em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="texatom" id="MathJax-Span-69"
      style="border: 0px; box-sizing: content-box; display: inline; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="mrow" id="MathJax-Span-70" style="border: 0px; box-sizing:
      content-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-71" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑛</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; clip:
      rect(3.336em, 1001.13em, 4.17em, -999.997em); left: 0.896em; line-height: normal; margin: 0px;
      padding: 0px; position: absolute; top: -3.688em; transition: none 0s ease 0s; vertical-align:
      0px;"><span class="texatom" id="MathJax-Span-72" style="border: 0px; box-sizing:
      content-box; display: inline; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mrow"
      id="MathJax-Span-73" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-74" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; font-size:
      11.8776px; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none
      0s ease 0s; vertical-align: 0px;">𝑖</span><span class="mo" id="MathJax-Span-75"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;">=</span><span
      class="mn" id="MathJax-Span-76" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">1</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-77" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">(</span><span
      class="msubsup" id="MathJax-Span-78" style="border: 0px; box-sizing: content-box; display:
      inline; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position:
      relative; transition: none 0s ease 0s; vertical-align: 0px; width: 0.777em;"><span
      style="border: 0px; box-sizing: content-box; clip: rect(3.396em, 1000.48em, 4.348em,
      -999.997em); left: 0em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -3.985em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-79" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px;">𝑞<span style="border: 0px;
      box-sizing: content-box; display: inline-block; height: 1px; line-height: normal; margin: 0px;
      overflow: hidden; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px; width: 0.003em;"></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-80" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-81" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-82" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑖</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-83" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.241em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">−</span><span class="msubsup" id="MathJax-Span-84" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px 0px
      0px 0.241em; position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 0px; line-height:
      normal; margin: 0px; padding: 0px; position: relative; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0.777em;"><span style="border: 0px; box-sizing: content-box;
      clip: rect(3.396em, 1000.48em, 4.348em, -999.997em); left: 0em; line-height: normal; margin:
      0px; padding: 0px; position: absolute; top: -3.985em; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mi" id="MathJax-Span-85" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;">𝑝</span><span style="border: 0px; box-sizing: content-box;
      display: inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box; left:
      0.479em; line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.807em;
      transition: none 0s ease 0s; vertical-align: 0px;"><span class="texatom"
      id="MathJax-Span-86" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span class="mrow" id="MathJax-Span-87" style="border: 0px;
      box-sizing: content-box; display: inline; line-height: normal; margin: 0px; padding: 0px;
      position: static; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mi"
      id="MathJax-Span-88" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Italic; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">𝑖</span></span></span><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="msubsup"
      id="MathJax-Span-89" style="border: 0px; box-sizing: content-box; display: inline;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px;"><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 0px; line-height: normal; margin: 0px; padding: 0px; position: relative;
      transition: none 0s ease 0s; vertical-align: 0px; width: 0.777em;"><span style="border:
      0px; box-sizing: content-box; clip: rect(3.158em, 1000.3em, 4.348em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span class="mo" id="MathJax-Span-90"
      style="border: 0px; box-sizing: content-box; display: inline; font-family:
      STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: 0px;">)</span><span style="border:
      0px; box-sizing: content-box; display: inline-block; height: 3.991em; line-height: normal;
      margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px;
      width: 0px;"></span></span><span style="border: 0px; box-sizing:
      content-box; left: 0.36em; line-height: normal; margin: 0px; padding: 0px; position: absolute;
      top: -4.283em; transition: none 0s ease 0s; vertical-align: 0px;"><span class="mn"
      id="MathJax-Span-91" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; font-size: 11.8776px; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">2</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: content-box; clip: rect(2.979em, 1005.9em, 3.396em, -999.997em); left: 1.074em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -4.342em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 0px; line-height: normal; margin: 0px; padding:
      0px; position: relative; transition: none 0s ease 0s; vertical-align: 0px; width:
      5.896em;"><span style="border: 0px; box-sizing: content-box; font-family:
      STIXGeneral-Regular; left: 0em; line-height: normal; margin: 0px; padding: 0px; position:
      absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align: 0px;">‾<span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: content-box; font-family: STIXGeneral-Regular; left: 5.36em; line-height: normal;
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
      font-family: STIXGeneral-Regular; left: 2.205em; line-height: normal; margin: 0px; padding:
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
      font-family: STIXGeneral-Regular; left: 3.098em; line-height: normal; margin: 0px; padding:
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
      style="border: 0px; box-sizing: content-box; font-family: STIXGeneral-Regular; left: 4.467em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.985em; transition:
      none 0s ease 0s; vertical-align: 0px;">‾<span style="border: 0px; box-sizing:
      content-box; display: inline-block; height: 3.991em; line-height: normal; margin: 0px;
      padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span><span style="border: 0px; box-sizing: content-box;
      font-family: STIXGeneral-Regular; left: 4.943em; line-height: normal; margin: 0px; padding:
      0px; position: absolute; top: -3.985em; transition: none 0s ease 0s; vertical-align:
      0px;">‾<span style="border: 0px; box-sizing: content-box; display: inline-block; height:
      3.991em; line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s
      ease 0s; vertical-align: 0px; width: 0px;"></span></span></span><span
      style="border: 0px; box-sizing: content-box; display: inline-block; height: 3.991em;
      line-height: normal; margin: 0px; padding: 0px; position: static; transition: none 0s ease 0s;
      vertical-align: 0px; width: 0px;"></span></span><span style="border: 0px;
      box-sizing: content-box; clip: rect(2.265em, 1001.07em, 4.467em, -999.997em); left: 0em;
      line-height: normal; margin: 0px; padding: 0px; position: absolute; top: -3.628em; transition:
      none 0s ease 0s; vertical-align: 0px;"><span style="border: 0px; box-sizing:
      content-box; font-family: &quot;stixsizeonesym&quot;; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">√</span><span style="border: 0px; box-sizing: content-box; display:
      inline-block; height: 3.991em; line-height: normal; margin: 0px; padding: 0px; position:
      static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span></span><span class="mo"
      id="MathJax-Span-92" style="border: 0px; box-sizing: content-box; display: inline;
      font-family: STIXGeneral-Regular; line-height: normal; margin: 0px; padding: 0px 0px 0px
      0.301em; position: static; transition: none 0s ease 0s; vertical-align:
      0px;">=</span><span class="mi" id="MathJax-Span-93" style="border: 0px;
      box-sizing: content-box; display: inline; font-family: STIXGeneral-Italic; line-height:
      normal; margin: 0px; padding: 0px 0px 0px 0.301em; position: static; transition: none 0s ease
      0s; vertical-align: 0px;">𝑑</span></span><span style="border: 0px;
      box-sizing: content-box; display: inline-block; height: 2.562em; line-height: normal; margin:
      0px; padding: 0px; position: static; transition: none 0s ease 0s; vertical-align: 0px; width:
      0px;"></span></span></span><span style="border-left-style: solid;
      border-width: 0px; box-sizing: content-box; display: inline-block; height: 2.361em;
      line-height: normal; margin: 0px; overflow: hidden; padding: 0px; position: static;
      transition: none 0s ease 0s; vertical-align: -0.854em; width:
      0px;"></span></span></nobr><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px; box-sizing: content-box; clip: rect(1px, 1px, 1px,
      1px); display: inline; height: 1px !important; left: 0px; line-height: normal; margin: 0px;
      overflow: hidden !important; padding: 0px; position: static; top: 0px; transition: none 0s
      ease 0s; user-select: none; vertical-align: 0px; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><munderover><mo>∑</mo><mrow
      class="MJX-TeXAtom-ORD"><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow
      class="MJX-TeXAtom-ORD"><mi>n</mi></mrow></munderover><mo
      stretchy="false">(</mo><msub><mi>q</mi><mrow
      class="MJX-TeXAtom-ORD"><mi>i</mi></mrow></msub><mo>−</mo><msub><mi>p</mi><mrow
      class="MJX-TeXAtom-ORD"><mi>i</mi></mrow></msub><msup><mo
      stretchy="false">)</mo><mn>2</mn></msup></msqrt><mo>=</mo><mi>d</mi></math></span></span></div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Remember that<span class="Apple-converted-space">&nbsp;</span><span
      class="tex-font-style-tt" style="font-family: &quot;courier new&quot; , monospace;
      font-size: 15.399999618530273px;">math.sqrt</span><span
      class="Apple-converted-space">&nbsp;</span>will calculate the square root of a
      number (you also have to add the line<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">import math</span><span
      class="Apple-converted-space">&nbsp;</span>at the top of the
      program).</div>
      </div>
      <div class="input-specification" style="margin: 0px; padding: 0px;">
      <div class="section-title" style="font-family: &quot;Helvetica Neue&quot;,
      Helvetica, Arial, sans-serif; font-size: 16.100000381469727px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Input</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      The first line contains the dimension D between 2 and 500. Then, D test cases will
      follow.</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Each test case N will consist of two lines: the value of the first point, and the value of the
      second point, in the Nth dimension.</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Each of these values is an integer between -5000 and 5000, inclusive.</div>
      </div>
      <div class="output-specification" style="margin: 0px 0px 1em; padding: 0px;">
      <div class="section-title" style="font-family: &quot;Helvetica Neue&quot;,
      Helvetica, Arial, sans-serif; font-size: 16.100000381469727px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Output</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      A decimal number N representing the distance between the two points. Do not round your
      answer.</div>
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
      input<br />
      <div class="input-output-copier" data-clipboard-target="#id0046852642491962215"
      id="id006075236872706138" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id0046852642491962215" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">2
      1
      1
      1
      2
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<br />
      <div class="input-output-copier" data-clipboard-target="#id009537393302302906"
      id="id002883530429935337" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id009537393302302906" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">1.0
      </pre>
      </div>
      <div class="input" style="border: 1px solid rgb(136, 136, 136); margin: 0px; padding:
      0px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      input<br />
      <div class="input-output-copier" data-clipboard-target="#id0032721992505030495"
      id="id006410191268087307" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id0032721992505030495" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">3
      7
      4
      3
      17
      6
      2
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<br />
      <div class="input-output-copier" data-clipboard-target="#id008843442704329753"
      id="id0031849032428984214" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id008843442704329753" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">14.866068747318506
      </pre>
      </div>
      <div class="input" style="border: 1px solid rgb(136, 136, 136); margin: 0px; padding:
      0px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      input<br />
      <div class="input-output-copier" data-clipboard-target="#id008907540205477039"
      id="id0010734803335265863" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id008907540205477039" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">4
      -2367
      -2873
      -4279
      -2321
      -1302
      -1341
      -2893
      651
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<br />
      <div class="input-output-copier" data-clipboard-target="#id007346579974327488"
      id="id006651840593885286" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id007346579974327488" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">4080.5951771769764</pre>
      </div>
      </div>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/e0c94ab44d51a094af4b0b96e360b9c4.js"></script>
      </div>


Write your content here...