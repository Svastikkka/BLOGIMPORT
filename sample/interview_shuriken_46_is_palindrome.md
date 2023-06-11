# Interview Shuriken 46: Is Palindrome

Published: 2020-08-10T20:56:00.001+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div _ngcontent-yip-c152="" class="padding" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: Roboto, sans-serif; font-size: 16px; margin: 0px;
      padding: 0px 0px 15px;">
      <div _ngcontent-yip-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">
      <a _ngcontent-yip-c152="" class="key" href="https://www.blogger.com/null"
      style="-webkit-font-smoothing: antialiased; color: #b3b3b3; font-size: 12px; letter-spacing:
      0.27px; line-height: 30px; margin: 0px; padding: 0px;">Level</a><a
      _ngcontent-yip-c152="" class="value" href="https://www.blogger.com/null"
      style="-webkit-font-smoothing: antialiased; color: #656565; font-size: 12px; font-weight: 700;
      letter-spacing: 0.27px; line-height: 30px; margin: 0px; padding: 0px 0px 0px
      8px;">&nbsp;EASY</a></div>
      </div>
      <div _ngcontent-yip-c152="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px;">
      <h4 id="this-problem-was-asked-in-snapdeal-microsoft-and-amazon"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">
      This problem was asked in Snapdeal, Microsoft and Amazon.</h4>
      <h4
      id="given-a-singly-linked-list-you-have-to-find-out-whether-it-is-a-palindrome-or-not-for-example-if-the-given-linked-list-is-1-gt-2-gt-3-gt-2-gt-1-gt-null-then-the-output-should-be-true"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">
      Given a singly linked list, you have to find out whether it is a palindrome or not. For
      example, if the given linked list is 1 -&gt; 2 -&gt; 3 -&gt; 2 -&gt; 1
      -&gt; null, then the output should be true.</h4>
      <h4
      id="follow-up-try-doing-it-in-o-n-time-complexity-here-n-is-the-number-of-nodes-in-the-linked-list-and-o-1-space-complexity"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">
      Follow up: Try doing it in O(n) time complexity, here, n is the number of nodes in the linked
      list and O(1) space complexity.</h4>
      <h5 id="input-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Input Format:</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">The first and only
      line of input contains space separated integers,</code></pre>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"> terminated by -1.
      These integers form data of nodes of linked list.
      </code></pre>
      <h5 id="output-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Output Format:</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">The first and only
      line of output contains true, if the linked list</code></pre>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"> is palindrome or
      false, if the linked list is not palindrome.
      </code></pre>
      </div>
      <div _ngcontent-yip-c152="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px;">
      <h5 id="sample-input-1" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Input 1 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">9 2 3 3 2 9 -1
      </code></pre>
      <h5 id="sample-output-1" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Output 1 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">true
      </code></pre>
      <h5 id="sample-input-2" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Input 2 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">0 2 3 2 5 -1
      </code></pre>
      <h5 id="sample-output-2" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Output 2 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: scroll; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">false</code></pre>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/a8b2826011ef73e92b88f71b6e5b2d29.js"></script>
      </div>


Write your content here...