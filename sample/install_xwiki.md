# Install XWIKI

Published: 2021-02-15T14:54:00.101+05:30

Description: <p>Hey everyone😀, today I want to share another interesting tool
      called XWiki. An amazing tool for enterprise level. For those who don't know about this tool,
      I recommended clicking this <a href="https://en.wikipedia.org/wiki/XWiki"
      target="_blank">Wikipedia URL</a>. So Let's see how to configure
      XWiki.</p><p><b>Step 1 Install
      JDK</b></p><ol><li><b>Check JAVA:-&nbsp;</b><span
      style="color: red; font-family: courier;">&nbsp;java
      -version</span></li><li><b>Update the repositories:-</b><span
      style="background-color: white; caret-color: rgb(31, 36, 56); font-size: 16px;
      text-size-adjust: auto;"><span style="color: red; font-family: courier;">sudo apt-get
      update</span></span></li><li><span style="caret-color: rgb(31, 36,
      56);"><b>Install OpenJDK:- </b></span><span><span style="color:
      red; font-family: courier;"><span style="background-color: white; caret-color: rgb(31,
      36, 56);">sudo apt-get install
      openjdk-8-jdk</span></span></span></li><li><span
      style="caret-color: rgb(31, 36, 56);"><b>Verify the version of the JDK:-
      </b></span><span><span style="color: red; font-family:
      courier;"><span style="background-color: white; caret-color: rgb(31, 36, 56);">java
      -version</span></span></span></li></ol><div><div
      class="separator" style="clear: both; color: red; font-family: courier; text-align:
      center;"><a
      href="https://1.bp.blogspot.com/-J3zD7ul_Yr8/YCospuYKM7I/AAAAAAAAAUk/493TT1Upo6IDItJcPoFiW6UYKhFWITgYgCNcBGAsYHQ/s1440/Screen%2BShot%2B2021-02-15%2Bat%2B1.41.00%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440"
      src="https://1.bp.blogspot.com/-J3zD7ul_Yr8/YCospuYKM7I/AAAAAAAAAUk/493TT1Upo6IDItJcPoFiW6UYKhFWITgYgCNcBGAsYHQ/s320/Screen%2BShot%2B2021-02-15%2Bat%2B1.41.00%2BPM.png"
      width="320" /></a></div><b>Step 2 Set up the XWiki LTS APT repo<br
      /></b><div class="separator" style="clear: both;">Log in as a <span
      style="color: red; font-family: courier;">sudo</span> user, and then download and set
      up the XWiki LTS (Long Term Support) APT repo on your server
      instance&nbsp;<i>(source:- internet)</i>:</div><div class="separator"
      style="clear: both; text-align: left;"><br /></div><div class="separator"
      style="clear: both;"><span style="color: red; font-family: courier;">cd<br
      /><br />
      </span></div><div class="separator" style="clear: both;"><span
      style="color: red; font-family: courier;">wget -q "https://maven.xwiki.org/public.gpg" -O-
      | sudo apt-key add -</span></div><div class="separator" style="clear:
      both;"><span style="color: red; font-family: courier;"><br
      /></span></div><div class="separator" style="clear: both;"><span
      style="color: red; font-family: courier;">sudo wget
      "https://maven.xwiki.org/lts/xwiki-lts.list" -P
      /etc/apt/sources.list.d/</span></div><div class="separator" style="clear:
      both;"><span style="color: red; font-family: courier;"><br
      /></span></div><div class="separator" style="clear: both;"><span
      style="color: red; font-family: courier;">sudo apt update</span><br /><br
      /><b>Note</b>: <i>If you want to try out the latest stable XWiki release
      (but NOT LTS), you can download the below XWiki APT repo instead (source:-
      internet):</i></div></div><div class="separator" style="clear:
      both;"><i><br /></i></div><span style="color: red; font-family:
      courier;">cd
      <br /><br />wget -q "https://maven.xwiki.org/public.gpg" -O- | sudo apt-key add -
      <br /><br />sudo wget "https://maven.xwiki.org/stable/xwiki-stable.list" -P
      /etc/apt/sources.list.d/
      <br /><br />sudo apt update</span><br
      /><p></p><div><span style="color: red; font-family:
      courier;"><br /></span></div><b>Step 3 Install the all in one XWiki
      bundle <br /></b>As a flexible wiki platform, XWiki officially provides various
      integration options. All we need a server (tomcat) and a database(MySQL)<div><span
      style="background-color: #f2f5ff; color: red; font-family: courier; font-size: inherit;
      white-space: pre;"><br /></span></div><div><span
      style="background-color: #f2f5ff; color: red; font-family: courier; font-size: inherit;
      white-space: pre;"><br /></span></div><div><span style="color:
      red; font-family: courier;">apt search xwiki<br /><br /><br
      /></span><span style="background-color: white; font-family: inherit; font-size:
      15px;">If you want to use XWiki with the most common dependencies, you can install all
      required components in one command as follows:</span></div><div><span
      style="color: red; font-family: courier;">sudo apt install xwiki-tomcat9-mysql
      -y</span></div><div><span style="color: red; font-family:
      courier;"><br /></span></div><br /><br />During the
      installation process, you will be asked to set up a new password for the MySQL root user
      several times. Just leave the password field blank and press <span style="color: red;
      font-family: courier;">Enter</span> to skip this step for now. We will tackle this
      problem later while securing the installation of MySQL.<br /><div><br
      /></div>When being asked whether you want to <span style="color: red; font-family:
      courier;">Configure database for XWiki with dbconfig-common?</span>, choose <span
      style="color: red; font-family: courier;">&lt;Yes&gt;</span> and then press
      <span style="color: red; font-family: courier;">ENTER</span>.<div><br
      /></div>When being asked to provide a <span style="color: red; font-family:
      courier;">MySQL application password for XWiki,</span> you can either input a
      specific MySQL application password or leave the password field blank. The latter will tell
      XWiki to use a random MySQL application password.<div><br /></div><br
      /><br />Having XWiki and all of the required dependencies installed, secure the
      installation of MySQL:<br /><div><br /></div><span style="color:
      red; font-family: courier;">sudo
      /usr/bin/mysql_secure_installation</span><div><span style="color: red;
      font-family: courier;"><br /></span></div>During the process, the program
      will ask you a few questions. Reply to them as below:-<div><br
      /></div><div><ul style="text-align: left;"><li>Would you like to
      setup VALIDATE PASSWORD plugin?&nbsp; <span style="color: red; font-family:
      courier;">Y</span></li><li>Please enter 0 = LOW, 1 = MEDIUM and 2 =
      STRONG: <span style="color: red; font-family:
      courier;">2</span></li><li>New password: <span style="color: red;
      font-family:
      courier;">a-strong-MySQL-root-password</span></li><li>Re-enter new
      password: <span style="color: red; font-family:
      courier;">a-strong-MySQL-root-password</span></li><li>Do you wish to
      continue with the password provided? <span style="color: red; font-family:
      courier;">Y</span></li><li>Remove anonymous
      users?&nbsp;&nbsp;<span style="color: red; font-family:
      courier;">Y</span></li><li>Disallow root login
      remotely?&nbsp;&nbsp;<span style="color: red; font-family:
      courier;">Y</span></li><li>Remove test database and access to
      it?&nbsp;&nbsp;<span style="color: red; font-family:
      courier;">Y</span></li><li>Reload privilege tables
      now?&nbsp;&nbsp;<span style="color: red; font-family:
      courier;">Y</span></li></ul>To enhance the security of XWiki modifying
      the XWiki config file.&nbsp;Use the vim editor to open an XWiki config
      file:</div><div><br /></div><span style="color: red; font-family:
      courier;">sudo vi /etc/xwiki/xwiki.cfg</span><div><span style="color: red;
      font-family: courier;"><br /></span></div>Find the two lines shown
      below:<div><br /></div><span style="color: red; font-family:
      courier;">xwiki.authentication.validationKey=totototototototototototototototo
      xwiki.authentication.encryptionKey=titititititititititititititititi</span><div><br
      /></div>Change&nbsp; both values with two different random strings, and just make
      sure that the length of each string is the same as the other one, for
      example:<div><br /></div><span style="color: red; font-family:
      courier;">xwiki.authentication.validationKey=m01s0dfa6ga141e920d5e1056184c03n
      xwiki.authentication.encryptionKey=a8hku91rw235tgjdnvkegmns91ab1ges</span><div><span
      style="color: red; font-family: courier;"><br /></span></div>Save and
      quit:<br /><div><br /></div><span style="color: red; font-family:
      courier;">:wq!<br /></span><br />Restart Tomcat 9 in order to bring all
      of your modifications into effect:<div><br /><span style="color: red;
      font-family: courier;">sudo systemctl restart
      tomcat9.service</span></div><div><span style="color: red; font-family:
      courier;"><br /></span></div>Enable Tomcat 9 in order to start the
      application automatically after every&nbsp; restart:<div><br
      /><div><span style="color: red; font-family: courier;">sudo systemctl enable
      tomcat9.service</span></div><br /><br />Modify UFW firewall rules in
      order to allow web access on port <span style="color: red; font-family:
      courier;">8080</span>:<br /><div><br /></div><span
      style="color: red; font-family: courier;">sudo ufw allow
      8080&nbsp;</span><div><span style="color: red; font-family:
      courier;">sudo ufw enable</span></div><br /><br />By default, since
      Tomcat can serve more than one application at the same time, you need to access your XWiki
      site at the URL <span style="color: red; font-family: courier;"><a
      href="http://localhost:8080/xwiki">http://localhost:8080/xwiki</a></span><div><span
      style="text-align: center;"><br /></span></div><div><span
      style="text-align: center;">In the next blog, <a
      href="https://www.svastikkka.com/2021/03/how-to-setup-nginx-reverse-proxy-with.html"
      target="_blank">we will see&nbsp; how to add an SSL certificate for xwiki using
      Nginx</a> and how to short the URL of xwiki</span></div><div
      style="text-align: center;">Hope you enjoyed my blog post.😎</div></div>

Write your content here...