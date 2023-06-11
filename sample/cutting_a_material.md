#  Cutting a material

Published: 2020-07-26T23:36:00.000+05:30

Description: 
      You are given a disk-shaped or circular material. Determine the maximum
      number of pieces&nbsp;in which the&nbsp;material can be cut into by using
      exactly&nbsp;<span class="mathjax-latex"><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-1-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.009ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -748.3 888.5 865.1" width="2.064ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M234 637Q231 637 226
      637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181
      616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643
      679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880
      642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261
      344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100
      2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287
      635 234 637Z" id="E1-MJMATHI-4E" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E1-MJMATHI-4E"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></span></span>&nbsp;straight
      cuts.<p></p><p>You must perform the task for<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-2-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.009ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -748.3 704.5 865.1" width="1.636ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M40 437Q21 437 21 445Q21
      450 37 501T71 602L88 651Q93 669 101 677H569H659Q691 677 697 676T704 667Q704 661 687 553T668
      444Q668 437 649 437Q640 437 637 437T631 442L629 445Q629 451 635 490T641 551Q641 586 628
      604T573 629Q568 630 515 631Q469 631 457 630T439 622Q438 621 368 343T298 60Q298 48 386 46Q418
      46 427 45T436 36Q436 31 433 22Q429 4 424 1L422 0Q419 0 415 0Q410 0 363 1T228 2Q99 2 64 0H49Q43
      6 43 9T45 27Q49 40 55 46H83H94Q174 46 189 55Q190 56 191 56Q196 59 201 76T241 233Q258 301 269
      344Q339 619 339 625Q339 630 310 630H279Q212 630 191 624Q146 614 121 583T67 467Q60 445 57
      441T43 437H40Z" id="E2-MJMATHI-54" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E2-MJMATHI-54"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>tasks
      separately.</span></p><p><span style="font-weight: 600;">Input
      format</span></p><ul style="padding-left: 40px;"><li
      style="margin-bottom: 5px;">The first line contains<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-3-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.009ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -748.3 704.5 865.1" width="1.636ex"
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>denoting&nbsp;the number of test
      cases.</span></li><li style="margin-bottom: 5px;">Next<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-4-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.009ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -748.3 704.5 865.1" width="1.636ex"
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
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>lines contain a single integer<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-5-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.009ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -748.3 888.5 865.1" width="2.064ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M234 637Q231 637 226
      637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181
      616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643
      679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880
      642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261
      344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100
      2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287
      635 234 637Z" id="E5-MJMATHI-4E" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E5-MJMATHI-4E"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></span></span>.</span></span></li></ul><p><span
      style="font-weight: 600;">Output format</span></p><p>Print<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-6-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.009ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -748.3 704.5 865.1" width="1.636ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M40 437Q21 437 21 445Q21
      450 37 501T71 602L88 651Q93 669 101 677H569H659Q691 677 697 676T704 667Q704 661 687 553T668
      444Q668 437 649 437Q640 437 637 437T631 442L629 445Q629 451 635 490T641 551Q641 586 628
      604T573 629Q568 630 515 631Q469 631 457 630T439 622Q438 621 368 343T298 60Q298 48 386 46Q418
      46 427 45T436 36Q436 31 433 22Q429 4 424 1L422 0Q419 0 415 0Q410 0 363 1T228 2Q99 2 64 0H49Q43
      6 43 9T45 27Q49 40 55 46H83H94Q174 46 189 55Q190 56 191 56Q196 59 201 76T241 233Q258 301 269
      344Q339 619 339 625Q339 630 310 630H279Q212 630 191 624Q146 614 121 583T67 467Q60 445 57
      441T43 437H40Z" id="E6-MJMATHI-54" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E6-MJMATHI-54"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>separate lines each containing answer
      for each test case.</span></p><p><span style="font-weight:
      600;">Note</span>:<span style="font-weight: 600;">&nbsp;</span>Use a
      64-bit variable to store and read all the variables.</p><p><span
      style="font-weight: 600;">Constraints</span></p><p><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;5&lt;/mn&gt;&lt;/msup&gt;&lt;mspace
      linebreak=&quot;newline&quot;
      /&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;8&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-7-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="6.143ex" role="img" style="vertical-align:
      -3.871ex;" viewbox="0 -977.9 5512 2644.7" width="12.802ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M213 578L200 573Q186 568
      160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302
      660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46
      152 46T177 47T193 50T201 52T207 57T213 61V578Z" id="E7-MJMAIN-31"
      stroke-width="1"></path><path d="M674 636Q682 636 688 630T694 615T687 601Q686 600
      417 472L151 346L399 228Q687 92 691 87Q694 81 694 76Q694 58 676 56H670L382 192Q92 329 90 331Q83
      336 83 348Q84 359 96 365Q104 369 382 500T665 634Q669 636 674 636ZM84 -118Q84 -108 99
      -98H678Q694 -104 694 -118Q694 -130 679 -138H98Q84 -131 84 -118Z" id="E7-MJMAIN-2264"
      stroke-width="1"></path><path d="M40 437Q21 437 21 445Q21 450 37 501T71 602L88
      651Q93 669 101 677H569H659Q691 677 697 676T704 667Q704 661 687 553T668 444Q668 437 649 437Q640
      437 637 437T631 442L629 445Q629 451 635 490T641 551Q641 586 628 604T573 629Q568 630 515
      631Q469 631 457 630T439 622Q438 621 368 343T298 60Q298 48 386 46Q418 46 427 45T436 36Q436 31
      433 22Q429 4 424 1L422 0Q419 0 415 0Q410 0 363 1T228 2Q99 2 64 0H49Q43 6 43 9T45 27Q49 40 55
      46H83H94Q174 46 189 55Q190 56 191 56Q196 59 201 76T241 233Q258 301 269 344Q339 619 339 625Q339
      630 310 630H279Q212 630 191 624Q146 614 121 583T67 467Q60 445 57 441T43 437H40Z"
      id="E7-MJMATHI-54" stroke-width="1"></path><path d="M96 585Q152 666 249 666Q297
      666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198
      -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571
      145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362
      478 354 524T321 597Z" id="E7-MJMAIN-30" stroke-width="1"></path><path d="M164
      157Q164 133 148 117T109 101H102Q148 22 224 22Q294 22 326 82Q345 115 345 210Q345 313 318
      349Q292 382 260 382H254Q176 382 136 314Q132 307 129 306T114 304Q97 304 95 310Q93 314 93
      485V614Q93 664 98 664Q100 666 102 666Q103 666 123 658T178 642T253 634Q324 634 389 662Q397 666
      402 666Q410 666 410 648V635Q328 538 205 538Q174 538 149 544L139 546V374Q158 388 169 396T205
      412T256 420Q337 420 393 355T449 201Q449 109 385 44T229 -22Q148 -22 99 32T50 154Q50 178 61
      192T84 210T107 214Q132 214 148 197T164 157Z" id="E7-MJMAIN-35"
      stroke-width="1"></path><path d="M234 637Q231 637 226 637Q201 637 196 638T191
      649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592
      723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684
      682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633
      769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268
      46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14
      34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"
      id="E7-MJMATHI-4E" stroke-width="1"></path><path d="M70 417T70 494T124 618T248
      666Q319 666 374 624T429 515Q429 485 418 459T392 417T361 389T335 371T324 363L338 354Q352 344
      366 334T382 323Q457 264 457 174Q457 95 399 37T249 -22Q159 -22 101 29T43 155Q43 263 172 335L154
      348Q133 361 127 368Q70 417 70 494ZM286 386L292 390Q298 394 301 396T311 403T323 413T334 425T345
      438T355 454T364 471T369 491T371 513Q371 556 342 586T275 624Q268 625 242 625Q201 625 165
      599T128 534Q128 511 141 492T167 463T217 431Q224 426 228 424L286 386ZM250 21Q308 21 350 55T392
      137Q392 154 387 169T375 194T353 216T330 234T301 253T274 270Q260 279 244 289T218 306L210
      311Q204 311 181 294T133 239T107 157Q107 98 150 60T250 21Z" id="E7-MJMAIN-38"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E7-MJMAIN-31" y="0"></use><use x="778" xlink:href="#E7-MJMAIN-2264"
      y="0"></use><use x="1834" xlink:href="#E7-MJMATHI-54" y="0"></use><use
      x="2816" xlink:href="#E7-MJMAIN-2264" y="0"></use><g
      transform="translate(3873,0)"><use xlink:href="#E7-MJMAIN-31"></use><use
      x="500" xlink:href="#E7-MJMAIN-30" y="0"></use><use transform="scale(0.707)"
      x="1415" xlink:href="#E7-MJMAIN-35" y="557"></use></g><g
      transform="translate(0,-1436)"><use x="0" xlink:href="#E7-MJMAIN-30"
      y="0"></use><use x="778" xlink:href="#E7-MJMAIN-2264" y="0"></use><use
      x="1834" xlink:href="#E7-MJMATHI-4E" y="0"></use><use x="3000"
      xlink:href="#E7-MJMAIN-2264" y="0"></use><g
      transform="translate(4057,0)"><use xlink:href="#E7-MJMAIN-31"></use><use
      x="500" xlink:href="#E7-MJMAIN-30" y="0"></use><use transform="scale(0.707)"
      x="1415" xlink:href="#E7-MJMAIN-38"
      y="557"></use></g></g></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>T</mi><mo>≤</mo><msup><mn>10</mn><mn>5</mn></msup><mspace
      linebreak="newline"></mspace><mn>0</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><msup><mn>10</mn><mn>8</mn></msup></math></span></span></span></p><div
      class="less-margin-2 input-output-container" style="border-radius: 3px; border: 1px solid
      rgb(229, 231, 232); font-size: 14px; line-height: 21px; margin: 10px 0px 0px;"><div
      class="input-output right-border" style="border-right: 1px solid rgb(229, 231, 232);
      box-sizing: border-box; float: left; overflow-x: auto; white-space: nowrap; width:
      330.5px;"><div class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232);
      color: #252c33; padding: 6px 10px;"><div class="weight-600 less-margin-right light
      float-left small" style="color: #9ca3a8; float: left; font-size: 12px; font-weight: 600;
      margin-right: 5px;">SAMPLE INPUT</div><div class="input-output-opt float-right"
      style="float: right;"><a class="track-problem-sample-input tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/july-circuits-20/problems/b6114b78c74d11ea.txt?Signature=30xn%2BEUVMV0GcQ1uKtvzIluZU7w%3D&amp;Expires=1595790179&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
      style="color: #4c9cdf; cursor: pointer; font-size: 16px; margin: 0px 5px;
      text-decoration-line: none;" target="_blank"><span class="fa fa-link"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; line-height: 1; text-rendering:
      auto;"></span></a><span
      class="Apple-converted-space">&nbsp;</span><a
      class="track-problem-sample-input-copy input-output-copy tool-tip" style="color: #4c9cdf;
      cursor: pointer; font-size: 16px; margin: 0px 5px;"><span class="fa fa-files-o"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; line-height: 1; text-rendering:
      auto;"></span></a></div><div class="clear" style="clear:
      both;"></div></div><div class="dark" style="color: #46535e;"><pre
      class="word-spacing-0" style="margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word;
      overflow-x: auto; padding: 10px; white-space: pre-wrap;">2
      0
      4</pre></div></div><div class="input-output" style="box-sizing:
      border-box; float: left; overflow-x: auto; white-space: nowrap; width: 330.5px;"><div
      class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); color: #252c33;
      padding: 6px 10px;"><div class="weight-600 float-left less-margin-right light small"
      style="color: #9ca3a8; float: left; font-size: 12px; font-weight: 600; margin-right:
      5px;">SAMPLE OUTPUT</div><div class="input-output-opt float-right" style="float:
      right;"><a class="track-problem-sample-output tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/july-circuits-20/problems/b60ac0dcc74d11ea.txt?Signature=Ovr1vRrC9FGjqyU%2BPooOmoBri9A%3D&amp;Expires=1595790179&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
      style="color: #4c9cdf; cursor: pointer; font-size: 16px; margin: 0px 5px;
      text-decoration-line: none;" target="_blank"><span class="fa fa-link"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; line-height: 1; text-rendering:
      auto;"></span></a><span
      class="Apple-converted-space">&nbsp;</span><a
      class="track-problem-sample-output-copy input-output-copy tool-tip" style="color: #4c9cdf;
      cursor: pointer; font-size: 16px; margin: 0px 5px;"><span class="fa fa-files-o"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; line-height: 1; text-rendering:
      auto;"></span></a></div><div class="clear" style="clear:
      both;"></div></div><div class="dark" style="color: #46535e;"><pre
      class="word-spacing-0" style="margin-bottom: 0px; margin-top: 0px; overflow-wrap: break-word;
      overflow-x: auto; padding: 10px; white-space: pre-wrap;">1
      11</pre></div></div><div class="clear" style="clear:
      both;"></div></div><div class="standard-margin" style="margin: 30px 0px
      0px;"><span class="weight-600 form-label" style="color: #252c33; font-size: 14px;
      font-weight: 600;">Explanation</span><div class="less-margin" style="margin: 5px
      0px 0px;"><p>For the first case where N = 0, using 0 cuts you&nbsp;can get a
      maximum of 1 piece of the material.</p><p>For the second case where N = 4, using
      exactly 4 straight cuts you&nbsp;can get 11 pieces of
      material.</p></div></div></span>
      <script
      src="https://gist.github.com/Svastikkka/17b4ff266b64c00a927554ccc024074a.js"></script>

Write your content here...