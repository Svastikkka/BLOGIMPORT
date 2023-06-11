# Palindrome LinkedList

Published: 2020-08-06T10:47:00.004+05:30

Description: 
      <div _ngcontent-jtq-c236="" class="description" style="background-color:
      white; font-family: muli, sans-serif; margin: 0px; padding: 30px 0px 0px;"><h4
      id="you-have-been-given-a-head-to-a-singly-linked-list-of-integers-write-a-function-check-to-whether-the-list-given-is-a-39-palindrome-39-or-not"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">You have been given a head to a singly linked
      list of integers. Write a function check to whether the list given is a 'Palindrome' or
      not.</h4><h5 id="input-format" style="color: #2d2d2d; font-size: 15px; margin: 0px;
      padding: 0px;">&nbsp;Input format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">The first line contains an Integer 't' which denotes
      the number of test cases or queries to be run. Then the test cases follow.

      First and the only line of each test case or query contains the the elements of the singly
      linked list separated by a single space.
      </code></pre><h5 id="remember-consider" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">&nbsp;Remember/Consider :</h5><pre
      style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px
      0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">While specifying the
      list elements for input, -1 indicates the end of the singly linked list and hence, would never
      be a list element.
      </code></pre><h5 id="output-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">&nbsp;Output format :</h5><pre
      style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px
      0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">For each test case,
      the only line of output that print 'true' if the list is Palindrome or 'false' otherwise.
      </code></pre><h5 id="constraints" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">&nbsp;Constraints :</h5><pre
      style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px
      0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1 &lt;= t
      &lt;= 10^2
      0 &lt;= M &lt;= 10^5
      Time Limit: 1sec

      Where 'M' is the size of the singly linked list.
      </code></pre></div><div _ngcontent-jtq-c236="" class="description"
      style="background-color: white; font-family: muli, sans-serif; margin: 0px; padding: 30px 0px
      0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Sample
      Input 1 :</h5><pre style="background-color: whitesmoke; border-radius: 4px;
      box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight:
      600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding:
      15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family: muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">1
      9 2 3 3 2 9 -1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 1 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">true
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Input 2 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">2
      0 2 3 2 5 -1
      -1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 2 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">false
      true
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Explanation for the Sample Input 2 :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">For the first query, it is pretty intuitive that the
      the given list is not a palindrome, hence the output is 'false'.

      For the second query, the list is empty. An empty list is always a palindrome , hence the
      output is 'true'.</code></pre></div>

      <script
      src="https://gist.github.com/Svastikkka/805b1a4b9e0ca5cad67d853dd03bed73.js"></script>

Write your content here...