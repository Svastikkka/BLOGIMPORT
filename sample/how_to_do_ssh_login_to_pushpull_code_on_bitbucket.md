# How to do ssh login to push/pull code on bitbucket

Published: 2020-12-15T00:10:00.001+05:30

Description: <p>Hey everyone 😀&nbsp; Tonight (11:43 pm) I am writing this
      blog post for those who find difficulty in ssh login on bitbucket and also for those who loves
      learn new thinsgs.</p><p></p><ol style="-webkit-text-stroke-width: 0px;
      background-color: white; box-sizing: border-box; color: #24292e; font-family: -apple-system,
      system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color
      Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; font-style: normal;
      font-variant-caps: normal; font-variant-ligatures: normal; font-weight: 400; letter-spacing:
      normal; margin-bottom: 0px; margin-top: 0px; orphans: 2; padding-left: 2em; text-align: start;
      text-decoration-color: initial; text-decoration-style: initial; text-decoration-thickness:
      initial; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing:
      0px;"></ol><p></p>Please follow the steps to add ssh key into bitbucket
      account to solve your issue.<br /><ol style="text-align: left;"><li>Open
      <span style="color: red;"><span style="font-family: Source Code Pro;">git
      bash</span> </span>terminal and enter the command <span style="color: red;
      font-family: Source Code Pro;">ssh-keygen -t rsa -C "your email
      address"</span></li><li style="box-sizing: border-box; margin-top:
      0.25em;">Enter passphrase (leave it blank) and enter</li><li>Enter the same
      phrase again (leave it blank) and enter</li><li><span face="-apple-system,
      system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color
      Emoji&quot;, &quot;Segoe UI Emoji&quot;" style="background-color: white; color:
      #24292e; font-size: 16px;">Copy the&nbsp;</span><span style="color: red;
      font-family: Source Code Pro;">id_rsa.pub</span><span face="-apple-system,
      system-ui, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"
      style="color: #24292e;"><span style="background-color: white;">&nbsp;file content
      from where it is residing in your
      system</span></span></li><ol><li><span style="color:
      #24292e;"><span style="color: #24292e; font-family: inherit;">For
      Windows:-&nbsp;</span></span>C:\Users\username.ssh</li><li>For
      Mac:- /Users/UserName(Account Name)</li></ol><li>Login to bitbucket
      account&nbsp;</li><ol><li>Click top right-most <b>user icon
      -&gt; bitbucket settings -&gt; ssh keys </b>under <b>security
      menu&nbsp;</b></li><li>Paste into key-field and save
      it.&nbsp;</li></ol><li>Restart your git bash terminal&nbsp;and now
      you are able to push your work, clone others work and pull your repos✌</li></ol>

Write your content here...