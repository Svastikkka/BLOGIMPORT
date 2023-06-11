# A sorted string

Published: 2020-07-11T11:41:00.001+05:30

Description: 
      You are given a string<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-1-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.143ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -805.7 645.5 922.5" width="1.499ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M308 24Q367 24 416
      76T466 197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302
      673 343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627
      704T632 705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478
      551 494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263
      480 278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164
      528 137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65
      -22Q52 -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144
      186T142 153Q144 114 160 87T203 47T255 29T308 24Z" id="E1-MJMATHI-53"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E1-MJMATHI-53" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>of length<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-2-Frame" role="presentation" style="border: 0px; direction: ltr; display:
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
      635 234 637Z" id="E2-MJMATHI-4E" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E2-MJMATHI-4E"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></span></span>.
      The string contains only '<span class="mathjax-latex"><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-3-Frame" role="presentation" style="border: 0px; direction: ltr; display:
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
      26Q217 26 254 59T298 110Q300 114 325 217T351 328Z" id="E3-MJMATHI-61"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E3-MJMATHI-61" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></span></span>',
      '<span class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-4-Frame" role="presentation" style="border: 0px; direction: ltr; display:
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
      id="E4-MJMATHI-62" stroke-width="1"></path></defs><g fill="currentColor"
      stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E4-MJMATHI-62" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></span></span>',
      and '<span class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;c&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-5-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="1.476ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -518.7 433.5 635.5" width="1.007ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M34 159Q34 268 120
      355T306 442Q362 442 394 418T427 355Q427 326 408 306T360 285Q341 285 330 295T319 325T330
      359T352 380T366 386H367Q367 388 361 392T340 400T306 404Q276 404 249 390Q228 381 206 359Q162
      315 142 235T121 119Q121 73 147 50Q169 26 205 26H209Q321 26 394 111Q403 121 406 121Q410 121 419
      112T429 98T420 83T391 55T346 25T282 0T202 -11Q127 -11 81 37T34 159Z" id="E5-MJMATHI-63"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E5-MJMATHI-63" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math></span></span>'.<p></p><p>Your&nbsp;task
      is to find the count of substrings in&nbsp;string<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-6-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.143ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -805.7 645.5 922.5" width="1.499ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M308 24Q367 24 416
      76T466 197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302
      673 343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627
      704T632 705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478
      551 494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263
      480 278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164
      528 137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65
      -22Q52 -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144
      186T142 153Q144 114 160 87T203 47T255 29T308 24Z" id="E6-MJMATHI-53"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E6-MJMATHI-53" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>that have<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;F&lt;/mi&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;msup&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mo&gt;&amp;#x003E;&lt;/mo&gt;&lt;mi&gt;F&lt;/mi&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;msup&gt;&lt;mi&gt;c&lt;/mi&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-7-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.809ex" role="img" style="vertical-align:
      -0.805ex;" viewbox="0 -863.1 6533.3 1209.6" width="15.174ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M48 1Q31 1 31 11Q31 13
      34 25Q38 41 42 43T65 46Q92 46 125 49Q139 52 144 61Q146 66 215 342T285 622Q285 629 281 629Q273
      632 228 634H197Q191 640 191 642T193 659Q197 676 203 680H742Q749 676 749 669Q749 664 736
      557T722 447Q720 440 702 440H690Q683 445 683 453Q683 454 686 477T689 530Q689 560 682 579T663
      610T626 626T575 633T503 634H480Q398 633 393 631Q388 629 386 623Q385 622 352 492L320
      363H375Q378 363 398 363T426 364T448 367T472 374T489 386Q502 398 511 419T524 457T529 475Q532
      480 548 480H560Q567 475 567 470Q567 467 536 339T502 207Q500 200 482 200H470Q463 206 463
      212Q463 215 468 234T473 274Q473 303 453 310T364 317H309L277 190Q245 66 245 60Q245 46 334
      46H359Q365 40 365 39T363 19Q359 6 353 0H336Q295 2 185 2Q120 2 86 2T48 1Z" id="E7-MJMATHI-46"
      stroke-width="1"></path><path d="M94 250Q94 319 104 381T127 488T164 576T202
      643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275 667T226 581T184
      443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318 -250H315H302L274 -226Q180
      -141 137 -14T94 250Z" id="E7-MJMAIN-28" stroke-width="1"></path><path d="M79 43Q73
      43 52 49T30 61Q30 68 85 293T146 528Q161 560 198 560Q218 560 240 545T262 501Q262 496 260
      486Q259 479 173 263T84 45T79 43Z" id="E7-MJMAIN-2032"
      stroke-width="1"></path><path d="M33 157Q33 258 109 349T280 441Q331 441 370
      392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374 43 381 35T402 26Q411 27
      422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506 144Q506 138 501 117T481
      63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299 52 296 50Q294 48 292
      46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323 385T277 405Q242 405 210
      374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179 26Q217 26 254 59T298
      110Q300 114 325 217T351 328Z" id="E7-MJMATHI-61" stroke-width="1"></path><path
      d="M60 749L64 750Q69 750 74 750H86L114 726Q208 641 251 514T294 250Q294 182 284 119T261 12T224
      -76T186 -143T145 -194T113 -227T90 -246Q87 -249 86 -250H74Q66 -250 63 -250T58 -247T55 -238Q56
      -237 66 -225Q221 -64 221 250T66 725Q56 737 55 738Q55 746 60 749Z" id="E7-MJMAIN-29"
      stroke-width="1"></path><path d="M84 520Q84 528 88 533T96 539L99 540Q106 540 253
      471T544 334L687 265Q694 260 694 250T687 235Q685 233 395 96L107 -40H101Q83 -38 83 -20Q83 -19 83
      -17Q82 -10 98 -1Q117 9 248 71Q326 108 378 132L626 250L378 368Q90 504 86 509Q84 513 84 520Z"
      id="E7-MJMAIN-3E" stroke-width="1"></path><path d="M34 159Q34 268 120 355T306
      442Q362 442 394 418T427 355Q427 326 408 306T360 285Q341 285 330 295T319 325T330 359T352
      380T366 386H367Q367 388 361 392T340 400T306 404Q276 404 249 390Q228 381 206 359Q162 315 142
      235T121 119Q121 73 147 50Q169 26 205 26H209Q321 26 394 111Q403 121 406 121Q410 121 419 112T429
      98T420 83T391 55T346 25T282 0T202 -11Q127 -11 81 37T34 159Z" id="E7-MJMATHI-63"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E7-MJMATHI-46" y="0"></use><g transform="translate(749,0)"><use
      x="0" xlink:href="#E7-MJMAIN-28" y="0"></use><use transform="scale(0.707)" x="550"
      xlink:href="#E7-MJMAIN-2032" y="513"></use></g><g
      transform="translate(1433,0)"><use x="0" xlink:href="#E7-MJMATHI-61"
      y="0"></use><use transform="scale(0.707)" x="748" xlink:href="#E7-MJMAIN-2032"
      y="513"></use></g><use x="2258" xlink:href="#E7-MJMAIN-29"
      y="0"></use><use x="2925" xlink:href="#E7-MJMAIN-3E" y="0"></use><use
      x="3981" xlink:href="#E7-MJMATHI-46" y="0"></use><g
      transform="translate(4731,0)"><use x="0" xlink:href="#E7-MJMAIN-28"
      y="0"></use><use transform="scale(0.707)" x="550" xlink:href="#E7-MJMAIN-2032"
      y="513"></use></g><g transform="translate(5415,0)"><use x="0"
      xlink:href="#E7-MJMATHI-63" y="0"></use><use transform="scale(0.707)" x="613"
      xlink:href="#E7-MJMAIN-2032" y="513"></use></g><use x="6143"
      xlink:href="#E7-MJMAIN-29" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><msup><mo
      stretchy="false">(</mo><mo>′</mo></msup><msup><mi>a</mi><mo>′</mo></msup><mo
      stretchy="false">)</mo><mo>&gt;</mo><mi>F</mi><msup><mo
      stretchy="false">(</mo><mo>′</mo></msup><msup><mi>c</mi><mo>′</mo></msup><mo
      stretchy="false">)</mo></math></span></span>.
      Print&nbsp;<span class="mathjax-latex"><span class="MathJax_Preview"
      style="color: inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi
      mathvariant=&quot;normal&quot;&gt;&amp;#x0025;&lt;/mi&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mrow
      class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mn&gt;9&lt;/mn&gt;&lt;/mrow&gt;&lt;/msup&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mn&gt;7&lt;/mn&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-8-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="3.076ex" role="img" style="vertical-align:
      -0.805ex;" viewbox="0 -977.9 6390.4 1324.4" width="14.842ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M33 157Q33 258 109
      349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374
      43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506
      144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299
      52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323
      385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179
      26Q217 26 254 59T298 110Q300 114 325 217T351 328Z" id="E8-MJMATHI-61"
      stroke-width="1"></path><path d="M21 287Q22 293 24 303T36 341T56 388T89 425T135
      442Q171 442 195 424T225 390T231 369Q231 367 232 367L243 378Q304 442 382 442Q436 442 469
      415T503 336T465 179T427 52Q427 26 444 26Q450 26 453 27Q482 32 505 65T540 145Q542 153 560
      153Q580 153 580 145Q580 144 576 130Q568 101 554 73T508 17T439 -10Q392 -10 371 17T350 73Q350 92
      386 193T423 345Q423 404 379 404H374Q288 404 229 303L222 291L189 157Q156 26 151 16Q138 -11 108
      -11Q95 -11 87 -5T76 7T74 17Q74 30 112 180T152 343Q153 348 153 366Q153 405 129 405Q91 405 66
      305Q60 285 60 284Q58 278 41 278H27Q21 284 21 287Z" id="E8-MJMATHI-6E"
      stroke-width="1"></path><path d="M131 289Q131 321 147 354T203 415T300 442Q362 442
      390 415T419 355Q419 323 402 308T364 292Q351 292 340 300T328 326Q328 342 337 354T354 372T367
      378Q368 378 368 379Q368 382 361 388T336 399T297 405Q249 405 227 379T204 326Q204 301 223
      291T278 274T330 259Q396 230 396 163Q396 135 385 107T352 51T289 7T195 -10Q118 -10 86 19T53
      87Q53 126 74 143T118 160Q133 160 146 151T160 120Q160 94 142 76T111 58Q109 57 108 57T107 55Q108
      52 115 47T146 34T201 27Q237 27 263 38T301 66T318 97T323 122Q323 150 302 164T254 181T195
      196T148 231Q131 256 131 289Z" id="E8-MJMATHI-73" stroke-width="1"></path><path
      d="M465 605Q428 605 394 614T340 632T319 641Q332 608 332 548Q332 458 293 403T202 347Q145 347
      101 402T56 548Q56 637 101 693T202 750Q241 750 272 719Q359 642 464 642Q580 642 650 732Q662 748
      668 749Q670 750 673 750Q682 750 688 743T693 726Q178 -47 170 -52Q166 -56 160 -56Q147 -56 142
      -45Q137 -36 142 -27Q143 -24 363 304Q469 462 525 546T581 630Q528 605 465 605ZM207 385Q235 385
      263 427T292 548Q292 617 267 664T200 712Q193 712 186 709T167 698T147 668T134 615Q132 595 132
      548V527Q132 436 165 403Q183 385 203 385H207ZM500 146Q500 234 544 290T647 347Q699 347 737
      292T776 146T737 0T646 -56Q590 -56 545 0T500 146ZM651 -18Q679 -18 707 24T736 146Q736 215 711
      262T644 309Q637 309 630 306T611 295T591 265T578 212Q577 200 577 146V124Q577 -18 647 -18H651Z"
      id="E8-MJMAIN-25" stroke-width="1"></path><path d="M94 250Q94 319 104 381T127
      488T164 576T202 643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275
      667T226 581T184 443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318
      -250H315H302L274 -226Q180 -141 137 -14T94 250Z" id="E8-MJMAIN-28"
      stroke-width="1"></path><path d="M213 578L200 573Q186 568 160 563T102
      556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310
      54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193
      50T201 52T207 57T213 61V578Z" id="E8-MJMAIN-31" stroke-width="1"></path><path
      d="M96 585Q152 666 249 666Q297 666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362
      16T301 -15T250 -22Q224 -22 198 -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629
      250 629Q208 629 178 597Q153 571 145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16
      318 46Q347 76 354 130T362 333Q362 478 354 524T321 597Z" id="E8-MJMAIN-30"
      stroke-width="1"></path><path d="M352 287Q304 211 232 211Q154 211 104 270T44
      396Q42 412 42 436V444Q42 537 111 606Q171 666 243 666Q245 666 249 666T257 665H261Q273 665 286
      663T323 651T370 619T413 560Q456 472 456 334Q456 194 396 97Q361 41 312 10T208 -22Q147 -22 108
      7T68 93T121 149Q143 149 158 135T173 96Q173 78 164 65T148 49T135 44L131 43Q131 41 138 37T164
      27T206 22H212Q272 22 313 86Q352 142 352 280V287ZM244 248Q292 248 321 297T351 430Q351 508 343
      542Q341 552 337 562T323 588T293 615T246 625Q208 625 181 598Q160 576 154 546T147 441Q147 358
      152 329T172 282Q197 248 244 248Z" id="E8-MJMAIN-39" stroke-width="1"></path><path
      d="M56 237T56 250T70 270H369V420L370 570Q380 583 389 583Q402 583 409 568V270H707Q722 262 722
      250T707 230H409V-68Q401 -82 391 -82H389H387Q375 -82 369 -68V230H70Q56 237 56 250Z"
      id="E8-MJMAIN-2B" stroke-width="1"></path><path d="M55 458Q56 460 72 567L88 674Q88
      676 108 676H128V672Q128 662 143 655T195 646T364 644H485V605L417 512Q408 500 387 472T360
      435T339 403T319 367T305 330T292 284T284 230T278 162T275 80Q275 66 275 52T274 28V19Q270 2 255
      -10T221 -22Q210 -22 200 -19T179 0T168 40Q168 198 265 368Q285 400 349 489L395 552H302Q128 552
      119 546Q113 543 108 522T98 479L95 458V455H55V458Z" id="E8-MJMAIN-37"
      stroke-width="1"></path><path d="M60 749L64 750Q69 750 74 750H86L114 726Q208 641
      251 514T294 250Q294 182 284 119T261 12T224 -76T186 -143T145 -194T113 -227T90 -246Q87 -249 86
      -250H74Q66 -250 63 -250T58 -247T55 -238Q56 -237 66 -225Q221 -64 221 250T66 725Q56 737 55
      738Q55 746 60 749Z" id="E8-MJMAIN-29" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E8-MJMATHI-61" y="0"></use><use x="529"
      xlink:href="#E8-MJMATHI-6E" y="0"></use><use x="1130" xlink:href="#E8-MJMATHI-73"
      y="0"></use><use x="1599" xlink:href="#E8-MJMAIN-25" y="0"></use><use
      x="2433" xlink:href="#E8-MJMAIN-28" y="0"></use><g
      transform="translate(2822,0)"><use xlink:href="#E8-MJMAIN-31"></use><use
      x="500" xlink:href="#E8-MJMAIN-30" y="0"></use><use transform="scale(0.707)"
      x="1415" xlink:href="#E8-MJMAIN-39" y="557"></use></g><use x="4499"
      xlink:href="#E8-MJMAIN-2B" y="0"></use><use x="5500" xlink:href="#E8-MJMAIN-37"
      y="0"></use><use x="6000" xlink:href="#E8-MJMAIN-29"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>n</mi><mi>s</mi><mi
      mathvariant="normal">%</mi><mo
      stretchy="false">(</mo><msup><mn>10</mn><mrow
      class="MJX-TeXAtom-ORD"><mn>9</mn></mrow></msup><mo>+</mo><mn>7</mn><mo
      stretchy="false">)</mo></math></span></span>.</span></span></span></p><p>Here,&nbsp;<span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;F&lt;/mi&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-9-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.809ex" role="img" style="vertical-align:
      -0.805ex;" viewbox="0 -863.1 2101 1209.6" width="4.88ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M48 1Q31 1 31 11Q31 13
      34 25Q38 41 42 43T65 46Q92 46 125 49Q139 52 144 61Q146 66 215 342T285 622Q285 629 281 629Q273
      632 228 634H197Q191 640 191 642T193 659Q197 676 203 680H742Q749 676 749 669Q749 664 736
      557T722 447Q720 440 702 440H690Q683 445 683 453Q683 454 686 477T689 530Q689 560 682 579T663
      610T626 626T575 633T503 634H480Q398 633 393 631Q388 629 386 623Q385 622 352 492L320
      363H375Q378 363 398 363T426 364T448 367T472 374T489 386Q502 398 511 419T524 457T529 475Q532
      480 548 480H560Q567 475 567 470Q567 467 536 339T502 207Q500 200 482 200H470Q463 206 463
      212Q463 215 468 234T473 274Q473 303 453 310T364 317H309L277 190Q245 66 245 60Q245 46 334
      46H359Q365 40 365 39T363 19Q359 6 353 0H336Q295 2 185 2Q120 2 86 2T48 1Z" id="E9-MJMATHI-46"
      stroke-width="1"></path><path d="M94 250Q94 319 104 381T127 488T164 576T202
      643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275 667T226 581T184
      443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318 -250H315H302L274 -226Q180
      -141 137 -14T94 250Z" id="E9-MJMAIN-28" stroke-width="1"></path><path d="M52
      289Q59 331 106 386T222 442Q257 442 286 424T329 379Q371 442 430 442Q467 442 494 420T522 361Q522
      332 508 314T481 292T458 288Q439 288 427 299T415 328Q415 374 465 391Q454 404 425 404Q412 404
      406 402Q368 386 350 336Q290 115 290 78Q290 50 306 38T341 26Q378 26 414 59T463 140Q466 150 469
      151T485 153H489Q504 153 504 145Q504 144 502 134Q486 77 440 33T333 -11Q263 -11 227 52Q186 -10
      133 -10H127Q78 -10 57 16T35 71Q35 103 54 123T99 143Q142 143 142 101Q142 81 130 66T107 46T94
      41L91 40Q91 39 97 36T113 29T132 26Q168 26 194 71Q203 87 217 139T245 247T261 313Q266 340 266
      352Q266 380 251 392T217 404Q177 404 142 372T93 290Q91 281 88 280T72 278H58Q52 284 52 289Z"
      id="E9-MJMATHI-78" stroke-width="1"></path><path d="M60 749L64 750Q69 750 74
      750H86L114 726Q208 641 251 514T294 250Q294 182 284 119T261 12T224 -76T186 -143T145 -194T113
      -227T90 -246Q87 -249 86 -250H74Q66 -250 63 -250T58 -247T55 -238Q56 -237 66 -225Q221 -64 221
      250T66 725Q56 737 55 738Q55 746 60 749Z" id="E9-MJMAIN-29"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E9-MJMATHI-46" y="0"></use><use x="749" xlink:href="#E9-MJMAIN-28"
      y="0"></use><use x="1139" xlink:href="#E9-MJMATHI-78" y="0"></use><use
      x="1711" xlink:href="#E9-MJMAIN-29" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo
      stretchy="false">(</mo><mi>x</mi><mo
      stretchy="false">)</mo></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>denotes the frequency of occurrence of
      character<span class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-10-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="1.476ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -518.7 572.5 635.5" width="1.33ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M52 289Q59 331 106
      386T222 442Q257 442 286 424T329 379Q371 442 430 442Q467 442 494 420T522 361Q522 332 508
      314T481 292T458 288Q439 288 427 299T415 328Q415 374 465 391Q454 404 425 404Q412 404 406
      402Q368 386 350 336Q290 115 290 78Q290 50 306 38T341 26Q378 26 414 59T463 140Q466 150 469
      151T485 153H489Q504 153 504 145Q504 144 502 134Q486 77 440 33T333 -11Q263 -11 227 52Q186 -10
      133 -10H127Q78 -10 57 16T35 71Q35 103 54 123T99 143Q142 143 142 101Q142 81 130 66T107 46T94
      41L91 40Q91 39 97 36T113 29T132 26Q168 26 194 71Q203 87 217 139T245 247T261 313Q266 340 266
      352Q266 380 251 392T217 404Q177 404 142 372T93 290Q91 281 88 280T72 278H58Q52 284 52 289Z"
      id="E10-MJMATHI-78" stroke-width="1"></path></defs><g fill="currentColor"
      stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E10-MJMATHI-78" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>in the
      string.</span></span></p><p><span style="font-weight:
      600;">Input format</span></p><ul style="padding-left: 40px;"><li
      style="margin-bottom: 5px;">The first line contains an integer<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-11-Frame" role="presentation" style="border: 0px; direction: ltr; display:
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
      635 234 637Z" id="E11-MJMATHI-4E" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E11-MJMATHI-4E"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>that denotes the length of the
      string.</span></li><li style="margin-bottom: 5px;">The next
      line&nbsp;contains string<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-12-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.143ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -805.7 645.5 922.5" width="1.499ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M308 24Q367 24 416
      76T466 197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302
      673 343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627
      704T632 705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478
      551 494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263
      480 278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164
      528 137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65
      -22Q52 -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144
      186T142 153Q144 114 160 87T203 47T255 29T308 24Z" id="E12-MJMATHI-53"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E12-MJMATHI-53" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></span></span>.</span></li></ul><p><span
      style="font-weight: 600;">Output format</span></p><p>Print the count of
      substrings in&nbsp;string<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-13-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.143ex" role="img" style="vertical-align:
      -0.271ex;" viewbox="0 -805.7 645.5 922.5" width="1.499ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M308 24Q367 24 416
      76T466 197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302
      673 343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627
      704T632 705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478
      551 494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263
      480 278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164
      528 137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65
      -22Q52 -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144
      186T142 153Q144 114 160 87T203 47T255 29T308 24Z" id="E13-MJMATHI-53"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E13-MJMATHI-53" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>that have<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;F&lt;/mi&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;msup&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mo&gt;&amp;#x003E;&lt;/mo&gt;&lt;mi&gt;F&lt;/mi&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;msup&gt;&lt;mi&gt;c&lt;/mi&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-14-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.809ex" role="img" style="vertical-align:
      -0.805ex;" viewbox="0 -863.1 6533.3 1209.6" width="15.174ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M48 1Q31 1 31 11Q31 13
      34 25Q38 41 42 43T65 46Q92 46 125 49Q139 52 144 61Q146 66 215 342T285 622Q285 629 281 629Q273
      632 228 634H197Q191 640 191 642T193 659Q197 676 203 680H742Q749 676 749 669Q749 664 736
      557T722 447Q720 440 702 440H690Q683 445 683 453Q683 454 686 477T689 530Q689 560 682 579T663
      610T626 626T575 633T503 634H480Q398 633 393 631Q388 629 386 623Q385 622 352 492L320
      363H375Q378 363 398 363T426 364T448 367T472 374T489 386Q502 398 511 419T524 457T529 475Q532
      480 548 480H560Q567 475 567 470Q567 467 536 339T502 207Q500 200 482 200H470Q463 206 463
      212Q463 215 468 234T473 274Q473 303 453 310T364 317H309L277 190Q245 66 245 60Q245 46 334
      46H359Q365 40 365 39T363 19Q359 6 353 0H336Q295 2 185 2Q120 2 86 2T48 1Z" id="E14-MJMATHI-46"
      stroke-width="1"></path><path d="M94 250Q94 319 104 381T127 488T164 576T202
      643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275 667T226 581T184
      443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318 -250H315H302L274 -226Q180
      -141 137 -14T94 250Z" id="E14-MJMAIN-28" stroke-width="1"></path><path d="M79
      43Q73 43 52 49T30 61Q30 68 85 293T146 528Q161 560 198 560Q218 560 240 545T262 501Q262 496 260
      486Q259 479 173 263T84 45T79 43Z" id="E14-MJMAIN-2032"
      stroke-width="1"></path><path d="M33 157Q33 258 109 349T280 441Q331 441 370
      392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374 43 381 35T402 26Q411 27
      422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506 144Q506 138 501 117T481
      63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299 52 296 50Q294 48 292
      46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323 385T277 405Q242 405 210
      374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179 26Q217 26 254 59T298
      110Q300 114 325 217T351 328Z" id="E14-MJMATHI-61" stroke-width="1"></path><path
      d="M60 749L64 750Q69 750 74 750H86L114 726Q208 641 251 514T294 250Q294 182 284 119T261 12T224
      -76T186 -143T145 -194T113 -227T90 -246Q87 -249 86 -250H74Q66 -250 63 -250T58 -247T55 -238Q56
      -237 66 -225Q221 -64 221 250T66 725Q56 737 55 738Q55 746 60 749Z" id="E14-MJMAIN-29"
      stroke-width="1"></path><path d="M84 520Q84 528 88 533T96 539L99 540Q106 540 253
      471T544 334L687 265Q694 260 694 250T687 235Q685 233 395 96L107 -40H101Q83 -38 83 -20Q83 -19 83
      -17Q82 -10 98 -1Q117 9 248 71Q326 108 378 132L626 250L378 368Q90 504 86 509Q84 513 84 520Z"
      id="E14-MJMAIN-3E" stroke-width="1"></path><path d="M34 159Q34 268 120 355T306
      442Q362 442 394 418T427 355Q427 326 408 306T360 285Q341 285 330 295T319 325T330 359T352
      380T366 386H367Q367 388 361 392T340 400T306 404Q276 404 249 390Q228 381 206 359Q162 315 142
      235T121 119Q121 73 147 50Q169 26 205 26H209Q321 26 394 111Q403 121 406 121Q410 121 419 112T429
      98T420 83T391 55T346 25T282 0T202 -11Q127 -11 81 37T34 159Z" id="E14-MJMATHI-63"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E14-MJMATHI-46" y="0"></use><g
      transform="translate(749,0)"><use x="0" xlink:href="#E14-MJMAIN-28"
      y="0"></use><use transform="scale(0.707)" x="550" xlink:href="#E14-MJMAIN-2032"
      y="513"></use></g><g transform="translate(1433,0)"><use x="0"
      xlink:href="#E14-MJMATHI-61" y="0"></use><use transform="scale(0.707)" x="748"
      xlink:href="#E14-MJMAIN-2032" y="513"></use></g><use x="2258"
      xlink:href="#E14-MJMAIN-29" y="0"></use><use x="2925" xlink:href="#E14-MJMAIN-3E"
      y="0"></use><use x="3981" xlink:href="#E14-MJMATHI-46" y="0"></use><g
      transform="translate(4731,0)"><use x="0" xlink:href="#E14-MJMAIN-28"
      y="0"></use><use transform="scale(0.707)" x="550" xlink:href="#E14-MJMAIN-2032"
      y="513"></use></g><g transform="translate(5415,0)"><use x="0"
      xlink:href="#E14-MJMATHI-63" y="0"></use><use transform="scale(0.707)" x="613"
      xlink:href="#E14-MJMAIN-2032" y="513"></use></g><use x="6143"
      xlink:href="#E14-MJMAIN-29" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><msup><mo
      stretchy="false">(</mo><mo>′</mo></msup><msup><mi>a</mi><mo>′</mo></msup><mo
      stretchy="false">)</mo><mo>&gt;</mo><mi>F</mi><msup><mo
      stretchy="false">(</mo><mo>′</mo></msup><msup><mi>c</mi><mo>′</mo></msup><mo
      stretchy="false">)</mo></math></span></span>&nbsp;modulus<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;9&lt;/mn&gt;&lt;/msup&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mn&gt;7&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-15-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.676ex" role="img" style="vertical-align:
      -0.405ex;" viewbox="0 -977.9 3178.4 1152.1" width="7.382ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M213 578L200 573Q186 568
      160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302
      660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46
      152 46T177 47T193 50T201 52T207 57T213 61V578Z" id="E15-MJMAIN-31"
      stroke-width="1"></path><path d="M96 585Q152 666 249 666Q297 666 345 640T423
      548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82
      83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137
      333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354
      524T321 597Z" id="E15-MJMAIN-30" stroke-width="1"></path><path d="M352 287Q304 211
      232 211Q154 211 104 270T44 396Q42 412 42 436V444Q42 537 111 606Q171 666 243 666Q245 666 249
      666T257 665H261Q273 665 286 663T323 651T370 619T413 560Q456 472 456 334Q456 194 396 97Q361 41
      312 10T208 -22Q147 -22 108 7T68 93T121 149Q143 149 158 135T173 96Q173 78 164 65T148 49T135
      44L131 43Q131 41 138 37T164 27T206 22H212Q272 22 313 86Q352 142 352 280V287ZM244 248Q292 248
      321 297T351 430Q351 508 343 542Q341 552 337 562T323 588T293 615T246 625Q208 625 181 598Q160
      576 154 546T147 441Q147 358 152 329T172 282Q197 248 244 248Z" id="E15-MJMAIN-39"
      stroke-width="1"></path><path d="M56 237T56 250T70 270H369V420L370 570Q380 583 389
      583Q402 583 409 568V270H707Q722 262 722 250T707 230H409V-68Q401 -82 391 -82H389H387Q375 -82
      369 -68V230H70Q56 237 56 250Z" id="E15-MJMAIN-2B" stroke-width="1"></path><path
      d="M55 458Q56 460 72 567L88 674Q88 676 108 676H128V672Q128 662 143 655T195 646T364
      644H485V605L417 512Q408 500 387 472T360 435T339 403T319 367T305 330T292 284T284 230T278
      162T275 80Q275 66 275 52T274 28V19Q270 2 255 -10T221 -22Q210 -22 200 -19T179 0T168 40Q168 198
      265 368Q285 400 349 489L395 552H302Q128 552 119 546Q113 543 108 522T98 479L95 458V455H55V458Z"
      id="E15-MJMAIN-37" stroke-width="1"></path></defs><g fill="currentColor"
      stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use
      xlink:href="#E15-MJMAIN-31"></use><use x="500" xlink:href="#E15-MJMAIN-30"
      y="0"></use><use transform="scale(0.707)" x="1415" xlink:href="#E15-MJMAIN-39"
      y="557"></use><use x="1677" xlink:href="#E15-MJMAIN-2B"
      y="0"></use><use x="2677" xlink:href="#E15-MJMAIN-37"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>9</mn></msup><mo>+</mo><mn>7</mn></math></span></span>.&nbsp;</span></span></span></p><p><span
      style="font-weight: 600;">Constraints</span><br /><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;mo&gt;&amp;#x2264;&lt;/mo&gt;&lt;msup&gt;&lt;mn&gt;10&lt;/mn&gt;&lt;mn&gt;5&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;"
      id="MathJax-Element-16-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.809ex" role="img" style="vertical-align:
      -0.538ex;" viewbox="0 -977.9 5512 1209.6" width="12.802ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M213 578L200 573Q186 568
      160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302
      660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46
      152 46T177 47T193 50T201 52T207 57T213 61V578Z" id="E16-MJMAIN-31"
      stroke-width="1"></path><path d="M674 636Q682 636 688 630T694 615T687 601Q686 600
      417 472L151 346L399 228Q687 92 691 87Q694 81 694 76Q694 58 676 56H670L382 192Q92 329 90 331Q83
      336 83 348Q84 359 96 365Q104 369 382 500T665 634Q669 636 674 636ZM84 -118Q84 -108 99
      -98H678Q694 -104 694 -118Q694 -130 679 -138H98Q84 -131 84 -118Z" id="E16-MJMAIN-2264"
      stroke-width="1"></path><path d="M234 637Q231 637 226 637Q201 637 196 638T191
      649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592
      723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684
      682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633
      769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268
      46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14
      34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"
      id="E16-MJMATHI-4E" stroke-width="1"></path><path d="M96 585Q152 666 249 666Q297
      666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198
      -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571
      145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362
      478 354 524T321 597Z" id="E16-MJMAIN-30" stroke-width="1"></path><path d="M164
      157Q164 133 148 117T109 101H102Q148 22 224 22Q294 22 326 82Q345 115 345 210Q345 313 318
      349Q292 382 260 382H254Q176 382 136 314Q132 307 129 306T114 304Q97 304 95 310Q93 314 93
      485V614Q93 664 98 664Q100 666 102 666Q103 666 123 658T178 642T253 634Q324 634 389 662Q397 666
      402 666Q410 666 410 648V635Q328 538 205 538Q174 538 149 544L139 546V374Q158 388 169 396T205
      412T256 420Q337 420 393 355T449 201Q449 109 385 44T229 -22Q148 -22 99 32T50 154Q50 178 61
      192T84 210T107 214Q132 214 148 197T164 157Z" id="E16-MJMAIN-35"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E16-MJMAIN-31" y="0"></use><use x="778" xlink:href="#E16-MJMAIN-2264"
      y="0"></use><use x="1834" xlink:href="#E16-MJMATHI-4E"
      y="0"></use><use x="3000" xlink:href="#E16-MJMAIN-2264" y="0"></use><g
      transform="translate(4057,0)"><use xlink:href="#E16-MJMAIN-31"></use><use
      x="500" xlink:href="#E16-MJMAIN-30" y="0"></use><use transform="scale(0.707)"
      x="1415" xlink:href="#E16-MJMAIN-35"
      y="557"></use></g></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><msup><mn>10</mn><mn>5</mn></msup></math></span></span></span></p><p>&nbsp;</p><div
      class="less-margin-2 input-output-container" style="border-radius: 3px; border: 1px solid
      rgb(229, 231, 232); font-size: 14px; line-height: 21px; margin: 10px 0px 0px;"><div
      class="input-output right-border" style="border-right: 1px solid rgb(229, 231, 232);
      box-sizing: border-box; float: left; overflow-x: auto; white-space: nowrap; width:
      330.5px;"><div class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232);
      color: #252c33; padding: 6px 10px;"><div class="weight-600 less-margin-right light
      float-left small" style="color: #9ca3a8; float: left; font-size: 12px; font-weight: 600;
      margin-right: 5px;">SAMPLE INPUT</div><div class="input-output-opt float-right"
      style="float: right;"><a class="track-problem-sample-input tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/data-structures-and-algorithms-coding-contest-july-2020/problems/5e77f10ac28911ea.txt?Signature=44ZrDUt0JDnHTrR0PR6snxqg0mY%3D&amp;Expires=1594451274&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
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
      overflow-x: auto; padding: 10px; white-space: pre-wrap;">7
      abccaab</pre></div></div><div class="input-output" style="box-sizing:
      border-box; float: left; overflow-x: auto; white-space: nowrap; width: 330.5px;"><div
      class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); color: #252c33;
      padding: 6px 10px;"><div class="weight-600 float-left less-margin-right light small"
      style="color: #9ca3a8; float: left; font-size: 12px; font-weight: 600; margin-right:
      5px;">SAMPLE OUTPUT</div><div class="input-output-opt float-right" style="float:
      right;"><a class="track-problem-sample-output tool-tip"
      href="https://he-s3.s3.amazonaws.com/media/hackathon/data-structures-and-algorithms-coding-contest-july-2020/problems/5e73ef6ac28911ea.txt?Signature=skAlVthFkz%2FAEnc1DOJxNdzhj0s%3D&amp;Expires=1594451274&amp;AWSAccessKeyId=AKIA6I2ISGOYH7WWS3G5"
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
      overflow-x: auto; padding: 10px; white-space:
      pre-wrap;">11</pre></div></div><div class="clear" style="clear:
      both;"></div></div><div class="standard-margin" style="margin: 30px 0px
      0px;"><span class="weight-600 form-label" style="color: #252c33; font-size: 14px;
      font-weight: 600;">Explanation</span><div class="less-margin" style="margin: 5px
      0px 0px;"><p>There are total 11 substrings in which<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;msup&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mo&gt;&amp;gt;&lt;/mo&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;msup&gt;&lt;mi&gt;c&lt;/mi&gt;&lt;mo&gt;&amp;#x2032;&lt;/mo&gt;&lt;/msup&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-17-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; line-height: normal; margin: 0px; max-height:
      none; max-width: none; min-height: 0px; min-width: 0px; overflow-wrap: normal; padding: 0px;
      position: relative; white-space: nowrap; word-spacing: normal;" tabindex="0"><svg
      aria-hidden="true" focusable="false" height="2.809ex" role="img" style="vertical-align:
      -0.805ex;" viewbox="0 -863.1 6135.3 1209.6" width="14.25ex"
      xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M118 -162Q120 -162 124
      -164T135 -167T147 -168Q160 -168 171 -155T187 -126Q197 -99 221 27T267 267T289 382V385H242Q195
      385 192 387Q188 390 188 397L195 425Q197 430 203 430T250 431Q298 431 298 432Q298 434 307
      482T319 540Q356 705 465 705Q502 703 526 683T550 630Q550 594 529 578T487 561Q443 561 443
      603Q443 622 454 636T478 657L487 662Q471 668 457 668Q445 668 434 658T419 630Q412 601 403
      552T387 469T380 433Q380 431 435 431Q480 431 487 430T498 424Q499 420 496 407T491 391Q489 386
      482 386T428 385H372L349 263Q301 15 282 -47Q255 -132 212 -173Q175 -205 139 -205Q107 -205 81
      -186T55 -132Q55 -95 76 -78T118 -61Q162 -61 162 -103Q162 -122 151 -136T127 -157L118 -162Z"
      id="E17-MJMATHI-66" stroke-width="1"></path><path d="M94 250Q94 319 104 381T127
      488T164 576T202 643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275
      667T226 581T184 443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318
      -250H315H302L274 -226Q180 -141 137 -14T94 250Z" id="E17-MJMAIN-28"
      stroke-width="1"></path><path d="M79 43Q73 43 52 49T30 61Q30 68 85 293T146 528Q161
      560 198 560Q218 560 240 545T262 501Q262 496 260 486Q259 479 173 263T84 45T79 43Z"
      id="E17-MJMAIN-2032" stroke-width="1"></path><path d="M33 157Q33 258 109 349T280
      441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374 43 381
      35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506 144Q506
      138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299 52 296
      50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323 385T277
      405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179 26Q217
      26 254 59T298 110Q300 114 325 217T351 328Z" id="E17-MJMATHI-61"
      stroke-width="1"></path><path d="M60 749L64 750Q69 750 74 750H86L114 726Q208 641
      251 514T294 250Q294 182 284 119T261 12T224 -76T186 -143T145 -194T113 -227T90 -246Q87 -249 86
      -250H74Q66 -250 63 -250T58 -247T55 -238Q56 -237 66 -225Q221 -64 221 250T66 725Q56 737 55
      738Q55 746 60 749Z" id="E17-MJMAIN-29" stroke-width="1"></path><path d="M84 520Q84
      528 88 533T96 539L99 540Q106 540 253 471T544 334L687 265Q694 260 694 250T687 235Q685 233 395
      96L107 -40H101Q83 -38 83 -20Q83 -19 83 -17Q82 -10 98 -1Q117 9 248 71Q326 108 378 132L626
      250L378 368Q90 504 86 509Q84 513 84 520Z" id="E17-MJMAIN-3E"
      stroke-width="1"></path><path d="M34 159Q34 268 120 355T306 442Q362 442 394
      418T427 355Q427 326 408 306T360 285Q341 285 330 295T319 325T330 359T352 380T366 386H367Q367
      388 361 392T340 400T306 404Q276 404 249 390Q228 381 206 359Q162 315 142 235T121 119Q121 73 147
      50Q169 26 205 26H209Q321 26 394 111Q403 121 406 121Q410 121 419 112T429 98T420 83T391 55T346
      25T282 0T202 -11Q127 -11 81 37T34 159Z" id="E17-MJMATHI-63"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E17-MJMATHI-66" y="0"></use><g
      transform="translate(550,0)"><use x="0" xlink:href="#E17-MJMAIN-28"
      y="0"></use><use transform="scale(0.707)" x="550" xlink:href="#E17-MJMAIN-2032"
      y="513"></use></g><g transform="translate(1234,0)"><use x="0"
      xlink:href="#E17-MJMATHI-61" y="0"></use><use transform="scale(0.707)" x="748"
      xlink:href="#E17-MJMAIN-2032" y="513"></use></g><use x="2059"
      xlink:href="#E17-MJMAIN-29" y="0"></use><use x="2726" xlink:href="#E17-MJMAIN-3E"
      y="0"></use><use x="3782" xlink:href="#E17-MJMATHI-66" y="0"></use><g
      transform="translate(4333,0)"><use x="0" xlink:href="#E17-MJMAIN-28"
      y="0"></use><use transform="scale(0.707)" x="550" xlink:href="#E17-MJMAIN-2032"
      y="513"></use></g><g transform="translate(5017,0)"><use x="0"
      xlink:href="#E17-MJMATHI-63" y="0"></use><use transform="scale(0.707)" x="613"
      xlink:href="#E17-MJMAIN-2032" y="513"></use></g><use x="5745"
      xlink:href="#E17-MJMAIN-29" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><msup><mo
      stretchy="false">(</mo><mo>′</mo></msup><msup><mi>a</mi><mo>′</mo></msup><mo
      stretchy="false">)</mo><mo>&gt;</mo><mi>f</mi><msup><mo
      stretchy="false">(</mo><mo>′</mo></msup><msup><mi>c</mi><mo>′</mo></msup><mo
      stretchy="false">)</mo></math></span></span>. These are:<br
      />['a','ab', 'abccaa', 'abccaab', 'a', 'a', 'aa', 'ab', 'aab', 'caa',
      'caab']</span></p><p><span class="mathjax-latex">Note:- Partially
      Solved TIME EXTENDED</span></p><p><span class="mathjax-latex"><br
      /></span></p></div></div></span></span></span></span></span>
      <script
      src="https://gist.github.com/Svastikkka/5e04d785425dbf39b2f9aa16413df9d3.js"></script>

Write your content here...