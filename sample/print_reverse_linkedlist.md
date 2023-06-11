# Print Reverse LinkedList

Published: 2020-08-05T14:43:00.003+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div _ngcontent-ogb-c236="" class="description" style="background-color: white;
      font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px 0px;">
      <h4
      id="you-have-been-given-a-singly-linked-list-of-integers-write-a-function-to-print-the-list-in-a-reverse-order"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">
      You have been given a singly linked list of integers. Write a function to print the list in a
      reverse order.</h4>
      <h4
      id="to-explain-it-further-you-need-to-start-printing-the-data-from-the-tail-and-move-towards-the-head-of-the-list-printing-the-head-data-at-the-end"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">
      To explain it further, you need to start printing the data from the tail and move towards the
      head of the list, printing the head data at the end.</h4>
      <h5 id="note" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Note :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">You can’t change any
      of the pointers in the linked list, just print it in the reverse order.
      </code></pre>
      <h5 id="input-format" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      &nbsp;Input format :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">The first line
      contains an Integer 't' which denotes the number of test cases or queries to be run. Then the
      test cases follow.

      The first and the only line of each test case or query contains the elements of the singly
      linked list separated by a single space.
      </code></pre>
      <h5 id="remember-constraints" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      Remember/Constraints :</h5>
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
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">For each test case,
      print the singly linked list of integers in a reverse fashion, in a row, separated by a single
      space.

      Output for every test case will be printed in a seperate line.
      </code></pre>
      <h5 id="constraints" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      &nbsp;Constraints :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1 &lt;= t
      &lt;= 10^2
      0 &lt;= M &lt;= 10^3
      Time Limit: 1sec

      Where 'M' is the size of the singly linked list.
      </code></pre>
      </div>
      <div _ngcontent-ogb-c236="" class="description" style="background-color: white;
      font-family: Muli, sans-serif; margin: 0px; padding: 30px 0px 0px;">
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Input 1 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1
      1 2 3 4 5 -1
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Output 1 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">5 4 3 2 1
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Input 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">2
      1 2 3 -1
      10 20 30 40 50 -1
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Output 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: Muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">3 2 1
      50 40 30 20 10</code></pre>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/da012a1b851ed67005d5d068bd111847.js"></script></div>


Write your content here...