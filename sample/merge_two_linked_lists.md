# Merge Two linked lists

Published: 2020-08-23T14:40:00.001+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div _ngcontent-mvi-c152="" class="padding" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: Roboto, sans-serif; font-size: 16px; margin: 0px;
      padding: 0px 0px 15px;">
      <div _ngcontent-mvi-c152="" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">
      Level&nbsp;MEDIUM</div>
      </div>
      <div _ngcontent-mvi-c152="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; margin: 0px; padding: 0px;">
      <h4
      id="given-two-linked-lists-sorted-in-increasing-order-merge-them-such-a-way-that-the-result-list-is-in-decreasing-order-reverse-order"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">
      Given two linked lists sorted in increasing order. Merge them such a way that the result list
      is in decreasing order (reverse order).</h4>
      <h4
      id="try-solving-without-reverse-with-o-1-auxiliary-space-in-place-and-only-one-traversal-of-both-lists-you-just-need-to-return-the-head-of-new-linked-list-don-39-t-print-the-elements"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">
      Try solving without reverse, with O(1) auxiliary space (in-place) and only one traversal of
      both lists. You just need to return the head of the new linked list, don't print the
      elements.</h4>
      <h5 id="input-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Input format :</h5>
      <pre style="background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding: 25px;
      text-align: left;"><code style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">Line 1 : Linked list 1 elements of length n (separated by
      space</code></pre>
      <pre style="background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;open sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding: 25px;
      text-align: left;"><code style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">and terminated by -1)
      Line 2 : Linked list 2 elements of length m (separated by space </code></pre>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">and terminated by
      -1)
      </code></pre>
      <h5 id="output-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Output format :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">Merged list
      elements (separated by space)
      </code></pre>
      <h5 id="constraints" style="-webkit-font-smoothing: antialiased; color: #353535; font-size:
      14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Constraints :</h5>
      <h4 id="1-lt-n-m-lt-10-4" style="-webkit-font-smoothing: antialiased; color: #565656;
      font-size: 14px; font-weight: 400; letter-spacing: 0.3px; line-height: 25px; margin: 0px;
      padding: 15px 0px 5px;">
      <strong style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"><em
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">1 &lt;= n, m
      &lt;= 10^4</em></strong></h4>
      </div>
      <div _ngcontent-mvi-c152="" class="description ng-star-inserted" style="margin: 0px;
      padding: 0px;">
      <h5 id="sample-input" style="background-color: white; color: #353535; font-family: roboto,
      sans-serif; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Input :</h5>
      <pre style="background-color: white; background-image: linear-gradient(-90deg, rgba(255,
      205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;open sans&quot;,
      sans-serif; font-size: 16px; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"> 2 5 8 12 -1
      3 6 9 -1
      </code></pre>
      <h4
      id="note-1-at-the-end-of-input-is-just-a-terminator-representing-the-end-of-linked-list-this-1-is-not-part-of-the-linked-list-size-of-1st-linked-list-is-4-and-that-of-2nd-linked-list-is-3"
      style="background-color: white; color: #565656; font-family: roboto, sans-serif; font-size:
      14px; font-weight: 400; letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px
      0px 5px;">
      Note: -1 at the end of input is just a terminator representing the end of the linked list.
      This -1 is not part of the linked list. Size of 1st linked list is 4 and that of 2nd linked
      list is 3.</h4>
      <div>
      <br />
      <span style="background-color: white; color: #353535; font-family:
      &quot;roboto&quot; , sans-serif; font-size: 14px; letter-spacing: 0.4px;">Sample
      Output :</span></div>
      <pre style="background-color: white; background-image: linear-gradient(-90deg, rgba(255,
      205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;open sans&quot;,
      sans-serif; font-size: 16px; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: scroll; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"> 12 9 8 6 5 3 2
      </code></pre>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/c28c6ac3b971001f96ef0eed98fadff1.js"></script>
      </div>


Write your content here...