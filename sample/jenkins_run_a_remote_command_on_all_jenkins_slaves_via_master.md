# Jenkins :- Run a remote command on all Jenkins slaves via Master

Published: 2021-09-05T13:18:00.012+05:30

Description: <div class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-0rOzdtWU4zg/YTR_J6GkmSI/AAAAAAAAAXs/Esv1zkecKf4c747WynBqV95NjoPGtag5gCNcBGAsYHQ/s500/logo.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="500"
      data-original-width="500" height="320"
      src="https://1.bp.blogspot.com/-0rOzdtWU4zg/YTR_J6GkmSI/AAAAAAAAAXs/Esv1zkecKf4c747WynBqV95NjoPGtag5gCNcBGAsYHQ/s320/logo.png"
      width="320" /></a></div><div class="separator" style="clear: both;
      text-align: left;">Hi everyone 😀, Today I want to share a solution related to run a common
      command in all slave nodes via the master node in Jenkins using the Jenkins pipeline. I also
      faced a similar issue before where I had to run docker related commands in all nodes. The
      approach is simple&nbsp;</div><p>First, we need to define an agent in our
      Jenkins pipeline.</p><div class="separator" style="clear: both; text-align:
      center;"><a
      href="https://1.bp.blogspot.com/-PtKNjBZEqmY/YTRuIDpZWRI/AAAAAAAAAW8/frmdsDmDOQ8iXaQtbp4GUJ_owzlQfB2ygCNcBGAsYHQ/s1116/Screen%2BShot%2B2021-09-05%2Bat%2B12.32.27%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="23"
      data-original-width="1116" height="6"
      src="https://1.bp.blogspot.com/-PtKNjBZEqmY/YTRuIDpZWRI/AAAAAAAAAW8/frmdsDmDOQ8iXaQtbp4GUJ_owzlQfB2ygCNcBGAsYHQ/w320-h6/Screen%2BShot%2B2021-09-05%2Bat%2B12.32.27%2BPM.png"
      width="320" /></a></div><p>Second, we need to define two stages first one
      for the master (optional) and the second one are for slaves.</p><div
      class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-wfOlb0yfgGE/YTRxDNeBMZI/AAAAAAAAAXE/xb5mJevexwwjNqlOV3hVzxpx63qxlztIACNcBGAsYHQ/s926/Screen%2BShot%2B2021-09-05%2Bat%2B12.55.10%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="403"
      data-original-width="926" height="140"
      src="https://1.bp.blogspot.com/-wfOlb0yfgGE/YTRxDNeBMZI/AAAAAAAAAXE/xb5mJevexwwjNqlOV3hVzxpx63qxlztIACNcBGAsYHQ/w320-h140/Screen%2BShot%2B2021-09-05%2Bat%2B12.55.10%2BPM.png"
      width="320" /></a></div><p>Third, we need some built-in
      functions</p><p></p><ul style="text-align: left;"><li><span
      style="color: red; font-family:
      courier;">jenkins.model.Jenkins.instance.getNodes()</span>:-&nbsp; Returns all
      <a href="https://javadoc.jenkins-ci.org/hudson/model/Node.html">Node</a>s in the
      system, excluding <a
      href="https://javadoc.jenkins-ci.org/jenkins/model/Jenkins.html">Jenkins</a> instance
      itself which represents the built-in node</li><li><span style="color: red;
      font-family: courier;">slave.toComputer().isOnline()</span><span
      style="font-family: inherit;">:-&nbsp; To check slave node is
      online</span></li><li><span style="color: red; font-family:
      courier;">getDisplayName()</span><span style="font-family:
      inherit;">:-&nbsp; To get the name of the slave
      node</span></li></ul><div>thereafter we create a user-define function
      and in this,&nbsp; we define two loops first one for getting all names of slave nodes and
      the second one is to define a&nbsp;node-block that is capable of executing commands in the
      slave nodes. The function will look something like in the given below:-</div><div
      class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-M7hA2FSD_XY/YTR0F9HSaJI/AAAAAAAAAXQ/IGBuWzkQAjEbj1t8TGP9ihautiDN4GcJACNcBGAsYHQ/s931/Screen%2BShot%2B2021-09-05%2Bat%2B1.04.58%2BPM.png"
      style="margin-left: 1em; margin-right: 1em;"><span style="color: red;"><img
      border="0" data-original-height="481" data-original-width="931" height="166"
      src="https://1.bp.blogspot.com/-M7hA2FSD_XY/YTR0F9HSaJI/AAAAAAAAAXQ/IGBuWzkQAjEbj1t8TGP9ihautiDN4GcJACNcBGAsYHQ/w320-h166/Screen%2BShot%2B2021-09-05%2Bat%2B1.04.58%2BPM.png"
      width="320" /></span></a></div><div><br /></div>Full
      code is given below<br /><div><br /></div><div><br
      /></div><script
      src="https://gist.github.com/Svastikkka/035a10063b6addbd5143b58d12a7c51d.js"></script><div
      style="text-align: center;">Hope you enjoyed my blog post.
      😎</div><p></p>


Write your content here...