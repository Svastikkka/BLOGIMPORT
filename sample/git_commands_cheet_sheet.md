# Git Commands Cheet Sheet 

Published: 2020-07-30T13:55:00.011+05:30

Description: <p>This guide includes an introduction to Git, a glossary of terms
      and lists of commonly used Git commands.</p><h3><b>What is Git?
      🤔</b></h3><div>Git gives each developer their own repository containing the
      entire history of changes. More formally&nbsp;Git is a fast, scalable, distributed
      revision control system with an unusually rich command set that provides both high-level
      operations and full access to internals.<br /></div><div><h3
      style="box-sizing: border-box; margin-bottom: 1rem; margin-top: 0px;"><b>Before you
      get started with Git, you need to understand some important
      terms:😀</b></h3><ul><li><b>Commit:-&nbsp;</b>It<b>&nbsp;</b>represents
      a specific point in your project's
      history.</li><li><b>Checkout:-</b>&nbsp;Checkout command to switch
      between
      branches.</li><li><b>Fetch:-&nbsp;</b>Fetch&nbsp;command
      copies and downloads all of a branch's files to your device.<span
      class="Apple-converted-space">&nbsp;</span></li><li><b>Fork:-</b>&nbsp;A
      fork is a copy of a repository. Take a copy of the project for doing some
      changes&nbsp;without affecting your main
      project.</li><li><b>Head:-&nbsp;</b>It represents the most current
      commit of the repository you're currently working in. The commit at the top of a branch is
      called the head.</li><li><b>Index:-&nbsp;</b>Whenever you add,
      delete or alter a file, it remains in the index until you are ready to commit the changes.
      Think of it as the staging area for Git. Use the git status command to see the contents of
      your index. Changes highlighted in green are ready to be committed while those in red still
      need to be added to staging.<h3 class="anchor__location" id="master" style="box-sizing:
      border-box; font-size: 1.75rem; line-height: 1.1; margin-bottom: 0.5rem; margin-top:
      1.5rem;"></h3></li><li><b>Master:-&nbsp;</b>The master is
      the primary branch of all your
      repositories.</li><li><b>Merge:-&nbsp;</b>Use the git merge
      command to add changes from one branch to
      another.</li><li><b>Origin:-&nbsp;</b>Origin refers to the default
      version of a repository. Also serves as a system alias for communicating with the master
      branch. Use the command git push origin master to push local changes to the master
      branch.</li><li><b>Pull:-&nbsp;</b>The git pull command is used to
      add changes from someone's branch to the master
      branch.</li><li><b>Push:-&nbsp;</b>Git<b>&nbsp;</b>push
      command is used to update remote branches with the latest changes you've
      committed.</li><li><b>Rebase:-&nbsp;</b>Rebasing is the process of
      moving or combining a sequence of commits to a new base
      commit.</li><li><b>Remote:-&nbsp;</b>The git remote command lets
      you create, view, and delete connections to other repositories. Remote connections are more
      like bookmarks rather than direct links into other
      repositories.</li><li><b>Repository:-&nbsp;</b>Git repositories
      hold all of your project's files including branches, tags and
      commits.</li><li><b>Stash:-&nbsp;</b>Git&nbsp;stash
      temporarily stashes changes you've made to your working copy so you can work on something
      else, and then come back and re-apply them later
      on.</li><li><b>Tags:-</b>Tagging is generally used to capture a point
      in history that is used for a marked version release (i.e. v1.0.1). A tag is like a branch
      that doesn’t change. Unlike branches, tags, after being created, have no further history of
      commits.</li><li><b>Upstream:-&nbsp;</b>Upstream&nbsp;refers
      to where you push your changes, which is typically the master
      branch.</li><li><b>gitignore</b>:- Specifies untracked files to
      ignore.</li></ul><h3><b>Configuring
      Git&nbsp;</b></h3><ul><li><b>Set the
      username:-&nbsp;</b><font color="#ff0000" face="courier">git config –global
      user.name [name]</font></li><li><b>Set the user
      email:-&nbsp;&nbsp;</b><font color="#ff0000" face="courier">git config
      –global user.email [email]</font></li><li><font
      face="inherit"><b>Create a Git command
      shortcut:-&nbsp;</b></font><font color="#ff0000" face="courier">git
      config –global alias. [alias name] [git
      command]&nbsp;</font></li><li><b>Set the preferred text
      editor:-&nbsp;</b><font color="#ff0000" face="courier">git config –-system
      core.editor [editor name]</font></li><li><b>Open and edit the global
      configuration file in the text editor:-&nbsp;</b><font color="#ff0000"
      face="courier">git config –global –edit</font></li><li><b>Enable
      command line highlighting:-&nbsp;</b><font color="#ff0000" face="courier">git
      config –global color.ui auto</font></li></ul><h3><b>Commands for
      setting up Git repositories</b></h3><div><p style="box-sizing:
      border-box; caret-color: rgb(46, 50, 52); margin-bottom: 1rem; margin-top: 0px;
      text-size-adjust: auto;"></p><ul><li><b>Create an empty repository
      in the project folder:-</b>&nbsp;<font color="#ff0000" face="courier">git
      init</font></li><li><b>Clone a repository from GitHub and add it to
      the project folder:-</b><font color="#ff0000" face="courier">&nbsp;git clone
      [repo URL]</font></li><li><b>Clone a repository to a specific
      folder:-</b>&nbsp;<font color="#ff0000" face="courier">git clone [repo URL]
      [folder]</font></li><li><b>Display a list of remote repositories with
      URLs:-</b>&nbsp;<font color="#ff0000" face="courier">git remote
      -v</font></li><li><b>Remove a remote
      repository:-&nbsp;</b><font color="#ff0000" face="courier">git remote rm
      [remote repo name]</font></li><li><b>Retrieve the most recent changes
      from origin but don't merge:-</b>&nbsp;<font color="#ff0000"
      face="courier">git fetch</font></li><li><b>Retrieve the most recent
      changes from the origin and merge:-<font color="#ff0000"
      face="courier">&nbsp;</font></b><font color="#ff0000"
      face="courier">git pull</font></li></ul><h3>Commands for managing
      file changes</h3><ul><li><b>Add file changes to
      staging:-&nbsp;</b><font color="#ff0000" face="courier">git add
      [filename]</font></li><li><b>Add all directory changes to
      staging:-&nbsp;</b><font color="#ff0000" face="courier">git add
      .</font></li><li><span style="caret-color: rgb(46, 50,
      52);"><b>Add new and modified files to
      staging:-&nbsp;</b></span><br /></li><li><b>Remove a
      file and stop tracking it:-&nbsp;</b><font color="#ff0000" face="courier">git
      rm [file_name]</font></li><li><b>Untrack the current
      file:&nbsp;</b><font color="#ff0000" face="courier">git rm –cached
      [file_name]</font></li><li><b>Recover a deleted file and prepare it
      for commit:&nbsp;</b><font color="#ff0000" face="courier">git checkout
      [deleted file name]</font></li><li><font
      face="inherit"><b>Display the status of modified
      files:&nbsp;</b></font><font color="#ff0000" face="courier">git
      status</font></li><li><b>Display a list of ignored
      files:&nbsp;</b><font color="#ff0000" face="courier">git ls-files –other
      –ignored –exclude-standard</font></li><li><font
      face="inherit"><b>Display all unstaged changes in the index and the current
      directory:&nbsp;</b></font><font color="#ff0000" face="courier">git diff
      SOURCE_BRANCH origin/TARGET_BRANCH&nbsp;
      PATH</font></li><li><b>Display differences between files in staging
      and the most recent versions:&nbsp;</b><font color="#ff0000"
      face="courier">git diff –staged</font></li><li><p style="box-sizing:
      border-box; caret-color: rgb(46, 50, 52); margin-bottom: 1rem; margin-top: 0px;
      text-size-adjust: auto;"><b style="font-size: 16px;">Display changes in a file
      compared to the most recent commit:&nbsp;</b><font color="#ff0000"
      face="courier">git diff
      [file_name]</font></p></li></ul><div><h3>Commands for
      declaring Git commits</h3><div><ul><li><span
      style="background-color: white; caret-color: rgb(46, 50, 52); font-size: 16px;
      text-size-adjust: auto;"><font face="inherit"><b>Commit changes along with a
      custom message:&nbsp;</b></font></span><font color="#ff0000"
      face="courier">git commit -m "[message]"</font></li><li><font
      face="inherit"><b>Commit and add all changes to
      staging:&nbsp;</b></font><font color="#ff0000" face="courier">git commit
      -am "[message]"</font></li><li><font face="inherit"><b>Switch to
      a commit in the current branch:&nbsp;</b></font><font color="#ff0000"
      face="courier">git checkout [commit]</font></li><li><font
      face="inherit"><b>Show metadata and content changes of a
      commit:&nbsp;</b></font><font color="#ff0000" face="courier">git show
      [commit]</font></li><li><font face="inherit"><b>Discard all
      changes to a commit:&nbsp;</b></font><font color="#ff0000"
      face="courier">git reset –hard [commit]</font></li><li><font
      face="inherit"><b>Discard all local changes in the
      directory:&nbsp;</b></font><font color="#ff0000" face="courier">git
      reset –hard Head</font></li><li><font face="inherit"><b>Show the
      history of changes:&nbsp;</b></font><font color="#ff0000"
      face="courier">git log</font></li><li><font
      face="inherit"><b>Stash all modified files:&nbsp;</b></font><font
      color="#ff0000" face="courier">git stash</font></li><li><b>Retrieve
      stashed files:&nbsp;</b><span style="color: red; font-family: courier;">git
      stash pop</span></li><li><span style="font-family:
      inherit;"><b>Empty stash:&nbsp;</b></span><span style="color: red;
      font-family: courier;">git stash drop</span></li><li><b><span
      style="font-family: inherit;">Define a tag:</span><span style="color: red;
      font-family: courier;">&nbsp;</span></b><span style="color: red;
      font-family: courier;">git tag [tag_name]</span></li><li><span
      style="font-family: inherit;"><b>Push changes to
      origin:&nbsp;</b></span><span style="color: red; font-family:
      courier;">git push</span></li></ul><h3><span style="font-family:
      inherit;"><span style="background-color: white; caret-color: rgb(46, 50,
      52);">Commands for Git
      branching</span></span></h3></div><div><ul><li><span
      style="font-family: inherit;"><span style="background-color: white; caret-color: rgb(46,
      50, 52); font-weight: 600;">Push all local branches to a designated remote
      repository:&nbsp;</span></span><span style="color: red; font-family:
      courier;">git push –all</span></li><li><span style="font-family:
      inherit;"><b>Preview changes before merging
      branches:&nbsp;</b></span><span style="color: red; font-family:
      courier;">git diff
      [sourcebranch][targetbranch]</span></li><li><b>Fetch a branch from the
      repository:&nbsp;</b><span style="color: red; font-family: courier;">git fetch
      remote [branchname]</span></li><li><b style="font-family:
      inherit;">Merge a different branch with your active branch:&nbsp;</b><span
      style="color: red; font-family: courier;">git merge
      [branchname]</span></li><li><b>Delete a
      branch:&nbsp;</b><span style="color: red; font-family: courier;">git branch -d
      [branchname]</span></li><li><span style="font-family:
      inherit;"><b>Switch to a branch:&nbsp;</b></span><span
      style="color: red; font-family: courier;">git checkout
      [branchname]</span></li><li><span style="font-family:
      inherit;"><b>Make a new branch and switch to
      it:&nbsp;</b></span><span style="color: red; font-family: courier;">git
      checkout -b [branchname]</span></li><li><span style="font-family:
      inherit;"><b>Display a list of all branches:&nbsp;</b></span><span
      style="color: red; font-family: courier;">git
      branch</span></li></ul></div><h3><span style="font-family:
      inherit;">Reference</span></h3></div></div><div><a
      href="https://www.atlassian.com/git/tutorials">https://www.atlassian.com/git/tutorials</a></div></div><div><a
      href="https://git-scm.com/docs">https://git-scm.com/docs</a></div><div>KeyCDN</div><div><br
      /></div><div><b>Note</b>:- In this post, there is only one thing
      left which is explaining by example. Soon I will also add that thing too.</div>

Write your content here...