# Reverse Level Order Traversal

Published: 2020-07-22T04:38:00.002+05:30

Description: 
      <div _ngcontent-iwb-c152="" class="padding"
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px 0px 15px;"><div
      _ngcontent-iwb-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">Level MEDIUM<br /><br /><span style="background-color: white; color:
      #565656; font-family: roboto, sans-serif; font-size: 14px; letter-spacing: 0.3px;">Given a
      binary tree.Traverse the tree in the manner of reverse level
      order</span></div></div><div _ngcontent-iwb-c152="" class="description
      ng-star-inserted" style="-webkit-font-smoothing: antialiased; background-color: white;
      font-family: roboto, sans-serif; font-size: 16px; margin: 0px; padding: 0px;"><h4
      id="example" style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px;
      font-weight: 400; letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px
      5px;">Example:</h4><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">
      5
      / \
      6 2
      / \
      2 3
      / \
      9 7

      Reverse level order traversal for this tree is:
      7 9 3 2 2 6 5
      </code></pre><h5 id="input-format" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Input format :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">Line 1 : Elements in level order form (separated by space)
      (If any node does not have left or right child, take -1 in its place)
      </code></pre><h5 id="output-format" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Output Format :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">Print Reverse level order traversal
      </code></pre><h5 id="constraints" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Constraints :</h5><h4 id="1-lt-n-lt-10-5" style="-webkit-font-smoothing:
      antialiased; color: #565656; font-size: 14px; font-weight: 400; letter-spacing: 0.3px;
      line-height: 25px; margin: 0px; padding: 15px 0px 5px;">1 &lt;= N &lt;=
      10^5</h4></div><div _ngcontent-iwb-c152="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px;"><h5 id="input"
      style="-webkit-font-smoothing: antialiased; color: #353535; font-size: 14px; letter-spacing:
      0.4px; margin: 0px; padding: 15px 0px 0px;">Input:</h5><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;open
      sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">5 6 2 2 3 -1 -1 9 7
      -1 -1 -1 -1
      </code></pre><h5 id="output" style="-webkit-font-smoothing: antialiased; color:
      #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Output :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: scroll; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">7 9 3 2 2 6 5</code></pre></div>
      <script
      src="https://gist.github.com/Svastikkka/f883731c708669d986964a8b22d6bf47.js"></script>

Write your content here...