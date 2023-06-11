# How to pass parameters in webhook?

Published: 2021-01-23T11:19:00.005+05:30

Description: <p>Hey everyone 😊, Today I want to share another interesting thing
      which I found in <b>StackOverflow</b> and that is how to pass parameters in
      webhook. Those who don't know about webhook I advise you to google about it before going
      further reading.&nbsp;</p><p>So for demonstration purpose, I am going to use
      <b>Jenkins</b> and <b>Generic Webhook plugin</b>. I created a job and
      called it <b>testing&nbsp;</b>and select <b>Generic Webhook&nbsp;
      Trigger</b>.</p><div class="separator" style="clear: both; text-align:
      center;"><a
      href="https://1.bp.blogspot.com/-_HUkcE-_uFk/YAUsnFWwIMI/AAAAAAAAASo/M3InEgDITGYqSTvcvnkBdOaWPktUvaEgACNcBGAsYHQ/s1440/Screen%2BShot%2B2021-01-18%2Bat%2B12.05.27%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="258"
      data-original-width="1440" height="71"
      src="https://1.bp.blogspot.com/-_HUkcE-_uFk/YAUsnFWwIMI/AAAAAAAAASo/M3InEgDITGYqSTvcvnkBdOaWPktUvaEgACNcBGAsYHQ/w400-h71/Screen%2BShot%2B2021-01-18%2Bat%2B12.05.27%2BPM.png"
      width="400" /></a></div><br /><p>Thereafter I add <b>Request
      Parameter</b>&nbsp; and in the request parameter I added the name of the request
      which is <b>name</b></p><p></p><div class="separator"
      style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-ydsaPYncl4I/YAUt35SuRGI/AAAAAAAAAS0/3jIExT1E518zWV-j6jppM1ohypqILWRSgCNcBGAsYHQ/s1440/Screen%2BShot%2B2021-01-18%2Bat%2B12.10.36%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="287"
      data-original-width="1440" height="80"
      src="https://1.bp.blogspot.com/-ydsaPYncl4I/YAUt35SuRGI/AAAAAAAAAS0/3jIExT1E518zWV-j6jppM1ohypqILWRSgCNcBGAsYHQ/w400-h80/Screen%2BShot%2B2021-01-18%2Bat%2B12.10.36%2BPM.png"
      width="400" /></a></div><br />Thereafter I added a token to specify that
      this job can only be triggered.<p></p><div class="separator" style="clear:
      both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-7nMVU8GQLuc/YAUu-jsux2I/AAAAAAAAATA/AEcZbiXJemImc3Veq4ui8r6flUK4tp-2gCNcBGAsYHQ/s1440/Screen%2BShot%2B2021-01-18%2Bat%2B12.16.14%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="157"
      data-original-width="1440" height="44"
      src="https://1.bp.blogspot.com/-7nMVU8GQLuc/YAUu-jsux2I/AAAAAAAAATA/AEcZbiXJemImc3Veq4ui8r6flUK4tp-2gCNcBGAsYHQ/w400-h44/Screen%2BShot%2B2021-01-18%2Bat%2B12.16.14%2BPM.png"
      width="400" /></a></div><br /><p>After this, I select
      <b>Execute Shell</b> from Build&nbsp; and write the following
      code&nbsp;</p><div class="separator" style="clear: both; text-align:
      center;"><a
      href="https://1.bp.blogspot.com/-IqCWS9q80-4/YAu71VkJAWI/AAAAAAAAATk/fSaT1ZXXKW019uhqw-F8bxeZbwYbdw77QCNcBGAsYHQ/s1207/Screen%2BShot%2B2021-01-23%2Bat%2B11.30.25%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="484"
      data-original-width="1207"
      src="https://1.bp.blogspot.com/-IqCWS9q80-4/YAu71VkJAWI/AAAAAAAAATk/fSaT1ZXXKW019uhqw-F8bxeZbwYbdw77QCNcBGAsYHQ/s320/Screen%2BShot%2B2021-01-23%2Bat%2B11.30.25%2BAM.png"
      width="320" /></a></div><br /><p><br
      /></p><p><br /></p><p>After doing this add webhook URL in
      bitbucket repository or&nbsp; GitHub repository with the parameter. The URL is look
      something like this&nbsp;</p><p>Webhook URL:- <span style="color:
      red;">https://[YOUR_JENKINS_URL]/generic-webhook-trigger/invoke?token=trigger&amp;name=Svastikkka</span></p><p>&nbsp;The
      configuration will something like this</p><div class="separator" style="clear: both;
      text-align: center;"><a
      href="https://1.bp.blogspot.com/-3jIaC7tTIXU/YAu5pgewyHI/AAAAAAAAATY/_6pIH4GyCqkf1z5v2zqFaWBSWjKvViHNQCNcBGAsYHQ/s638/Screen%2BShot%2B2021-01-23%2Bat%2B11.21.43%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="525"
      data-original-width="638"
      src="https://1.bp.blogspot.com/-3jIaC7tTIXU/YAu5pgewyHI/AAAAAAAAATY/_6pIH4GyCqkf1z5v2zqFaWBSWjKvViHNQCNcBGAsYHQ/s320/Screen%2BShot%2B2021-01-23%2Bat%2B11.21.43%2BAM.png"
      width="320" /></a></div><div class="separator" style="clear: both;
      text-align: center;"><br /></div><div class="separator" style="clear: both;
      text-align: center;"><br /></div><div class="separator" style="clear: both;
      text-align: left;">After saving my webhook configuration I trigger my webhook by pushing
      code in the repository and finally, the result will something like this.</div><div
      class="separator" style="clear: both; text-align: left;"><br /></div><div
      class="separator" style="clear: both; text-align: left;"><br /></div><div
      class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-XjlS8iCxwlY/YAu-5tQcPQI/AAAAAAAAATw/iDI1r5vWLRwDjsltBgHEqojd7-7sxBAzACNcBGAsYHQ/s1440/Screen%2BShot%2B2021-01-23%2Bat%2B11.44.15%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="642"
      data-original-width="1440" height="179"
      src="https://1.bp.blogspot.com/-XjlS8iCxwlY/YAu-5tQcPQI/AAAAAAAAATw/iDI1r5vWLRwDjsltBgHEqojd7-7sxBAzACNcBGAsYHQ/w400-h179/Screen%2BShot%2B2021-01-23%2Bat%2B11.44.15%2BAM.png"
      width="400" /></a></div><br /><div class="separator" style="clear:
      both; text-align: left;"><span style="text-align: center;"><br
      /></span></div><div class="separator" style="clear: both; text-align:
      left;"><span style="text-align: center;"><br /></span></div><div
      class="separator" style="clear: both; text-align: center;"><span style="text-align:
      center;">Hope you enjoyed my blog post.😎</span></div>

Write your content here...