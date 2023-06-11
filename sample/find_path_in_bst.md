# Find path in BST

Published: 2022-07-16T17:12:00.001+05:30

Description: 
      <div _ngcontent-orn-c711="" class="description ng-star-inserted"
      imageoverlay="" style="background-color: white; font-family: Muli, sans-serif; margin: 0px;
      padding: 30px 0px 0px;"><h4
      id="given-a-bst-and-an-integer-k-find-and-return-the-path-from-the-node-with-data-k-and-root-if-a-node-with-data-k-is-present-in-given-bst-in-a-list-return-empty-list-otherwise"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">Given a BST and an integer k. Find and return
      the path from the node with data k and root (if a node with data k is present in given BST) in
      a list. Return empty list otherwise.</h4><h4
      id="note-assume-that-bst-contains-all-unique-elements" style="color: #626262; font-size: 13px;
      font-weight: 400; letter-spacing: 0.3px; line-height: 20px; margin: 0px; padding: 0px 0px
      15px;">Note: Assume that BST contains all unique elements.</h4><h5
      id="input-format" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Input
      Format :</h5><pre style="background-color: whitesmoke; border-radius: 4px;
      box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight:
      600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding:
      15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">The first line of input contains data of the nodes of the tree in level order form.
      The data of the nodes of the tree is separated by space. If any node does not have left or
      right child, take -1 in its place. Since -1 is used as an indication whether the left or right
      nodes exist, therefore, it will not be a part of the data of any node.
      The following line of input contains an integer, that denotes the value of k.
      </code></pre><h5 id="output-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Output Format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">The first line and only line of output prints the data
      of the nodes in the path from node k to root. The data of the nodes is separated by single
      space.
      </code></pre><h5 id="constraints" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Constraints:</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">Time Limit: 1 second
      </code></pre></div><div _ngcontent-orn-c711="" class="description
      ng-star-inserted" style="background-color: white; font-family: Muli, sans-serif; margin: 0px;
      padding: 30px 0px 0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px;
      padding: 0px;">Sample Input 1:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
      2
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 1:</h5></div><p><span style="background-color:
      whitesmoke; color: #626262; font-family: Muli, sans-serif; font-size: 13px; letter-spacing:
      0.23px; white-space: pre-wrap;">2 5 8</span>&nbsp;</p><p><br
      /></p><p><br /><script
      src="https://gist.github.com/Svastikkka/6b4742cd4a965fa95e13af9a637cfbd3.js"></script></p>

Write your content here...