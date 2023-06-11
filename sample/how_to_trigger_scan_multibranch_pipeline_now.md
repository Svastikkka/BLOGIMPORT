# How to trigger "Scan Multibranch Pipeline Now"

Published: 2021-02-06T21:58:00.012+05:30

Description: <p>&nbsp;Hey everyone 😀, Sometimes developers face a common
      issue related to trigger a job using the Jenkins pipeline. As we all know to trigger
      <b>Freestyle</b> Job using pipeline&nbsp; we write code something similar
      which is mention below</p><p><span style="color: red; font-family:
      courier;">build JOB_NAME;</span></p><p><span style="font-family:
      inherit;">but what if we want to trigger a multi-branch job or
      trigger<b>&nbsp;</b></span><b>Scan Multibranch Pipeline Now.
      </b>If we try to trigger a multibranch job by using the above code&nbsp; it gives an
      error, something similar like&nbsp;</p><p><span style="caret-color: rgb(51,
      51, 51); font-size: var(--font-size-monospace); white-space: pre-wrap;"><span
      style="color: red; font-family: courier;">ERROR: Waiting for non-job items is not
      supported</span></span></p><p><span style="caret-color: rgb(51, 51,
      51); font-size: var(--font-size-monospace); white-space: pre-wrap;"><span style="color:
      red; font-family: courier;"><br
      /></span></span></p><p><span style="caret-color: rgb(51, 51,
      51); font-size: var(--font-size-monospace); white-space:
      pre-wrap;"></span></p><div class="separator" style="clear: both; text-align:
      center;"><a
      href="https://1.bp.blogspot.com/-BmOEwrr5VSg/YBrQjboSZ1I/AAAAAAAAAUE/C4c0LqFt3Y8we2QGyjWaygS2G4gFb0CqgCNcBGAsYHQ/s1440/Screen%2BShot%2B2021-02-03%2Bat%2B10.03.45%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="807"
      data-original-width="1440" height="224"
      src="https://1.bp.blogspot.com/-BmOEwrr5VSg/YBrQjboSZ1I/AAAAAAAAAUE/C4c0LqFt3Y8we2QGyjWaygS2G4gFb0CqgCNcBGAsYHQ/w400-h224/Screen%2BShot%2B2021-02-03%2Bat%2B10.03.45%2BPM.png"
      width="400" /></a></div><br /><span style="font-family:
      inherit;">As we see it doesn't work, the reason is that it is a non-wait
      </span><span style="caret-color: rgb(51, 51, 51); white-space:
      pre-wrap;">type</span><span style="caret-color: rgb(51, 51, 51); font-family:
      inherit; font-size: var(--font-size-monospace); white-space: pre-wrap;"> job item, so the
      only thing we need to do is to add a </span><span style="caret-color: rgb(51, 51,
      51); font-size: var(--font-size-monospace); white-space: pre-wrap;"><span style="color:
      red; font-family: courier;">wait=false</span></span><span
      style="caret-color: rgb(51, 51, 51); font-family: inherit; font-size:
      var(--font-size-monospace); white-space: pre-wrap;"> statement in the code.
      </span><p></p><div><span style="caret-color: rgb(51, 51, 51);
      font-family: inherit; font-size: var(--font-size-monospace); white-space: pre-wrap;"><br
      /></span></div><div><br /></div><div><br
      /></div><div><br />
      <script
      src="https://gist.github.com/Svastikkka/8fc4175fdb0aefb5cb2ad5fd2e1c6ccb.js"></script>
      </div><div><br /></div><div><div><span
      style="caret-color: rgb(51, 51, 51); white-space: pre-wrap;"><br
      class="Apple-interchange-newline" />I know it's not so big thing but sometimes people
      missed this little thing.</span></div><div style="text-align: center;">Hope
      you enjoyed my blog post.😎&nbsp;</div></div>


Write your content here...