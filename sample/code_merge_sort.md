# Code : Merge Sort

Published: 2020-09-27T23:24:00.001+05:30

Description: 
      <p><span style="background-color: white; color: #626262;
      font-family: Muli, sans-serif; font-size: 13px; letter-spacing: 0.3px;">Given a singly
      linked list of integers, sort it using 'Merge Sort.'</span></p><div
      _ngcontent-nmb-c266="" class="description" style="background-color: white; font-family: Muli,
      sans-serif; margin: 0px; padding: 30px 0px 0px;"><h5 id="note" style="color: #2d2d2d;
      font-size: 15px; margin: 0px; padding: 0px;">Note :</h5><pre
      style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px
      0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">No need to print the
      list, it has already been taken care. Only return the new head to the list.
      </code></pre><h5 id="input-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Input format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">The first line contains an Integer 't' which denotes
      the number of test cases or queries to be run. Then the test cases follow.

      The first and the only line of each test case or query contains the elements of the singly
      linked list separated by a single space.
      </code></pre><h5 id="remember-consider" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Remember/Consider :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">While specifying the list elements for input, -1
      indicates the end of the singly linked list and hence, would never be a list element
      </code></pre><h5 id="output-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Output format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">For each test case/query, print the elements of the
      sorted singly linked list.

      Output for every test case will be printed in a seperate line.
      </code></pre><h5 id="constraints" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Constraints :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">1 &lt;= t &lt;= 10^2
      0 &lt;= M &lt;= 10^5
      Where M is the size of the singly linked list.

      Time Limit: 1sec
      </code></pre></div><div _ngcontent-nmb-c266="" class="description"
      style="background-color: white; font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px
      0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Sample
      Input 1 :</h5><pre style="background-color: whitesmoke; border-radius: 4px;
      box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight:
      600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding:
      15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">1
      10 9 8 7 6 5 4 3 -1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 1 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;"> 3 4 5 6 7 8 9 10
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">&nbsp;Sample Output 2 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">2
      -1
      10 -5 9 90 5 67 1 89 -1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 2 :</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">-5 1 5 9 10 67 89
      90</code></pre></div>
      <script
      src="https://gist.github.com/Svastikkka/9a7708931bc5d9f4529bc27c7c296640.js"></script>

Write your content here...