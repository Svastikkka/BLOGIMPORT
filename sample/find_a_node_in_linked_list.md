# Find a Node in Linked List

Published: 2020-08-03T16:43:00.002+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div _ngcontent-kwh-c219="" class="description" style="background-color: white;
      font-family: muli, sans-serif; margin: 0px; padding: 30px 0px 0px;">
      <h4
      id="you-have-been-given-a-singly-linked-list-of-integers-write-a-function-that-returns-the-index-position-of-an-integer-data-denoted-by-39-n-39-if-it-exists-1-otherwise"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">
      You have been given a singly linked list of integers. Write a function that returns the
      index/position of an integer data denoted by 'N'(if it exists). -1 otherwise.</h4>
      <h5 id="note" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Note :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">Assume that the
      Indexing for the singly linked list always starts from 0.
      </code></pre>
      <h5 id="input-format" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      Input format :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">The first line
      contains an Integer 't' which denotes the number of test cases or queries to be run. Then the
      test cases follow.

      The first line of each test case or query contains the elements of the singly linked list
      separated by a single space.

      The second line contains the integer value 'N'. It denotes the data to be searched in the
      given singly linked list.
      </code></pre>
      <h5 id="remember-consider" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      Remember/Consider :</h5>
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
      Output format :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">For each test
      case/query, print the index/position of 'N' in the singly linked list. -1, otherwise.

      Output for every test case will be printed in a seperate line.
      </code></pre>
      <h5 id="constraints" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">
      &nbsp;Constraints :</h5>
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
      <div _ngcontent-kwh-c219="" class="description" style="background-color: white;
      font-family: muli, sans-serif; margin: 0px; padding: 30px 0px 0px;">
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Input 1 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">2
      3 4 5 2 6 1 9 -1
      5
      10 20 30 40 50 60 70 -1
      6
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Output 1 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">2
      -1
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Input 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1
      3 4 5 2 6 1 9 -1
      6
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      Sample Output 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">4
      </code></pre>
      <h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">
      &nbsp;An explanation for Sample Input 2 :</h5>
      <pre style="background-color: whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0,
      0.06) 0px 0px 4px 0px; font-family: muli, sans-serif; font-weight: 600; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: #626262; font-family: muli, sans-serif; font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">For the given singly
      linked list, considering the indices starting from 0, progressing in a left to right manner
      with a jump of 1, then the N = 6 appears at position 4.</code></pre>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/f00b489468c0b4998de29cb9b53e35d7.js"></script></div>


Write your content here...