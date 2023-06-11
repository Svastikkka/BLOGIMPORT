# Create a custom AMI with default 6GIB minimum EBS volume size

Published: 2021-04-12T00:47:00.002+05:30

Description: <p>Hey everyone, Today I would like to share another interesting post
      related to AWS AMI. Those who don't know about Amazon AMI you visit this&nbsp;<a
      href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html" target="_blank">Amazon
      Machine Images (AMI)</a>. In this post, we will see how to create a custom AMI (our own
      personal AMI) with a minimum EBS volume size of 6 GIB. To create a custom AMI we first need to
      create an EC2 instance. The specifications of our instances are as
      follows:</p><p></p><ol style="text-align: left;"><li>OS type
      Amazon Linux 2</li><li>Volume size 8GIB (Minimum size that amazon
      allows)</li><li>Tag with Key: Name and value:
      <b>MyInstance</b></li></ol><div>So after creating our ec2
      instance, we need to follow the following instructions:</div><ol style="text-align:
      left;"><li>First, Shut down the instance (<b>MyInstance</b>) to prevent
      any problem.</li><li>Create a new 6GIB EBS
      volume.</li><ol><li>Go to Elastic Block Store
      Volumes</li><li>Click Create Volume</li><li>Choose the same volume
      type same with your old volume</li><li>Enter your desired size; In our case
      6Gib</li><li>Choose availability zone; The volume will be available to an instance
      in the same availability zone.</li><li>Add a tag with Key: Name and value:
      NewVolume6Gib</li></ol><li>Attach the new volume
      (<b>myVolume</b>)</li><ol><li>Right-click on the new volume
      (<b>myVolume</b>).</li><li>Click Attach
      Volume.</li><li>Choose instance, select
      <b>MyInstance.</b></li><li>Click
      Attach.</li></ol><li>Format the volume
      (optional)</li><ol><li>&nbsp;Just to check whether the volume has any
      data by using command&nbsp;<span style="color: red; font-family: courier;">sudo file
      -s /dev/xvdf</span><span style="font-family:
      inherit;">.</span></li><li>If it is displaying <span style="color:
      red; font-family: courier;">/dev/xvdf: data</span>, it means the volume is empty. We
      could format the volume.</li><li>If it is displaying any other thing except the
      above output, it means the volume have data.&nbsp;</li><li>If you want to
      format the volume you can use the command&nbsp;<span style="color: red; font-family:
      courier;">sudo mkfs -t ext4 /dev/xvdf</span>.</li></ol><li>Mount
      the new volume (<b>myVolume</b>)</li><ol><li>Create a directory
      to mount using the command <span style="color: red; font-family: courier;">sudo
      mkdir</span> <span style="background-color: white; color: red; font-family:
      courier;">/mnt/myVolume</span></li><li>Mount new volume
      (<b>myVolume</b>)&nbsp;&nbsp;into a directory using command <span
      style="color: red; font-family: courier;">sudo mount /dev/xvdf /<span
      style="background-color: white;">mnt</span>/</span><span style="color: red;
      font-family: courier;">myVolume</span>&nbsp;</li><li>Check volume by
      using command <span style="color: red; font-family: courier;">df
      -h&nbsp;</span>The new volume (<b>myVolume</b>)&nbsp;should be
      mounted now.</li></ol><li>Copy data from the old volume to the new volume
      (<b>myVolume</b>)</li><ol><li>Use <span style="color: red;
      font-family: courier;">rysnc</span> to copy from old volume to the new volume
      (<b>myVolume</b>)&nbsp;<span style="color: red; font-family:
      courier;">sudo rsync -axv / /mnt/myVolume/</span><span style="font-family:
      inherit;">.</span></li><li>Wait until it’s finished.
      ✋</li></ol><li>Install GRUB&nbsp;</li><ol><li>Install
      grub on&nbsp;<span style="color: red; font-family:
      courier;">myVolume</span>&nbsp;using command <span style="color: red;
      font-family: courier;">sudo grub2-install --root-directory=/mnt/myVolume/ --force
      /dev/xvdf</span><span style="font-family:
      inherit;">.</span></li><li>Unmount&nbsp;<span style="color: red;
      font-family: courier;">myVolume,&nbsp;</span>&nbsp;<span style="color:
      red; font-family: courier;">sudo umount&nbsp;</span><span style="color: red;
      font-family: courier;">/mnt/myVolume</span></li><li>Check UUID using
      command <span style="color: red; font-family:
      courier;">blkid</span></li><li>Copy UUID of
      <b>/dev/xvda1</b>.&nbsp;</li><li>Use <span style="font-family:
      inherit;"><b>tune2fs</b></span> to replace UUID <span style="color:
      red; font-family: courier;">sudo tune2fs -U COPIED_UUID
      /dev/xvdf</span></li><li>Check label by using the following command <span
      style="color: red; font-family: courier;">sudo lsblk -o name, mountpoint, label, size,
      uuid</span></li><li>Replace&nbsp;<b><span style="font-family:
      inherit;">myVolume</span></b>&nbsp;label with old-volume label using
      command <span style="color: red; font-family: courier;">sudo e2label /dev/xvdf
      cloudimg-rootfs</span></li><li>Log out from the instance and shut it
      down.</li></ol><li>Detach old volume and attach the new volume
      (<b>myVolume</b>)</li><ol><li>Detach&nbsp;<b>old
      volume</b></li><li>Detach new volume (<b><span style="font-family:
      inherit;">myVolume</span></b>)</li><li>Attach new volume
      (<b>myVolume</b>) to
      <b>/dev/xvda</b></li><li>Start&nbsp;&nbsp;<b>MyInstance&nbsp;</b>instance,
      you see an instance is now running with 6GIB EBS volume
      size.</li></ol><li>Create a custom AMI</li><ol><li>To
      create an AMI from an instance,&nbsp;Right-click the instance you want to use as the basis
      for your AMI, and choose to&nbsp;<b>Create Image</b> from the context
      menu.&nbsp;</li><li>In the Create Image dialogue box, type a unique name and
      description, and then choose Create Image.&nbsp;<div class="separator" style="clear:
      both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-3E6PjVhYsUw/YHNLDaa7nYI/AAAAAAAAAVc/AqafW9IGPwYLqLHRvpsvOzo-1AAgYctpACNcBGAsYHQ/s1440/Screen%2BShot%2B2021-04-11%2Bat%2B11.50.10%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="689"
      data-original-width="1440"
      src="https://1.bp.blogspot.com/-3E6PjVhYsUw/YHNLDaa7nYI/AAAAAAAAAVc/AqafW9IGPwYLqLHRvpsvOzo-1AAgYctpACNcBGAsYHQ/s320/Screen%2BShot%2B2021-04-11%2Bat%2B11.50.10%2BAM.png"
      width="320" /></a></div><br /></li><li>It may take a few
      minutes for the AMI to be created. After it is created, it will appear in the AMIs view in AWS
      Explorer.<div class="separator" style="clear: both; text-align: center;"><a
      href="https://1.bp.blogspot.com/-0JYi1CMCsdQ/YHNK0A54S4I/AAAAAAAAAVY/1dMHhSa_bH8X0w3pilbFnLl8jGUui-lnwCNcBGAsYHQ/s1440/Screen%2BShot%2B2021-04-11%2Bat%2B11.51.04%2BAM.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="377"
      data-original-width="1440"
      src="https://1.bp.blogspot.com/-0JYi1CMCsdQ/YHNK0A54S4I/AAAAAAAAAVY/1dMHhSa_bH8X0w3pilbFnLl8jGUui-lnwCNcBGAsYHQ/s320/Screen%2BShot%2B2021-04-11%2Bat%2B11.51.04%2BAM.png"
      width="320" /></a></div><br /></li></ol></ol><div
      style="text-align: center;"><br /></div><div style="text-align:
      center;"><br /></div><div style="text-align: center;"><br
      /></div><div style="text-align: center;"><br /></div><div
      style="text-align: center;"><br /></div><div style="text-align:
      center;"><br /></div><div style="text-align: center;"><br
      /></div><div style="text-align: center;">Hope you enjoyed my blog
      post.😎</div><div style="text-align: center;">Let me know in the comments below if
      you face any problem.</div><p></p>

Write your content here...