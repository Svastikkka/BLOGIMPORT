# C. Pig Latin

Published: 2020-07-02T13:18:00.001+05:30

Description: 
      <div class="header" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px 0px 1em; padding: 0px; text-align: center; text-size-adjust:
      auto;"><div class="title" style="font-size: 21px; margin: 0px 0px 0.5em; padding:
      0px;">C. Pig Latin</div><div class="time-limit" style="margin: 0px auto; padding:
      0px;"><div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px
      0px 0px;">time limit per test</div>1 second</div><div class="memory-limit"
      style="margin: 0px auto; padding: 0px;"><div class="property-title" style="display:
      inline; margin: 0px; padding: 0px 4px 0px 0px;">memory limit per test</div>256
      megabytes</div><div class="input-file" style="margin: 0px auto; padding:
      0px;"><div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px
      0px 0px;">input</div>standard input</div><div class="output-file"
      style="margin: 0px auto; padding: 0px;"><div class="property-title" style="display:
      inline; margin: 0px; padding: 0px 4px 0px 0px;">output</div>standard
      output</div></div><div style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px; padding: 0px; text-size-adjust: auto;"><p style="font-size: 1em;
      line-height: 1.4em; margin: 0px 0px 1em !important; padding: 0px;"><a
      href="https://en.wikipedia.org/wiki/Pig_Latin" style="color: #4d87c7; text-decoration-line:
      none;">https://en.wikipedia.org/wiki/Pig_Latin</a></p><p style="font-size:
      1em; line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;">Pig Latin is a secret
      language which is similar to English. To convert an English word to Pig Latin, take the first
      letter of that word, move it to the end, and then add "ay".</p><p style="font-size:
      1em; line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;">Peccy and Danbo are two
      Amazon mascots. They like sending each other messages over Amazon Chime, but they've realised
      that their messages are unencrypted! Help Peccy and Danbo encrypt their messages by converting
      them into Pig Latin.<span
      class="Apple-converted-space">&nbsp;</span></p><p style="font-size: 1em;
      line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;">Make sure to check the
      examples.</p><center><img alt="C. Pig Lantin" class="tex-graphics"
      src="https://espresso.codeforces.com/b6b777a587282111079103e0226e8f8343f4d6b8.png"
      style="border: 0px; display: block; margin: 0px; max-height: 100%; max-width: 100%;" title="C.
      Pig Lantin" /></center></div><div class="input-specification"
      style="caret-color: rgb(34, 34, 34); color: #222222; font-family: &quot;Helvetica
      Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin: 0px; padding: 0px;
      text-size-adjust: auto;"><div class="section-title" style="font-size: 16.1px;
      font-weight: bold; margin: 0px; padding: 0px;">Input</div><p style="font-size:
      1em; line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;">The first line will contain
      an integer<span class="Apple-converted-space">&nbsp;</span><span
      class="tex-span" style="font-family: &quot;times new roman&quot;, sans-serif;
      font-size: 17.5px; white-space: nowrap;"><i>T</i></span>, where<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-span"
      style="font-family: &quot;times new roman&quot;, sans-serif; font-size: 17.5px;
      white-space: nowrap;"><i>T</i></span><span
      class="Apple-converted-space">&nbsp;</span>is the number of sentences
      given.<span class="Apple-converted-space">&nbsp;</span></p><p
      style="font-size: 1em; line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;">Each
      sentence will be on a new line and will not contain punctuation. However, they will be
      capitalised at the beginning (but not anywhere else). Make sure you check the examples
      given.<span
      class="Apple-converted-space">&nbsp;</span></p></div><div
      class="output-specification" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin: 0px
      0px 1em; padding: 0px; text-size-adjust: auto;"><div class="section-title"
      style="font-size: 16.1px; font-weight: bold; margin: 0px; padding:
      0px;">Output</div><p style="font-size: 1em; line-height: 1.4em; margin: 1.5em 0px
      0px; padding: 0px;">A list of sentences in Pig Latin. Each sentence should be on a new line
      and should not contain punctuation, but it should start with a capital letter.<span
      class="Apple-converted-space">&nbsp;</span></p></div><div
      class="sample-tests" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 0.9em; margin: 0px; padding: 0px; text-size-adjust: auto;"><div
      class="section-title" style="font-family: &quot;Helvetica Neue&quot;, Helvetica,
      Arial, sans-serif; font-size: 14.489999771118164px; font-weight: bold; margin: 0px; padding:
      0px;">Examples</div><div class="sample-test" style="margin: 0px; padding:
      0px;"><div class="input" style="border: 1px solid rgb(136, 136, 136); margin: 0px;
      padding: 0px;"><div class="title" style="border-bottom-color: rgb(136, 136, 136);
      border-bottom-style: solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold;
      margin: 0px; padding: 0.25em; text-transform: lowercase;">input<div
      class="input-output-copier" data-clipboard-target="#id009324492888017143"
      id="id0005075874079501608" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;"
      title="Copy">Copy</div></div><pre id="id009324492888017143"
      style="background-color: #efefef; color: #880000; font-family: Consolas, &quot;Lucida
      Console&quot;, &quot;Andale Mono&quot;, &quot;Bitstream Vera Sans
      Mono&quot;, &quot;Courier New&quot;, Courier; font-size: 12.6px; line-height:
      1.25em; margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">1<br />Hello world<br /></pre></div><div
      class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em; padding: 0px;
      position: relative; top: -1px;"><div class="title" style="border-bottom-color: rgb(136,
      136, 136); border-bottom-style: solid; border-bottom-width: 1px; font-size: 1.3em;
      font-weight: bold; margin: 0px; padding: 0.25em; text-transform: lowercase;">output<div
      class="input-output-copier" data-clipboard-target="#id008234679533821785"
      id="id0008022832545212277" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;"
      title="Copy">Copy</div></div><pre id="id008234679533821785"
      style="background-color: #efefef; color: #880000; font-family: Consolas, &quot;Lucida
      Console&quot;, &quot;Andale Mono&quot;, &quot;Bitstream Vera Sans
      Mono&quot;, &quot;Courier New&quot;, Courier; font-size: 12.6px; line-height:
      1.25em; margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">Ellohay orldway <br /></pre></div><div
      class="input" style="border: 1px solid rgb(136, 136, 136); margin: 0px; padding:
      0px;"><div class="title" style="border-bottom-color: rgb(136, 136, 136);
      border-bottom-style: solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold;
      margin: 0px; padding: 0.25em; text-transform: lowercase;">input<div
      class="input-output-copier" data-clipboard-target="#id006253281629348914"
      id="id003210644670796604" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;"
      title="Copy">Copy</div></div><pre id="id006253281629348914"
      style="background-color: #efefef; color: #880000; font-family: Consolas, &quot;Lucida
      Console&quot;, &quot;Andale Mono&quot;, &quot;Bitstream Vera Sans
      Mono&quot;, &quot;Courier New&quot;, Courier; font-size: 12.6px; line-height:
      1.25em; margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">8<br />Hello danbo<br />Hello peccy<br />How are
      you today<br />Good how are you<br />Oh no<br />Whats wrong<br />It
      seems like our messages are not being encrypted<br />Dont panic<br
      /></pre></div><div class="output" style="border: 1px solid rgb(136, 136,
      136); margin: 0px 0px 1em; padding: 0px; position: relative; top: -1px;"><div
      class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style: solid;
      border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding: 0.25em;
      text-transform: lowercase;">output<div class="input-output-copier"
      data-clipboard-target="#id009546655459654714" id="id006286407089551603" style="border: 1px
      solid rgb(185, 185, 185); color: rgb(136, 136, 136) !important; cursor: pointer; float: right;
      font-size: 1.2rem; line-height: 1.1rem; margin: 1px; padding: 3px; text-transform: none;"
      title="Copy">Copy</div></div><pre id="id009546655459654714"
      style="background-color: #efefef; color: #880000; font-family: Consolas, &quot;Lucida
      Console&quot;, &quot;Andale Mono&quot;, &quot;Bitstream Vera Sans
      Mono&quot;, &quot;Courier New&quot;, Courier; font-size: 12.6px; line-height:
      1.25em; margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">Ellohay anboday <br />Ellohay eccypay <br />Owhay reaay
      ouyay odaytay <br />Oodgay owhay reaay ouyay <br />Hoay onay <br />Hatsway
      rongway <br />Tiay eemssay ikelay uroay essagesmay reaay otnay eingbay ncryptedeay
      <br />Ontday anicpay <br /></pre></div></div></div><div
      class="note" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin:
      0px; padding: 0px; text-size-adjust: auto;"><div class="section-title" style="font-size:
      16.1px; font-weight: bold; margin: 0px; padding: 0px;">Note</div><p
      style="font-size: 1em; line-height: 1.4em; margin: 1.5em 0px 0px; padding: 0px;"><span
      class="tex-font-style-underline" style="text-decoration-line:
      underline;">Constraints</span>:</p><p style="font-size: 1em; line-height:
      1.4em; margin: 1.5em 0px 0px; padding: 0px;"><span class="tex-span" style="font-family:
      &quot;times new roman&quot;, sans-serif; font-size: 17.5px; white-space: nowrap;">1
      ≤ <i>T</i> ≤ 20</span></p><p style="font-size: 1em; line-height:
      1.4em; margin: 1.5em 0px 0px; padding: 0px;">Each sentence will not contain punctuation and
      will be all lowercase English characters, except for the very first letter of the very first
      word, which will be an uppercase English character.</p></div>


      <script
      src="https://gist.github.com/Svastikkka/e1c5dbc4a85d6021af3620c7967263f2.js"></script>

Write your content here...