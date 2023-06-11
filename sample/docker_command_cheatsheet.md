# Docker command cheatsheet

Published: 2020-11-28T00:40:00.025+05:30

Description: 
      <div style="text-align: left;">The reason for creating this cheat
      sheet is because a long time ago I was called for an interview and he asked me some basic
      command questions regarding docker and in reply, I said "I forget the actual command 😑" yeah
      you read it right I know it sounds not good so for the next time I make sure this won't happen
      again in my life that is why I wrote down below some basic commands that every docker user
      should know. Hope this cheat sheet is also helpfully for you.😀<br />To see all commands
      of docker&nbsp;<br />Write down&nbsp;<span style="color: red; font-family:
      courier;">docker</span> on the command line. You will see all the commands of docker
      in the image below.</div><div class="separator" style="clear: both; text-align:
      center;"><a
      href="https://1.bp.blogspot.com/-suhi9oqYCTI/X8FNpOwZO1I/AAAAAAAAAP0/of_ZFvvS6g03-toPJOG0CsNyL7xhZsCswCNcBGAsYHQ/s1440/Screen%2BShot%2B2020-11-28%2Bat%2B12.33.32%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="900"
      data-original-width="1440" height="400"
      src="https://1.bp.blogspot.com/-suhi9oqYCTI/X8FNpOwZO1I/AAAAAAAAAP0/of_ZFvvS6g03-toPJOG0CsNyL7xhZsCswCNcBGAsYHQ/w640-h400/Screen%2BShot%2B2020-11-28%2Bat%2B12.33.32%2BAM.png"
      width="640" /></a></div><br /><p><br
      /></p><p><b><span><span style="font-family: arial;">Get the
      status of the docker
      daemon</span></span></b></p><p></p><ol
      style="text-align: left;"><li><b style="font-family: arial;">Docker
      information:- </b><span style="color: red; font-family: courier;">docker
      info</span></li></ol><p></p><p><b><span><span
      style="font-family: arial;">C</span></span><span style="caret-color: rgb(0,
      0, 0); font-family: arial; white-space: pre-wrap;">reate a container without&nbsp;
      starting It</span></b></p><span
      id="docs-internal-guid-32d4bf05-7fff-92e7-e730-4c21c4fd03ec"><ol style="caret-color:
      rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-size-adjust: auto;"><li
      dir="ltr" style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline; white-space: pre;"><p dir="ltr" role="presentation" style="line-height: 1.38;
      margin-bottom: 0pt; margin-top: 0pt;"><span><span style="font-family: arial;
      font-variant-east-asian: normal; font-weight: 700; vertical-align: baseline; white-space:
      pre-wrap;">Creates container:-</span><span style="font-family: arial;
      font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">
      </span><span style="color: red; font-family: courier; font-variant-east-asian:
      normal; vertical-align: baseline; white-space: pre-wrap;">docker create [image
      name]</span></span></p></li></ol></span><span><br
      /><p dir="ltr" style="caret-color: rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt; text-size-adjust: auto;"><span style="font-family: Arial;
      font-variant-east-asian: normal; font-weight: 700; vertical-align: baseline; white-space:
      pre-wrap;">Docker run commands&nbsp;</span></p><p dir="ltr"
      style="caret-color: rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;
      text-size-adjust: auto;"></p><ol style="caret-color: rgb(0, 0, 0); text-align:
      left; text-size-adjust: auto;"><li><span
      id="docs-internal-guid-32d4bf05-7fff-92e7-e730-4c21c4fd03ec" style="caret-color: rgb(0, 0, 0);
      text-size-adjust: auto;"><p dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt;"><span><span style="font-family: arial; font-variant-east-asian:
      normal; font-weight: 700; vertical-align: baseline; white-space: pre-wrap;">Run
      container:-</span><span style="font-family: arial; font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;"> </span><span style="color: red;
      font-family: courier; font-variant-east-asian: normal; vertical-align: baseline; white-space:
      pre-wrap;">docker run [image
      name]</span></span></p></span></li></ol><p
      style="caret-color: rgb(0, 0, 0); text-size-adjust: auto;"></p><ol start="2"
      style="caret-color: rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-size-adjust:
      auto;"><li dir="ltr" style="font-variant-east-asian: normal; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span><span
      style="font-family: arial; font-variant-east-asian: normal; font-weight: 700; vertical-align:
      baseline; white-space: pre-wrap;">Run container with specified image
      version:-</span><span style="font-family: arial; font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;"> </span><span style="color: red;
      font-family: courier; font-variant-east-asian: normal; vertical-align: baseline; white-space:
      pre-wrap;">docker run [image
      name]:[version]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align: baseline;
      white-space: pre;"><p dir="ltr" role="presentation" style="line-height: 1.38;
      margin-bottom: 0pt; margin-top: 0pt;"><span><span style="font-family: arial;
      font-variant-east-asian: normal; font-weight: 700; vertical-align: baseline; white-space:
      pre-wrap;">Docker run in background/detach mode image :-</span><span
      style="font-family: arial; font-variant-east-asian: normal; vertical-align: baseline;
      white-space: pre-wrap;"> </span><span style="color: red; font-family: courier;
      font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">docker
      run -d [image name]</span></span></p></li></ol><p dir="ltr"
      style="caret-color: rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;
      text-size-adjust: auto;"><b><span style="font-family: arial;"><br
      /></span></b></p><p dir="ltr" style="caret-color: rgb(0, 0, 0);
      line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-size-adjust:
      auto;"><b><span style="font-family: arial;">Docker naming
      container</span></b></p><p dir="ltr" style="caret-color: rgb(0, 0, 0);
      line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-size-adjust:
      auto;"></p><ol style="text-align: left;"><li><b style="font-family:
      arial;">Docker naming container:- </b><span style="color: red; font-family:
      courier;">docker run -it --name [container name] [image
      name]&nbsp;</span></li></ol><p></p><p dir="ltr"
      style="caret-color: rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;
      text-size-adjust: auto;"><span style="font-family: Arial; font-variant-east-asian:
      normal; font-weight: 700; vertical-align: baseline; white-space: pre-wrap;">Docker renaming
      existing&nbsp; container</span></p><br /><ol style="caret-color:
      rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-size-adjust: auto;"><li
      dir="ltr" style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span><span
      style="font-family: arial; font-variant-east-asian: normal; vertical-align: baseline;
      white-space: pre-wrap;">Docker renaming existing container :- </span><span
      style="color: red; font-family: courier; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker rename [container name] [new
      container name]</span></span></p></li></ol><div
      style="caret-color: rgb(0, 0, 0); text-size-adjust: auto;"><span style="color: red;
      font-family: arial;"><span style="white-space: pre-wrap;"><br
      /></span></span></div><p dir="ltr" style="caret-color: rgb(0, 0, 0);
      line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-size-adjust: auto;"><span
      style="font-family: arial; white-space: pre-wrap;"><b>Listing out running/stop
      containers, images, events of the container, history of
      images</b></span></p><br /></span><ol style="caret-color:
      rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-align: left; text-size-adjust:
      auto;"><span><li style="font-variant-east-asian: normal; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p role="presentation" style="line-height:
      1.38; margin-bottom: 0pt; margin-top: 0pt;"><span><span style="font-family: arial;
      font-variant-east-asian: normal; font-weight: 700; vertical-align: baseline; white-space:
      pre-wrap;">List all running containers:-</span><span style="font-family: arial;
      font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">
      </span><span style="color: red; font-family: courier; font-variant-east-asian:
      normal; vertical-align: baseline; white-space: pre-wrap;">docker
      ps</span></span></p></li><li style="font-variant-east-asian:
      normal; list-style-type: decimal; vertical-align: baseline; white-space: pre;"><p
      role="presentation" style="line-height: 1.38; margin-bottom: 0pt; margin-top:
      0pt;"><span><span style="font-family: arial; font-variant-east-asian: normal;
      font-weight: 700; vertical-align: baseline; white-space: pre-wrap;">List all running/stop
      containers:-</span><span style="font-family: arial; font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;"> </span><span style="color: red;
      font-family: courier; font-variant-east-asian: normal; vertical-align: baseline; white-space:
      pre-wrap;">docker ps -a</span></span></p></li><li
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p role="presentation" style="line-height:
      1.38; margin-bottom: 0pt; margin-top: 0pt;"><span><span style="font-family: arial;
      font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">Lst out
      most recently created images:- </span><span style="font-family: arial;
      font-variant-east-asian: normal; font-weight: 400; vertical-align: baseline; white-space:
      pre-wrap;">&nbsp;</span><span style="color: red; font-family: courier;
      font-variant-east-asian: normal; font-weight: 400; vertical-align: baseline; white-space:
      pre-wrap;">docker images</span></span></p></li><li
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p role="presentation" style="line-height:
      1.38; margin-bottom: 0pt; margin-top: 0pt;"><span><span style="font-family: arial;
      font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">List
      all&nbsp; images:- </span><span style="font-family: arial;
      font-variant-east-asian: normal; font-weight: 400; vertical-align: baseline; white-space:
      pre-wrap;">&nbsp;</span><span style="color: red; font-family: courier;
      font-variant-east-asian: normal; font-weight: 400; vertical-align: baseline; white-space:
      pre-wrap;">docker image ls</span></span></p></li><li
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p role="presentation" style="line-height:
      1.38; margin-bottom: 0pt; margin-top: 0pt;"><span><span style="background-color:
      white; font-family: arial; font-variant-east-asian: normal; vertical-align: baseline;
      white-space: pre-wrap;">List real-time events from a container</span><span
      style="font-family: arial; font-variant-east-asian: normal; vertical-align: baseline;
      white-space: pre-wrap;">:- </span><span style="font-family: arial;
      font-variant-east-asian: normal; font-weight: 400; vertical-align: baseline; white-space:
      pre-wrap;">&nbsp;</span><span style="color: red; font-family: courier;
      font-variant-east-asian: normal; font-weight: 400; vertical-align: baseline; white-space:
      pre-wrap;">docker events [container
      name]</span></span></p></li><li style="font-variant-east-asian:
      normal; font-weight: 700; list-style-type: decimal; vertical-align: baseline; white-space:
      pre;"><p role="presentation" style="line-height: 1.38; margin-bottom: 0pt; margin-top:
      0pt;"><span><span style="font-family: arial; font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Check history&nbsp; of images :-
      </span><span style="font-family: arial; font-variant-east-asian: normal; font-weight:
      400; vertical-align: baseline; white-space: pre-wrap;">&nbsp;</span><span
      style="color: red; font-family: courier; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker history [option]
      [image]</span></span></p></li></span><li
      style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><p role="presentation" style="line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt;"><span><span style="font-family: arial; font-weight: 700;
      white-space: pre;">Show running processes in a container:-
      </span></span><span style="color: red; font-family: courier;">docker top
      [CONTAINER]</span></p></li><li style="font-variant-east-asian: normal;
      list-style-type: decimal; vertical-align: baseline;"><div style="line-height: 1.38;
      margin-bottom: 0pt; margin-top: 0pt;"><span style="font-family: arial;
      font-variant-east-asian: normal; font-weight: 700; vertical-align: baseline; white-space:
      pre-wrap;">List all networks:-</span><span style="font-family: arial;
      font-variant-east-asian: normal; vertical-align: baseline; white-space: pre-wrap;">
      </span><span style="font-family: courier;"><span style="color: red;
      font-variant-east-asian: normal; vertical-align: baseline; white-space:
      pre-wrap;">docker</span><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;"> </span><span style="color:
      red;">network
      ls</span></span></div></li></ol><div><span
      style="color: red; font-family: courier;"><span style="white-space: pre-wrap;"><br
      /></span></span></div><span><p dir="ltr" style="caret-color:
      rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-size-adjust:
      auto;"><span style="font-family: Arial; font-variant-east-asian: normal; font-weight:
      700; vertical-align: baseline; white-space: pre-wrap;">Docker&nbsp; start, stop,
      restart, pause, unpause, wait, kill, attach the container</span></p><br
      /><ol style="caret-color: rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px;
      text-size-adjust: auto;"><li dir="ltr" style="font-variant-east-asian: normal;
      font-weight: 700; list-style-type: decimal; vertical-align: baseline; white-space:
      pre;"><p dir="ltr" role="presentation" style="line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt;"><span style="font-family: arial;"><span
      style="font-variant-east-asian: normal; vertical-align: baseline; white-space:
      pre-wrap;">Stop docker container :- </span><span style="color: red;
      font-variant-east-asian: normal; font-weight: 400; vertical-align: baseline; white-space:
      pre-wrap;">docker stop [container
      name/id]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Start docker container :-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker start [container
      name/id]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Restart docker container :-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker restart [container
      name/id]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Pause docker container :-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker pause [container
      name/id]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Unpause docker container :-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker unpause [container
      name/id]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Wait docker container:-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker wait [container
      name/id]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Kill docker container :-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker kill [container
      name/id]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Attach docker container :-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker attach [container
      name/id]</span></span></p></li></ol><div><span
      style="color: red; font-family: arial;"><span style="white-space: pre-wrap;"><br
      /></span></span></div><p dir="ltr" style="caret-color: rgb(0, 0, 0);
      line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-size-adjust: auto;"><span
      style="font-variant-east-asian: normal; font-weight: 700; vertical-align: baseline;
      white-space: pre-wrap;"><span style="font-family: arial;">Docker
      remove</span></span></p></span><ol style="caret-color: rgb(0, 0,
      0); margin-bottom: 0px; margin-top: 0px; text-size-adjust: auto;"><span><li
      dir="ltr" style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Remove&nbsp; docker container :-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker rm [container
      name/id]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Remove&nbsp; docker image :-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker rmi [image
      name]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Remove&nbsp; all unused docker
      container:- </span><span style="color: red; font-variant-east-asian: normal;
      font-weight: 400; vertical-align: baseline; white-space: pre-wrap;">docker container
      prune</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Remove&nbsp; all unused docker
      images:- </span><span style="color: red; font-variant-east-asian: normal;
      font-weight: 400; vertical-align: baseline; white-space: pre-wrap;">docker image
      prune&nbsp;</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="font-variant-east-asian: normal;
      vertical-align: baseline; white-space: pre-wrap;">Remove all unused images as well as
      containers:- </span><span style="color: red; font-variant-east-asian: normal;
      font-weight: 400; vertical-align: baseline; white-space: pre-wrap;">docker system
      prune</span><span style="font-variant-east-asian: normal; vertical-align: baseline;
      white-space:
      pre-wrap;">&nbsp;</span></span></p></li></span><li
      dir="ltr" style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><p dir="ltr" role="presentation" style="line-height: 1.38; margin-bottom:
      0pt; margin-top: 0pt;"><span><span style="font-family: arial; font-weight: 700;
      white-space: pre;">Remove one or more networks:- </span></span><span
      style="color: red; font-family: arial;">docker network rm
      [NETWORK]</span></p></li></ol><span><div style="caret-color:
      rgb(0, 0, 0); text-size-adjust: auto;"><span style="font-family: arial;"><span
      style="white-space: pre-wrap;"><b><br
      /></b></span></span></div><div style="caret-color: rgb(0, 0, 0);
      text-size-adjust: auto;"><p dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt;"><span style="font-variant-east-asian: normal; font-weight: 700;
      vertical-align: baseline; white-space: pre-wrap;"><span style="font-family:
      arial;">Docker update</span></span></p><ol style="margin-bottom: 0px;
      margin-top: 0px;"><li dir="ltr" style="font-variant-east-asian: normal; list-style-type:
      decimal; vertical-align: baseline; white-space: pre;"><span style="font-family:
      arial;"><b>Update the configuration of one or more containers:- </b><span
      style="color: red;">docker update
      [CONTAINER]</span></span></li></ol><div><span style="color:
      red; font-family: arial;"><span style="white-space: pre;"><br
      /></span></span></div></div></span><div
      style="caret-color: rgb(0, 0, 0); text-size-adjust: auto;"><span><p dir="ltr"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-variant-east-asian: normal; font-weight: 700; vertical-align: baseline;
      white-space: pre-wrap;"><span style="font-family: arial;">Docker
      import</span></span></p></span><ol style="margin-bottom: 0px;
      margin-top: 0px; text-align: left;"><li style="font-variant-east-asian: normal;
      list-style-type: decimal; vertical-align: baseline;"><div style="line-height: 1.38;
      margin-bottom: 0pt; margin-top: 0pt;"><span><span style="font-family: arial;
      white-space: pre;"><span style="font-variant-east-asian: normal; vertical-align:
      baseline; white-space: pre-wrap;"><span style="background-color: white; white-space:
      normal;"><b>Create an image from a tarball</b></span><b>:-
      </b></span></span></span><span style="color: red; font-family:
      arial;">docker import
      [URL/FILE]</span></div></li></ol><div><span style="color:
      red; font-family: arial;"><br /></span></div><div><p dir="ltr"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-variant-east-asian: normal; font-weight: 700; vertical-align: baseline;
      white-space: pre-wrap;"><span style="font-family: arial;">Docker
      commit</span></span></p><ol style="margin-bottom: 0px; margin-top:
      0px;"><li dir="ltr" style="font-variant-east-asian: normal; list-style-type: decimal;
      vertical-align: baseline;"><span style="font-family: arial;"><b>Create an image
      from a container:-&nbsp;</b><span style="color: red;">docker commit
      [CONTAINER]
      [NEW_IMAGE_NAME]</span></span></li></ol><div><span
      style="color: red; font-family: arial;"><br
      /></span></div><div><p dir="ltr" style="line-height: 1.38;
      margin-bottom: 0pt; margin-top: 0pt;"><span style="font-variant-east-asian: normal;
      font-weight: 700; vertical-align: baseline; white-space: pre-wrap;"><span
      style="font-family: arial;">Docker load</span></span></p><ol
      style="margin-bottom: 0px; margin-top: 0px;"><li dir="ltr"
      style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><span style="font-family: arial;"><b>Load an image from a tar
      archive or stdin:-&nbsp;</b><span style="color: red;">docker load
      [TAR_FILE/STDIN_FILE]</span></span></li></ol></div></div></div><span><br
      /><p dir="ltr" style="caret-color: rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt; text-size-adjust: auto;"><span style="font-variant-east-asian: normal;
      font-weight: 700; vertical-align: baseline; white-space: pre-wrap;"><span
      style="font-family: arial;">Docker pull</span></span></p><ol
      style="caret-color: rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-size-adjust:
      auto;"><li dir="ltr" style="font-variant-east-asian: normal; font-weight: 700;
      list-style-type: decimal; vertical-align: baseline; white-space: pre;"><p dir="ltr"
      role="presentation" style="line-height: 1.38; margin-bottom: 0pt; margin-top:
      0pt;"><span style="font-family: arial;"><span style="font-variant-east-asian:
      normal; vertical-align: baseline; white-space: pre-wrap;">Pull&nbsp; docker image:-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker pull [image
      name]</span></span></p></li></ol><div><span
      style="color: red; font-family: arial;"><span style="white-space: pre-wrap;"><br
      /></span></span></div></span><div><span><p dir="ltr"
      style="caret-color: rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;
      text-size-adjust: auto;"><span style="font-variant-east-asian: normal; font-weight: 700;
      vertical-align: baseline; white-space: pre-wrap;"><span style="font-family:
      arial;">Docker save</span></span></p></span><ol
      style="caret-color: rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-align: left;
      text-size-adjust: auto;"><li style="font-variant-east-asian: normal; list-style-type:
      decimal; vertical-align: baseline;"><div style="line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt;"><span style="font-family: arial;"><span><span
      style="white-space: pre;"><span style="font-variant-east-asian: normal; vertical-align:
      baseline; white-space: pre-wrap;"><span style="white-space: pre;"><b>Save
      </b></span></span></span></span><b>an image to a tar
      archive, streamed to STDOUT&nbsp;with all parent layers, tags, and
      versions</b></span><b style="font-family: arial;">:-</b><span
      style="font-family: arial;">&nbsp;</span><span style="color: red; font-family:
      arial;">docker save [IMAGE] &gt;
      [TAR_FILE]</span></div></li></ol></div><span><br
      /><p dir="ltr" style="caret-color: rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt; text-size-adjust: auto;"><span style="font-variant-east-asian: normal;
      font-weight: 700; vertical-align: baseline; white-space: pre-wrap;"><span
      style="font-family: arial;">Docker Mapping</span></span></p><ol
      style="caret-color: rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-size-adjust:
      auto;"><li dir="ltr" style="font-variant-east-asian: normal; font-weight: 700;
      list-style-type: decimal; vertical-align: baseline; white-space: pre;"><p dir="ltr"
      role="presentation" style="line-height: 1.38; margin-bottom: 0pt; margin-top:
      0pt;"><span style="font-family: arial;"><span style="font-variant-east-asian:
      normal; vertical-align: baseline; white-space: pre-wrap;">Docker port mapping :-
      </span><span style="font-variant-east-asian: normal; vertical-align: baseline;
      white-space: pre-wrap;">&nbsp;</span><span style="color: red;
      font-variant-east-asian: normal; font-weight: 400; vertical-align: baseline; white-space:
      pre-wrap;">docker run -p&nbsp; [base ip:container ip] [image
      name]</span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial;"><span style="color: red; font-variant-east-asian: normal;
      font-weight: 400; vertical-align: baseline; white-space: pre-wrap;"><span style="color:
      black; font-variant-east-asian: normal; font-weight: 700; vertical-align: baseline;">Docker
      volume mapping :- </span><span style="color: red; font-variant-east-asian: normal;
      vertical-align: baseline;">docker run -v&nbsp; [base dir:container dir] [image
      name]</span></span></span></p></li><li dir="ltr"
      style="font-variant-east-asian: normal; font-weight: 700; list-style-type: decimal;
      vertical-align: baseline; white-space: pre;"><p dir="ltr" role="presentation"
      style="line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;"><span
      style="font-family: arial; font-weight: 400; white-space: normal;"><b>Show port (or
      specific) mapping for a container:-&nbsp;</b></span><span style="color:
      red; font-family: arial; font-weight: 400; white-space: normal;">docker port
      [CONTAINER]</span></p></li></ol><div style="caret-color: rgb(0, 0,
      0); text-size-adjust: auto;"><span style="caret-color: rgb(0, 0, 0); text-size-adjust:
      auto;"><br /></span></div><br /><p dir="ltr" style="caret-color:
      rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-size-adjust:
      auto;"><span style="font-family: Arial; font-variant-east-asian: normal; font-weight:
      700; vertical-align: baseline; white-space: pre-wrap;">Docker run in
      interactive</span></p><ol style="caret-color: rgb(0, 0, 0); margin-bottom: 0px;
      margin-top: 0px; text-size-adjust: auto;"><li dir="ltr" style="font-variant-east-asian:
      normal; font-weight: 700; list-style-type: decimal; vertical-align: baseline; white-space:
      pre;"><p dir="ltr" role="presentation" style="line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt;"><span style="font-family: arial;"><span
      style="font-variant-east-asian: normal; vertical-align: baseline; white-space:
      pre-wrap;">Docker run in an interactive way:- </span><span style="color: red;
      font-variant-east-asian: normal; font-weight: 400; vertical-align: baseline; white-space:
      pre-wrap;">docker run -it [image
      name]</span></span></p></li></ol><p dir="ltr"
      style="caret-color: rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt;
      text-size-adjust: auto;"><br /></p><p dir="ltr" style="caret-color: rgb(0,
      0, 0); line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-size-adjust:
      auto;"><span style="font-variant-east-asian: normal; font-weight: 700; vertical-align:
      baseline; white-space: pre-wrap;"><span style="font-family: arial;">Docker
      inspect</span></span></p></span><ol style="caret-color: rgb(0, 0,
      0); margin-bottom: 0px; margin-top: 0px; text-align: left; text-size-adjust:
      auto;"><span><li dir="ltr" style="font-variant-east-asian: normal; font-weight:
      700; list-style-type: decimal; vertical-align: baseline; white-space: pre;"><p dir="ltr"
      role="presentation" style="line-height: 1.38; margin-bottom: 0pt; margin-top:
      0pt;"><span style="font-family: arial;"><span style="font-variant-east-asian:
      normal; vertical-align: baseline; white-space: pre-wrap;">Docker find additional details of
      container :- </span><span style="color: red; font-variant-east-asian: normal;
      font-weight: 400; vertical-align: baseline; white-space: pre-wrap;">docker inspect
      [container name/id]</span></span></p></li></span><li
      style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><div style="line-height: 1.38; margin-bottom: 0pt; margin-top:
      0pt;"><span><span style="font-family: arial; white-space: pre;"><b>Show
      information on one or more networks:- </b></span></span><span
      style="color: red; font-family: arial;">docker network inspect
      [NETWORK]</span></div></li></ol><span><div><span
      style="color: red; font-family: arial;"><span style="white-space: pre-wrap;"><br
      /></span></span></div></span><div><div style="caret-color:
      rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt; margin-top: 0pt; text-align: left;
      text-size-adjust: auto;"><span style="font-family: arial;"><span
      style="white-space: pre-wrap;"><b>Docker
      stats</b></span></span></div><span><ol style="caret-color:
      rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-size-adjust: auto;"><li
      dir="ltr" style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline; white-space: pre;"><b><span style="font-family: arial;">Show live
      resource usage statistics of containers</span>:- </b><span style="color: red;
      font-family: arial;">docker stats
      [CONTAINER]</span></li></ol></span></div><span><br
      /><p dir="ltr" style="caret-color: rgb(0, 0, 0); line-height: 1.38; margin-bottom: 0pt;
      margin-top: 0pt; text-size-adjust: auto;"><span style="font-variant-east-asian: normal;
      font-weight: 700; vertical-align: baseline; white-space: pre-wrap;"><span
      style="font-family: arial;">Docker logs </span></span></p><ol
      style="caret-color: rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-size-adjust:
      auto;"><li dir="ltr" style="font-variant-east-asian: normal; font-weight: 700;
      list-style-type: decimal; vertical-align: baseline; white-space: pre;"><p dir="ltr"
      role="presentation" style="line-height: 1.38; margin-bottom: 0pt; margin-top:
      0pt;"><span style="font-family: arial;"><span style="font-variant-east-asian:
      normal; vertical-align: baseline; white-space: pre-wrap;">Docker check logs of container:-
      </span><span style="color: red; font-variant-east-asian: normal; font-weight: 400;
      vertical-align: baseline; white-space: pre-wrap;">docker logs&nbsp; [container
      name/id]</span></span></p></li></ol><div><br
      /></div><div><span style="caret-color: rgb(0, 0, 0); font-family: arial;
      font-weight: 700; white-space: pre-wrap;">Docker
      connect</span></div></span><ol style="caret-color: rgb(0, 0, 0);
      margin-bottom: 0px; margin-top: 0px; text-size-adjust: auto;"><li dir="ltr"
      style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><span><span style="font-family: arial;"><span style="font-weight:
      700; white-space: pre;">Connects a container to a network:-
      </span></span></span><span style="color: red; font-family:
      arial;">docker network connect [NETWORK] [CONTAINER]</span></li><li
      dir="ltr" style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><span><span style="font-family: arial;"><b style="white-space:
      pre;">Disconnect a container from a network:- </b></span></span><span
      style="color: red; font-family: arial;">docker network disconnect [NETWORK]
      [CONTAINER]</span></li></ol><div><span style="color: red;
      font-family: arial;"><br /></span></div><div><span
      style="caret-color: rgb(0, 0, 0); font-family: arial; font-weight: 700; white-space:
      pre-wrap;">Docker space</span></div><div><ol style="caret-color:
      rgb(0, 0, 0); margin-bottom: 0px; margin-top: 0px; text-size-adjust: auto;"><li
      dir="ltr" style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><span><span style="font-family: arial;"><span style="font-weight:
      700; white-space: pre;">Detailed disk usage:-
      </span></span></span><span style="color: red; font-family:
      arial;">docker system df</span></li><li dir="ltr"
      style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><span><span style="font-family: arial;"><b style="white-space:
      pre;">Space used by each container, image and volume:-
      </b></span></span><span style="color: red; font-family:
      arial;">docker&nbsp;</span><span style="color: red; font-family:
      arial;">system df -v</span></li><li dir="ltr"
      style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><b><span style="font-family: arial;">Space used by running
      containers:-&nbsp;</span></b><span style="color: red; font-family:
      arial;">docker ps -s</span></li><li dir="ltr"
      style="font-variant-east-asian: normal; list-style-type: decimal; vertical-align:
      baseline;"><b><span style="font-family: arial;">Filter only &gt;= 1GB :-
      </span></b><span style="color: red; font-family: arial;">docker system df -v
      | grep GB</span></li></ol></div><ol style="caret-color: rgb(0, 0,
      0); margin-bottom: 0px; margin-top: 0px; text-size-adjust: auto;"><br
      /></ol><div><span style="font-family: arial;"><span
      style="white-space: pre-wrap;"><b>Note:- </b></span></span>These
      are some basic commands. I am not mentioning each and every command but if you are curious to
      know more docker commands you can click on the below link.</div><div><a
      href="https://docs.docker.com/engine/reference/commandline/docker/">https://docs.docker.com/engine/reference/commandline/docker/</a></div>

Write your content here...