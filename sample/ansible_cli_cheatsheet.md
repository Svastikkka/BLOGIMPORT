# Ansible CLI cheatsheet

Published: 2021-04-21T01:56:00.016+05:30

Description: <div>Hey everyone, I would like to share some of the basic commands
      of ansible as I am practising ansible. Well, it is another helpful tool that describes how
      machines should be configured or what actions should be taken on them
      (systems).&nbsp;</div><div><br /><b>What is
      ansible?</b></div> Ansible
      is&nbsp;<div><ul><li>Cross-platform configuration management
      tool</li><li>An open-source software</li><li>Application deployment
      tool</li><li>An intra-service orchestration
      tool</li></ul><div>Basically, it is a&nbsp;radically simple IT
      automation
      engine.</div></div><div><b>Introduction</b></div>This
      cheat sheet-style guide provides a quick reference to CLI commands which are commonly
      used.<div><b>Glossary</b></div><div><ol><li><b>Node</b>:-
      A system where Ansible is installed and configured to connect to other
      systems.</li><li><b>Inventory File</b>:-&nbsp; A&nbsp;file
      that contains information about the servers Ansible controls, typically located at <span
      style="color: red; font-family:
      courier;">/etc/ansible/hosts</span></li><li><b>Playbook</b>:-
      A&nbsp;YML file containing a series of tasks to be executed on a remote
      server.</li><li><b>Role</b>:- A collection of playbooks and other
      files that are relevant to a goal such as installing a web
      server.</li><li><b>Play</b>:-&nbsp;A play can have several
      playbooks and roles, included from a single playbook that acts as an entry
      point.</li></ol><b>Testing Connectivity to Nodes</b></div>The
      <span style="color: red; font-family: courier;">ping</span> module will test if
      you have valid credentials for connecting to the nodes defined in your inventory
      file<div><ol style="text-align: left;"><li>Check all hosts are able to
      connect by ansible:-<b>&nbsp;</b><span style="color: red; font-family:
      courier;">ansible all -m ping</span></li><li>Check all hosts with a
      particular user is able to connect by ansible:-<span style="color: red; font-family:
      courier;">ansible all -m ping -u svastikkka</span></li><li>Check all
      hosts are able to connect by Ansible with custom
      ssh:-&nbsp;<b>&nbsp;</b><span style="color: red; font-family:
      courier;">ansible all -m ping
      --private-key=~/.ssh/custom_id</span></li><li>Check all hosts are able to
      connect by Ansible with custom&nbsp;password-based
      authentication:-<b>&nbsp;</b><span style="color: red; font-family:
      courier;">ansible all -m ping --ask-pass</span></li><li>If the user needs
      to provide a password in order to run&nbsp;<span style="color: red; font-family:
      courier;">sudo</span>&nbsp;commands:- <span style="color: red; font-family:
      courier;">ansible all -m ping --ask-become-pass</span></li><li>To point a
      Custom Inventory File:-<b>&nbsp;</b><span style="color: red; font-family:
      courier;">ansible all -m ping -i
      MY_CUSTOM_INVENTORY</span></li></ol><div><span style="font-family:
      inherit;">with </span><span style="color: red; font-family:
      courier;">ansible-playbook</span></div><div><ol><li>Check all
      hosts with a particular user is able to connect by ansible:-&nbsp;<span style="color:
      red; font-family: courier;">ansible-playbook MYPLAYBOOK.yml
      -u&nbsp;</span><span style="color: red; font-family:
      courier;">svastikkka</span></li><li>Check all hosts are able to connect
      by Ansible with custom ssh:-&nbsp;<b>&nbsp;</b><span style="color: red;
      font-family: courier;">ansible-playbook MYPLAYBOOK.yml
      --private-key=~/.ssh/custom_id</span></li><li>Check all hosts are able to
      connect by Ansible with custom&nbsp;password-based
      authentication:-<b>&nbsp;</b><span style="color: red; font-family:
      courier;">ansible-playbook MYPLAYBOOK.yml --ask-pass</span></li><li>If
      the user needs to provide a password in order to run&nbsp;<span style="color: red;
      font-family: courier;">sudo</span>&nbsp;commands:- <span style="color: red;
      font-family: courier;">ansible-playbook myplaybook.yml
      --ask-become-pass</span></li><li>To point a Custom Inventory
      File:-<b>&nbsp;</b><span style="color: red; font-family:
      courier;">ansible-playbook MYPLAYBOOK.yml -i&nbsp;</span><span style="color:
      red; font-family:
      courier;">MY_CUSTOM_INVENTORY</span></li></ol></div><b>Running
      ad-hoc Commands</b></div>To execute a command on a node, use the <span
      style="color: red; font-family: courier;">-a </span>option followed by the command
      you want to run in double-quotes.<div><ol style="text-align: left;"><li>Try
      to run&nbsp;<span style="color: red; font-family: courier;">uname
      -a&nbsp;</span>command:- <span style="color: red; font-family:
      courier;">ansible all -a "uname -a</span><span style="color:
      red;">"</span></li><li>Try to run a command that installs the
      package&nbsp;<span style="color: red; font-family: courier;">vim</span> on
      server1&nbsp;from your inventory:-<b>&nbsp;</b><span style="color: red;
      font-family: courier;">ansible server1 -m apt -a
      "name=vim</span></li><li><span style="font-family: inherit;">Try
      to&nbsp;</span>dry run to predict how the systems would be affected by your
      command:-&nbsp;<span style="color: red;"><span style="font-family:
      courier;">ansible server1 -m apt -a "name=vim"
      --check</span></span></li></ol><b>Running
      Playbooks</b></div><ol><li>To run a playbook and execute all the tasks
      defined within it, use the <span style="color: red; font-family:
      courier;">ansible-playbook</span> command:-&nbsp;<span style="color: red;
      font-family: courier;">ansible-playbook MYPLAYBOOK.yml</span></li><li>To
      overwrite the default hosts option in the playbook and limit execution to a certain group or
      host, include the option <span style="color: red; font-family: courier;">-l</span>
      in your command:&nbsp;<span style="color: red; font-family:
      courier;">ansible-playbook -l server1
      MYPLAYBOOK.yml</span></li><li>Getting information about a Play (list all
      tasks that would be executed by a play without making any changes to the remote
      servers):-&nbsp;<span style="color: red; font-family: courier;">ansible-playbook
      MYPLAYBOOK.yml --list-tasks</span></li><li>List all hosts that would be
      affected by a play, without running any tasks on the remote servers:-&nbsp;<span
      style="color: red; font-family: courier;">ansible-playbook MYPLAYBOOK.yml
      --list-hosts</span></li><li>To list all tags available in a play, use the
      option <span style="color: red; font-family:
      courier;">--list-tags</span>:-&nbsp;<span style="color: red; font-family:
      courier;">ansible-playbook myplaybook.yml --list-tags</span></li><li>To
      define a new entry point for your playbook:-&nbsp;Ansible will then skip anything that
      comes before the specified task, executing the remaining of the play from that point on.
      </li><ol><li>Requires a valid task name as argument:-&nbsp;<span
      style="color: red; font-family: courier;">ansible-playbook MYPLAYBOOK.yml
      --start-at-task="Set Up Nginx"</span></li></ol><li>To only execute
      tasks associated with specific tags:-&nbsp;<span style="color: red; font-family:
      courier;">ansible-playbook MYPLAYBOOK.yml
      --tags=mysql,nginx</span></li><li>If you want to skip all tasks that are
      under specific tags:-&nbsp;<span style="color: red; font-family:
      courier;">ansible-playbook MYPLAYBOOK.yml
      --skip-tags=mysql</span></li></ol>

Write your content here...