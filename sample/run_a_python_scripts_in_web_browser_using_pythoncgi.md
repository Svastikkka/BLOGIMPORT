# Run a python scripts in web browser using PythonCGI 

Published: 2020-10-03T02:30:00.009+05:30

Description: Hello everyone 😀&nbsp; &nbsp;today I want to share another
      interesting topic which is python CGI. CGI stands for the Common Gateway Interface. This
      interface allows a web browser to pass input to Python scripts and pass the output of Python
      scripts to a web browser. Building a web interface is similar to building a graphical user
      interface.<br /><br />We will run our demonstrations on a Mac OS X computer.<br
      /><br /><ol style="text-align: left;"><li>Apache is already installed on
      Mac OS X, launch Safari with<span style="color: red; font-family: courier;">
      http://localhost/</span> to verify.</li><li>To enable web sharing, select
      Sharing from the System Preferences.</li><li>Instead of <span style="color:
      red; font-family: courier;">public_html</span>, the Sites the directory is where Mac
      users store their web pages.</li><li>Instead of <span style="color: red;
      font-family: courier;">/var/www/cgi-bin</span>, CGI scripts are in <span
      style="color: red; font-family: courier;">/Library/WebServer/CGI-Executables</span>.
      CGI = Common Gateway Interface is a set of protocols through which applications interact with
      web servers.</li></ol><h3 style="text-align: left;">Apache
      Configuration</h3><div>To check the version of Apache, we can type the following
      at the command prompt in a terminal window:<div><span style="color: red; font-family:
      courier;">httpd -v</span></div><div><span style="color:
      red;"><br /></span></div>To launch Apache, type <span
      style="font-family: courier;"><span style="color: red;">sudo
      /usr/sbin/apachectl</span> <span style="color:
      red;">graceful</span></span> in a Terminal window.&nbsp;<div><span
      style="caret-color: rgb(0, 0, 0); text-align: justify; text-size-adjust: auto;"><br
      /></span></div><div><span style="caret-color: rgb(0, 0, 0);
      text-align: justify; text-size-adjust: auto;">Pointing the browser to localhost (or
      127.0.0.1) shows <span style="color: red;"><span style="font-family: courier;">It
      works!</span> </span>if Apache was configured correctly. To check the
      configuration of Apache, type <span style="color: red; font-family: courier;">apachectl
      configtest</span> at the command prompt<span face="sans-serif"><span
      style="background-color:
      white;">.</span></span></span></div></div><div><span
      style="caret-color: rgb(0, 0, 0); text-align: justify; text-size-adjust: auto;"><span
      face="sans-serif"><span style="background-color: white;"><br
      /></span></span></span></div><div><span style="text-align:
      justify; text-size-adjust: auto;"><h3 style="caret-color: rgb(0, 0, 0); text-align:
      left;">CGI Configuration</h3><span style="caret-color: rgb(0, 0, 0);">1. To
      serve web pages from user directories, in the file </span><span style="caret-color:
      rgb(0, 0, 0); color: red; font-family: courier;">/etc/apache2/extra/httpd-userdir.conf
      </span><span style="caret-color: rgb(0, 0, 0);">uncomment the line that
      contains&nbsp;</span><br /><div style="caret-color: rgb(0, 0,
      0);"><div style="text-align: start;"><span></span><span style="color:
      #2b00fe; font-family: courier;"><br /></span></div><div
      style="text-align: start;"><span><a name='more'></a></span><span
      style="color: #2b00fe; font-family: courier;"><br /></span></div><div
      style="text-align: start;"><span style="color: #2b00fe; font-family: Source Code
      Pro;">Include /private/etc/apache2/users/*.conf</span></div><div
      style="text-align: start;"><span><!--more--></span><span style="color:
      #2b00fe; font-family: courier;"><br /></span></div><div
      style="text-align: start;"><span style="color: #2b00fe; font-family: courier;"><br
      /></span></div><br /><div style="text-align: left;">2. In <span
      style="color: red; font-family: courier;">/etc/apache2/httpd.conf</span> uncomment
      the lines</div><div style="text-align: left;"><br
      /></div><span><!--more--></span><span style="color: #666666;
      font-family: Source Code Pro;"># They are maybe in different
      lines&nbsp;</span></div><div style="caret-color: rgb(0, 0, 0);"><span
      style="color: #2b00fe; font-family: Source Code Pro;">LoadModule userdir_module
      libexec/apache2/mod_userdir.so&nbsp;</span></div><div style="caret-color:
      rgb(0, 0, 0);"><span style="font-family: Source Code Pro;"><br
      /></span></div><div style="caret-color: rgb(0, 0, 0);"><span
      style="color: #2b00fe; font-family: Source Code Pro;">Include
      /private/etc/apache2/extra/httpd-userdir.conf</span></div><div
      style="caret-color: rgb(0, 0, 0);"><span style="color: #2b00fe; font-family: Source Code
      Pro;"><br /></span></div><div style="caret-color: rgb(0, 0,
      0);"><span style="color: #2b00fe; font-family: Source Code Pro;">LoadModule
      cgi_module libexec/apache2/mod_cgi.so</span></div><div style="caret-color:
      rgb(0, 0, 0);"><span><!--more--></span><span style="color: #2b00fe;
      font-family: courier;"><br /></span></div><br /><div
      style="caret-color: rgb(0, 0, 0);">3.&nbsp;Finally, in the folder <span
      style="color: red; font-family: courier;">/etc/apache2/users</span>, if <span
      style="color: red; font-family: courier;">&lt;user&gt;</span> is your user
      name, in the file <span style="color: red; font-family:
      courier;">&lt;user&gt;</span>.conf, then add the line in the
      file&nbsp;<span style="color: red; font-family:
      courier;">&lt;user&gt;</span>.conf.</div><div style="caret-color:
      rgb(0, 0, 0);"><br /></div><span><!--more--></span><span
      style="color: #2b00fe; font-family: Source Code Pro;">Require all
      granted</span></span></div><span style="color: #2b00fe; font-family:
      Source Code Pro;">&lt;Directory
      "/Users/&lt;user&gt;/Sites/"&gt;&nbsp;</span><div><span
      style="color: #2b00fe; font-family: Source Code Pro;">&nbsp; &nbsp; &nbsp;
      Options Indexes MultiViews&nbsp;</span></div><div><span style="color:
      #2b00fe; font-family: Source Code Pro;">&nbsp; &nbsp; &nbsp; AllowOverride
      None&nbsp;</span></div><div><span style="color: #2b00fe; font-family:
      Source Code Pro;">&nbsp; &nbsp; &nbsp; Require all
      granted&nbsp;</span></div><div><span style="color: #2b00fe;
      font-family: Source Code Pro;">&lt;/Directory&gt;</span><div><span
      style="text-align: justify; text-size-adjust:
      auto;"><span><!--more--></span><span style="color: #2b00fe;
      font-family: courier;"><br
      /></span></span></div></div><div><span style="text-align:
      justify; text-size-adjust: auto;"><span style="color: #2b00fe; font-family:
      courier;"><br /></span></span></div><div><span
      style="caret-color: rgb(0, 0, 0); text-align: justify;">4.&nbsp;Now go
      to&nbsp;</span><span style="color: red; font-family:
      courier;">/Library/WebServer/CGI-Executables&nbsp;</span>Python script
      python&nbsp;<b>works.py</b></div><div><b><br
      /></b></div><div>5. Now add this code in works.py
      file</div><div><br
      /></div><div><span></span><span><!--more--></span></div><span
      style="color: #2b00fe; font-family: Source Code
      Pro;">#!/usr/bin/python&nbsp;</span><div><span style="color: #2b00fe;
      font-family: Source Code
      Pro;">"""&nbsp;&nbsp;</span></div><div><span style="color:
      #2b00fe; font-family: Source Code Pro;">&nbsp; &nbsp; Place this in
      /Library/WebServer/CGI-Executables.&nbsp;</span></div><div><span
      style="color: #2b00fe; font-family: Source Code
      Pro;">"""&nbsp;</span></div><div><span style="color: #2b00fe;
      font-family: Source Code Pro;">print("Content-Type:
      text/plain\n\n")&nbsp;</span></div><div><span style="color: #2b00fe;
      font-family: Source Code Pro;"><span>print("</span><span style="caret-color:
      rgb(0, 0, 0); white-space: pre-wrap;">cgi working
      fine</span>")</span></div><div><span><!--more--></span><div><br
      /></div><div>5.&nbsp;Now type URL&nbsp;&nbsp;<span style="color:
      #2b00fe; font-family:
      courier;">http://localhost/cgi-bin/works.py</span></div><div><span
      style="color: #2b00fe; font-family: courier;"><br
      /></span></div><div><span style="color: #2b00fe; font-family:
      courier;"><br /><div class="separator" style="clear: both; text-align:
      left;"><a
      href="https://1.bp.blogspot.com/-J3Jh6xcvL10/X3eUoX9PHkI/AAAAAAAAAPM/zoUXf1wEleQpY2JibbZbEWQ7hfnNYZhmQCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-10-03%2Bat%2B2.28.51%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="401"
      src="https://1.bp.blogspot.com/-J3Jh6xcvL10/X3eUoX9PHkI/AAAAAAAAAPM/zoUXf1wEleQpY2JibbZbEWQ7hfnNYZhmQCNcBGAsYHQ/w634-h401/Screen%2BShot%2B2020-10-03%2Bat%2B2.28.51%2BAM.png"
      width="634" /></a></div><br
      /></span></div></div><div><br
      /></div><div><span style="color: red; font-family: courier;"><br
      /></span></div>

Write your content here...