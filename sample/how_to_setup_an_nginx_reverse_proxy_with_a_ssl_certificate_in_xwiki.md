# How to setup an Nginx reverse proxy with a SSL certificate in XWIKI

Published: 2021-03-14T01:37:00.005+05:30

Description: <p>Hey everyone,&nbsp; Tonight I continue my previous post of the
      complete setup of xwiki. This post is about how to setup&nbsp;&nbsp;Nginx as a reverse
      proxy with an SSL certificate.</p><p>Before moving further we consider that xwiki
      runs on the server( EC2 server) with a domain name called
      <b>example.in</b></p><p>To create a custom domain name using AWS you
      can follow this link:-&nbsp;<a
      href="https://aws.amazon.com/getting-started/hands-on/get-a-domain/">https://aws.amazon.com/getting-started/hands-on/get-a-domain/</a></p>By
      default, Tomcat 9 works on port <span style="color: red;">8080</span>, and you can
      only visit your XWiki site from the same port. If you want to facilitate visitors' access by
      removing the port number part, you can install Nginx as a reverse proxy between XWiki and
      visitors.<div><br /></div>Step 1, Install Nginx using
      apt:<div><span style="color: red; font-family: courier;">sudo apt install nginx
      -y</span></div>Step 2, Setup Nginx as a reverse proxy by modifying its default
      site configurations:<br /><span style="color: red; font-family: courier;">cd
      /etc/nginx/sites-available&nbsp;</span><div><span style="color: red;
      font-family: courier;">sudo mv default
      default.bak&nbsp;</span></div><div><span style="color: red;
      font-family: courier;">sudo vi default</span><div>Step 3, Edit the
      file</div></div><span style="color: red; font-family: courier;">server
      {&nbsp;</span><div><span style="color: red; font-family:
      courier;">listen 0.0.0.0:80;&nbsp;</span></div><div><span
      style="color: red; font-family: courier;">proxy_request_buffering
      off;&nbsp;</span></div><div><span style="color: red; font-family:
      courier;">proxy_buffering off;&nbsp;</span></div><div><span
      style="color: red; font-family: courier;">location /
      {&nbsp;</span></div><div><span style="color: red; font-family:
      courier;"><span>&nbsp;&nbsp; &nbsp;</span>proxy_pass
      http://127.0.0.1:8080;</span></div><div><span style="color: red;
      font-family: courier;"><span>&nbsp;&nbsp;
      </span>&nbsp;proxy_redirect off;</span></div><div><span
      style="color: red; font-family: courier;"><span>&nbsp;&nbsp;
      &nbsp;</span>proxy_set_header Host
      $host;&nbsp;</span></div><div><span style="color: red; font-family:
      courier;"><span>&nbsp;&nbsp; &nbsp;</span>proxy_set_header
      X-Real-IP $remote_addr;&nbsp;</span></div><div><span style="color:
      red; font-family: courier;"><span>&nbsp;&nbsp;
      &nbsp;</span>proxy_set_header X-Forwarded-For
      $proxy_add_x_forwarded_for;</span></div><div><span style="color: red;
      font-family: courier;"><span>&nbsp;&nbsp;
      &nbsp;</span>proxy_set_header X-Forwarded-Host
      $server_name;&nbsp;</span></div><div><span style="color: red;
      font-family: courier;"><span>&nbsp;&nbsp;
      &nbsp;</span>}&nbsp;</span></div><div><span style="color:
      red; font-family: courier;">}</span></div><div><br
      /></div><div>Save and quit</div>Step 4, Start the Nginx service and set
      it to automatically start on system startup:<div><span style="color: red;
      font-family: courier;">sudo systemctl restart
      nginx.service&nbsp;</span></div><div><span style="color: red;
      font-family: courier;">sudo systemctl enable
      nginx.service</span></div><div><br /></div>Step 5,&nbsp;
      Modify the UFW firewall rules accordingly:<br /><div><br
      /></div><span style="color: red; font-family: courier;">sudo ufw allow
      80&nbsp;</span><div><span style="color: red; font-family: courier;">sudo
      ufw deny 8080&nbsp;</span></div><div><span style="color: red;
      font-family: courier;">sudo ufw reload</span></div><div><br
      /></div><div>Step 6, Verify</div><div>So just check the
      port&nbsp; number 80 is working or not on the browser</div><div><br
      /></div><div><span style="color: red; font-family:
      courier;">example.in:80</span></div><div>Also, check port number 8080 is
      not working&nbsp;</div><div><br /></div><div><span
      style="color: red; font-family:
      courier;">example.in:8080</span></div><div><br
      /></div><div>Step 7, Add SSL certificate</div>First, download the Let’s
      Encrypt client, certbot:<div><span style="color: red; font-family:
      courier;">apt-get update&nbsp;</span></div><div><span
      style="color: red; font-family: courier;">sudo apt-get install
      certbot&nbsp;</span></div><div><span style="color: red; font-family:
      courier;">apt-get install python-certbot-nginx</span></div><div><br
      /></div><div>Step 8,&nbsp; Obtain the SSL/TLS Certificate</div>The
      NGINX plug‑in for certbot takes care of reconfiguring NGINX and reloading its configuration
      whenever necessary.<div><ol><li>Run the following command to generate
      certificates with the NGINX plug‑in:&nbsp;<span style="border: 0px; box-sizing:
      inherit; font-size: 15px; margin: 0px; outline: 0px; padding: 0px; vertical-align: baseline;
      white-space: pre-wrap;"><span style="color: red; font-family: courier;">sudo certbot
      --nginx -d example.in -d example.in</span></span></li><li>Respond to
      prompts from certbot to configure your HTTPS settings, which involves entering your email
      address and agreeing to the Let’s Encrypt terms of service.</li><li>certbot
      generates a message indicating that certificate generation was successful and specifying the
      location of the certificate on your server. When certificate generation completes, NGINX
      reloads with the new settings.</li><li>If you look at domain‑name.conf, you see
      that certbot has modified it:</li></ol><div class="separator" style="clear:
      both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-Lj9VkV_tJlU/YE0ZwpotpNI/AAAAAAAAAVA/2970RlpF-JEdF4fJS9TBXJa4d7460nX3gCNcBGAsYHQ/s790/Screen%2BShot%2B2021-03-14%2Bat%2B1.29.10%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="552"
      data-original-width="790" height="280"
      src="https://1.bp.blogspot.com/-Lj9VkV_tJlU/YE0ZwpotpNI/AAAAAAAAAVA/2970RlpF-JEdF4fJS9TBXJa4d7460nX3gCNcBGAsYHQ/w400-h280/Screen%2BShot%2B2021-03-14%2Bat%2B1.29.10%2BAM.png"
      width="400" /></a></div><br /><div><br
      /></div></div><div>Now check the URL <a
      href="https://example.in">https://example.in</a></div><div><br
      /></div><div style="text-align: center;">Hope you enjoyed my blog
      post.😎</div>

Write your content here...