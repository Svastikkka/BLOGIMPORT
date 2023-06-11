#  Anti-palindrome strings

Published: 2020-09-05T17:58:00.001+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      You are given a string&nbsp;<span style="font-size: 14px; white-space: nowrap;
      word-spacing: normal;">S&nbsp;</span><span style="font-weight:
      600;">containing&nbsp;only lowercase alphabets.&nbsp;You can swap two adjacent
      characters any number of times (including 0).</span><br />
      <span style="font-weight: 600;"></span><br />
      <span style="font-weight: 600;">A string is called&nbsp;anti-palindrome&nbsp;if
      it is not a palindrome. If it is possible to make a string anti-palindrome, then find
      the&nbsp;lexicographically smallest anti-palindrome.<span
      class="Apple-converted-space">&nbsp;</span>Otherwise, print -1<span
      class="mathjax-latex"><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-2-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-weight: normal; line-height: normal; margin:
      0px; max-height: none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap:
      normal; padding: 0px; position: relative; white-space: nowrap; word-spacing: normal;"
      tabindex="0"><span class="MJX_Assistive_MathML" role="presentation" style="border: 0px
      !important; clip: rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important;
      left: 0px; overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute
      !important; top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px
      !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><mn>1</mn></math></span></span></span></span><br
      />
      <span style="font-weight: 600;">Input format</span><br />
      <ul style="padding-left: 40px;">
      <li style="margin-bottom: 5px;"><span style="font-weight: 600;">The first
      line&nbsp;contains a single integer&nbsp;<span class="mathjax-latex"><span
      class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax_SVG"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-3-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-weight: normal; line-height: normal; margin:
      0px; max-height: none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap:
      normal; padding: 0px; position: relative; white-space: nowrap; word-spacing: normal;"
      tabindex="0"><svg aria-hidden="true" focusable="false" height="2.009ex" role="img"
      style="vertical-align: -0.271ex;" viewbox="0 -748.3 704.5 865.1" width="1.636ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M40 437Q21 437 21 445Q21
      450 37 501T71 602L88 651Q93 669 101 677H569H659Q691 677 697 676T704 667Q704 661 687 553T668
      444Q668 437 649 437Q640 437 637 437T631 442L629 445Q629 451 635 490T641 551Q641 586 628
      604T573 629Q568 630 515 631Q469 631 457 630T439 622Q438 621 368 343T298 60Q298 48 386 46Q418
      46 427 45T436 36Q436 31 433 22Q429 4 424 1L422 0Q419 0 415 0Q410 0 363 1T228 2Q99 2 64 0H49Q43
      6 43 9T45 27Q49 40 55 46H83H94Q174 46 189 55Q190 56 191 56Q196 59 201 76T241 233Q258 301 269
      344Q339 619 339 625Q339 630 310 630H279Q212 630 191 624Q146 614 121 583T67 467Q60 445 57
      441T43 437H40Z" id="E3-MJMATHI-54" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E3-MJMATHI-54"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></span></span>&nbsp;denoting
      the number of test cases. The description of&nbsp;<span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-4-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-weight: normal; line-height: normal; margin:
      0px; max-height: none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap:
      normal; padding: 0px; position: relative; white-space: nowrap; word-spacing: normal;"
      tabindex="0"><svg aria-hidden="true" focusable="false" height="2.009ex" role="img"
      style="vertical-align: -0.271ex;" viewbox="0 -748.3 704.5 865.1" width="1.636ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M40 437Q21 437 21 445Q21
      450 37 501T71 602L88 651Q93 669 101 677H569H659Q691 677 697 676T704 667Q704 661 687 553T668
      444Q668 437 649 437Q640 437 637 437T631 442L629 445Q629 451 635 490T641 551Q641 586 628
      604T573 629Q568 630 515 631Q469 631 457 630T439 622Q438 621 368 343T298 60Q298 48 386 46Q418
      46 427 45T436 36Q436 31 433 22Q429 4 424 1L422 0Q419 0 415 0Q410 0 363 1T228 2Q99 2 64 0H49Q43
      6 43 9T45 27Q49 40 55 46H83H94Q174 46 189 55Q190 56 191 56Q196 59 201 76T241 233Q258 301 269
      344Q339 619 339 625Q339 630 310 630H279Q212 630 191 624Q146 614 121 583T67 467Q60 445 57
      441T43 437H40Z" id="E4-MJMATHI-54" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E4-MJMATHI-54"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></span></span>&nbsp;test
      cases follows.</span></span></span></li>
      <li style="margin-bottom: 5px;"><span style="font-weight: 600;">Each line contains
      a string&nbsp;<span class="mathjax-latex"><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-5-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-weight: normal; line-height: normal; margin:
      0px; max-height: none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap:
      normal; padding: 0px; position: relative; white-space: nowrap; word-spacing: normal;"
      tabindex="0"><svg aria-hidden="true" focusable="false" height="2.143ex" role="img"
      style="vertical-align: -0.271ex;" viewbox="0 -805.7 645.5 922.5" width="1.499ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M308 24Q367 24 416
      76T466 197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302
      673 343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627
      704T632 705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478
      551 494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263
      480 278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164
      528 137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65
      -22Q52 -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144
      186T142 153Q144 114 160 87T203 47T255 29T308 24Z" id="E5-MJMATHI-53"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E5-MJMATHI-53" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>of lower case alphabets
      only.</span></span></li>
      </ul>
      <br />
      <span style="font-weight: 600;">Output format</span><br />
      <span style="font-weight: 600;">For each test case, print the answer in a new
      line.</span><br />
      <span style="font-weight: 600;">Constraints</span><br />
      <span style="font-weight: 600;"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;100&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-6-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-weight: normal; line-height: normal; margin:
      0px; max-height: none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap:
      normal; padding: 0px; position: relative; white-space: nowrap; word-spacing: normal;"
      tabindex="0"><svg aria-hidden="true" focusable="false" height="2.276ex" role="img"
      style="vertical-align: -0.538ex;" viewbox="0 -748.3 5374.6 979.9" width="12.483ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M213 578L200 573Q186 568
      160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302
      660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46
      152 46T177 47T193 50T201 52T207 57T213 61V578Z" id="E6-MJMAIN-31"
      stroke-width="1"></path><path d="M674 636Q682 636 688 630T694 615T687 601Q686 600
      417 472L151 346L399 228Q687 92 691 87Q694 81 694 76Q694 58 676 56H670L382 192Q92 329 90 331Q83
      336 83 348Q84 359 96 365Q104 369 382 500T665 634Q669 636 674 636ZM84 -118Q84 -108 99
      -98H678Q694 -104 694 -118Q694 -130 679 -138H98Q84 -131 84 -118Z" id="E6-MJMAIN-2264"
      stroke-width="1"></path><path d="M40 437Q21 437 21 445Q21 450 37 501T71 602L88
      651Q93 669 101 677H569H659Q691 677 697 676T704 667Q704 661 687 553T668 444Q668 437 649 437Q640
      437 637 437T631 442L629 445Q629 451 635 490T641 551Q641 586 628 604T573 629Q568 630 515
      631Q469 631 457 630T439 622Q438 621 368 343T298 60Q298 48 386 46Q418 46 427 45T436 36Q436 31
      433 22Q429 4 424 1L422 0Q419 0 415 0Q410 0 363 1T228 2Q99 2 64 0H49Q43 6 43 9T45 27Q49 40 55
      46H83H94Q174 46 189 55Q190 56 191 56Q196 59 201 76T241 233Q258 301 269 344Q339 619 339 625Q339
      630 310 630H279Q212 630 191 624Q146 614 121 583T67 467Q60 445 57 441T43 437H40Z"
      id="E6-MJMATHI-54" stroke-width="1"></path><path d="M96 585Q152 666 249 666Q297
      666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198
      -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571
      145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362
      478 354 524T321 597Z" id="E6-MJMAIN-30" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E6-MJMAIN-31" y="0"></use><use x="778"
      xlink:href="#E6-MJMAIN-2264" y="0"></use><use x="1834" xlink:href="#E6-MJMATHI-54"
      y="0"></use><use x="2816" xlink:href="#E6-MJMAIN-2264" y="0"></use><g
      transform="translate(3873,0)"><use xlink:href="#E6-MJMAIN-31"></use><use
      x="500" xlink:href="#E6-MJMAIN-30" y="0"></use><use x="1001"
      xlink:href="#E6-MJMAIN-30" y="0"></use></g></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>T</mi><mo>≤</mo><mn>100</mn></math></span></span></span><br
      />
      <span style="font-weight: 600;"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;|&lt;/mo&gt;&lt;/mrow&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;|&lt;/mo&gt;&lt;/mrow&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;&amp;#x00D7;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;5&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-7-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-weight: normal; line-height: normal; margin:
      0px; max-height: none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap:
      normal; padding: 0px; position: relative; white-space: nowrap; word-spacing: normal;"
      tabindex="0"><svg aria-hidden="true" focusable="false" height="3.076ex" role="img"
      style="vertical-align: -0.805ex;" viewbox="0 -977.9 7549.5 1324.4" width="17.534ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M109 429Q82 429 66
      447T50 491Q50 562 103 614T235 666Q326 666 387 610T449 465Q449 422 429 383T381 315T301 241Q265
      210 201 149L142 93L218 92Q375 92 385 97Q392 99 409 186V189H449V186Q448 183 436 95T421
      3V0H50V19V31Q50 38 56 46T86 81Q115 113 136 137Q145 147 170 174T204 211T233 244T261 278T284
      308T305 340T320 369T333 401T340 431T343 464Q343 527 309 573T212 619Q179 619 154 602T119
      569T109 550Q109 549 114 549Q132 549 151 535T170 489Q170 464 154 447T109 429Z"
      id="E7-MJMAIN-32" stroke-width="1"></path><path d="M674 636Q682 636 688 630T694
      615T687 601Q686 600 417 472L151 346L399 228Q687 92 691 87Q694 81 694 76Q694 58 676 56H670L382
      192Q92 329 90 331Q83 336 83 348Q84 359 96 365Q104 369 382 500T665 634Q669 636 674 636ZM84
      -118Q84 -108 99 -98H678Q694 -104 694 -118Q694 -130 679 -138H98Q84 -131 84 -118Z"
      id="E7-MJMAIN-2264" stroke-width="1"></path><path d="M139 -249H137Q125 -249 119
      -235V251L120 737Q130 750 139 750Q152 750 159 735V-235Q151 -249 141 -249H139Z"
      id="E7-MJMAIN-7C" stroke-width="1"></path><path d="M308 24Q367 24 416 76T466
      197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302 673
      343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627 704T632
      705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478 551
      494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263 480
      278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164 528
      137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65 -22Q52
      -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144 186T142
      153Q144 114 160 87T203 47T255 29T308 24Z" id="E7-MJMATHI-53"
      stroke-width="1"></path><path d="M630 29Q630 9 609 9Q604 9 587 25T493 118L389
      222L284 117Q178 13 175 11Q171 9 168 9Q160 9 154 15T147 29Q147 36 161 51T255 146L359 250L255
      354Q174 435 161 449T147 471Q147 480 153 485T168 490Q173 490 175 489Q178 487 284 383L389
      278L493 382Q570 459 587 475T609 491Q630 491 630 471Q630 464 620 453T522 355L418 250L522
      145Q606 61 618 48T630 29Z" id="E7-MJMAIN-D7" stroke-width="1"></path><path d="M213
      578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285
      666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100
      0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" id="E7-MJMAIN-31"
      stroke-width="1"></path><path d="M96 585Q152 666 249 666Q297 666 345 640T423
      548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82
      83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137
      333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354
      524T321 597Z" id="E7-MJMAIN-30" stroke-width="1"></path><path d="M164 157Q164 133
      148 117T109 101H102Q148 22 224 22Q294 22 326 82Q345 115 345 210Q345 313 318 349Q292 382 260
      382H254Q176 382 136 314Q132 307 129 306T114 304Q97 304 95 310Q93 314 93 485V614Q93 664 98
      664Q100 666 102 666Q103 666 123 658T178 642T253 634Q324 634 389 662Q397 666 402 666Q410 666
      410 648V635Q328 538 205 538Q174 538 149 544L139 546V374Q158 388 169 396T205 412T256 420Q337
      420 393 355T449 201Q449 109 385 44T229 -22Q148 -22 99 32T50 154Q50 178 61 192T84 210T107
      214Q132 214 148 197T164 157Z" id="E7-MJMAIN-35"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E7-MJMAIN-32" y="0"></use><use x="778" xlink:href="#E7-MJMAIN-2264"
      y="0"></use><use x="1834" xlink:href="#E7-MJMAIN-7C" y="0"></use><use
      x="2113" xlink:href="#E7-MJMATHI-53" y="0"></use><use x="2758"
      xlink:href="#E7-MJMAIN-7C" y="0"></use><use x="3314" xlink:href="#E7-MJMAIN-2264"
      y="0"></use><use x="4371" xlink:href="#E7-MJMAIN-32" y="0"></use><use
      x="5093" xlink:href="#E7-MJMAIN-D7" y="0"></use><g
      transform="translate(6094,0)"><use xlink:href="#E7-MJMAIN-31"></use><use
      x="500" xlink:href="#E7-MJMAIN-30" y="0"></use><use transform="scale(0.707)"
      x="1415" xlink:href="#E7-MJMAIN-35"
      y="557"></use></g></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mrow
      class="MJX-TeXAtom-ORD"><mo
      stretchy="false">|</mo></mrow><mi>S</mi><mrow
      class="MJX-TeXAtom-ORD"><mo
      stretchy="false">|</mo></mrow><mo>≤</mo><mn>2</mn><mo>×</mo><msup><mn>10</mn><mn>5</mn></msup></math></span></span></span><br
      />
      <span style="font-weight: 600;"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-8-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-weight: normal; line-height: normal; margin:
      0px; max-height: none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap:
      normal; padding: 0px; position: relative; white-space: nowrap; word-spacing: normal;"
      tabindex="0"><svg aria-hidden="true" focusable="false" height="2.143ex" role="img"
      style="vertical-align: -0.271ex;" viewbox="0 -805.7 645.5 922.5" width="1.499ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M308 24Q367 24 416
      76T466 197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302
      673 343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627
      704T632 705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478
      551 494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263
      480 278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164
      528 137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65
      -22Q52 -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144
      186T142 153Q144 114 160 87T203 47T255 29T308 24Z" id="E8-MJMATHI-53"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E8-MJMATHI-53" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></span></span>&nbsp;contains
      only lowercase alphabets.</span><br />
      <div class="less-margin-2 input-output-container" style="border-radius: 3px; border: 1px
      solid rgb(229, 231, 232); font-size: 14px; line-height: 21px; margin: 10px 0px 0px;">
      <div class="input-output right-border" style="border-right: 1px solid rgb(229, 231, 232);
      box-sizing: border-box; float: left; overflow-x: auto; white-space: nowrap; width:
      330.5px;">
      <div class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); color: #252c33;
      padding: 6px 10px;">
      <div class="weight-600 less-margin-right light float-left small" style="color: #9ca3a8;
      float: left; font-size: 12px; font-weight: 600; margin-right: 5px;">
      SAMPLE INPUT</div>
      <div class="input-output-opt float-right" style="float: right;">
      </div>
      <div class="clear" style="clear: both;">
      </div>
      </div>
      <div class="dark" style="color: #46535e;">
      <pre class="word-spacing-0" style="margin-bottom: 0px; margin-top: 0px; overflow-wrap:
      break-word; overflow-x: auto; padding: 10px; white-space: pre-wrap;"><span
      style="font-weight: 600;">4
      bpc
      pp
      deep
      zyx</span></pre>
      </div>
      </div>
      <div class="input-output" style="box-sizing: border-box; float: left; overflow-x: auto;
      white-space: nowrap; width: 330.5px;">
      <div class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); color: #252c33;
      padding: 6px 10px;">
      <div class="weight-600 float-left less-margin-right light small" style="color: #9ca3a8;
      float: left; font-size: 12px; font-weight: 600; margin-right: 5px;">
      SAMPLE OUTPUT</div>
      <div class="input-output-opt float-right" style="float: right;">
      </div>
      <div class="clear" style="clear: both;">
      </div>
      </div>
      <div class="dark" style="color: #46535e;">
      <pre class="word-spacing-0" style="margin-bottom: 0px; margin-top: 0px; overflow-wrap:
      break-word; overflow-x: auto; padding: 10px; white-space: pre-wrap;"><span
      style="font-weight: 600;">bcp
      -1
      deep
      xyz
      </span></pre>
      </div>
      </div>
      <div class="clear" style="clear: both;">
      </div>
      </div>
      <div class="standard-margin" style="margin: 30px 0px 0px;">
      <span style="font-weight: 600;"><span class="weight-600 form-label" style="color:
      #252c33; font-size: 14px;">Explanation</span></span><br />
      <div class="less-margin" style="margin: 5px 0px 0px;">
      <ul style="padding-left: 40px;">
      <li style="margin-bottom: 5px;"><span style="font-weight: 600;">In the first test
      case, you&nbsp;can create "bcp" which is not a palindrome and it is
      a&nbsp;lexicographically-smallest string.</span></li>
      <li style="margin-bottom: 5px;"><span style="font-weight: 600;">In the second test
      case, you&nbsp;cannot form any anti palindrome.</span></li>
      </ul>
      </div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/c0b9e9f1a93de6fd08799ca90453d476.js"></script></div>


Write your content here...