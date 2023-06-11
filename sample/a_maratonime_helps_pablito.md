# A. MaratonIME helps Pablito

Published: 2020-06-24T16:28:00.002+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div class="header" style="caret-color: rgb(34, 34, 34); color: #222222; font-family:
      &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; margin: 0px
      0px 1em; padding: 0px; text-align: center; text-size-adjust: auto;">
      <div class="title" style="font-size: 21px; margin: 0px 0px 0.5em; padding: 0px;">
      A. MaratonIME helps Pablito</div>
      <div class="time-limit" style="margin: 0px auto; padding: 0px;">
      <div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px 0px
      0px;">
      time limit per test</div>
      6 seconds</div>
      <div class="memory-limit" style="margin: 0px auto; padding: 0px;">
      <div class="property-title" style="display: inline; margin: 0px; padding: 0px 4px 0px
      0px;">
      memory limit per test</div>
      64 megabytes</div>
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
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      As is well known by any cultured person, rats are the smartest beings on earth. Followed
      directly by dolphins.</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      MaratonIME knows about the species hierarchy and uses this knowledge in it's regard. Usually,
      when they need some resource, they know it's always useful to have a smart rat available.
      Unfortunately, rats are not very fond of us, primates, and will only help us if they owe us
      some favour.</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      With that in mind, MaratonIME decided to help a little rat called Pablito. Pablito is studying
      rat's genealogy, to help with cloning and genetic mapping. luckily, the way rats identify
      themselves make the job much easier.</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      The rat society is, historically, matriarchal. At first, there were little families, each of
      which had it's own leading matriarch. At that time, it was decided that rats would organize
      themselves according to the following rules:</div>
      <ul style="font-size: 1em; line-height: 1.5em; list-style-image: initial;
      list-style-position: outside; margin: 0.5em 0px 0px 1em; padding: 0px;">
      <li style="font-size: 1em; line-height: 1.5em; margin: 0px 0px 0px 0.8em; padding:
      0px;">Each martiarch had an id number greater than one.<span
      class="Apple-converted-space">&nbsp;</span></li>
      <li style="font-size: 1em; line-height: 1.5em; margin: 0px 0px 0px 0.8em; padding:
      0px;">Each of these ids were chosen in a way such that they would have the least amount of
      divisors possible.<span class="Apple-converted-space">&nbsp;</span></li>
      <li style="font-size: 1em; line-height: 1.5em; margin: 0px 0px 0px 0.8em; padding:
      0px;">Each family member had the same id as the matriarch.<span
      class="Apple-converted-space">&nbsp;</span></li>
      <li style="font-size: 1em; line-height: 1.5em; margin: 0px 0px 0px 0.8em; padding:
      0px;">The id of any newborn rat would be the product of its parents id's.<span
      class="Apple-converted-space">&nbsp;</span></li>
      </ul>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      For instance, the offspring of a rat with id 6 and another with id 7 is 42.</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Pablito needs to know if two given rats have a common ancestor, but his only tool is the id
      number of each of the two rats, which is always a positive integer greater than 1 with no more
      than 16 digits. Can you help him?</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Create a program that decides if a pair of rats have some common ancestor.</div>
      </div>
      <div class="input-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Input</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      The input begins with a positive integer<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-span"
      style="font-family: &quot;times new roman&quot; , sans-serif; font-size: 17.5px;
      white-space: nowrap;"><i>t</i> ≤ 10<span class="upper-index"
      style="font-size: 13.125px; line-height: 0; position: relative; top: -0.5em; vertical-align:
      baseline;">5</span></span>, the number of test cases.</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      After that, follows<span class="Apple-converted-space">&nbsp;</span><span
      class="tex-span" style="font-family: &quot;times new roman&quot; , sans-serif;
      font-size: 17.5px; white-space: nowrap;"><i>t</i></span><span
      class="Apple-converted-space">&nbsp;</span>lines, each with two integers<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-span"
      style="font-family: &quot;times new roman&quot; , sans-serif; font-size: 17.5px;
      white-space: nowrap;"><i>a</i><span class="lower-index" style="bottom:
      -0.25em; font-size: 13.125px; line-height: 0; position: relative; vertical-align:
      baseline;"><i>i</i></span></span><span
      class="Apple-converted-space">&nbsp;</span>e<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-span"
      style="font-family: &quot;times new roman&quot; , sans-serif; font-size: 17.5px;
      white-space: nowrap;"><i>b</i><span class="lower-index" style="bottom:
      -0.25em; font-size: 13.125px; line-height: 0; position: relative; vertical-align:
      baseline;"><i>i</i></span></span><span
      class="Apple-converted-space">&nbsp;</span>identifying two rats.</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      Every rat's id is a positive integer greater than<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-span"
      style="font-family: &quot;times new roman&quot; , sans-serif; font-size: 17.5px;
      white-space: nowrap;">1</span><span
      class="Apple-converted-space">&nbsp;</span>and with no more than<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-span"
      style="font-family: &quot;times new roman&quot; , sans-serif; font-size: 17.5px;
      white-space: nowrap;">16</span><span
      class="Apple-converted-space">&nbsp;</span>digits.</div>
      </div>
      <div class="output-specification" style="caret-color: rgb(34, 34, 34); color: #222222;
      font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size:
      14px; margin: 0px 0px 1em; padding: 0px; text-size-adjust: auto;">
      <div class="section-title" style="font-size: 16.1px; font-weight: bold; margin: 0px;
      padding: 0px;">
      Output</div>
      <div style="font-size: 1em; line-height: 1.4em; margin-top: 1.5em; padding: 0px;">
      For each test case, print "Sim" if the rats<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-span"
      style="font-family: &quot;times new roman&quot; , sans-serif; font-size: 17.5px;
      white-space: nowrap;"><i>a</i><span class="lower-index" style="bottom:
      -0.25em; font-size: 13.125px; line-height: 0; position: relative; vertical-align:
      baseline;"><i>i</i></span></span><span
      class="Apple-converted-space">&nbsp;</span>and<span
      class="Apple-converted-space">&nbsp;</span><span class="tex-span"
      style="font-family: &quot;times new roman&quot; , sans-serif; font-size: 17.5px;
      white-space: nowrap;"><i>b</i><span class="lower-index" style="bottom:
      -0.25em; font-size: 13.125px; line-height: 0; position: relative; vertical-align:
      baseline;"><i>i</i></span></span><span
      class="Apple-converted-space">&nbsp;</span>share a common ancestor and "Nao"
      otherwise.</div>
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
      <div class="input-output-copier" data-clipboard-target="#id0023714024541347922"
      id="id003444981388564098" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id0023714024541347922" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">2
      2 4
      3 5</pre>
      </div>
      <div class="output" style="border: 1px solid rgb(136, 136, 136); margin: 0px 0px 1em;
      padding: 0px; position: relative; top: -1px;">
      <div class="title" style="border-bottom-color: rgb(136, 136, 136); border-bottom-style:
      solid; border-bottom-width: 1px; font-size: 1.3em; font-weight: bold; margin: 0px; padding:
      0.25em; text-transform: lowercase;">
      output<br />
      <div class="input-output-copier" data-clipboard-target="#id004712401182219572"
      id="id00023808341694811164" style="border: 1px solid rgb(185, 185, 185); color: rgb(136, 136,
      136) !important; cursor: pointer; float: right; font-size: 1.2rem; line-height: 1.1rem;
      margin: 1px; padding: 3px; text-transform: none;" title="Copy">
      Copy</div>
      </div>
      <pre id="id004712401182219572" style="background-color: #efefef; color: #880000;
      font-family: Consolas, &quot;Lucida Console&quot;, &quot;Andale Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Courier New&quot;, Courier;
      font-size: 12.6px; line-height: 1.25em; overflow-wrap: break-word; padding: 0.25em;
      white-space: pre-wrap;">Sim
      Nao</pre>
      </div>
      </div>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/2cc5e1ad45294b625ea0e9c792feca44.js"></script></div>


Write your content here...