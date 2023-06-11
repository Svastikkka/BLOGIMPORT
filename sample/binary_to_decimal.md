# Binary to decimal

Published: 2020-05-29T20:39:00.001+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      <div _ngcontent-oap-c147="" class="padding" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: Roboto, sans-serif; font-size: 16px;
      font-variant-ligatures: normal; margin: 0px; orphans: 2; padding: 0px 0px 15px; widows:
      2;">
      <div _ngcontent-oap-c147="" style="-webkit-font-smoothing: antialiased; margin: 0px;
      padding: 0px;">
      Level&nbsp;EASY</div>
      </div>
      <div _ngcontent-oap-c147="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; font-variant-ligatures: normal; margin: 0px; orphans: 2; padding:
      0px; widows: 2;">
      <h4 id="given-a-binary-number-as-an-integer-n-convert-it-into-decimal-and-print"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">
      Given a binary number as an integer N, convert it into decimal and print.</h4>
      <h5 id="input-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Input format :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">An integer N in the
      Binary Format
      </code></pre>
      <h5 id="output-format" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Output format :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">Corresponding
      Decimal number (as integer)
      </code></pre>
      <h5 id="constraints" style="-webkit-font-smoothing: antialiased; color: #353535; font-size:
      14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Constraints :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">0 &lt;= N
      &lt;= 10^9
      </code></pre>
      </div>
      <div _ngcontent-oap-c147="" class="description ng-star-inserted"
      style="-webkit-font-smoothing: antialiased; background-color: white; font-family: Roboto,
      sans-serif; font-size: 16px; font-variant-ligatures: normal; margin: 0px; orphans: 2; padding:
      0px; widows: 2;">
      <h5 id="sample-input-1" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Input 1 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">1100
      </code></pre>
      <h5 id="sample-output-1" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Output 1 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">12
      </code></pre>
      <h5 id="sample-input-2" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Input 2 :</h5>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">111
      </code></pre>
      <h5 id="sample-output-2" style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">
      Sample Output 2 :</h5>
      <div>
      <br /></div>
      <div>
      <pre style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-variant-ligatures: normal; font-weight: 600; margin-bottom:
      20px; margin-top: 20px; max-width: 866px; orphans: 2; overflow-x: scroll; padding: 25px;
      widows: 2;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">7</code></pre>
      </div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      <div>
      <br /></div>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/11cacc1e456ce1e0e1a9a15463aa9214.js"></script></div>


Write your content here...