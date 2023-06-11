# Helm Commands Cheatsheet

Published: 2022-12-05T17:04:00.117+05:30

Description: <p></p><div><div>Hi everyone😎, Sharing helm
      commands that I use day to day.<br /><br />helm create:</div><div>This
      command creates a chart directory along with the common files and directories used in a
      chart.</div><div><ol style="text-align: left;"><li>Create a new chart
      with the given name:-&nbsp;<span style="color: red;">helm create
      [CHART]</span></li></ol><div><span></span><span><a
      name='more'></a></span><span style="color: red;"><br
      /></span></div>helm install:&nbsp;</div></div><div>This
      command installs a chart in a cluster.<br /><ol style="text-align:
      left;"><li>Install particular service using
      helm:-&nbsp;</li><ul><li><span style="color: red;">helm install
      [</span><span style="color: red;">RELEASE_NAME]
      [CHART]</span></li></ul><li>Install chart in particular
      namespace:-</li><ul><li><span style="color: red;">helm install
      [</span><span style="color: red;">RELEASE_NAME] [CHART] --namespace
      [NAMESPACE]</span></li></ul><li>Override the default values with those
      specified in a file of your choice:-</li><ul><li><span style="color:
      red;"><span>helm install [</span><span>RELEASE_NAME] [CHART] --namespace
      [NAMESPACE]&nbsp;</span>--values
      [yaml-file/url]</span></li></ul><li>Dry run helm chart:-&nbsp;
      <span style="color: red;">helm install [RELEASE_NAME] [CHART]
      --dry-run</span></li><li>Install in verbose mode:-<span style="color:
      red;"> helm install [RELEASE_NAME] [CHART]
      --debug</span></li><li><span>S</span>et values on the command:-
      <span style="color: red;">helm install [RELEASE_NAME] [CHART] --set
      [KEY]=[VALUE]</span></li></ol><div><span><!--more--></span>helm
      lint:</div><div>This command takes a path to a chart and runs a series of tests to
      verify that the chart is well-formed.</div><div><ol style="text-align:
      left;"><li>Examine a chart for possible issues:- <span style="color: red;">helm
      lint [CHART]</span></li></ol><div>helm list:</div>This command
      lists all of the releases for a specified namespace<br /><ol style="text-align:
      left;"><li>List releases:-&nbsp;<span style="color: red;">helm list
      [FLAG]&nbsp; </span>or<span style="color: red;">&nbsp;helm ls
      [FLAG]&nbsp;</span></li></ol><!--more--><div><br
      /></div></div><div>helm uninstall:</div></div><div>This
      command takes a release name and uninstalls the
      release.</div><div><div><ol><li>Uninstall deployed
      release:-&nbsp;<span style="color: red;">helm uninstall
      [RELEASE_NAME]</span></li><li><span>Uninstall deployed
      release&nbsp;in specific namespace:-</span><span style="color:
      red;">&nbsp;</span><span style="color: red;">helm uninstall [RELEASE_NAME]
      --namespace
      [NAMESPACE]</span></li></ol><div><span><!--more--></span><span
      style="color: red;"><br /></span></div><div>helm
      upgrade:</div>This command upgrades a release to a new version of a
      chart.</div><div><ol><li>Upgrade a release:- <span style="color:
      red;">helm upgrade [RELEASE_NAME] [CHART]</span></li><li>Upgrade a
      release by overriding the values with those specified in the file:- <span style="color:
      red;">helm upgrade [RELEASE_NAME] [CHART]</span></li><li>Upgrade a
      release. If it does not exist on the system, install it:- <span style="color: red;">helm
      upgrade [RELEASE_NAME] [CHART] --install</span></li><li>Upgrade to a
      specified version:- <span style="color: red;">helm upgrade [RELEASE_NAME] [CHART]
      --version
      [VERSION-NUMBER]</span></li></ol><span><!--more--></span><div><br
      /></div><div>helm repo:</div><div>This command is used to add,
      remove, list, and index chart repositories.<br
      /></div></div><div><ol style="text-align: left;"><li>Add a
      chart repository:-&nbsp;<span style="color: red;">helm repo add
      [URL]</span></li><li>Update information of available charts locally from
      chart repositories:- <span style="color: red;">helm repo
      update</span></li><li>List chart repositories:- <span style="color:
      red;">helm repo
      list</span></li></ol></div><div><div><!--more--><br
      /></div></div><div>helm rollback:</div><div><div>This
      command rolls back a release to a previous revision.</div><ol style="text-align:
      left;"><li><span>Roll back a release to a previous revision:-
      </span><span style="color: red;">helm rollback [RELEASE_NAME]
      [REVISION]</span></li></ol></div></div><div><span><!--more--></span><b><br
      /></b></div><div>helm search:</div><div>Search provides the
      ability to search for Helm charts in the various places they can be stored including the
      Artifact Hub and repositories we have added.</div><ol style="text-align:
      left;"><li>Search for charts in the Artifact Hub or your own hub
      instance:-&nbsp;<span style="color: red;">helm search hub [KEYWORD]
      [flags]</span></li><li>Search repositories for a keyword in charts:-
      <span style="color: red;">helm search repo&nbsp;[KEYWORD</span><span
      style="color: red;">]</span>&nbsp;</li></ol><div
      style="text-align: center;">Hope you like my blog post</div><p></p>

Write your content here...