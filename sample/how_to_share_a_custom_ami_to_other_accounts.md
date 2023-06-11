# How to share a custom AMI to other accounts

Published: 2021-10-23T14:14:00.003+05:30

Description: <p>Hi everyone 🙂, I am Manshu Sharma and today we are going to
      discuss an interesting topic that will help us to share custom private AMI in all accounts
      &amp; regions. In this post first, create a custom encrypted AMI from the public AMI, and
      then share the custom AMI with encrypted EBS snapshots across accounts and regions. This
      approach allows you to launch Amazon EC2 instances globally from multiple accounts by using
      the same base-encrypted AMI.
      </p><p><b>Requirments</b></p><p></p><ol
      style="text-align: left;"><li>We need two AWS accounts i.e SourceAccount &amp;
      DestinationAccount</li><li>Have a basic knowledge of AWS
      services</li><li>SourceAccount:- In which you build a custom AMI and encrypt the
      associated EBS snapshots.</li><li>DestinationAccount:- In which you launch
      instances using the shared custom AMI with encrypted
      snapshots.</li></ol><div><b>Note</b>:- While writing this blog
      post I am considering two imaginary AWS account ids&nbsp;<span style="color: red;
      font-family: courier;">111111111111</span>&nbsp; with region <span
      style="color: red; font-family: courier;">us-east-1</span> for&nbsp;
      SourceAccount &amp; <span style="color: red; font-family:
      courier;">999999999999</span>&nbsp; with <span style="color: red; font-family:
      courier;">us-east-1</span> for DestinationAccount so be sure you replace this account
      id with your original account id.</div><div><br
      /></div><div><b>Start with
      SourceAccount</b></div><div>In the SourceAccount,&nbsp; We first going
      to create&nbsp; <a
      href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html"
      target="_blank">AWS CMK&nbsp;</a>&amp; call it <span style="color:
      red;">cmkSource. </span><span>Remember while creating <span style="color:
      red;">cmkSource</span> you also need to give the AWS DestinationAccount id in the
      "<b>Others AWS account</b>" section.</span></div><div><div
      class="separator" style="clear: both; text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/a/AVvXsEjKYUqJQV7F3KRDNjX0dmKnB8-A58iHMJmQJVaOMUa2rYJzUZ-5FhGe4041VjG_sUzD4QTFKHP48Xjo5QZxO043uDIco-MS8iR9DlOjUEje1aTmohsNrIvCo9bITIqVBo4ZOHBXDNHCoO7gx91f8hoJ0Zio7G8ZAQA3FRkvdCjr1fCWPtsMmKF4Vz97=s637"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="637"
      data-original-width="493" height="320"
      src="https://blogger.googleusercontent.com/img/a/AVvXsEjKYUqJQV7F3KRDNjX0dmKnB8-A58iHMJmQJVaOMUa2rYJzUZ-5FhGe4041VjG_sUzD4QTFKHP48Xjo5QZxO043uDIco-MS8iR9DlOjUEje1aTmohsNrIvCo9bITIqVBo4ZOHBXDNHCoO7gx91f8hoJ0Zio7G8ZAQA3FRkvdCjr1fCWPtsMmKF4Vz97=s320"
      width="248" /></a></div><br /><span>Thereafter we create an IAM
      policy for&nbsp;</span>the&nbsp;<span style="color:
      red;">cmkSource</span>. This delegate permission to the SourceAccount. I call it
      <span style="color: red;">cmkSourcePolicy.</span></div><div><pre
      style="background-color: #f7f7f7; border-radius: 0px; border: 1px solid rgb(247, 247, 247);
      box-sizing: border-box; color: #333333; font-size: 14px; overflow: auto; padding: 15px 0px
      15px 15px;"><span style="font-family: Consolas, Andale Mono WT, Andale Mono, Lucida
      Console, Lucida Sans Typewriter, DejaVu Sans Mono, Bitstream Vera Sans Mono, Liberation Mono,
      Nimbus Mono L, Monaco, Courier New, Courier, monospace;">{
      "Version": "2012-10-17",
      "Statement": [
      {
      "Effect": "Allow",
      "Action": [
      "kms:ReEncrypt*",
      "kms:GenerateDataKey*",
      "kms:CreateGrant",
      "kms:DescribeKey*"
      ],
      "Resource": [
      "arn:aws:kms:us-east-1:</span><span style="box-sizing: border-box; color: red;
      font-family: Consolas, &quot;Andale Mono WT&quot;, &quot;Andale Mono&quot;,
      &quot;Lucida Console&quot;, &quot;Lucida Sans Typewriter&quot;,
      &quot;DejaVu Sans Mono&quot;, &quot;Bitstream Vera Sans Mono&quot;,
      &quot;Liberation Mono&quot;, &quot;Nimbus Mono L&quot;, Monaco,
      &quot;Courier New&quot;, Courier, monospace;"><span face="AmazonEmberBold,
      &quot;Helvetica Neue Bold&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial,
      sans-serif" style="box-sizing: border-box;">111111111111</span></span><span
      style="font-family: Consolas, Andale Mono WT, Andale Mono, Lucida Console, Lucida Sans
      Typewriter, DejaVu Sans Mono, Bitstream Vera Sans Mono, Liberation Mono, Nimbus Mono L,
      Monaco, Courier New, Courier, monospace;">:</span><span style="box-sizing:
      border-box; color: red;"><span style="font-family: Consolas, Andale Mono WT, Andale
      Mono, Lucida Console, Lucida Sans Typewriter, DejaVu Sans Mono, Bitstream Vera Sans Mono,
      Liberation Mono, Nimbus Mono L, Monaco, Courier New, Courier,
      monospace;">key/</span><span face="AmazonEmber, Helvetica Neue, Helvetica, Arial,
      sans-serif"><i>KEYID OF cmkSource</i></span></span><span
      style="font-family: Consolas, Andale Mono WT, Andale Mono, Lucida Console, Lucida Sans
      Typewriter, DejaVu Sans Mono, Bitstream Vera Sans Mono, Liberation Mono, Nimbus Mono L,
      Monaco, Courier New, Courier, monospace;">"
      ]
      },
      {
      "Effect": "Allow",
      "Action": [
      "kms:ListKeys",
      "kms:ListAliases"
      ],
      "Resource": [
      "*"
      ]
      },
      {
      "Effect": "Allow",
      "Action": [
      "ec2:RunInstances",
      "ec2:StartInstances",
      "ec2:CreateImage",
      "ec2:CopyImage",
      "ec2:ModifySnapshotAttribute",
      "ec2:CreateSecurityGroup",
      "ec2:AuthorizeSecurityGroupIngress",
      "ec2:Describe*"
      ],
      "Resource": [
      "*"
      ]
      }
      ]
      }</span></pre></div><div><span style="color: red;"><br
      /></span></div><div><b>In the
      DestinationAccount</b></div><div>Now in the DestinationAccount&nbsp;IAM
      user or role in the DestinationAccount&nbsp;needs permission to create an AMI.
      </div><div>So similarly we need to create&nbsp;&nbsp;<a
      href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html"
      target="_blank">AWS CMK&nbsp;</a>&nbsp;&amp; call it&nbsp;<span
      style="color: red;">cmkTarget.&nbsp;</span></div><div><span
      style="color: red;"><br
      /></span></div><div><span><b>Note</b>:- This
      time&nbsp;</span>you don't need to give the AWS DestinationAccount id in the
      "<b>Others AWS account</b>" section.</div><div><span style="color:
      red;"><br /></span></div><div><div class="separator"
      style="clear: both; text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/a/AVvXsEjaofJaxyAc0EkiWhRdM7pYR7zJu7qIhKuEU7a8oV_JIa41JGeQnA9qBfgwuMtNfv6VX6Zg4K6elkdth-XTfbygpKsQ44etnudmKuIF7vBYDXmievZFMNJBTe38R638K74dwku8VoWvl4DI7cL55jRR1hIGUon9IKJBQLVevYt-flWXJyMMMGml9r51=s477"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="430"
      data-original-width="477" height="288"
      src="https://blogger.googleusercontent.com/img/a/AVvXsEjaofJaxyAc0EkiWhRdM7pYR7zJu7qIhKuEU7a8oV_JIa41JGeQnA9qBfgwuMtNfv6VX6Zg4K6elkdth-XTfbygpKsQ44etnudmKuIF7vBYDXmievZFMNJBTe38R638K74dwku8VoWvl4DI7cL55jRR1hIGUon9IKJBQLVevYt-flWXJyMMMGml9r51=s320"
      width="320" /></a></div><br /><br /></div><div>Now add
      the following JSON policy document that shows an example of the permissions that the IAM user
      or role policy needs in the DestinationAccount.&nbsp;</div><div><pre
      style="background-color: #f7f7f7; border-radius: 0px; border: 1px solid rgb(247, 247, 247);
      box-sizing: border-box; color: #333333; font-family: Consolas, &quot;Andale Mono
      WT&quot;, &quot;Andale Mono&quot;, &quot;Lucida Console&quot;,
      &quot;Lucida Sans Typewriter&quot;, &quot;DejaVu Sans Mono&quot;,
      &quot;Bitstream Vera Sans Mono&quot;, &quot;Liberation Mono&quot;,
      &quot;Nimbus Mono L&quot;, Monaco, &quot;Courier New&quot;, Courier,
      monospace; font-size: 14px; overflow: auto; padding: 15px 0px 15px 15px;">{
      "Version": "2012-10-17",
      "Statement": [
      {
      "Effect": "Allow",
      "Action": [
      "kms:DescribeKey",
      "kms:CreateGrant",
      "kms:Decrypt"
      ],
      "Resource": [
      "arn:aws:kms:us-east-1:<span style="box-sizing: border-box; color: red;"><span
      face="AmazonEmberBold, &quot;Helvetica Neue Bold&quot;, &quot;Helvetica
      Neue&quot;, Helvetica, Arial, sans-serif" style="box-sizing:
      border-box;">111111111111</span></span>:key/<span style="box-sizing:
      border-box; color: red;"><span face="AmazonEmberBold, &quot;Helvetica Neue
      Bold&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif"
      style="box-sizing: border-box;"><em style="box-sizing: border-box; font-family:
      AmazonEmber, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;">key-id
      </em></span><span face="AmazonEmberBold, &quot;Helvetica Neue
      Bold&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif"
      style="box-sizing: border-box;"><em style="box-sizing: border-box; font-family:
      AmazonEmber, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;">of
      cmkSource</em></span></span>"
      ]
      },
      {
      "Effect": "Allow",
      "Action": [
      "kms:CreateGrant",
      "kms:Encrypt",
      "kms:Decrypt",
      "kms:DescribeKey",
      "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": [
      "arn:aws:kms:eu-west-1:<span style="box-sizing: border-box; color: red;"><span
      face="AmazonEmberBold, &quot;Helvetica Neue Bold&quot;, &quot;Helvetica
      Neue&quot;, Helvetica, Arial, sans-serif" style="box-sizing:
      border-box;">999999999999</span></span>:key/<span style="box-sizing:
      border-box; color: red;"><span face="AmazonEmberBold, &quot;Helvetica Neue
      Bold&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif"
      style="box-sizing: border-box;"><em style="box-sizing: border-box; font-family:
      AmazonEmber, &quot;Helvetica Neue&quot;, Helvetica, Arial,
      sans-serif;">key-id</em></span><span face="AmazonEmberBold,
      &quot;Helvetica Neue Bold&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial,
      sans-serif" style="box-sizing: border-box;"><em style="box-sizing: border-box;
      font-family: AmazonEmber, &quot;Helvetica Neue&quot;, Helvetica, Arial,
      sans-serif;"> of cmkTarget</em></span></span>"
      ]
      },
      {
      "Effect": "Allow",
      "Action": [
      "kms:ListKeys",
      "kms:ListAliases"
      ],
      "Resource": [
      "*"
      ]
      },
      {
      "Effect": "Allow",
      "Action": [
      "ec2:ModifySnapshotAttribute",
      "ec2:CreateImage",
      "ec2:CopyImage",
      "ec2:RegisterImage",
      "ec2:CopySnapshot",
      "ec2:Describe*"
      ],
      "Resource": [
      "*"
      ]
      }
      ]
      }</pre><br /></div><div><b>Share custom AMI to other
      regions/accounts</b></div><div>Step 1 Go to SourceAccount and launch an
      instance from a public AMI:-&nbsp;Launch an EC2 instance from an EBS-backed public AMI in
      SourceAccount.&nbsp;I am using Amazon Linux 2 AMI (HVM) for this walkthrough, as shown in
      the following screenshot. </div><div class="separator" style="clear: both;
      text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/a/AVvXsEjHArrnPwX8gcFwceRpcmiTuI_9czKQFV-O3e2w8cuKagI4oBB4GlK-z8Bu3Iidmg1F9RFqy2CIGr44IXZjACjv6_js2lmFxICaLFwvuilduDAyWfdlofeBucJrsvM8v0ouBV61jxVsO-N0UuM0qKdnEb1hnU7AKwAS91Uwe13kw02uCjbV9DDMvnXd=s577"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="337"
      data-original-width="577" height="187"
      src="https://blogger.googleusercontent.com/img/a/AVvXsEjHArrnPwX8gcFwceRpcmiTuI_9czKQFV-O3e2w8cuKagI4oBB4GlK-z8Bu3Iidmg1F9RFqy2CIGr44IXZjACjv6_js2lmFxICaLFwvuilduDAyWfdlofeBucJrsvM8v0ouBV61jxVsO-N0UuM0qKdnEb1hnU7AKwAS91Uwe13kw02uCjbV9DDMvnXd=s320"
      width="320" /></a></div><br /><div><br
      /></div><div><br /></div><div>Step 2 Create a custom image
      from the instance:- Go into your newly created instance and customize according to your need
      then right-click on the newly created instance and select <span style="color:
      red;">Image and template</span> then select&nbsp;&nbsp;<span style="color:
      red;">Create image</span>&nbsp; thereafter click on the create image
      button&nbsp;to save the configuration as a custom AMI</div><div><br
      /></div><div class="separator" style="clear: both; text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/a/AVvXsEiD1d45qnsaUitpFqj-opasEDjA6000bVMkffDoe3oAVO2N6Wr_J_cwtb0Cf65xxIs4wGm8EddzlCUnop_tR0Ti1px55YIgAZXNkBTWMBMkFyYh0b0eideWkmyjH2JmXklPn4V3ugDnXrfaDga3Ui5efG5PphvKHhflQS5_4jqAV7tvMw04UchLnzsf=s482"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="482"
      data-original-width="451" height="320"
      src="https://blogger.googleusercontent.com/img/a/AVvXsEiD1d45qnsaUitpFqj-opasEDjA6000bVMkffDoe3oAVO2N6Wr_J_cwtb0Cf65xxIs4wGm8EddzlCUnop_tR0Ti1px55YIgAZXNkBTWMBMkFyYh0b0eideWkmyjH2JmXklPn4V3ugDnXrfaDga3Ui5efG5PphvKHhflQS5_4jqAV7tvMw04UchLnzsf=s320"
      width="299" /></a></div><br /><div><br
      /></div><div><br /></div><div>Step 3 Create a copy of newly
      custom AMI:- The reason for doing this is because the default Master key <span
      style="color: red;">aws/ebs</span> will not allow to share encrypted EBS AMI to other
      accounts and regions. To copy an AMI right-click on the custom AMI you created and select Copy
      AMI.</div><div><br /></div><div class="separator" style="clear:
      both; text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/a/AVvXsEhiXcZFJaqPhg0Z3jcHJhj3m0u0EvMRRSONGIC6gtu5eCCKybS-UTBTA42gCyf2nba5RKJ3XgQGF93KkriCSLMFbDM60xYsdokn9XcQ3Yp0gjAkmXQQ4hQGtCeCtF957l3T14YwV6x6ype1YPym0SK7_FCqTMQkqwdAzMbU7nM1oiar5O_F0oBV8e7S=s360"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="304"
      data-original-width="360" height="270"
      src="https://blogger.googleusercontent.com/img/a/AVvXsEhiXcZFJaqPhg0Z3jcHJhj3m0u0EvMRRSONGIC6gtu5eCCKybS-UTBTA42gCyf2nba5RKJ3XgQGF93KkriCSLMFbDM60xYsdokn9XcQ3Yp0gjAkmXQQ4hQGtCeCtF957l3T14YwV6x6ype1YPym0SK7_FCqTMQkqwdAzMbU7nM1oiar5O_F0oBV8e7S=s320"
      width="320" /></a></div><br /><div>Thereafter select the
      destination region <span style="color: red;">North Virginia </span>(my
      region)&nbsp; and select Master key <span style="color: red;">cmkSource</span>
      and check the Encrypt target EBS snapshots.</div><div><br
      /></div><div class="separator" style="clear: both; text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/a/AVvXsEgZ284Msqyoc0AqffQ1p7MwR9lTLYxvIfjLoNtNZMuml4xq8quOXLXP2XYSHY8ZmEtQDqX7yYCVs_EUvtiHBQJXIAMav-eMlx54jtEU8amL8lDGFpED2skz1u9pmvNPhSAru1-9UX1YrXOXoYs8MkG3MfVeDglDH-6nfIKJA3_xata89YDgxKzqPyL5=s536"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="371"
      data-original-width="536" height="221"
      src="https://blogger.googleusercontent.com/img/a/AVvXsEgZ284Msqyoc0AqffQ1p7MwR9lTLYxvIfjLoNtNZMuml4xq8quOXLXP2XYSHY8ZmEtQDqX7yYCVs_EUvtiHBQJXIAMav-eMlx54jtEU8amL8lDGFpED2skz1u9pmvNPhSAru1-9UX1YrXOXoYs8MkG3MfVeDglDH-6nfIKJA3_xata89YDgxKzqPyL5=s320"
      width="320" /></a></div><br /><div><br
      /></div><div><b>Note</b>:- I didn't change the AMI name and
      In-destination region I&nbsp; select the same SourceAccount's region.</div>A custom
      AMI with encrypted snapshots is created, as shown in the following
      screenshot.<p></p><div class="separator" style="clear: both; text-align:
      center;"><a
      href="https://blogger.googleusercontent.com/img/a/AVvXsEiGw2izTLs2Pb4IoOvwRMLaZNCZJMhSvfGt7PlqC5P4wFykjzVZj4PsGwbLXwgXZmr66lL282UzDN4roruVxN8XHIBA2V4e5s2dPuADiXyml23gjf6mKspn7zTwviVTUuqCiT2Sw9XvJZF4JhRcnvbTc-SOW5g4W2I1l9Nwuwt38x65_-1ypbozyygm=s620"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="276"
      data-original-width="620" height="142"
      src="https://blogger.googleusercontent.com/img/a/AVvXsEiGw2izTLs2Pb4IoOvwRMLaZNCZJMhSvfGt7PlqC5P4wFykjzVZj4PsGwbLXwgXZmr66lL282UzDN4roruVxN8XHIBA2V4e5s2dPuADiXyml23gjf6mKspn7zTwviVTUuqCiT2Sw9XvJZF4JhRcnvbTc-SOW5g4W2I1l9Nwuwt38x65_-1ypbozyygm=s320"
      width="320" /></a></div><div><br /></div>Step 4 Share a
      custom AMI with the target account:- Now select the newly generated copied AMI and click on
      the <span style="color: red;">Actions&nbsp;</span>button and select <span
      style="color: red;">Modify Image Permission </span>and&nbsp;Type the target
      account number in the AWS Account Number box and click save.<div class="separator"
      style="clear: both; text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/a/AVvXsEi0FAzOCtJuko-Y64M1HFq3dDnVlJL44b1bhhiE55fESX8dlaYJCItqFext634RglLTjsjffXar0zc81X25ri09qH2rufs3FAqE5zbmREzin0Le1dHt2NnMtQog-t5-v7HPAj9y9yJd7jUoLdrC6ThuXdnJVEe2f_OsYfTFuBPP7x1OHSTWFU-WOI5o=s580"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="307"
      data-original-width="580" height="169"
      src="https://blogger.googleusercontent.com/img/a/AVvXsEi0FAzOCtJuko-Y64M1HFq3dDnVlJL44b1bhhiE55fESX8dlaYJCItqFext634RglLTjsjffXar0zc81X25ri09qH2rufs3FAqE5zbmREzin0Le1dHt2NnMtQog-t5-v7HPAj9y9yJd7jUoLdrC6ThuXdnJVEe2f_OsYfTFuBPP7x1OHSTWFU-WOI5o=s320"
      width="320" /></a></div><br /><div>Step 5 Check AMI comes in
      DestinationAccount :- Now go to the destination account in EC2 select AMI from the navigation
      bar, you can see Our custom AMI will appear in the console.</div><div><br
      /></div><div><br /></div>

Write your content here...