#  Fitting circles

Published: 2020-09-05T22:17:00.000+05:30

Description: 
      <div dir="ltr" style="text-align: left;" trbidi="on">
      You are given a rectangle of length<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-1-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="1.476ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -518.7 529.5 635.5" width="1.23ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M33 157Q33 258 109
      349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374
      43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506
      144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299
      52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323
      385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179
      26Q217 26 254 59T298 110Q300 114 325 217T351 328Z" id="E1-MJMATHI-61"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E1-MJMATHI-61" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>and width<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-2-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.143ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -805.7 429.5 922.5" width="0.998ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M73 647Q73 657 77 670T89
      683Q90 683 161 688T234 694Q246 694 246 685T212 542Q204 508 195 472T180 418L176 399Q176 396 182
      402Q231 442 283 442Q345 442 383 396T422 280Q422 169 343 79T173 -11Q123 -11 82 27T40 150V159Q40
      180 48 217T97 414Q147 611 147 623T109 637Q104 637 101 637H96Q86 637 83 637T76 640T73 647ZM336
      325V331Q336 405 275 405Q258 405 240 397T207 376T181 352T163 330L157 322L136 236Q114 150 114
      114Q114 66 138 42Q154 26 178 26Q211 26 245 58Q270 81 285 114T318 219Q336 291 336 325Z"
      id="E2-MJMATHI-62" stroke-width="1"></path></defs><g fill="currentColor"
      stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E2-MJMATHI-62" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></span></span>.
      You are required to determine a circle that contains the maximum circumference that fits
      inside the rectangle. This type of circle is called a big circle. Your task is to determine
      the maximum number of big circles that can fit inside the
      rectangle.&nbsp;</span></span><br />
      <br />
      <span style="font-weight: 600;">Input format</span><br />
      <ul style="padding-left: 40px;">
      <li style="margin-bottom: 5px;">First line: An integer<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-3-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="1.876ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -690.9 361.5 807.7" width="0.84ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M26 385Q19 392 19 395Q19
      399 22 411T27 425Q29 430 36 430T87 431H140L159 511Q162 522 166 540T173 566T179 586T187 603T197
      615T211 624T229 626Q247 625 254 615T261 596Q261 589 252 549T232 470L222 433Q222 431 272
      431H323Q330 424 330 420Q330 398 317 385H210L174 240Q135 80 135 68Q135 26 162 26Q197 26 230
      60T283 144Q285 150 288 151T303 153H307Q322 153 322 145Q322 142 319 133Q314 117 301 95T267
      48T216 6T155 -11Q125 -11 98 4T59 56Q57 64 57 83V101L92 241Q127 382 128 383Q128 385 77 385H26Z"
      id="E3-MJMATHI-74" stroke-width="1"></path></defs><g fill="currentColor"
      stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E3-MJMATHI-74" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></span></span>&nbsp;denoting
      the number of test cases</span></li>
      <li style="margin-bottom: 5px;">First line of each test case: Integers<span
      class="Apple-converted-space">&nbsp;</span><span style="font-weight:
      600;"><em><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-4-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="1.476ex" role="img" style="vertical-align: -0.271ex;" viewbox="0 -518.7 529.5 635.5"
      width="1.23ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M33
      157Q33 258 109 349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412
      234T374 68Q374 43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483
      153H487Q506 153 506 144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336
      5T306 36L300 51Q299 52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351
      334 346 350T323 385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118
      106Q118 61 136 44T179 26Q217 26 254 59T298 110Q300 114 325 217T351 328Z" id="E4-MJMATHI-61"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E4-MJMATHI-61" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>and<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-5-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="2.143ex" role="img" style="vertical-align: -0.271ex;" viewbox="0 -805.7 429.5 922.5"
      width="0.998ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M73
      647Q73 657 77 670T89 683Q90 683 161 688T234 694Q246 694 246 685T212 542Q204 508 195 472T180
      418L176 399Q176 396 182 402Q231 442 283 442Q345 442 383 396T422 280Q422 169 343 79T173 -11Q123
      -11 82 27T40 150V159Q40 180 48 217T97 414Q147 611 147 623T109 637Q104 637 101 637H96Q86 637 83
      637T76 640T73 647ZM336 325V331Q336 405 275 405Q258 405 240 397T207 376T181 352T163 330L157
      322L136 236Q114 150 114 114Q114 66 138 42Q154 26 178 26Q211 26 245 58Q270 81 285 114T318
      219Q336 291 336 325Z" id="E5-MJMATHI-62" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E5-MJMATHI-62"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></span></span></span></em></span></li>
      </ul>
      <span style="font-weight: 600;"><em>Output format</em></span><br
      />
      <span style="font-weight: 600;"><em>For each test case, print the answer on a new
      line denoting&nbsp;the maximum number of big circles that can fit in the provided
      rectangle. &nbsp;</em></span><br />
      <span style="font-weight: 600;"><em>Constraints</em></span><br
      />
      <span style="font-weight: 600;"><em><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mn&gt;1000&lt;/mn&gt;&lt;mspace
      linebreak=&quot;newline&quot;
      /&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;9&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-6-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="5.743ex" role="img" style="vertical-align: -4.005ex;" viewbox="0 -748.3 6027.7 2472.5"
      width="14ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M213
      578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285
      666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100
      0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" id="E6-MJMAIN-31"
      stroke-width="1"></path><path d="M674 636Q682 636 688 630T694 615T687 601Q686 600
      417 472L151 346L399 228Q687 92 691 87Q694 81 694 76Q694 58 676 56H670L382 192Q92 329 90 331Q83
      336 83 348Q84 359 96 365Q104 369 382 500T665 634Q669 636 674 636ZM84 -118Q84 -108 99
      -98H678Q694 -104 694 -118Q694 -130 679 -138H98Q84 -131 84 -118Z" id="E6-MJMAIN-2264"
      stroke-width="1"></path><path d="M26 385Q19 392 19 395Q19 399 22 411T27 425Q29 430
      36 430T87 431H140L159 511Q162 522 166 540T173 566T179 586T187 603T197 615T211 624T229 626Q247
      625 254 615T261 596Q261 589 252 549T232 470L222 433Q222 431 272 431H323Q330 424 330 420Q330
      398 317 385H210L174 240Q135 80 135 68Q135 26 162 26Q197 26 230 60T283 144Q285 150 288 151T303
      153H307Q322 153 322 145Q322 142 319 133Q314 117 301 95T267 48T216 6T155 -11Q125 -11 98 4T59
      56Q57 64 57 83V101L92 241Q127 382 128 383Q128 385 77 385H26Z" id="E6-MJMATHI-74"
      stroke-width="1"></path><path d="M96 585Q152 666 249 666Q297 666 345 640T423
      548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82
      83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137
      333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354
      524T321 597Z" id="E6-MJMAIN-30" stroke-width="1"></path><path d="M33 157Q33 258
      109 349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374
      68Q374 43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506
      153 506 144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306
      36L300 51Q299 52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334
      346 350T323 385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61
      136 44T179 26Q217 26 254 59T298 110Q300 114 325 217T351 328Z" id="E6-MJMATHI-61"
      stroke-width="1"></path><path d="M78 35T78 60T94 103T137 121Q165 121 187 96T210
      8Q210 -27 201 -60T180 -117T154 -158T130 -185T117 -194Q113 -194 104 -185T95 -172Q95 -168 106
      -156T131 -126T157 -76T173 -3V9L172 8Q170 7 167 6T161 3T152 1T140 0Q113 0 96 17Z"
      id="E6-MJMAIN-2C" stroke-width="1"></path><path d="M73 647Q73 657 77 670T89 683Q90
      683 161 688T234 694Q246 694 246 685T212 542Q204 508 195 472T180 418L176 399Q176 396 182
      402Q231 442 283 442Q345 442 383 396T422 280Q422 169 343 79T173 -11Q123 -11 82 27T40 150V159Q40
      180 48 217T97 414Q147 611 147 623T109 637Q104 637 101 637H96Q86 637 83 637T76 640T73 647ZM336
      325V331Q336 405 275 405Q258 405 240 397T207 376T181 352T163 330L157 322L136 236Q114 150 114
      114Q114 66 138 42Q154 26 178 26Q211 26 245 58Q270 81 285 114T318 219Q336 291 336 325Z"
      id="E6-MJMATHI-62" stroke-width="1"></path><path d="M352 287Q304 211 232 211Q154
      211 104 270T44 396Q42 412 42 436V444Q42 537 111 606Q171 666 243 666Q245 666 249 666T257
      665H261Q273 665 286 663T323 651T370 619T413 560Q456 472 456 334Q456 194 396 97Q361 41 312
      10T208 -22Q147 -22 108 7T68 93T121 149Q143 149 158 135T173 96Q173 78 164 65T148 49T135 44L131
      43Q131 41 138 37T164 27T206 22H212Q272 22 313 86Q352 142 352 280V287ZM244 248Q292 248 321
      297T351 430Q351 508 343 542Q341 552 337 562T323 588T293 615T246 625Q208 625 181 598Q160 576
      154 546T147 441Q147 358 152 329T172 282Q197 248 244 248Z" id="E6-MJMAIN-39"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E6-MJMAIN-31" y="0"></use><use x="778" xlink:href="#E6-MJMAIN-2264"
      y="0"></use><use x="1834" xlink:href="#E6-MJMATHI-74" y="0"></use><use
      x="2473" xlink:href="#E6-MJMAIN-2264" y="0"></use><g
      transform="translate(3530,0)"><use xlink:href="#E6-MJMAIN-31"></use><use
      x="500" xlink:href="#E6-MJMAIN-30" y="0"></use><use x="1001"
      xlink:href="#E6-MJMAIN-30" y="0"></use><use x="1501" xlink:href="#E6-MJMAIN-30"
      y="0"></use></g><g transform="translate(0,-1436)"><use x="0"
      xlink:href="#E6-MJMAIN-31" y="0"></use><use x="778" xlink:href="#E6-MJMAIN-2264"
      y="0"></use><use x="1834" xlink:href="#E6-MJMATHI-61" y="0"></use><use
      x="2364" xlink:href="#E6-MJMAIN-2C" y="0"></use><use x="2809"
      xlink:href="#E6-MJMATHI-62" y="0"></use><use x="3516" xlink:href="#E6-MJMAIN-2264"
      y="0"></use><g transform="translate(4572,0)"><use
      xlink:href="#E6-MJMAIN-31"></use><use x="500" xlink:href="#E6-MJMAIN-30"
      y="0"></use><use transform="scale(0.707)" x="1415" xlink:href="#E6-MJMAIN-39"
      y="557"></use></g></g></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>t</mi><mo>≤</mo><mn>1000</mn><mspace
      linebreak="newline"></mspace><mn>1</mn><mo>≤</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></span></span></em></span><br
      />
      <div class="less-margin-2 input-output-container" style="border-radius: 3px; border: 1px
      solid rgb(229, 231, 232); font-size: 14px; line-height: 21px; margin: 10px 0px 0px;">
      <div class="input-output right-border" style="border-right: 1px solid rgb(229, 231, 232);
      box-sizing: border-box; float: left; overflow-x: auto; white-space: nowrap; width:
      330.5px;">
      <div class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); color: #252c33;
      padding: 6px 10px;">
      <div class="weight-600 less-margin-right light float-left small" style="color: #9ca3a8;
      float: left; font-size: 12px; font-weight: 600; margin-right: 5px;">
      <em>SAMPLE INPUT</em></div>
      <div class="input-output-opt float-right" style="float: right;">
      <span style="font-weight: 600;"><em><a class="track-problem-sample-input
      tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/december-easy-19/problems/7674dde6184c11ea.txt?Signature=n4Q%2BUO3sLQvnqQCMJ4%2BlxsrEooQ%3D&amp;Expires=1599327912&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
      style="color: #4c9cdf; cursor: pointer; font-size: 16px; margin: 0px 5px;
      text-decoration-line: none;" target="_blank"><span class="fa fa-link"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; font-style: normal; font-weight: normal;
      line-height: 1; text-rendering: auto;"></span></a><span
      class="Apple-converted-space">&nbsp;</span><a
      class="track-problem-sample-input-copy input-output-copy tool-tip"
      href="https://www.blogger.com/null" style="color: #4c9cdf; cursor: pointer; font-size: 16px;
      margin: 0px 5px;"><span class="fa fa-files-o" style="-webkit-font-smoothing:
      antialiased; display: inline-block; font-family: FontAwesome; font-size: inherit;
      font-stretch: normal; font-style: normal; font-weight: normal; line-height: 1; text-rendering:
      auto;"></span></a></em></span></div>
      <div class="clear" style="clear: both;">
      </div>
      </div>
      <div class="dark" style="color: #46535e;">
      <pre class="word-spacing-0" style="overflow-wrap: break-word; overflow-x: auto; padding:
      10px; white-space: pre-wrap;"><span style="font-weight: 600;"><em>1
      40 10
      </em></span></pre>
      </div>
      </div>
      <div class="input-output" style="box-sizing: border-box; float: left; overflow-x: auto;
      white-space: nowrap; width: 330.5px;">
      <div class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); color: #252c33;
      padding: 6px 10px;">
      <div class="weight-600 float-left less-margin-right light small" style="color: #9ca3a8;
      float: left; font-size: 12px; font-weight: 600; margin-right: 5px;">
      <em>SAMPLE OUTPUT</em></div>
      <div class="input-output-opt float-right" style="float: right;">
      <span style="font-weight: 600;"><em><a class="track-problem-sample-output
      tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/december-easy-19/problems/7670a4ba184c11ea.txt?Signature=jPHDlWHcIrLzoQjH4FzszSBP4a4%3D&amp;Expires=1599327912&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
      style="color: #4c9cdf; cursor: pointer; font-size: 16px; margin: 0px 5px;
      text-decoration-line: none;" target="_blank"><span class="fa fa-link"
      style="-webkit-font-smoothing: antialiased; display: inline-block; font-family: FontAwesome;
      font-size: inherit; font-stretch: normal; font-style: normal; font-weight: normal;
      line-height: 1; text-rendering: auto;"></span></a><span
      class="Apple-converted-space">&nbsp;</span><a
      class="track-problem-sample-output-copy input-output-copy tool-tip"
      href="https://www.blogger.com/null" style="color: #4c9cdf; cursor: pointer; font-size: 16px;
      margin: 0px 5px;"><span class="fa fa-files-o" style="-webkit-font-smoothing:
      antialiased; display: inline-block; font-family: FontAwesome; font-size: inherit;
      font-stretch: normal; font-style: normal; font-weight: normal; line-height: 1; text-rendering:
      auto;"></span></a></em></span></div>
      <div class="clear" style="clear: both;">
      </div>
      </div>
      <div class="dark" style="color: #46535e;">
      <pre class="word-spacing-0" style="overflow-wrap: break-word; overflow-x: auto; padding:
      10px; white-space: pre-wrap;"><span style="font-weight:
      600;"><em>4</em></span></pre>
      </div>
      </div>
      <div class="clear" style="clear: both;">
      </div>
      </div>
      <span class="mathjax-latex"><span
      class="mathjax-latex"></span></span><br />
      <div class="standard-margin" style="margin: 30px 0px 0px;">
      <strong style="font-weight: 600;"><em><span class="weight-600 form-label"
      style="color: #252c33; font-size: 14px; font-weight: 600;">Explanation</span><div
      class="less-margin" style="margin: 5px 0px 0px;">
      4 circles of radius 10 can fit inside the rectangle.</div>
      </em></strong></div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/669cf961f39aabd6d54ed796122f551a.js"></script>

Write your content here...