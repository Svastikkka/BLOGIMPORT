# Construct Tree Using Inorder and Preorder

Published: 2020-09-15T11:32:00.001+05:30

Description: 
      <p><span style="background-color: white; color: #626262;
      font-family: Muli, sans-serif; font-size: 13px; letter-spacing: 0.3px;">Given Preorder and
      Inorder traversal of a binary tree, create the binary tree associated with the traversals. You
      just need to construct the tree and return the root.</span></p><div
      _ngcontent-umi-c259="" class="description" style="background-color: white; font-family: Muli,
      sans-serif; margin: 0px; padding: 30px 0px 0px;"><h5
      id="note-assume-binary-tree-contains-only-unique-elements" style="color: #2d2d2d; font-size:
      15px; margin: 0px; padding: 0px;">Note: Assume binary tree contains only unique
      elements.</h5><p style="margin: 0px; padding: 0px;"><code style="font-family:
      Muli, sans-serif; margin: 0px; padding: 0px;">Input format :</code></p><p
      style="margin: 0px; padding: 0px;"><code style="font-family: Muli, sans-serif; margin:
      0px; padding: 0px;">Line 1 : n (Total number of nodes in binary
      tree)</code></p><p style="margin: 0px; padding: 0px;"><code
      style="font-family: Muli, sans-serif; margin: 0px; padding: 0px;">Line 2 : Pre order
      traversal</code></p><p style="margin: 0px; padding: 0px;"><code
      style="font-family: Muli, sans-serif; margin: 0px; padding: 0px;">Line 3 : Inorder
      Traversal</code></p><p style="margin: 0px; padding: 0px;"><code
      style="font-family: Muli, sans-serif; margin: 0px; padding: 0px;">Output Format
      :</code></p><p style="margin: 0px; padding: 0px;"><code
      style="font-family: Muli, sans-serif; margin: 0px; padding: 0px;">Elements are printed
      level wise, each level in new line (separated by
      space).</code></p></div><div _ngcontent-umi-c259="" class="description"
      style="background-color: white; font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px
      0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Sample
      Input :</h5><pre style="background-color: whitesmoke; border-radius: 4px; box-shadow:
      rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">12
      1 2 3 4 15 5 6 7 8 10 9 12
      4 15 3 2 5 1 6 10 8 7 9 12
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output :</h5><pre style="background-color: whitesmoke; border-radius:
      4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif;
      font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden;
      padding: 15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family:
      Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px;
      padding: 0px;">1
      2 6
      3 5 7
      4 8 9
      15 10 12</code></pre></div>
      <script
      src="https://gist.github.com/Svastikkka/4f81faf26963a6231ffd6708d2f5a226.js"></script>

Write your content here...