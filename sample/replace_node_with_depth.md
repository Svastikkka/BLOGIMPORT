# Replace Node With Depth

Published: 2020-09-10T12:58:00.001+05:30

Description: 
      <p><span style="background-color: white; color: #626262;
      font-family: Muli, sans-serif; font-size: 13px; letter-spacing: 0.3px;">Given a a binary
      tree. Replace each of it's data with the depth of tree.</span></p><div
      _ngcontent-jca-c259="" class="description" style="background-color: white; font-family: Muli,
      sans-serif; margin: 0px; padding: 30px 0px 0px;"><h4
      id="root-is-at-depth-0-change-its-value-to-0-and-next-level-nodes-are-at-depth-1-and-so-on"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">Root is at depth 0, change its value to 0 and
      next level nodes are at depth 1 and so on.</h4><h4
      id="print-the-tree-after-modifying-in-inorder-fashion" style="color: #626262; font-size: 13px;
      font-weight: 400; letter-spacing: 0.3px; line-height: 20px; margin: 0px; padding: 0px 0px
      15px;">Print the tree after modifying in inorder fashion.</h4><h4 id="example"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">Example:</h4><p style="margin: 0px;
      padding: 0px;"><strong style="margin: 0px; padding:
      0px;">Input</strong></p><p style="margin: 0px; padding: 0px;"><img
      alt="Alt text" height="235" src="https://ninjasfiles.s3.amazonaws.com/0000000000000614.PNG"
      style="margin: 0px; max-width: 100%; padding: 0px;" width="374" /></p><p
      style="margin: 0px; padding: 0px;"><strong style="margin: 0px; padding:
      0px;">Output</strong></p><p style="margin: 0px; padding: 0px;"><img
      alt="Alt text" height="190" src="https://ninjasfiles.s3.amazonaws.com/0000000000000617.PNG"
      style="margin: 0px; max-width: 100%; padding: 0px;" width="328" /></p><h5
      id="input-format" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Input
      format :</h5><pre style="background-color: whitesmoke; border-radius: 4px;
      box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight:
      600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding:
      15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">Line 1 : Elements in level order form (separated by space)
      (If any node does not have left or right child, take -1 in its place)
      </code></pre><h5 id="output-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Output Format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;"> Inorder traversal of modified tree.
      </code></pre></div><div _ngcontent-jca-c259="" class="description"
      style="background-color: white; font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px
      0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Sample
      Input 1:</h5><pre style="background-color: whitesmoke; border-radius: 4px;
      box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight:
      600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding:
      15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;"> 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 1:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;"> 2
      1
      2
      0
      2
      1
      2</code></pre></div>

      <script
      src="https://gist.github.com/Svastikkka/c9df9ac3aaa8d1ce7bd352ea1698ab8b.js"></script>

Write your content here...