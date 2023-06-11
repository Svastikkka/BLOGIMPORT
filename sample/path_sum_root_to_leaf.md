# Path Sum Root to Leaf

Published: 2020-11-23T21:50:00.002+05:30

Description: 
      <p><span style="background-color: white; color: #626262;
      font-family: Muli, sans-serif; font-size: 13px; letter-spacing: 0.3px;">For a given Binary
      Tree of type integer and a number K, print out all root-to-leaf paths where the sum of all the
      node data along the path is equal to K.</span></p><div _ngcontent-tju-c267=""
      class="description" style="background-color: white; font-family: Muli, sans-serif; margin:
      0px; padding: 30px 0px 0px;"><h5 id="example" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Example:</h5><p style="margin: 0px; padding:
      0px;"><img alt="alt txt"
      src="https://files.codingninjas.in/binary-tree-page-2-1-4808.png" style="margin: 0px;
      max-width: 100%; padding: 0px;" /></p><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">If you see in the above-depicted picture of Binary
      Tree, we see that there are a total of two paths, starting from the root and ending at the
      leaves which sum up to a value of K = 13.

      The paths are:
      a. 2 3 4 4
      b. 2 3 8

      One thing to note here is, there is another path in the right sub-tree in reference to the
      root, which sums up to 13 but since it doesn't end at the leaf, we discard it.
      The path is: 2 9 2(not a leaf)
      </code></pre><h5 id="input-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">&nbsp;Input Format:</h5><pre
      style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px
      0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">The first line of
      input will contain the node data, all separated by a single space. Since -1 is used as an
      indication whether the left or right node data exist for root, it will not be a part of the
      node data.

      The second line of input contains an integer value K.
      </code></pre><h5 id="output-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Output Format:</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">Lines equal to the total number of paths will be
      printed. All the node data in every path will be printed in a linear fashion taken in the
      order they appear from top to down bottom in the tree. A single space will separate them all.
      </code></pre><h5 id="constriants" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Constriants:</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">1 &lt;= N &lt;= 10^5
      0 &lt;= K &lt;= 10^8
      Where N is the total number of nodes in the binary tree.

      Time Limit: 1 second
      </code></pre></div><div _ngcontent-tju-c267="" class="description"
      style="background-color: white; font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px
      0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Sample
      Input 1:</h5><pre style="background-color: whitesmoke; border-radius: 4px;
      box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight:
      600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding:
      15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">2 3 9 4 8 -1 2 4 -1 -1 -1 6 -1 -1 -1 -1 -1
      13
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">&nbsp;Sample Output 1:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">2 3 4 4
      2 3 8
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Input 2:</h5><pre style="background-color: whitesmoke; border-radius:
      4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif;
      font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden;
      padding: 15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family:
      Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px;
      padding: 0px;">5 6 7 2 3 -1 1 -1 -1 -1 9 -1 -1 -1 -1
      13
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">&nbsp;Sample Output 2:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">5 6 2
      5 7 1</code></pre></div>
      <script
      src="https://gist.github.com/Svastikkka/e2cf3557579ec164c0fc52bc3717931f.js"></script>

Write your content here...