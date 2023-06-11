# 013. Resistors in Parallel

Published: 2020-08-20T13:58:00.001+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div class="header" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin: 0px
      0px 1em; padding: 0px; text-align: center; text-size-adjust: auto;">
      <div class="title" style="font-size: 21px; margin: 0px 0px 0.5em; padding: 0px;">
      013. Resistors in Parallel</div>
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
      When two resistors with resistances<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">a</span><span
      class="Apple-converted-space">&nbsp;</span>and<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">b</span><span
      class="Apple-converted-space">&nbsp;</span>are parallel in an electronic circuit,
      their equivalent resistance is calculated as (<span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">a</span><span
      class="Apple-converted-space">&nbsp;</span>*<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">b</span>) / (<span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">a</span><span
      class="Apple-converted-space">&nbsp;</span>+<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">b</span>). Given the resistances of two resistors, calculate
      their equivalent resistance.</div>
      </div>
      <div class="input-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Input</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      The first line of input contains a single positive integer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">a</span>: the resistance of the first resistor. The second
      line of input contains a single positive integer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">b</span>: the resistance of the second resistor.</div>
      </div>
      <div class="output-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px 0px 1em; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Output</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Output a single positive decimal number<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">r</span>: the equivalent resistance of the two resistors,
      calculated using the above formula.</div>
      </div>
      <div class="sample-tests" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 0.9em; margin: 0px; padding: 0px; text-size-adjust: auto;">
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
      <div class="input-output-copier" data-clipboard-target="#id007545134357832604"
      id="id0033611404197826344" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id007545134357832604" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">60
      40
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<br />
      <div class="input-output-copier" data-clipboard-target="#id0002114365007615082"
      id="id009586896892641664" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id0002114365007615082" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">24.0
      </pre>
      </div>
      <div class="input" style="border: 1px solid rgb(136, 136, 136); margin: 0px; padding:
      0px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      input<br />
      <div class="input-output-copier" data-clipboard-target="#id006463175102999038"
      id="id006909014013290855" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id006463175102999038" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">80
      70
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<br />
      <div class="input-output-copier" data-clipboard-target="#id005221023299632138"
      id="id007923929527151434" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id005221023299632138" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">37.333333333333336</pre>
      </div>
      </div>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/28700696c38ea2ffb164da57b5bc8bf6.js"></script>


Write your content here...