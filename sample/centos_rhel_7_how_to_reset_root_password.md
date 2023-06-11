# CentOS / RHEL 7 : How to Reset root password

Published: 2020-09-02T11:13:00.117+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      Hey, everyone😀, I am Svastikkka when we are a beginner in Linux or we just started to use
      Linux operating system we always thought what if we forget the password of our Linux account
      it may be a root account or any other user-defined account so in here I am going to show that
      "<b>how to reset the root password of Linux operating system account</b>". Also,
      it is important for the system administrator to know how to reset the root password.<br
      />
      We consider RedHat operating system (RHEL7) to demonstrate how to reset the root
      password.<br />
      <h3 style="text-align: left;">
      Reset Root Password</h3>
      <div>
      Step 1 Restart your system&nbsp;</div>
      Step 2 Press e on your keyboard when you see this screen:<br />
      <div>
      <br />
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-R1HaNkZflUw/X1CGRZyek0I/AAAAAAAAAM4/LlgeYO6gIrIdFXlh_j0YTN08iHQjQw8AgCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.29.00%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="313"
      src="https://1.bp.blogspot.com/-R1HaNkZflUw/X1CGRZyek0I/AAAAAAAAAM4/LlgeYO6gIrIdFXlh_j0YTN08iHQjQw8AgCNcBGAsYHQ/w500-h313/Screen%2BShot%2B2020-09-03%2Bat%2B11.29.00%2BAM.png"
      width="500" /></a></div>
      <div>
      <br />
      <div>
      Step 3 If you've done this correctly, you should see a screen similar to this one:</div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-QIhGeye_seI/X1CGxmFNLFI/AAAAAAAAANA/_C2DDZm0Li86G6bzmsmSh40SeYdMYkWyACNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.31.24%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-QIhGeye_seI/X1CGxmFNLFI/AAAAAAAAANA/_C2DDZm0Li86G6bzmsmSh40SeYdMYkWyACNcBGAsYHQ/w513-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.31.24%2BAM.png"
      width="513" /></a></div>
      <br />
      <div>
      <br /></div>
      <div>
      Step 4 Scroll down and find&nbsp; "linux16" word and use your arrow keys to move to the
      "linux16" line:</div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-q8nUa9cRnMo/X1CHo9w1-QI/AAAAAAAAANM/x0JnsfQ6gGYWzGrIOSJuYXcGr7EHJm3ggCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.34.27%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-q8nUa9cRnMo/X1CHo9w1-QI/AAAAAAAAANM/x0JnsfQ6gGYWzGrIOSJuYXcGr7EHJm3ggCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.34.27%2BAM.png"
      width="512" /></a></div>
      <br />
      <div>
      <br /></div>
      <div>
      Step 5 In the last "linux16" line append&nbsp;<span style="color: red; font-family:
      &quot;courier&quot;;">rd.break enforcing=0</span></div>
      <div>
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-ms_8d1rGu9I/X1CIKnM3u0I/AAAAAAAAANU/DThxFX759yQO3hIBYSOKvqcKqeTDwix1wCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.37.06%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-ms_8d1rGu9I/X1CIKnM3u0I/AAAAAAAAANU/DThxFX759yQO3hIBYSOKvqcKqeTDwix1wCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.37.06%2BAM.png"
      width="512" /></a></div>
      <br />
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div>
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      Step 6 Press Ctrl-x to start and the system will go in emergency mode.</div>
      <div>
      <br /></div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-DXwkTszvqcw/X1CI8XM6K6I/AAAAAAAAANg/mxnJluS4fO42ItIQMA9tFasgKjM9Y18lgCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.40.23%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-DXwkTszvqcw/X1CI8XM6K6I/AAAAAAAAANg/mxnJluS4fO42ItIQMA9tFasgKjM9Y18lgCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.40.23%2BAM.png"
      width="512" /></a></div>
      <br />
      <div>
      <br /></div>
      <div>
      <br />
      <div>
      <div>
      Step 7 In the emergency mode remount the hard drive with read-write
      access:&nbsp;&nbsp;<span style="color: red; font-family:
      &quot;courier&quot;;">#mount –o remount,rw /sysroot</span></div>
      <div>
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-7GOS4d7ka4g/X1CJbSpLjhI/AAAAAAAAANo/5fflOEg4AEYY0uRnPvj-V4wGWPk4UFtfQCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.42.25%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-7GOS4d7ka4g/X1CJbSpLjhI/AAAAAAAAANo/5fflOEg4AEYY0uRnPvj-V4wGWPk4UFtfQCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.42.25%2BAM.png"
      width="512" /></a></div>
      <br />
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div>
      <div style="text-align: left;">
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      Step 8 Run chroot to access the system:&nbsp;<span style="color: red; font-family:
      &quot;courier&quot;;">#chroot /sysroot</span></div>
      <div>
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-F5GOxt_bP-s/X1CJxddihbI/AAAAAAAAAN0/f9NHXZ2vLEYgreIMbHB6GG1q__ByHf4aQCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.44.11%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-F5GOxt_bP-s/X1CJxddihbI/AAAAAAAAAN0/f9NHXZ2vLEYgreIMbHB6GG1q__ByHf4aQCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.44.11%2BAM.png"
      width="512" /></a></div>
      <br />
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div style="text-align: left;">
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      Step 9 You can now change the root password:&nbsp;<span style="color: red; font-family:
      &quot;courier&quot;;">#passwd root</span></div>
      <div>
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-f4u_e9qnvik/X1CKUUwrrwI/AAAAAAAAAN8/lP2mbfD7mHENn_B2GLBwrZUFHChlzkCVQCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.46.32%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-f4u_e9qnvik/X1CKUUwrrwI/AAAAAAAAAN8/lP2mbfD7mHENn_B2GLBwrZUFHChlzkCVQCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.46.32%2BAM.png"
      width="512" /></a></div>
      <div>
      <br /></div>
      <br />
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-NJx9KiyE5SY/X1CKkdrgl3I/AAAAAAAAAOE/OeNuMzJ1KxwvETMeQuhdWgnkQ7MSujQ_gCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.47.38%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-NJx9KiyE5SY/X1CKkdrgl3I/AAAAAAAAAOE/OeNuMzJ1KxwvETMeQuhdWgnkQ7MSujQ_gCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.47.38%2BAM.png"
      width="512" /></a></div>
      <div>
      <br /></div>
      After successful submission, you see authentication is successfully
      updated&nbsp;</div>
      <div>
      <br /></div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-J6RTo5ZvCnk/X1CLafEqs-I/AAAAAAAAAOQ/aU2OG3S4bPMfu1IAf0LGOAtquyWZr6fvQCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.51.16%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-J6RTo5ZvCnk/X1CLafEqs-I/AAAAAAAAAOQ/aU2OG3S4bPMfu1IAf0LGOAtquyWZr6fvQCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.51.16%2BAM.png"
      width="512" /></a></div>
      <br />
      <div>
      <br />
      <div style="color: red; font-family: courier; text-align: left;">
      <br /></div>
      <div>
      <div>
      Step 10 Type <span style="color: red; font-family:
      &quot;courier&quot;;">exit</span> twice to reboot the
      system.&nbsp;<span style="color: red; font-family:
      &quot;courier&quot;;">#exit</span></div>
      <div>
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-aSteGVUWYRA/X1CLoTW1Y2I/AAAAAAAAAOU/lnor_lz4qpI11iDATOyE7pNJQ9SLaqdLACNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.52.11%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-aSteGVUWYRA/X1CLoTW1Y2I/AAAAAAAAAOU/lnor_lz4qpI11iDATOyE7pNJQ9SLaqdLACNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.52.11%2BAM.png"
      width="512" /></a></div>
      <br />
      <span style="color: red; font-family: &quot;courier&quot;;"><br
      /></span></div>
      <div>
      <span style="font-family: inherit;">Step 11 After successful log out&nbsp; now you
      have to enter your new password&nbsp; for&nbsp; the root
      user&nbsp;</span></div>
      <div>
      <span style="font-family: inherit;"><br /></span></div>
      <div>
      <div class="separator" style="clear: both; text-align: center;">
      <a
      href="https://1.bp.blogspot.com/-yjc6b26XMl0/X1CM_qWZX4I/AAAAAAAAAOg/D84r0zmsywMb3ZTdvS_xdHAd8xvyY7NIgCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B11.55.12%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-yjc6b26XMl0/X1CM_qWZX4I/AAAAAAAAAOg/D84r0zmsywMb3ZTdvS_xdHAd8xvyY7NIgCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B11.55.12%2BAM.png"
      width="512" /></a></div>
      <br />
      <span style="font-family: inherit;"><br /></span></div>
      <div>
      <span style="font-family: inherit;">Step 12 Now after successful login open your
      terminal and type one of the following commands</span></div>
      <div>
      <span style="color: red; font-family: &quot;courier&quot;;">restorecon
      /etc/shadow </span><span style="font-family:
      inherit;">or&nbsp;</span><span style="color: red; font-family:
      &quot;courier&quot;;"> touch ./autorelabel</span></div>
      <div>
      <span style="font-family: inherit;"><br /></span></div>
      <div>
      <span style="font-family: inherit;"></span><br />
      <div class="separator" style="clear: both; text-align: center;">
      <span style="font-family: inherit;"><a
      href="https://1.bp.blogspot.com/-E8SNZ1jBQ5o/X1CNv4w-S_I/AAAAAAAAAOs/xeZBukVg2PENj_kwCdCYQQMaW-VETIqegCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-09-03%2Bat%2B12.01.14%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="320"
      src="https://1.bp.blogspot.com/-E8SNZ1jBQ5o/X1CNv4w-S_I/AAAAAAAAAOs/xeZBukVg2PENj_kwCdCYQQMaW-VETIqegCNcBGAsYHQ/w512-h320/Screen%2BShot%2B2020-09-03%2Bat%2B12.01.14%2BPM.png"
      width="512" /></a></span></div>
      <div>
      <span style="font-family: inherit;"><span style="font-family: inherit;"><br
      /></span></span></div>
      <span style="font-family: inherit;">Step 13 Kindly recheck your new password again
      😎</span></div>
      <div>
      <span style="font-family: inherit;"><br /></span></div>
      <div>
      <span style="font-family: inherit;">If you still face the problem in resetting your root
      password please checkout the video below.</span></div>
      <div>
      <div style="text-align: center;">
      <iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen="" frameborder="0" height="315"
      src="https://www.youtube.com/embed/3h1rnzC1gHE" width="560"></iframe></div>
      </div>
      </div>
      </div>
      </div>
      </div>


Write your content here...