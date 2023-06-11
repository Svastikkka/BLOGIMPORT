# Setup MongoDB statefulset on AWS Fargate

Published: 2022-02-20T10:23:00.008+05:30

Description: Hi everyone I am Manshu Sharma and today we will see how can we deploy the
      mongoDB on AWS fargate as a&nbsp;<a
      href="https://www.blogger.com/#">statefulset</a>&nbsp;with help of the mongoDB
      community operator but before we start let's have a quick overview of two important terms
      <b>statefulset,</b>&nbsp;<b>stateful
      application</b>.<div><br /><div>What actually statefulset is in
      Kubernetes?</div>StatefulSet is a Kubernetes resource used to manage stateful
      applications and It manages the <b>scaling</b>, <b>ordering</b> and
      <b>uniqueness</b> of each pod. It requires headless service and we are responsible
      for creating this service.<br /><br />What actually is stateful
      applications?</div>Stateful applications are those programs that save client data from
      the activities of one session for use in the next session. Consider it as an ongoing periodic
      conversation with the same person. Some examples of stateful applications are
      <b>MySQL,</b>&nbsp;&nbsp;<b>MongoDB,</b> <b>FTP
      server,&nbsp; Redis Cache, Kafka&nbsp;</b>and&nbsp;any Login service that
      stores client authentication data on the server, labelling clients as having a “connected” or
      “disconnected” state. It also stores information about previous requests from the same
      client.<div><br /></div><div>A diagrammatical representation of
      Kubernetes statefulset resource.</div><div class="separator" style="clear: both;
      text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/a/AVvXsEgEL6WhSoHIL7xjZqyujYn5pDpuuWmSAFykfSnQBjqrIVIwByuuoMW1xHOvw6y59IG_o7WCpp-QlMWlvTFmuzpJ9MU2eE1Kc07JwbVqnVfBxiEAf2EDsdmnRehar3F9LBuTMTPQVmIA3Gt25rIBLc99acZeJbyWGnco-oV8oWBpY8AUFaHIkDNJ5rHt=s996"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="996"
      data-original-width="938" height="320"
      src="https://blogger.googleusercontent.com/img/a/AVvXsEgEL6WhSoHIL7xjZqyujYn5pDpuuWmSAFykfSnQBjqrIVIwByuuoMW1xHOvw6y59IG_o7WCpp-QlMWlvTFmuzpJ9MU2eE1Kc07JwbVqnVfBxiEAf2EDsdmnRehar3F9LBuTMTPQVmIA3Gt25rIBLc99acZeJbyWGnco-oV8oWBpY8AUFaHIkDNJ5rHt=s320"
      width="301" /></a></div><div>In the above diagram, we can see that there
      is one headless service for routing and two statefulset pods with different PVC and PV
      resources. Each resource has its own different session and has a completely different isolated
      environment.</div><div><br /></div>Overview completed. Now let's see
      the setup of the mongoDB application as a statefulset using MongoDB community
      operator.<div><br /></div><b>Installation</b><br />The
      MongoDB Community Kubernetes Operator allows you to deploy secure MongoDB Replica Sets in your
      Kubernetes cluster.<div style="text-align: left;"><ul style="text-align:
      left;"><li>Before we can deploy MongoDB, we need to ensure that we have created the
      required CustomResourceDefinition.</li><ul><li><span style="color:
      red;">kubectl apply -f
      https://raw.githubusercontent.com/mongodb/mongodb-kubernetes-operator/master/config/crd/bases/mongodbcommunity.mongodb.com_mongodbcommunity.yaml</span></li></ul></ul></div><ul
      style="text-align: left;"><li>Create a namespace for our
      deployment.</li><ul><li><span style="color: red;">kubectl create
      namespace mongodb</span></li></ul><li>Install the latest version of
      the operator.</li><ul><li><span style="color: red;">kubectl apply -f
      https://raw.githubusercontent.com/mongodb/mongodb-kubernetes-operator/master/config/crd/bases/mongodbcommunity.mongodb.com_mongodbcommunity.yaml</span></li></ul><li>Add
      authorizations.</li><br /><ul><li><span style="color:
      red;">kubectl apply -f
      https://raw.githubusercontent.com/mongodb/mongodb-kubernetes-operator/master/config/rbac/role_binding.yaml&nbsp;</span></li><li><span
      style="color: red;">kubectl apply -f
      https://raw.githubusercontent.com/mongodb/mongodb-kubernetes-operator/master/config/rbac/service_account.yaml</span></li><li><span
      style="color: red;">kubectl apply -f
      https://raw.githubusercontent.com/mongodb/mongodb-kubernetes-operator/master/config/rbac/role.yaml</span></li></ul></ul>Congratulation
      we have successfully set up our mongoDB community operator.<br
      /><div><b>Note</b>: This above operation requires cluster-admin
      permissions.<br /><div><ol start="2" style="-webkit-font-smoothing:
      subpixel-antialiased; background-color: #f5f6f7; box-sizing: border-box; color: #42494f;
      font-family: &quot;Akzidenz Grotesk BQ Light&quot;, Helvetica; font-size: 16px;
      padding-left: 30px;"></ol></div></div><b>Deploying a SCRAM Enabled
      Replica Set</b><br /><div><b><br /></b></div>MongoDB
      community operator creates secure SCRAM-SHA-256 enabled deployments by default. This means
      that we need to define our users and what roles we want them to have, alongside a set of
      credentials for the user to use.<div>We can create the user's credentials in the form of
      a Kubernetes Secret</div><ul style="text-align: left;"><li><span
      style="color: red;">kubectl create secret generic my-mongodb-user-password -n mongodb
      --from-literal="admin-password=TXs3ZsuIqT-pQFvwxOec" </span></li></ul>Once
      we have created the secret, we can deploy a MongoDB replica set but wait✋ without persistent
      volumes the data will not be retained permanently and so as fargate supports efs csi driver we
      are going to use it as our persistent volume support. For this, we going to create two
      resources multiple times which are persistent volume and persistent volume claim. We also need
      to install <a href="https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html"
      target="_blank">AWS EFS CSI DRIVER</a>&nbsp;in our eks and storage class. Here
      below is the full code which will deploy storage class, PV and PVC.<div><script
      src="https://gist.github.com/Svastikkka/e52e8cf84d469372e52b66ca8d022dcc.js"></script></div><div><br
      /></div><div>Once we have created our PV and PVC we are now ready to
      deploy&nbsp;MongoDBCommunity statefulset</div><div><div><script
      src="https://gist.github.com/Svastikkka/f57eb66c26fdfb32007d9ec3ec758b71.js"></script><br
      /><div><br /></div></div></div><div><br
      /></div>

Write your content here...