# Length of LL

Published: 2020-08-02T14:00:00.003+05:30

Description: 
      <div _ngcontent-uex-c219="" class="description" style="background-color:
      white; font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px 0px;"><h4
      id="for-a-given-singly-linked-list-of-integers-find-and-return-its-length-do-it-using-an-iterative-method"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">For a given singly linked list of integers, find
      and return its length. Do it using an iterative method.</h4><h5 id="input-format"
      style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Input format
      :</h5><pre style="background-color: whitesmoke; border-radius: 4px; box-shadow:
      rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">The first line contains an Integer 't' which denotes the number of test cases or
      queries to be run. Then the test cases follow.

      First and the only line of each test case or query contains elements of the singly linked list
      separated by a single space.
      </code></pre><h5 id="remember-consider" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">&nbsp;Remember/Consider :</h5><pre
      style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px
      0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">While specifying the
      list elements for input, -1 indicates the end of the singly linked list and hence, would never
      be a list element.
      </code></pre><h5 id="output-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Output format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">For each test case, print the length of the linked
      list.

      Output for every test case will be printed in a seperate line.
      </code></pre><h5 id="constraints" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">&nbsp;Constraints :</h5><pre
      style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px
      0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1 &lt;= t
      &lt;= 10^2
      0 &lt;= N &lt;= 10^5
      Time Limit: 1sec
      </code></pre></div><div _ngcontent-uex-c219="" class="description"
      style="background-color: white; font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px
      0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Sample
      Input 1 :</h5><pre style="background-color: whitesmoke; border-radius: 4px;
      box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight:
      600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding:
      15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">1
      3 4 5 2 6 1 9 -1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 1 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">7
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Input 2 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">2
      10 76 39 -3 2 9 -23 9 -1
      -1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 2 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">8
      0</code></pre></div>
      <script
      src="https://gist.github.com/Svastikkka/d0b82df07bde3d1ec10ad940cfc6f5c3.js"></script>

Write your content here...