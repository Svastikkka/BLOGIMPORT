# 007. Clock Seconds

Published: 2020-08-20T13:34:00.000+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div class="header" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin: 0px
      0px 1em; padding: 0px; text-align: center; text-size-adjust: auto;">
      <div class="title" style="font-size: 21px; margin: 0px 0px 0.5em; padding: 0px;">
      007. Clock Seconds</div>
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
      You have a clock that tells time in the usual way: hours, minutes, and seconds. When you wake
      up in the morning, you want to figure out how many seconds you slept for. Conveniently, you
      fell asleep the night before at exactly 12:00 AM. Remember that there are 60 seconds in a
      minute and 60 minutes in an hour.</div>
      </div>
      <div class="input-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Input</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      The first line of input contains a positive integer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">h</span><span
      class="Apple-converted-space">&nbsp;</span>indicating the current number of hours
      displayed on the clock (<span class="tex-font-style-tt" style="font-family:
      &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">1</span><span
      class="Apple-converted-space">&nbsp;</span>&lt;=<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">h</span><span
      class="Apple-converted-space">&nbsp;</span>&lt;=<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">11</span>). The second line of input contains a positive
      integer<span class="Apple-converted-space">&nbsp;</span><span
      class="tex-font-style-tt" style="font-family: &quot;courier new&quot; , monospace;
      font-size: 15.399999618530273px;">m</span><span
      class="Apple-converted-space">&nbsp;</span>indicating the current number of
      minutes displayed on the clock (<span class="tex-font-style-tt" style="font-family:
      &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">0</span><span
      class="Apple-converted-space">&nbsp;</span>&lt;=<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">m</span><span
      class="Apple-converted-space">&nbsp;</span>&lt;=<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">59</span>) The third line of input contains a positive
      integer<span class="Apple-converted-space">&nbsp;</span><span
      class="tex-font-style-tt" style="font-family: &quot;courier new&quot; , monospace;
      font-size: 15.399999618530273px;">s</span><span
      class="Apple-converted-space">&nbsp;</span>indicating the current number of
      seconds displayed on the clock (<span class="tex-font-style-tt" style="font-family:
      &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">0</span><span
      class="Apple-converted-space">&nbsp;</span>&lt;=<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">s</span><span
      class="Apple-converted-space">&nbsp;</span>&lt;=<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">59</span>) The fourth line of input contains a string<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">a</span><span
      class="Apple-converted-space">&nbsp;</span>indicating whether it is currently the
      morning or the afternoon.<span
      class="Apple-converted-space">&nbsp;</span><span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">a</span><span
      class="Apple-converted-space">&nbsp;</span>will be either<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">AM</span><span
      class="Apple-converted-space">&nbsp;</span>or<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">PM</span>. You are guaranteed to have slept for less than 24
      hours. Also, note that<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">h</span><span
      class="Apple-converted-space">&nbsp;</span>will never equal 12.</div>
      </div>
      <div class="output-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px 0px 1em; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Output</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Print a single positive integer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-font-style-tt"
      style="font-family: &quot;courier new&quot; , monospace; font-size:
      15.399999618530273px;">t</span>: the number of seconds of sleep that you
      got.</div>
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
      <div class="input-output-copier" data-clipboard-target="#id009116502153680951"
      id="id0037451756361575295" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id009116502153680951" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">6
      50
      34
      AM
      </pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<br />
      <div class="input-output-copier" data-clipboard-target="#id005554203129409718"
      id="id0029967033592380565" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id005554203129409718" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">24634</pre>
      </div>
      </div>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/c5277767eba96e2bc7859cee544edc53.js"></script></div>


Write your content here...