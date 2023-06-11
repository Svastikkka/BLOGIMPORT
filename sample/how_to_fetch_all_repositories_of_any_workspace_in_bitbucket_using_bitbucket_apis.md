# How to fetch all repositories of any workspace in bitbucket using bitbucket
      APIs

Published: 2020-12-28T16:52:00.011+05:30

Description: <p>Hey everyone 😄 recently I completed a team project regarding set
      up some CI/CD with Rest API and because it should
      have CI/CD so we use Jenkins but in here I am going to demonstrate that "How
      to fetch all repositories of any workspace in bitbucket ". So here, we use
      bash script and bitbucket rest API&nbsp;
      </p>
      <p>But first, we need to understand <b>curl</b> command.</p>
      Well according to GfG:- "curl is a command-line tool to transfer data to or from
      a server, using any of the supported protocols (HTTP, FTP, IMAP, POP3, SCP,
      SFTP, SMTP, TFTP, TELNET, LDAP or FILE). This tool is preferred for automation
      since it is designed to work without user interaction. curl can transfer
      multiple files at once."
      <div><br></div>
      <div>
      So hey we know, we need curl for sending/receiving request and response from
      bitbucket server.
      </div>
      <div><br></div>
      <div>
      The other thing we need is bitbucket APIs which can found in here
      <a href="https://developer.atlassian.com/bitbucket/api/2/reference/ "
      target="_blank">Bitbucket API</a>. In the website, there are lots of APIs available
      but we need only this one&nbsp;<a
      href="https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D"
      target="_blank">{workspace}</a>.&nbsp;
      </div>
      <div><br></div>
      <div>So we have both things now let's jump to the coding part&nbsp;</div>
      <div><br></div>
      <script
      src="https://gist.github.com/Svastikkka/0722991170725e5ec406542806b193d2.js"></script>
      <div><span style="font-family:
      inherit;"><br></span></div><div><span style="font-family:
      inherit;"><br></span></div><div><span style="font-family:
      inherit;"><div>In the above code, I use the following
      URL&nbsp;</div><div><br></div><span style="color: red;
      font-family:
      courier;">'https://api.bitbucket.org/2.0/repositories/'$i'/?pagelen=100&amp;page='$count'&amp;fields=next,values.links.branches.href,values.full_name'</span></span></div><div><span
      style="font-family: inherit;"><span style="color: red; font-family:
      courier;"><br></span></span></div><div>
      <span style="font-family: inherit;">But as you can see I added some extra fields in the
      URL which are
      "<b>pagelen</b>", "<b>page</b>"&nbsp; and
      "<b>fields</b>".</span>
      </div>
      <div>
      <span style="font-family: inherit;"><br></span>
      </div><div><ol style="text-align: left;"><li><span
      style="font-family: inherit;"><b>pagelen:- pagelen </b>is basically a length of
      page or how much data we need to have in a single response. In here we get 100 repository's
      data i.e names, links and branches in a single response by adding
      </span><span><span style="color: red; font-family:
      courier;">pagelen=100</span><span style="font-family:
      inherit;">.</span></span></li><li><span style="font-family:
      inherit;"><b>page</b>:-&nbsp; <b>page</b>&nbsp;is basically
      used to&nbsp;</span>specify the page of results to return. In here we use count
      variable so we can fetch all pages.</li><li><b>fields:-
      </b>With<b> fields</b>&nbsp;you can determine how much more data is
      available within the API or you can inspect/select particular data to receive in response. In
      here we select only following fields in response <span style="color: red; font-family:
      courier;">fields=next,values.links.branches.href,values.full_name</span></li></ol><div><span
      style="font-family: inherit;">So now we know what actually this URL
      doing.</span></div><div><span style="font-family:
      inherit;"><br></span></div><div><span style="font-family:
      inherit;"><b>Note</b>:- Be sure you created data.json file because the
      resultant data will store in there.</span></div><div><span
      style="font-family: inherit;"><br></span></div><div><span
      style="font-family: inherit;">In the end, we get JSON data of all
      repositories.</span></div><div><span style="font-family:
      inherit;"><br></span></div><div><div class="separator"
      style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-FgYkQkB5xyc/X-nAUy49ihI/AAAAAAAAASU/dKuApU7SV7UDEDoVtig3m2jjOOTetuCLgCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-12-28%2Bat%2B4.52.47%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="789"
      data-original-width="1440"
      src="https://1.bp.blogspot.com/-FgYkQkB5xyc/X-nAUy49ihI/AAAAAAAAASU/dKuApU7SV7UDEDoVtig3m2jjOOTetuCLgCNcBGAsYHQ/s320/Screen%2BShot%2B2020-12-28%2Bat%2B4.52.47%2BPM.png"
      width="320"></a></div></div><div><div class="separator"
      style="clear: both; text-align:
      center;"><br></div></div><div><span style="font-family:
      inherit;"><br></span></div><div style="text-align:
      center;"><span style="font-family: inherit;">Hope you enjoyed my blog
      post.😎</span></div></div>


Write your content here...