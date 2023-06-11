# AppendLastNToFirst

Published: 2020-08-07T12:18:00.002+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div _ngcontent-jtx-c236="" class="description" style="background-color: white;
      font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px 0px;">
      <h4
      id="you-have-been-given-a-singly-linked-list-of-integers-along-with-an-integer-39-n-39-write-a-function-to-append-the-last-39-n-39-nodes-towards-the-front-of-the-singly-linked-list-and-returns-the-new-head-to-the-list"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">
      You have been given a singly linked list of integers along with an integer 'N'. Write a
      function to append the last 'N' nodes towards the front of the singly linked list and returns
      the new head to the list.</h4>
      <h5 id="input-format" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      Input format :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">The first line
      contains an Integer 't' which denotes the number of test cases or queries to be run. Then the
      test cases follow.

      The first line of each test case or query contains the elements of the singly linked list
      separated by a single space.

      The second line contains the integer value 'N'. It denotes the number of nodes to be moved
      from last to the front of the singly linked list.
      </code></pre>
      <h5 id="remember-consider" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      Remember/Consider :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">While specifying the
      list elements for input, -1 indicates the end of the singly linked list and hence, would never
      be a list element.
      </code></pre>
      <h5 id="output-format" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      Output format :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">For each test
      case/query, print the resulting singly linked list of integers in a row, separated by a single
      space.

      Output for every test case will be printed in a seperate line.
      </code></pre>
      <h5 id="constraints" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      Constraints :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1 &lt;= t
      &lt;= 10^2
      0 &lt;= M &lt;= 10^5
      0 &lt;= N &lt; M
      Time Limit: 1sec

      Where 'M' is the size of the singly linked list.
      </code></pre>
      </div>
      <div _ngcontent-jtx-c236="" class="description" style="background-color: white;
      font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px 0px;">
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Input 1 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">2
      1 2 3 4 5 -1
      3
      10 20 30 40 50 60 -1
      5
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Output 1 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">3 4 5 1 2
      20 30 40 50 60 10
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Input 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1
      10 6 77 90 61 67 100 -1
      4
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Output 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">90 61 67 100 10 6 77
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      &nbsp;Explanation to Sample Input 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">We have been required
      to move the last 4 nodes to the front of the list. Here,
      "90-&gt;61-&gt;67-&gt;100" is the list which represents the last 4 nodes. When we
      move this list to the front then the remaining part of the initial list which is,
      "10-&gt;6-&gt;77" is attached after 100. Hence, the new list formed with an updated
      head pointing to 90.</code></pre>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/d081b4dd2b9d1bb075f83dbf79ce3198.js"></script></div>


Write your content here...