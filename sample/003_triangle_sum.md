# 003. Triangle Sum

Published: 2020-08-20T13:17:00.000+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div class="header" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin: 0px
      0px 1em; padding: 0px; text-align: center; text-size-adjust: auto;">
      <div class="title" style="font-size: 21px; margin: 0px 0px 0.5em; padding: 0px;">
      003. Triangle Sum</div>
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
      <div style="caret-color: rgb(34, 34, 34); color: #222222; font-family: &quot;Helvetica
      Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin: 0px; padding: 0px;
      text-size-adjust: auto;">
      <div style="font-size: 1em; line-height: 1.4em; margin-bottom: 1em !important; padding:
      0px;">
      Triangles are one of the simplest geometric shapes. Equilateral triangles have the special
      property of all three of their sides being equal to each other. In this problem, you will be
      given a list of side lengths of equilateral triangles. You should find the sum of the
      perimeters of the triangles, given that the triangles are all equilateral.</div>
      </div>
      <div class="input-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Input</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      The first line of the input will contain a positive integer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot;, monospace; font-size:
      15.399999618530273px;">n</span><span
      class="Apple-converted-space">&nbsp;</span>indicating the number of triangles.
      Each of the next<span class="Apple-converted-space">&nbsp;</span><span
      class="tex-font-style-tt" style="font-family: &quot;courier new&quot;, monospace;
      font-size: 15.399999618530273px;">n</span><span
      class="Apple-converted-space">&nbsp;</span>lines will contain an integer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot;, monospace; font-size:
      15.399999618530273px;">t</span>, indicating the side length of each
      triangle.</div>
      </div>
      <div class="output-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px 0px 1em; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Output</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Print one number, the calculated sum of the perimeters of the triangles.</div>
      </div>
      <div class="sample-tests" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 0.9em; margin: 0px; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-family: &quot;Helvetica Neue&quot;,
      Helvetica, Arial, sans-serif; font-size: 14.489999771118164px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Example</div>
      <div class="sample-test" style="margin: 0px; padding: 0px;">
      <div class="input" style="border: 1px solid rgb(136, 136, 136); margin: 0px; padding:
      0px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      input<div class="input-output-copier" data-clipboard-target="#id005387041306931422"
      id="id0048782448529235056" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id005387041306931422" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">3
      3
      4
      6
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<div class="input-output-copier" data-clipboard-target="#id0016805813751679233"
      id="id000015859405059847065" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id0016805813751679233" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">39
      </pre>
      </div>
      </div>
      </div>
      <div class="note" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin:
      0px; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Note</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      In the example, the first triangle has a side length of 3, so it has a perimeter of 9. The
      second triangle has a perimeter of 12, and the third triangle has a perimeter of
      18.</div>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/39643edefce27c1e97ed166030293b2e.js"></script>


Write your content here...