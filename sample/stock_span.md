# Stock Span

Published: 2022-07-16T18:06:00.001+05:30

Description: 
      <div _ngcontent-orn-c711="" class="description ng-star-inserted"
      imageoverlay="" style="background-color: white; font-family: Muli, sans-serif; margin: 0px;
      padding: 30px 0px 0px;"><h4
      id="afzal-has-been-working-with-an-organization-called-39-money-traders-39-for-the-past-few-years-the-organization-is-into-the-money-trading-business-his-manager-assigned-him-a-task-for-a-given-array-list-of-stock-39-s-prices-for-n-days-find-the-stock-39-s-span-for-each-day"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">Afzal has been working with an organization
      called 'Money Traders' for the past few years. The organization is into the money trading
      business. His manager assigned him a task. For a given array/list of stock's prices for N
      days, find the stock's span for each day.</h4><h4
      id="the-span-of-the-stock-39-s-price-today-is-defined-as-the-maximum-number-of-consecutive-days-starting-from-today-and-going-backwards-for-which-the-price-of-the-stock-was-less-than-today-39-s-price"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">The span of the stock's price today is defined
      as the maximum number of consecutive days(starting from today and going backwards) for which
      the price of the stock was less than today's price.</h4><h4
      id="for-example-if-the-price-of-a-stock-over-a-period-of-7-days-are-100-80-60-70-60-75-85-then-the-stock-spans-will-be-1-1-1-2-1-4-6"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">For example, if the price of a stock over a
      period of 7 days are [100, 80, 60, 70, 60, 75, 85], then the stock spans will be [1, 1, 1, 2,
      1, 4, 6].</h4><h5 id="explanation" style="color: #2d2d2d; font-size: 15px; margin:
      0px; padding: 0px;">Explanation:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">On the sixth day when the price of the stock was 75,
      the span came out to be 4, because the last 4 prices(including the current price of 75) were
      less than the current or the sixth day's price.

      Similarly, we can deduce the remaining results.
      </code></pre><h4
      id="afzal-has-to-return-an-array-list-of-spans-corresponding-to-each-day-39-s-stock-39-s-price-help-him-to-achieve-the-task"
      style="color: #626262; font-size: 13px; font-weight: 400; letter-spacing: 0.3px; line-height:
      20px; margin: 0px; padding: 0px 0px 15px;">Afzal has to return an array/list of spans
      corresponding to each day's stock's price. Help him to achieve the task.</h4><h5
      id="input-format" style="color: #2d2d2d; font-size: 15px; margin: 0px; padding: 0px;">Input
      Format:</h5><pre style="background-color: whitesmoke; border-radius: 4px; box-shadow:
      rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: #626262; font-family: Muli,
      sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding:
      0px;">The first line of input contains an integer N, denoting the total number of days.

      The second line of input contains the stock prices of each day. A single space will separate
      them.
      </code></pre><h5 id="output-format" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Output Format:</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">The only line of output will print the span for each
      day's stock price. A single space will separate them.
      </code></pre><h5 id="note" style="color: #2d2d2d; font-size: 15px; margin: 0px;
      padding: 0px;">Note:</h5><pre style="background-color: whitesmoke; border-radius:
      4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif;
      font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden;
      padding: 15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family:
      Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px;
      padding: 0px;">You are not required to print the expected output explicitly. It has already
      been taken care of.
      </code></pre><h5 id="constraints" style="color: #2d2d2d; font-size: 15px;
      margin: 0px; padding: 0px;">Constraints:</h5><pre style="background-color:
      whitesmoke; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family:
      Muli, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">0 &lt;= N &lt;= 10^7
      1 &lt;= X &lt;= 10^9
      Where X denotes the stock's price for a day.

      Time Limit: 1 second
      </code></pre></div><div _ngcontent-orn-c711="" class="description
      ng-star-inserted" style="background-color: white; font-family: Muli, sans-serif; margin: 0px;
      padding: 30px 0px 0px;"><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px;
      padding: 0px;">Sample Input 1:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">4
      10 10 10 10
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 1:</h5><pre style="background-color: whitesmoke;
      border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli,
      sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px;
      overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code style="color:
      #626262; font-family: Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing:
      0.23px; margin: 0px; padding: 0px;">1 1 1 1
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Input 2:</h5><pre style="background-color: whitesmoke; border-radius:
      4px; box-shadow: rgba(0, 0, 0, 0.06) 0px 0px 4px 0px; font-family: Muli, sans-serif;
      font-weight: 600; margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden;
      padding: 15px 18px; white-space: pre-wrap;"><code style="color: #626262; font-family:
      Muli, sans-serif; font-size: 13px; font-weight: 400; letter-spacing: 0.23px; margin: 0px;
      padding: 0px;">8
      60 70 80 100 90 75 80 120
      </code></pre><h5 style="color: #2d2d2d; font-size: 15px; margin: 0px; padding:
      0px;">Sample Output 2:</h5></div><p><span style="background-color:
      whitesmoke; color: #626262; font-family: Muli, sans-serif; font-size: 13px; letter-spacing:
      0.23px; white-space: pre-wrap;">1 2 3 4 1 1 2 8
      </span>&nbsp;</p><p><br /></p><p><br
      /><script
      src="https://gist.github.com/Svastikkka/c010a53af5cee0adb90825ba98e0cc84.js"></script></p>

Write your content here...