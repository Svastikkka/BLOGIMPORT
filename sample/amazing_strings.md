# Amazing Strings

Published: 2021-05-02T22:40:00.002+05:30

Description: 
      <p><span style="background-color: white; color: #565656;
      font-size: 14px; letter-spacing: 0.3px;">Given 3 Strings, check whether the 3rd string
      contains all the characters of strings 1 and 2 in any order. If all the characters are
      present, print "YES" otherwise print "NO".</span></p><div
      _ngcontent-rho-c119="" class="description ng-star-inserted" style="-webkit-font-smoothing:
      antialiased; background-color: white; font-family: Roboto, sans-serif; font-size: 16px;
      margin: 0px; padding: 0px;"><h4
      id="there-should-not-be-any-extra-character-and-any-missing-character"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">There should
      not be any extra character and any missing character.</h4><h4
      id="the-string-s-contains-uppercase-latin-letters-only" style="-webkit-font-smoothing:
      antialiased; color: #565656; font-size: 14px; font-weight: 400; letter-spacing: 0.3px;
      line-height: 25px; margin: 0px; padding: 15px 0px 5px;">The string s contains uppercase
      Latin letters only.</h4><h5 id="input-format" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Input format :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">Line 1 : First String
      Line 2 : Second String
      Line 3 : Third String
      </code></pre><h5 id="output-format" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Output format :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">YES or NO
      </code></pre><h5 id="constraints" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Constraints :</h5><h4 id="1-lt-n-length-of-1st-amp-2nd-strings-lt-100"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;"><strong
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;"><em
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">1 &lt;= n
      (Length of 1st &amp; 2nd Strings) &lt;=
      100</em></strong></h4></div><div _ngcontent-rho-c119=""
      class="description ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: Roboto, sans-serif; font-size: 16px; margin: 0px;
      padding: 0px;"><h5 id="sample-input-1" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Sample Input 1 :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">SANTACLAUS
      DEDMOROZ
      SANTAMOROZDEDCLAUS
      </code></pre><h5 id="sample-output-1" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 1 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">YES
      </code></pre><h5 id="sample-input-2" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Input 2 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">PAPAINOEL
      JOULUPUKKI
      JOULNAPAOILELUPUKKI
      </code></pre><h5 id="sample-output-2" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 2 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">NO
      </code></pre><h5 id="sample-input-3" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Input 3 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">BABBONATALE
      FATHERCHRISTMAS
      BABCHRISTMASBONATALLEFATHER
      </code></pre><h5 id="sample-output-3" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 3 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">NO
      </code></pre><h5 id="sample-output-explanation" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output Explanation :</h5><h4
      id="output-1-the-letters-written-in-the-last-line-can-be-used-to-write-the-names-and-there-won-39-t-be-any-extra-letters-left"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Output 1:
      the letters written in the last line can be used to write the names and there won't be any
      extra letters left.</h4><h4
      id="output-2-letter-quot-p-quot-is-missing-and-there-39-s-an-extra-letter-quot-l-quot"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Output 2:
      Letter "P" is missing and there's an extra letter "L"</h4><h4
      id="output-3-there-39-s-an-extra-letter-quot-l-quot" style="-webkit-font-smoothing:
      antialiased; color: #565656; font-size: 14px; font-weight: 400; letter-spacing: 0.3px;
      line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Output 3: There's an extra letter
      "L"</h4></div>
      <script
      src="https://gist.github.com/Svastikkka/cf586420d63edf4483e607355ed46824.js"></script>

Write your content here...