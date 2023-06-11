# Running Vault as a Stateful Set on AWS EKS Fargate

Published: 2022-07-20T08:44:00.003+05:30

Description: Hi everyone I am Manshu Sharma😎, In Today's blog post we are going to see
      How we can deploy the <a href="https://www.vaultproject.io/">vault</a> as a
      stateful set application in our AWS EKS Fargate but before we start let's have a quick
      overview of the Hashicorp Vault.<div><br /></div><div>What is
      Hashicorp Vault?</div>According to Hashicorp organization, HashiCorp Vault is a secret
      management tool designed to control access to sensitive credentials in a low-trust
      environment. It can be used to store sensitive values and at the same time dynamically
      generate access for specific services/applications on lease. Plus, Vault can be used to
      authenticate users (machines or humans) to make sure they’re authorized to access a particular
      file/resource.<div><br /></div><div>Following are the use cases of
      Hashicorp <a href="https://www.vaultproject.io/"
      target="_blank">Vault</a></div><ul><li><b>Secrets
      Management</b>: Centrally store, access, and deploy secrets across applications,
      systems, and infrastructure.</li><li><b>Dynamic Secrets</b>: Generate
      time-based access credentials dynamically based on policies and revoke access when the lease
      expires.</li><li><b>Kubernetes Secrets</b>: Secure Kubernetes clusters
      with Vault's power and dynamic secrets.</li><li><b>Database Credential
      Rotation</b>: Eliminate long-standing shared credentials and reduce the risk of breach
      and credential leakage with automated database credential
      rotation.</li><li><b>Automated PKI Infrastructure</b>: Quickly create
      X.509 certificates on-demand and reduce the manual
      overhead.</li><li><b>Identity-based Access</b>: Authenticate and
      access different clouds, systems, and endpoints using trusted
      identities.</li><li><b>Data Encryption &amp; Tokenization</b>:
      Secure application data with one centralized workflow that resides in untrusted or
      semi-trusted systems outside of Vault.</li><li><b>Key Management</b>:
      Standardize distribution workflow and lifecycle management across KMS
      providers.</li></ul>Overview completed. Now let's jump into the setup of the Vault
      application in our AWS EKS Fargate.<div><br
      /></div><div><i><b>Note</b>: We will need to copy and store
      vault-efs id and access-point id while creating our persistent
      volume.</i></div><div><b>Installation</b></div><div><br
      /></div><div>Step 1 After login inside the AWS console creates a frigate
      profile with a selector called a
      <b>vault.</b></div><div><b><br
      /></b></div><div><div>Step 2 After creating a fargate profile with
      selector create one efs volume&nbsp; and we call it
      <b>vault</b><b>-efs</b></div></div><div><b><br
      /></b></div><div><i><b>Note</b>: We will need to copy
      and store vault-efs id and access-point id while creating our persistent
      volume.</i></div><div><br /></div><div>Step 3 Create a
      vault namespace inside the cluster.</div><div><br
      /></div><div><span style="color: red; font-family: courier;">kubectl
      create ns vault</span></div><div><br /></div><div>Step 3
      Thereafter we need to install the EFS CSI driver as we are deploying our vault in AWS
      Fargate.&nbsp;To install we can refer to the <a
      href="https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html">AWS EFS CSI
      DRIVER</a> installation post for our AWS EKS Fargate.</div><div><br
      /></div><div>Step 4&nbsp;</div>

Write your content here...