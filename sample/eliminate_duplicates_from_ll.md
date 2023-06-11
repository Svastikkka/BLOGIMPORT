# Eliminate duplicates from LL

Published: 2020-08-10T00:18:00.004+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <span style="background-color: white; color: #626262; font-size: 13px; letter-spacing:
      0.3px;">You have been given a singly linked list of integers where the elements are sorted
      in ascending order. Write a function that removes the consecutive duplicate values such that
      the given list only contains unique elements and returns the head to the updated
      list.</span><br />
      <div _ngcontent-ilv-c236="" class="description" style="background-color: white;
      font-family: muli, sans-serif; margin: 0px; padding: 30px 0px 0px;">
      <h5 id="input-format" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      &nbsp;Input format :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">The first line
      contains an Integer 't' which denotes the number of test cases or queries to be run. Then the
      test cases follow.

      The first and the only line of each test case or query contains the elements(in ascending
      order) of the singly linked list separated by a single space.
      </code></pre>
      <h5 id="remember-consider" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      &nbsp;Remember/Consider :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">While specifying the
      list elements for input, -1 indicates the end of the singly linked list and hence, would never
      be a list element.
      </code></pre>
      <h5 id="output-format" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      &nbsp;Output format :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">For each test
      case/query, print the resulting singly linked list of integers in a row, separated by a single
      space.

      Output for every test case will be printed in a seperate line.
      </code></pre>
      <h5 id="constraints" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      Constraints :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1 &lt;= t
      &lt;= 10^2
      0 &lt;= M &lt;= 10^5
      Time Limit: 1sec

      Where 'M' is the size of the singly linked list.
      </code></pre>
      </div>
      <div _ngcontent-ilv-c236="" class="description" style="background-color: white;
      font-family: muli, sans-serif; margin: 0px; padding: 30px 0px 0px;">
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Input 1 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1
      1 2 3 3 4 3 4 5 4 5 5 7 -1
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Output 1 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1 2 3 4 3 4 5 4 5 7
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Input 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">2
      10 20 30 40 50 -1
      10 10 10 10 -1
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Output 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">10 20 30 40 50
      10</code></pre>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/e90442bedd6bf1f31d5aaf18f2e2229f.js"></script></div>


Write your content here...