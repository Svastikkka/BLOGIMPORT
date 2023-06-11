# Minimum Bracket Reversal

Published: 2022-07-16T18:11:00.002+05:30

Description: 
      <div _ngcontent-orn-c711="" class="description ng-star-inserted"
      imageoverlay="" style="background-color: white; font-family: Muli, sans-serif; margin: 0px;
      padding: 30px 0px 0px;"><h4
      id="for-a-given-expression-in-the-form-of-a-string-find-the-minimum-number-of-brackets-that-can-be-reversed-in-order-to-make-the-expression-balanced-the-expression-will-only-contain-curly-brackets"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">For a given expression in the form of a string,
      find the minimum number of brackets that can be reversed in order to make the expression
      balanced. The expression will only contain curly brackets.</h4><h4
      id="if-the-expression-can-39-t-be-balanced-return-1" style="color: #626262; font-size: 13px;
      font-weight: 400; letter-spacing: 0.3px; line-height: 20px; margin: 0px; padding: 0px 0px
      15px;">If the expression can't be balanced, return -1.</h4><h5 id="example"
      style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Example:</h5><pre style="background-color: whitesmoke; border-radius: 4px;
      box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight:
      600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding:
      15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">Expression: {{{{
      If we reverse the second and the fourth opening brackets, the whole expression will get
      balanced. Since we have to reverse two brackets to make the expression balanced, the expected
      output will be 2.

      Expression: {{{
      In this example, even if we reverse the last opening bracket, we would be left with the first
      opening bracket and hence will not be able to make the expression balanced and the output will
      be -1.
      </code></pre><h5 id="input-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Input Format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">The first and the only line of input contains a string
      expression, without any spaces in between.
      </code></pre><h5 id="output-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Output Format :</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">The only line of output will print the number of
      reversals required to balance the whole expression. Prints -1, otherwise.
      </code></pre><h5 id="note" style="color: #2d2d2d; font-size: 15px; margin: 0px;
      padding: 0px;">Note:</h5><pre style="background-color: whitesmoke; border-radius:
      4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif;
      font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden;
      padding: 15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family:
      Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px;
      padding: 0px;">You don't have to print anything. It has already been taken care of.
      </code></pre><h5 id="constraints" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Constraints:</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">0 &lt;= N &lt;= 10^6
      Where N is the length of the expression.

      Time Limit: 1sec
      </code></pre></div><div _ngcontent-orn-c711="" class="description
      ng-star-inserted" style="background-color: white; font-family: Muli, sans-serif; margin: 0px;
      padding: 30px 0px 0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px;
      padding: 0px;">Sample Input 1:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">{{{
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 1:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">-1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Input 2:</h5><pre style="background-color: whitesmoke; border-radius:
      4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif;
      font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden;
      padding: 15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family:
      Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px;
      padding: 0px;">{{{{}}
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 2:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">1</code></pre></div><p><br
      /></p><p><br /><script
      src="https://gist.github.com/Svastikkka/ce7e51b42c035624a71b4fdee0ae0ef7.js"></script></p><p>&nbsp;</p>

Write your content here...