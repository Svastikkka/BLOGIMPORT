# Print Levelwise

Published: 2020-09-15T11:30:00.001+05:30

Description: 
      <p><span style="background-color: white; color: #626262;
      font-family: Muli, sans-serif; font-size: 13px; letter-spacing: 0.3px;">Given a binary
      tree, print the tree in level wise order.</span></p><div _ngcontent-umi-c259=""
      class="description" style="background-color: white; font-family: Muli, sans-serif; margin:
      0px; padding: 30px 0px 0px;"><h4
      id="for-printing-a-node-with-data-n-you-need-to-follow-the-exact-format" style="color:
      #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height: 20px; margin:
      0px; padding: 0px 0px 15px;">For printing a node with data N, you need to follow the exact
      format -</h4><pre style="background-color: whitesmoke; border-radius: 4px;
      box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight:
      600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding:
      15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">N:L:x,R:y
      </code></pre><h4
      id="wherer-n-is-data-of-any-node-present-in-the-binary-tree-x-and-y-are-the-values-of-left-and-right-child-of-node-n-print-1-if-any-child-is-null"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">wherer, N is data of any node present in the
      binary tree. x and y are the values of left and right child of node N. Print -1. if any child
      is null.</h4><h4 id="there-is-no-space-in-between" style="color: #626262; font-size:
      13px; font-weight: 400; letter-spacing: 0.3px; line-height: 20px; margin: 0px; padding: 0px
      0px 15px;">There is no space in between.</h4><h4
      id="you-need-to-print-all-nodes-in-the-level-order-form-in-different-lines" style="color:
      #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height: 20px; margin:
      0px; padding: 0px 0px 15px;">You need to print all nodes in the level order form in
      different lines.</h4><h5 id="input-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Input format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">Elements in level order form (separated by space)
      (If any node does not have left or right child, take -1 in its place)
      </code></pre></div><div _ngcontent-umi-c259="" class="description"
      style="background-color: white; font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px
      0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Sample
      Input :</h5><pre style="background-color: whitesmoke; border-radius: 4px; box-shadow:
      rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output :</h5><pre style="background-color: whitesmoke; border-radius:
      4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif;
      font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden;
      padding: 15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family:
      Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px;
      padding: 0px;">8:L:3,R:10
      3:L:1,R:6
      10:L:-1,R:14
      1:L:-1,R:-1
      6:L:4,R:7
      14:L:13,R:-1
      4:L:-1,R:-1
      7:L:-1,R:-1
      13:L:-1,R:-1</code></pre></div>
      <script
      src="https://gist.github.com/Svastikkka/239e744acac94dc2b614d90d6f2829b6.js"></script>

Write your content here...