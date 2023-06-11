# Division of 4

Published: 2021-03-28T23:57:00.005+05:30

Description: 
      <p>Level EASY<br /><br /><span
      style="background-color: white; font-size: 14px; letter-spacing: 0.3px;">Given an array,
      update each element of the array by the value obtained by dividing the element by 4 (take only
      integer part). If the value obtained by dividing the element by 4 comes out to be 0, then
      update the element with value -1.</span></p><h4
      id="note-do-not-return-or-print-array-and-make-changes-in-the-same-array" style="color:
      var(--text-general); font-family: Muli, sans-serif; font-size: 14px; letter-spacing: 0.3px;
      line-height: 22px; margin: 0px; padding: 0px 0px 15px;"><span style="background-color:
      white;">Note: Do not return or print the array and make changes in the same
      array.</span></h4><div><div _ngcontent-serverapp-c167=""
      class="description" style="color: rgba(0, 0, 0, 0.87); font-family: Muli, sans-serif; margin:
      0px; padding: 30px 0px 0px;"><h5 id="input-format" style="color: var(--text-title);
      font-family: var(--app-font); font-size: 14px; line-height: 22px; margin: 0px; padding: 0px;
      text-transform: capitalize;">Input Format :</h5><pre style="border-radius: 5px;
      color: var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: var(--block-color); font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">Line 1: An Integer N
      i.e. size of the array
      Line 2: N integers which are elements of the array, separated by spaces
      </code></pre><h5 id="output-format" style="color: var(--text-title);
      font-family: var(--app-font); font-size: 14px; line-height: 22px; margin: 0px; padding: 0px;
      text-transform: capitalize;">Output Format :</h5><pre style="border-radius: 5px;
      color: var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: var(--block-color); font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">N elements of the
      array, separated by space
      </code></pre><h5 id="constraints" style="color: var(--text-title); font-family:
      var(--app-font); font-size: 14px; line-height: 22px; margin: 0px; padding: 0px;
      text-transform: capitalize;">Constraints :</h5><pre style="border-radius: 5px;
      color: var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: var(--block-color); font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">1 &lt;= N
      &lt;= 10^5
      0 &lt;= array[i] &lt;= 100

      Time Limit: 1 sec
      </code></pre></div><div _ngcontent-serverapp-c167="" class="description"
      style="color: rgba(0, 0, 0, 0.87); font-family: Muli, sans-serif; margin: 0px; padding: 30px
      0px 0px;"><h5 style="color: var(--text-title); font-family: var(--app-font); font-size:
      14px; line-height: 22px; margin: 0px; padding: 0px; text-transform: capitalize;">Sample
      Input :</h5><pre style="border-radius: 5px; color: var(--block-color); font-size:
      14px; font-weight: 600; line-height: 20px; margin-bottom: 20px; margin-top: 10px; max-width:
      866px; overflow-x: hidden; padding: 15px 18px; white-space: pre-wrap;"><code
      style="color: var(--block-color); font-size: 13px; font-weight: 400; letter-spacing: 0.23px;
      margin: 0px; padding: 0px;"> 2
      3 8
      </code></pre><h5 style="color: var(--text-title); font-family: var(--app-font);
      font-size: 14px; line-height: 22px; margin: 0px; padding: 0px; text-transform:
      capitalize;">Sample Output :</h5><pre style="border-radius: 5px; color:
      var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px; margin-bottom: 20px;
      margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px 18px; white-space:
      pre-wrap;"><code style="color: var(--block-color); font-size: 13px; font-weight: 400;
      letter-spacing: 0.23px; margin: 0px; padding: 0px;"> -1 2
      </code></pre><h5 style="color: var(--text-title); font-family: var(--app-font);
      font-size: 14px; line-height: 22px; margin: 0px; padding: 0px; text-transform:
      capitalize;">Sample Output Explanation :</h5><pre style="border-radius: 5px;
      color: var(--block-color); font-size: 14px; font-weight: 600; line-height: 20px;
      margin-bottom: 20px; margin-top: 10px; max-width: 866px; overflow-x: hidden; padding: 15px
      18px; white-space: pre-wrap;"><code style="color: var(--block-color); font-size: 13px;
      font-weight: 400; letter-spacing: 0.23px; margin: 0px; padding: 0px;">The input list is [
      3, 8 ] , after dividing each element by 4, our list becomes [ 0, 2 ] . So as the first element
      is 0 so replace it by -1.</code></pre></div></div>
      <script
      src="https://gist.github.com/Svastikkka/0bb20baa50dd55413f460a97f1c95430.js"></script>

Write your content here...