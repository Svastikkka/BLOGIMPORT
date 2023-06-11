# 004. Polygons

Published: 2020-08-20T13:24:00.000+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div class="header" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin: 0px
      0px 1em; padding: 0px; text-align: center; text-size-adjust: auto;">
      <div class="title" style="font-size: 21px; margin: 0px 0px 0.5em; padding: 0px;">
      004. Polygons</div>
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
      The sum of the angles in a triangle is 180, and the sum of the angles in a square is 360. In
      fact, the sum of angles in any polygon increases by 180 with each side added to the polygon.
      In this problem, you must figure out the sum of angles of a polygon, given its number of
      sides.</div>
      </div>
      <div class="input-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Input</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      The first line of the input contains a positive integer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">T</span><span
      class="Apple-converted-space">&nbsp;</span>indicating the number of test cases in
      the problem. The next<span class="Apple-converted-space">&nbsp;</span><span
      class="tex-font-style-tt" style="font-family: &quot;courier new&quot; , monospace;
      font-size: 15.399999618530273px;">T</span><span
      class="Apple-converted-space">&nbsp;</span>lines each contain a positive
      integer<span class="Apple-converted-space">&nbsp;</span><span
      class="tex-font-style-tt" style="font-family: &quot;courier new&quot; , monospace;
      font-size: 15.399999618530273px;">n</span><span
      class="Apple-converted-space">&nbsp;</span>(<span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">1</span><span
      class="Apple-converted-space">&nbsp;</span>&lt;=<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">n</span><span
      class="Apple-converted-space">&nbsp;</span>&lt;=<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">100</span>): the number of sides of each polygon.</div>
      </div>
      <div class="output-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px 0px 1em; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Output</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Output<span class="Apple-converted-space">&nbsp;</span><span
      class="tex-font-style-tt" style="font-family: &quot;courier new&quot; , monospace;
      font-size: 15.399999618530273px;">T</span><span
      class="Apple-converted-space">&nbsp;</span>integers: the sum of the angles in
      each polygon.</div>
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
      input<br />
      <div class="input-output-copier" data-clipboard-target="#id0031853445450070916"
      id="id00563340680401764" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id0031853445450070916" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">4
      3
      4
      5
      6
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<br />
      <div class="input-output-copier" data-clipboard-target="#id007015116002261352"
      id="id002622598926448213" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id007015116002261352" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">180
      360
      540
      720</pre>
      </div>
      </div>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/f7da529df7acbb01bf4e9988922cf9ff.js"></script>
      </div>


Write your content here...