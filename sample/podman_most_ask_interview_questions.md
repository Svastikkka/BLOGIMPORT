# Podman most ask interview questions

Published: 2022-03-20T04:30:00.014+05:30

Description: 
      <p>Q1 Create a custom image using Dockerfile to configure app
      server&nbsp;</p><div><ol><li>Dockerfile is precreated in
      ./task1/</li><li>Base image is jboss/base-jdk:11 ()</li><li>Working
      directory is /opt/jboss</li><li>Copy the JBoSS tar inside
      /opt/jboss</li><li>Extract the tar file (wildfly-23.0.1.Final.tar.gz) inside
      /opt/jboss folder</li><li>Set the ENV variables for
      JBoss</li><ol><li>JBOSS_HOME=/opt/jboss/wildfly-23.0.1.Final.tar.gz</li><li>LAUNCH_JBOSS_IN_BACKGROUND=true</li></ol><li>The
      user should be `jboss`</li><li>Expose following
      ports</li><ol><li>8080 :- For a graphical interface</li><li>9990
      :- For the internal management portal</li><li>9999
      :-</li></ol><li>Commands to run JBoss server</li><li>To test
      your image port forward the following ports</li><ol><li>-
      8080</li><li>- 9990</li></ol></ol><div><br
      /></div></div><div><br /></div><div><br
      /></div><div><script
      src="https://gist.github.com/Svastikkka/0d01025304daf34ee748911fd80a9693.js"></script><br
      /></div><div><div>Q2&nbsp;There are 4 scripts to perform
      operations</div><div><ol><li>start.sh : To run container you created
      in task1 and container should be in demonised/detach mode and container name should be
      `task2`</li><li>stop.sh : To stop container</li><li>delete.sh : To
      delete container&nbsp;</li><li>tail.sh : Print the last 10 lines from the log
      of the container</li></ol></div></div><div><br
      /><script
      src="https://gist.github.com/Svastikkka/2b83be33a4c433ac669880e685df8223.js"></script></div><div>Q3
      Launch the database MYSQL/MariaDB as a container</div><div><ol
      style="text-align: left;"><li>Following are the ENV
      variables</li><ul><li>MYSQL_ROOT_PASSWORD=&nbsp;geheim</li><li>MYSQL_DATABASE=&nbsp;wp</li><li>MYSQL_USER=&nbsp;wordpress</li><li>MYSQL_PASSWORD=w0rdpr3ss</li></ul><li>The
      database should be persistent</li><li>Mount the database container to this PATH:-
      `./data:/var/lib/mysql`</li><li>Launch this container inside the pod
      `webapp`</li></ol>Launch the WordPress as a container</div><div><ol
      style="text-align: left;"><li>Port should be exposed and able to port
      forward</li></ol>Put both the container inside the pod name
      `webapp`</div><div><b>Note</b>:- The POD name `webapp` is not
      created</div><div><br /><script
      src="https://gist.github.com/Svastikkka/6da89817e0ecad41e1890a64c305499a.js"></script></div><div>Q4
      Write the podman scripts</div><div><ol style="text-align:
      left;"><li>Tag custom localhost&nbsp; JBoss image with this image name
      `workstation.example.com:5000/webapp:v1`</li><li>Push the
      `workstation.example.com:5000/webapp:v1` image to a private registry</li><li>Take
      a backup and save it in tar format in /tmp/w.tar
      folder.</li></ol><div><br /><script
      src="https://gist.github.com/Svastikkka/2c2882dabd8bc3c87bbbb2106c8cc5a3.js"></script></div></div>

Write your content here...