# Configure 5099 rpm packages using Yum Without Internet 

Published: 2020-12-02T02:16:00.014+05:30

Description: Hey everyone 😀, Today I want to share an exciting configuration tool which
      is called <b>YUM</b> "not <a
      href="https://en.wikipedia.org/wiki/Yama_(Hinduism)" target="_blank">Yumraj</a>" but
      RHEL's <b>Yum</b>. <b>Yum</b> is the default package management
      utility in RHEL/Centos Linux. For your knowledge <b>aptitude (apt)</b> is
      a&nbsp; default package manager for Debian GNU/Linux systems.<div><br
      /></div><div><b>Note</b>:- Without Yum or apt you will face
      difficulty to manually install the packages in a Linux system.<br /><div><br
      /></div><div><b>Why we need
      Yum?&nbsp;</b></div><div><b><br /></b></div>Yum
      is used to searching, installing, updating and removing necessary rpm files from the system.
      RHEL/Centos Linux use .rpm file to manage the software.</div><div><br
      /></div>A .<b>rpm</b> file extension represents the Linux software
      package file. Yum uses a repository to manage the rpm files. A repository is the collection of
      RPM files. Since Yum depends on the repository, there must be at least one working repository
      before it can be used. A repository can be configured either locally (on local hard) or
      remotely (on network or internet).<div><br
      /></div><div><b>KeyPoints To Remember</b></div><ol
      style="text-align: left;"><li>YUM stands for Yellow Dog Updater
      Manager.</li><li>Yum is the default package management utility in
      RHEL/Centos.</li><li>Yum uses a repository to get the necessary rpm
      files.</li><li>A repository is a collection of rpm
      files.</li><li>Repository may contain multiple versions of the same RPM
      package.</li><li>Repository may contain different builds for different
      architectures for example one for&nbsp;<span face="Arial, &quot;Helvetica
      Neue&quot;, Helvetica, sans-serif" style="background-color: white; color: #242729;
      font-size: 15px;">i386</span>&nbsp;and other for x86_64.</li><li>A
      repository can be configured locally or remotely.</li><li>Yum can automatically
      resolve software dependencies and based on system hardware it can automatically select the
      appropriate version of RPM package from the repository.</li></ol><div>So Yum
      sounds very helpful tool 😄&nbsp; for Linux RHEL users but like every tool Yum require
      settings or configurations to do his job in a required manner and also add some custom
      settings/configurations to do work in our manner.</div><div><br
      /></div><div>sorry I know, I talk too much 😑</div><div><br
      /></div><div>Now we going to see how we can configure our yum locally and
      without the internet we can download almost every package (Basic stuff) to full fill our
      needs</div><div><br /></div><div><br
      /></div><div>So first we need soo many rpm packages to get them we&nbsp;
      need our RHEL (Rhel 7) os image&nbsp;</div><div><br
      /></div><div class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-IMNdisrgfTo/X8ai_vFwRBI/AAAAAAAAAQA/HWLPdGnBZOg0SZ2P3CIs1sDh_uAPwZrTwCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B1.38.57%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-IMNdisrgfTo/X8ai_vFwRBI/AAAAAAAAAQA/HWLPdGnBZOg0SZ2P3CIs1sDh_uAPwZrTwCNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B1.38.57%2BAM.png"
      width="400" /></a></div><br /><div><br
      /></div><div>Second, select to <b>Package</b> folder and copy to
      desktop&nbsp;</div><div><br /></div><div class="separator"
      style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-nOrLgEQ3aqM/X8ajkNb70eI/AAAAAAAAAQI/nWJCoork4jcuSENNsQZLZhql3H1b5z8eQCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B1.41.40%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-nOrLgEQ3aqM/X8ajkNb70eI/AAAAAAAAAQI/nWJCoork4jcuSENNsQZLZhql3H1b5z8eQCNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B1.41.40%2BAM.png"
      width="400" /></a></div><div><br /></div><div>Third,
      select to <b>repodata</b>&nbsp;folder and copy to
      desktop&nbsp;</div><div><br /></div><div class="separator"
      style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-vt3_YYsQtT8/X8akMvCviFI/AAAAAAAAAQQ/ETa4SPfNuKYe9qlkqkqslPbmBKu39NICwCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B1.44.23%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-vt3_YYsQtT8/X8akMvCviFI/AAAAAAAAAQQ/ETa4SPfNuKYe9qlkqkqslPbmBKu39NICwCNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B1.44.23%2BAM.png"
      width="400" /></a></div><br /><div><div>Fourth, you can now
      eject your <b>RHEL</b> disc&nbsp;</div><div><br
      /></div><div class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-6PTaGsoc7cA/X8alg--KVtI/AAAAAAAAAQc/DkRcHQ8Yg8YPmwB8mSSYBrMA5nVlAmHOgCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B1.49.50%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-6PTaGsoc7cA/X8alg--KVtI/AAAAAAAAAQc/DkRcHQ8Yg8YPmwB8mSSYBrMA5nVlAmHOgCNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B1.49.50%2BAM.png"
      width="400" /></a></div><br /><div><br
      /></div><div>Fifth, put your <b>repodata</b> folder inside in
      <b>Package</b> folder</div></div><div><br
      /></div><div class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-wkNHzhiN6tI/X8al7QYU_II/AAAAAAAAAQk/X4aTRZI_SVARVaD3l90T2hUK8ZFaXZzdACNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B1.51.43%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-wkNHzhiN6tI/X8al7QYU_II/AAAAAAAAAQk/X4aTRZI_SVARVaD3l90T2hUK8ZFaXZzdACNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B1.51.43%2BAM.png"
      width="400" /></a></div><br /><div><br
      /></div><div><div>Sixth, now go to yum's config file <span
      style="color: red; font-family:
      arial;">cd&nbsp;&nbsp;/etc/yum.repos.d</span></div><div><b><br
      /></b></div><div><div class="separator" style="clear: both;
      text-align: center;"><a
      href="https://1.bp.blogspot.com/-Hl5PfKKCZmA/X8amvrioEgI/AAAAAAAAAQ4/kgYbOZX9SowBCcowovKywQwemQ4U0nS_wCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B1.55.18%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-Hl5PfKKCZmA/X8amvrioEgI/AAAAAAAAAQ4/kgYbOZX9SowBCcowovKywQwemQ4U0nS_wCNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B1.55.18%2BAM.png"
      width="400" /></a></div><div><br
      /></div><b>Note</b>:- Here <b>redhat.repo </b>is a default
      yum configuration file&nbsp;</div><div><br /></div><div
      class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-I09dw03CQYY/X8anbSbloNI/AAAAAAAAARE/nBgX-9wrWlgn2tFx6GGSTe1Q-6dhOFgJgCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B1.58.13%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-I09dw03CQYY/X8anbSbloNI/AAAAAAAAARE/nBgX-9wrWlgn2tFx6GGSTe1Q-6dhOFgJgCNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B1.58.13%2BAM.png"
      width="400" /></a></div><br /><div><br
      /></div><div><div>Seventh, create your own yum's configuration file
      <span style="color: red; font-family: arial;">vim
      dvd.repo</span></div></div><div><br /></div><div
      class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-p9ioMr59avA/X8ansgfUBFI/AAAAAAAAARM/WmCtYiQaSjA50W5POPDzKmXzeuY03P6HQCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B1.59.19%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-p9ioMr59avA/X8ansgfUBFI/AAAAAAAAARM/WmCtYiQaSjA50W5POPDzKmXzeuY03P6HQCNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B1.59.19%2BAM.png"
      width="400" /></a></div><br /><div><div>Eighth, write down
      the following config in your file and then save it.</div><div><br
      /></div><div class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-DsILO8WvCvY/X8aozAIGdsI/AAAAAAAAARY/qytVKxl5YPI9Ps5BLYjrs0XsZpjgeIIPgCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B2.04.03%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-DsILO8WvCvY/X8aozAIGdsI/AAAAAAAAARY/qytVKxl5YPI9Ps5BLYjrs0XsZpjgeIIPgCNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B2.04.03%2BAM.png"
      width="400" /></a></div><br /><div><div>Ninth, enter a
      command <span style="color: red; font-family: arial;">yum repolist </span><span
      style="font-family: arial;">and then you see something like
      this</span></div><div><span style="font-family: arial;"><br
      /></span></div><div><div class="separator" style="clear: both;
      text-align: center;"><a
      href="https://1.bp.blogspot.com/-eY4bsULrZHQ/X8apsLJcYNI/AAAAAAAAARk/2dZ4bzTpfoopPPejGpsHfb39CN8UZ7uOACNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-02%2Bat%2B2.07.10%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="250"
      src="https://1.bp.blogspot.com/-eY4bsULrZHQ/X8apsLJcYNI/AAAAAAAAARk/2dZ4bzTpfoopPPejGpsHfb39CN8UZ7uOACNcBGAsYHQ/w400-h250/Screen%2BShot%2B2020-12-02%2Bat%2B2.07.10%2BAM.png"
      width="400" /></a></div><div><br /></div>Wow, we just
      configure 5099 rpm packages so now we install these packages without
      internet.&nbsp;</div><div><br /></div><div><span
      style="color: red; font-family: arial;"><br
      /></span></div><div><b>Explanation through
      video&nbsp;</b></div></div><div><br
      /></div><div><div class="separator" style="clear: both; text-align:
      center;"><iframe allowfullscreen="" class="BLOG_video_class" height="332"
      src="https://www.youtube.com/embed/QmhLpMqv0ZM" width="561"
      youtube-src-id="QmhLpMqv0ZM"></iframe></div><br
      /></div></div><div><br /></div><div><b>To know
      more&nbsp;</b></div><div><ul style="text-align:
      left;"><li><a
      href="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-yum">Redhat
      CHAPTER 9. YUM</a></li><li><a
      href="https://en.wikipedia.org/wiki/Yum_(software)#:~:text=The%20Yellowdog%20Updater%2C%20Modified%20(YUM,using%20the%20RPM%20Package%20Manager.">Wikipedia
      Yum</a></li><li><a
      href="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/deployment_guide/c1-yum"
      target="_blank">CHAPTER 14. YUM (YELLOWDOG UPDATER
      MODIFIED)</a></li></ul><div><br
      /></div></div><div><br /></div></div>

Write your content here...