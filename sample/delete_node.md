# Delete node

Published: 2021-03-15T00:05:00.002+05:30

Description: 
      <p><span style="background-color: white; color: #626262;
      font-family: Muli, sans-serif; font-size: 13px; letter-spacing: 0.3px;">You have been given
      a linked list of integers. Your task is to write a function that deletes a node from a given
      position, 'pos'.</span></p><div _ngcontent-gqo-c424="" class="description
      ng-star-inserted" style="background-color: white; font-family: Muli, sans-serif; margin: 0px;
      padding: 30px 0px 0px;"><h5 id="note" style="color: #2d2d2d; font-size: 15px; margin:
      0px; padding: 0px;">Note :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">Assume that the Indexing for the linked list always
      starts from 0.

      If the position is greater than or equal to the length of the linked list, you should return
      the same linked list without any change.
      </code></pre><h5 id="illustration" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Illustration :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">The following images depict how the deletion has been
      performed.
      </code></pre><h4 id="image-i" style="color: #626262; font-size: 13px;
      font-weight: 400; letter-spacing: 0.3px; line-height: 20px; margin: 0px; padding: 0px 0px
      15px;">Image-I :</h4><p style="margin: 0px; padding: 0px;"><img alt="Alt
      txt" src="https://files.codingninjas.in/0000000000004029.png" style="margin: 0px; max-width:
      100%; padding: 0px;" /></p><h4 id="image-ii" style="color: #626262; font-size:
      13px; font-weight: 400; letter-spacing: 0.3px; line-height: 20px; margin: 0px; padding: 0px
      0px 15px;">Image-II :</h4><p style="margin: 0px; padding: 0px;"><img
      alt="Alt txt" src="https://files.codingninjas.in/0000000000004033.png" style="margin: 0px;
      max-width: 100%; padding: 0px;" /></p><h5 id="input-format" style="color: #2d2d2d;
      font-size: 15px; margin: 0px; padding: 0px;">Input format :</h5><pre
      style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px
      0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">The first line
      contains an Integer 't' which denotes the number of test cases or queries to be run. Then the
      test cases follow.

      The first line of each test case or query contains the elements of the linked list separated
      by a single space.

      The second line of each test case contains the integer value of 'pos'. It denotes the position
      in the linked list from where the node has to be deleted.
      </code></pre><h5 id="remember-consider" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">&nbsp;Remember/Consider :</h5><pre
      style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px
      0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">While specifying the
      list elements for input, -1 indicates the end of the singly linked list and hence, would never
      be a list element
      </code></pre><h5 id="output-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Output format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">For each test case/query, print the resulting linked
      list of integers in a row, separated by a single space.

      Output for every test case will be printed in a separate line.
      You don't need to print explicitly, it has been taken care of.
      </code></pre><h5 id="constraints" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Constraints :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">1 &lt;= t &lt;= 10^2
      0 &lt;= N &lt;= 10^5
      pos &gt;= 0
      Time Limit: 1sec

      Where 'N' is the size of the singly linked list.
      </code></pre></div><div _ngcontent-gqo-c424="" class="description
      ng-star-inserted" style="background-color: white; font-family: Muli, sans-serif; margin: 0px;
      padding: 30px 0px 0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px;
      padding: 0px;">Sample Input 1 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">1
      3 4 5 2 6 1 9 -1
      3
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 1 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">3 4 5 6 1 9
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Input 2 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">2
      3 4 5 2 6 1 9 -1
      0
      10 20 30 40 50 60 -1
      7
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 2 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">4 5 2 6 1 9
      10 20 30 40 50 60</code></pre></div>
      <script
      src="https://gist.github.com/Svastikkka/964fb52e7918d53c3aa75f38d6bc9100.js"></script>

Write your content here...