# Bubble Sort

Published: 2020-06-24T22:20:00.000+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      You are given&nbsp;arrays&nbsp;<em><span style="font-weight:
      600;"><span class="MathJax_Preview" style="color: inherit;"></span><span
      class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msub&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;&amp;#x2026;&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;"
      id="MathJax-Element-1-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="1.876ex" role="img" style="vertical-align: -0.671ex;" viewbox="0 -518.7 5695.6 807.7"
      width="13.229ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M33
      157Q33 258 109 349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412
      234T374 68Q374 43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483
      153H487Q506 153 506 144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336
      5T306 36L300 51Q299 52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351
      334 346 350T323 385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118
      106Q118 61 136 44T179 26Q217 26 254 59T298 110Q300 114 325 217T351 328Z" id="E1-MJMATHI-61"
      stroke-width="1"></path><path d="M213 578L200 573Q186 568 160 563T102
      556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310
      54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193
      50T201 52T207 57T213 61V578Z" id="E1-MJMAIN-31" stroke-width="1"></path><path
      d="M78 35T78 60T94 103T137 121Q165 121 187 96T210 8Q210 -27 201 -60T180 -117T154 -158T130
      -185T117 -194Q113 -194 104 -185T95 -172Q95 -168 106 -156T131 -126T157 -76T173 -3V9L172 8Q170 7
      167 6T161 3T152 1T140 0Q113 0 96 17Z" id="E1-MJMAIN-2C"
      stroke-width="1"></path><path d="M109 429Q82 429 66 447T50 491Q50 562 103 614T235
      666Q326 666 387 610T449 465Q449 422 429 383T381 315T301 241Q265 210 201 149L142 93L218 92Q375
      92 385 97Q392 99 409 186V189H449V186Q448 183 436 95T421 3V0H50V19V31Q50 38 56 46T86 81Q115 113
      136 137Q145 147 170 174T204 211T233 244T261 278T284 308T305 340T320 369T333 401T340 431T343
      464Q343 527 309 573T212 619Q179 619 154 602T119 569T109 550Q109 549 114 549Q132 549 151
      535T170 489Q170 464 154 447T109 429Z" id="E1-MJMAIN-32"
      stroke-width="1"></path><path d="M78 60Q78 84 95 102T138 120Q162 120 180 104T199
      61Q199 36 182 18T139 0T96 17T78 60ZM525 60Q525 84 542 102T585 120Q609 120 627 104T646 61Q646
      36 629 18T586 0T543 17T525 60ZM972 60Q972 84 989 102T1032 120Q1056 120 1074 104T1093 61Q1093
      36 1076 18T1033 0T990 17T972 60Z" id="E1-MJMAIN-2026"
      stroke-width="1"></path><path d="M21 287Q22 293 24 303T36 341T56 388T89 425T135
      442Q171 442 195 424T225 390T231 369Q231 367 232 367L243 378Q304 442 382 442Q436 442 469
      415T503 336T465 179T427 52Q427 26 444 26Q450 26 453 27Q482 32 505 65T540 145Q542 153 560
      153Q580 153 580 145Q580 144 576 130Q568 101 554 73T508 17T439 -10Q392 -10 371 17T350 73Q350 92
      386 193T423 345Q423 404 379 404H374Q288 404 229 303L222 291L189 157Q156 26 151 16Q138 -11 108
      -11Q95 -11 87 -5T76 7T74 17Q74 30 112 180T152 343Q153 348 153 366Q153 405 129 405Q91 405 66
      305Q60 285 60 284Q58 278 41 278H27Q21 284 21 287Z" id="E1-MJMATHI-6E"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E1-MJMATHI-61" y="0"></use><use transform="scale(0.707)" x="748"
      xlink:href="#E1-MJMAIN-31" y="-213"></use><use x="983" xlink:href="#E1-MJMAIN-2C"
      y="0"></use><g transform="translate(1428,0)"><use x="0"
      xlink:href="#E1-MJMATHI-61" y="0"></use><use transform="scale(0.707)" x="748"
      xlink:href="#E1-MJMAIN-32" y="-213"></use></g><use x="2411"
      xlink:href="#E1-MJMAIN-2C" y="0"></use><use x="2857" xlink:href="#E1-MJMAIN-2026"
      y="0"></use><use x="4196" xlink:href="#E1-MJMAIN-2C" y="0"></use><g
      transform="translate(4641,0)"><use x="0" xlink:href="#E1-MJMATHI-61"
      y="0"></use><use transform="scale(0.707)" x="748" xlink:href="#E1-MJMATHI-6E"
      y="-213"></use></g></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>…</mo><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub></math></span></span>.
      What will return the next function<span
      class="Apple-converted-space">&nbsp;</span><em><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;B&lt;/mi&gt;&lt;mi&gt;u&lt;/mi&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;mi&gt;l&lt;/mi&gt;&lt;mi&gt;e&lt;/mi&gt;&lt;mtext&gt;&amp;#xA0;&lt;/mtext&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;mi&gt;o&lt;/mi&gt;&lt;mi&gt;r&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mtext&gt;&amp;#xA0;&lt;/mtext&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo
      stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;"
      id="MathJax-Element-2-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="2.809ex" role="img" style="vertical-align: -0.805ex;" viewbox="0 -863.1 6929.5 1209.6"
      width="16.094ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M231
      637Q204 637 199 638T194 649Q194 676 205 682Q206 683 335 683Q594 683 608 681Q671 671 713
      636T756 544Q756 480 698 429T565 360L555 357Q619 348 660 311T702 219Q702 146 630 78T453 1Q446 0
      242 0Q42 0 39 2Q35 5 35 10Q35 17 37 24Q42 43 47 45Q51 46 62 46H68Q95 46 128 49Q142 52 147
      61Q150 65 219 339T288 628Q288 635 231 637ZM649 544Q649 574 634 600T585 634Q578 636 493 637Q473
      637 451 637T416 636H403Q388 635 384 626Q382 622 352 506Q352 503 351 500L320 374H401Q482 374
      494 376Q554 386 601 434T649 544ZM595 229Q595 273 572 302T512 336Q506 337 429 337Q311 337 310
      336Q310 334 293 263T258 122L240 52Q240 48 252 48T333 46Q422 46 429 47Q491 54 543 105T595 229Z"
      id="E2-MJMATHI-42" stroke-width="1"></path><path d="M21 287Q21 295 30 318T55
      370T99 420T158 442Q204 442 227 417T250 358Q250 340 216 246T182 105Q182 62 196 45T238 27T291
      44T328 78L339 95Q341 99 377 247Q407 367 413 387T427 416Q444 431 463 431Q480 431 488 421T496
      402L420 84Q419 79 419 68Q419 43 426 35T447 26Q469 29 482 57T512 145Q514 153 532 153Q551 153
      551 144Q550 139 549 130T540 98T523 55T498 17T462 -8Q454 -10 438 -10Q372 -10 347 46Q345 45 336
      36T318 21T296 6T267 -6T233 -11Q189 -11 155 7Q103 38 103 113Q103 170 138 262T173 379Q173 380
      173 381Q173 390 173 393T169 400T158 404H154Q131 404 112 385T82 344T65 302T57 280Q55 278 41
      278H27Q21 284 21 287Z" id="E2-MJMATHI-75" stroke-width="1"></path><path d="M73
      647Q73 657 77 670T89 683Q90 683 161 688T234 694Q246 694 246 685T212 542Q204 508 195 472T180
      418L176 399Q176 396 182 402Q231 442 283 442Q345 442 383 396T422 280Q422 169 343 79T173 -11Q123
      -11 82 27T40 150V159Q40 180 48 217T97 414Q147 611 147 623T109 637Q104 637 101 637H96Q86 637 83
      637T76 640T73 647ZM336 325V331Q336 405 275 405Q258 405 240 397T207 376T181 352T163 330L157
      322L136 236Q114 150 114 114Q114 66 138 42Q154 26 178 26Q211 26 245 58Q270 81 285 114T318
      219Q336 291 336 325Z" id="E2-MJMATHI-62" stroke-width="1"></path><path d="M117
      59Q117 26 142 26Q179 26 205 131Q211 151 215 152Q217 153 225 153H229Q238 153 241 153T246
      151T248 144Q247 138 245 128T234 90T214 43T183 6T137 -11Q101 -11 70 11T38 85Q38 97 39 102L104
      360Q167 615 167 623Q167 626 166 628T162 632T157 634T149 635T141 636T132 637T122 637Q112 637
      109 637T101 638T95 641T94 647Q94 649 96 661Q101 680 107 682T179 688Q194 689 213 690T243
      693T254 694Q266 694 266 686Q266 675 193 386T118 83Q118 81 118 75T117 65V59Z"
      id="E2-MJMATHI-6C" stroke-width="1"></path><path d="M39 168Q39 225 58 272T107
      350T174 402T244 433T307 442H310Q355 442 388 420T421 355Q421 265 310 237Q261 224 176 223Q139
      223 138 221Q138 219 132 186T125 128Q125 81 146 54T209 26T302 45T394 111Q403 121 406 121Q410
      121 419 112T429 98T420 82T390 55T344 24T281 -1T205 -11Q126 -11 83 42T39 168ZM373 353Q367 405
      305 405Q272 405 244 391T199 357T170 316T154 280T149 261Q149 260 169 260Q282 260 327 284T373
      353Z" id="E2-MJMATHI-65" stroke-width="1"></path><path d="M308 24Q367 24 416
      76T466 197Q466 260 414 284Q308 311 278 321T236 341Q176 383 176 462Q176 523 208 573T273 648Q302
      673 343 688T407 704H418H425Q521 704 564 640Q565 640 577 653T603 682T623 704Q624 704 627
      704T632 705Q645 705 645 698T617 577T585 459T569 456Q549 456 549 465Q549 471 550 475Q550 478
      551 494T553 520Q553 554 544 579T526 616T501 641Q465 662 419 662Q362 662 313 616T263 510Q263
      480 278 458T319 427Q323 425 389 408T456 390Q490 379 522 342T554 242Q554 216 546 186Q541 164
      528 137T492 78T426 18T332 -20Q320 -22 298 -22Q199 -22 144 33L134 44L106 13Q83 -14 78 -18T65
      -22Q52 -22 52 -14Q52 -11 110 221Q112 227 130 227H143Q149 221 149 216Q149 214 148 207T144
      186T142 153Q144 114 160 87T203 47T255 29T308 24Z" id="E2-MJMATHI-53"
      stroke-width="1"></path><path d="M201 -11Q126 -11 80 38T34 156Q34 221 64 279T146
      380Q222 441 301 441Q333 441 341 440Q354 437 367 433T402 417T438 387T464 338T476 268Q476 161
      390 75T201 -11ZM121 120Q121 70 147 48T206 26Q250 26 289 58T351 142Q360 163 374 216T388 308Q388
      352 370 375Q346 405 306 405Q243 405 195 347Q158 303 140 230T121 120Z" id="E2-MJMATHI-6F"
      stroke-width="1"></path><path d="M21 287Q22 290 23 295T28 317T38 348T53 381T73
      411T99 433T132 442Q161 442 183 430T214 408T225 388Q227 382 228 382T236 389Q284 441 347
      441H350Q398 441 422 400Q430 381 430 363Q430 333 417 315T391 292T366 288Q346 288 334 299T322
      328Q322 376 378 392Q356 405 342 405Q286 405 239 331Q229 315 224 298T190 165Q156 25 151 16Q138
      -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 114 189T154 366Q154 405 128 405Q107 405 92 377T68
      316T57 280Q55 278 41 278H27Q21 284 21 287Z" id="E2-MJMATHI-72"
      stroke-width="1"></path><path d="M26 385Q19 392 19 395Q19 399 22 411T27 425Q29 430
      36 430T87 431H140L159 511Q162 522 166 540T173 566T179 586T187 603T197 615T211 624T229 626Q247
      625 254 615T261 596Q261 589 252 549T232 470L222 433Q222 431 272 431H323Q330 424 330 420Q330
      398 317 385H210L174 240Q135 80 135 68Q135 26 162 26Q197 26 230 60T283 144Q285 150 288 151T303
      153H307Q322 153 322 145Q322 142 319 133Q314 117 301 95T267 48T216 6T155 -11Q125 -11 98 4T59
      56Q57 64 57 83V101L92 241Q127 382 128 383Q128 385 77 385H26Z" id="E2-MJMATHI-74"
      stroke-width="1"></path><path d="M94 250Q94 319 104 381T127 488T164 576T202
      643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275 667T226 581T184
      443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318 -250H315H302L274 -226Q180
      -141 137 -14T94 250Z" id="E2-MJMAIN-28" stroke-width="1"></path><path d="M208
      74Q208 50 254 46Q272 46 272 35Q272 34 270 22Q267 8 264 4T251 0Q249 0 239 0T205 1T141 2Q70 2 50
      0H42Q35 7 35 11Q37 38 48 46H62Q132 49 164 96Q170 102 345 401T523 704Q530 716 547
      716H555H572Q578 707 578 706L606 383Q634 60 636 57Q641 46 701 46Q726 46 726 36Q726 34 723
      22Q720 7 718 4T704 0Q701 0 690 0T651 1T578 2Q484 2 455 0H443Q437 6 437 9T439 27Q443 40 445
      43L449 46H469Q523 49 533 63L521 213H283L249 155Q208 86 208 74ZM516 260Q516 271 504 416T490
      562L463 519Q447 492 400 412L310 260L413 259Q516 259 516 260Z" id="E2-MJMATHI-41"
      stroke-width="1"></path><path d="M60 749L64 750Q69 750 74 750H86L114 726Q208 641
      251 514T294 250Q294 182 284 119T261 12T224 -76T186 -143T145 -194T113 -227T90 -246Q87 -249 86
      -250H74Q66 -250 63 -250T58 -247T55 -238Q56 -237 66 -225Q221 -64 221 250T66 725Q56 737 55
      738Q55 746 60 749Z" id="E2-MJMAIN-29" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E2-MJMATHI-42" y="0"></use><use x="759"
      xlink:href="#E2-MJMATHI-75" y="0"></use><use x="1332" xlink:href="#E2-MJMATHI-62"
      y="0"></use><use x="1761" xlink:href="#E2-MJMATHI-62" y="0"></use><use
      x="2191" xlink:href="#E2-MJMATHI-6C" y="0"></use><use x="2489"
      xlink:href="#E2-MJMATHI-65" y="0"></use><use x="3206" xlink:href="#E2-MJMATHI-53"
      y="0"></use><use x="3851" xlink:href="#E2-MJMATHI-6F" y="0"></use><use
      x="4337" xlink:href="#E2-MJMATHI-72" y="0"></use><use x="4788"
      xlink:href="#E2-MJMATHI-74" y="0"></use><use x="5400" xlink:href="#E2-MJMAIN-28"
      y="0"></use><use x="5789" xlink:href="#E2-MJMATHI-41" y="0"></use><use
      x="6540" xlink:href="#E2-MJMAIN-29" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>u</mi><mi>b</mi><mi>b</mi><mi>l</mi><mi>e</mi><mtext>&nbsp;</mtext><mi>S</mi><mi>o</mi><mi>r</mi><mi>t</mi><mtext>&nbsp;</mtext><mo
      stretchy="false">(</mo><mi>A</mi><mo
      stretchy="false">)</mo></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>in the next
      picture.</span></em></span></em><br />
      <br />
      Link to the image:<span class="Apple-converted-space">&nbsp;</span><a
      href="https://ibb.co/vzFR5kr" style="color: #4c9cdf; cursor: pointer; text-decoration-line:
      none;" target="_blank">https://ibb.co/vzFR5kr</a><br />
      <span style="font-weight: 600;">Input format</span><br />
      <ul style="padding-left: 40px;">
      <li>The first line contains the integer<span
      class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-3-Frame" role="presentation" style="border: 0px; direction: ltr; display:
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
      635 234 637Z" id="E3-MJMATHI-4E" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E3-MJMATHI-4E"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></span></span><span
      class="Apple-converted-space">&nbsp;</span>(<em><span
      style="font-weight: 600;"><span class="mathjax-latex"><span
      class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax_SVG"
      data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2A7D;&lt;/mo&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;mo&gt;&amp;#x2A7D;&lt;/mo&gt;&lt;mn&gt;5000&lt;/mn&gt;&lt;/math&gt;"
      id="MathJax-Element-4-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="2.276ex" role="img" style="vertical-align: -0.538ex;" viewbox="0 -748.3 6059.1 979.9"
      width="14.073ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M213
      578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285
      666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100
      0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" id="E4-MJMAIN-31"
      stroke-width="1"></path><path d="M674 636Q682 636 688 630T694 615T687 601Q686 600
      417 472L151 346L399 228Q687 92 691 87Q694 81 694 76Q694 58 676 56H670L382 192Q92 329 90 331Q83
      336 83 348Q84 359 96 365Q104 369 382 500T665 634Q669 636 674 636ZM94 170Q102 172 104 172Q110
      171 254 103T535 -30T678 -98Q694 -106 694 -118Q694 -136 676 -138H670L382 -2Q92 135 90 137Q83
      142 83 154Q84 164 94 170Z" id="E4-MJAMS-2A7D" stroke-width="1"></path><path
      d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683
      387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635
      650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682
      888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5
      453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272
      0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150
      85Q154 91 221 362L289 634Q287 635 234 637Z" id="E4-MJMATHI-4E"
      stroke-width="1"></path><path d="M164 157Q164 133 148 117T109 101H102Q148 22 224
      22Q294 22 326 82Q345 115 345 210Q345 313 318 349Q292 382 260 382H254Q176 382 136 314Q132 307
      129 306T114 304Q97 304 95 310Q93 314 93 485V614Q93 664 98 664Q100 666 102 666Q103 666 123
      658T178 642T253 634Q324 634 389 662Q397 666 402 666Q410 666 410 648V635Q328 538 205 538Q174
      538 149 544L139 546V374Q158 388 169 396T205 412T256 420Q337 420 393 355T449 201Q449 109 385
      44T229 -22Q148 -22 99 32T50 154Q50 178 61 192T84 210T107 214Q132 214 148 197T164 157Z"
      id="E4-MJMAIN-35" stroke-width="1"></path><path d="M96 585Q152 666 249 666Q297 666
      345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198
      -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571
      145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362
      478 354 524T321 597Z" id="E4-MJMAIN-30" stroke-width="1"></path></defs><g
      fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0
      0)"><use x="0" xlink:href="#E4-MJMAIN-31" y="0"></use><use x="778"
      xlink:href="#E4-MJAMS-2A7D" y="0"></use><use x="1834" xlink:href="#E4-MJMATHI-4E"
      y="0"></use><use x="3000" xlink:href="#E4-MJAMS-2A7D" y="0"></use><g
      transform="translate(4057,0)"><use xlink:href="#E4-MJMAIN-35"></use><use
      x="500" xlink:href="#E4-MJMAIN-30" y="0"></use><use x="1001"
      xlink:href="#E4-MJMAIN-30" y="0"></use><use x="1501" xlink:href="#E4-MJMAIN-30"
      y="0"></use></g></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>⩽</mo><mi>N</mi><mo>⩽</mo><mn>5000</mn></math></span></span>)
      denoting&nbsp;the number of elements of array<span
      class="Apple-converted-space">&nbsp;</span><em><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-5-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="2.143ex" role="img" style="vertical-align: -0.271ex;" viewbox="0 -805.7 750.5 922.5"
      width="1.743ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M208
      74Q208 50 254 46Q272 46 272 35Q272 34 270 22Q267 8 264 4T251 0Q249 0 239 0T205 1T141 2Q70 2 50
      0H42Q35 7 35 11Q37 38 48 46H62Q132 49 164 96Q170 102 345 401T523 704Q530 716 547
      716H555H572Q578 707 578 706L606 383Q634 60 636 57Q641 46 701 46Q726 46 726 36Q726 34 723
      22Q720 7 718 4T704 0Q701 0 690 0T651 1T578 2Q484 2 455 0H443Q437 6 437 9T439 27Q443 40 445
      43L449 46H469Q523 49 533 63L521 213H283L249 155Q208 86 208 74ZM516 260Q516 271 504 416T490
      562L463 519Q447 492 400 412L310 260L413 259Q516 259 516 260Z" id="E5-MJMATHI-41"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E5-MJMATHI-41" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></span></span>.</span></em></span></span></em></span></li>
      <li><em><span style="font-weight: 600;"><em>The second line
      contains<span class="Apple-converted-space">&nbsp;</span><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-6-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="2.009ex" role="img" style="vertical-align: -0.271ex;" viewbox="0 -748.3 888.5 865.1"
      width="2.064ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M234
      637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387
      683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650
      637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888
      672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453
      305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2
      151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221
      362L289 634Q287 635 234 637Z" id="E6-MJMATHI-4E"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E6-MJMATHI-4E" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML">N</math></span></span><span
      class="Apple-converted-space">&nbsp;</span>positive integers (<span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;&amp;#x2A7D;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;&amp;#x2A7D;&lt;/mo&gt;&lt;mi&gt;N&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-7-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="2.409ex" role="img" style="vertical-align: -0.538ex;" viewbox="0 -805.7 5151.9 1037.3"
      width="11.966ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M213
      578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285
      666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100
      0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" id="E7-MJMAIN-31"
      stroke-width="1"></path><path d="M674 636Q682 636 688 630T694 615T687 601Q686 600
      417 472L151 346L399 228Q687 92 691 87Q694 81 694 76Q694 58 676 56H670L382 192Q92 329 90 331Q83
      336 83 348Q84 359 96 365Q104 369 382 500T665 634Q669 636 674 636ZM94 170Q102 172 104 172Q110
      171 254 103T535 -30T678 -98Q694 -106 694 -118Q694 -136 676 -138H670L382 -2Q92 135 90 137Q83
      142 83 154Q84 164 94 170Z" id="E7-MJAMS-2A7D" stroke-width="1"></path><path
      d="M208 74Q208 50 254 46Q272 46 272 35Q272 34 270 22Q267 8 264 4T251 0Q249 0 239 0T205 1T141
      2Q70 2 50 0H42Q35 7 35 11Q37 38 48 46H62Q132 49 164 96Q170 102 345 401T523 704Q530 716 547
      716H555H572Q578 707 578 706L606 383Q634 60 636 57Q641 46 701 46Q726 46 726 36Q726 34 723
      22Q720 7 718 4T704 0Q701 0 690 0T651 1T578 2Q484 2 455 0H443Q437 6 437 9T439 27Q443 40 445
      43L449 46H469Q523 49 533 63L521 213H283L249 155Q208 86 208 74ZM516 260Q516 271 504 416T490
      562L463 519Q447 492 400 412L310 260L413 259Q516 259 516 260Z" id="E7-MJMATHI-41"
      stroke-width="1"></path><path d="M184 600Q184 624 203 642T247 661Q265 661 277
      649T290 619Q290 596 270 577T226 557Q211 557 198 567T184 600ZM21 287Q21 295 30 318T54 369T98
      420T158 442Q197 442 223 419T250 357Q250 340 236 301T196 196T154 83Q149 61 149 51Q149 26 166
      26Q175 26 185 29T208 43T235 78T260 137Q263 149 265 151T282 153Q302 153 302 143Q302 135 293
      112T268 61T223 11T161 -11Q129 -11 102 10T74 74Q74 91 79 106T122 220Q160 321 166 341T173
      380Q173 404 156 404H154Q124 404 99 371T61 287Q60 286 59 284T58 281T56 279T53 278T49 278T41
      278H27Q21 284 21 287Z" id="E7-MJMATHI-69" stroke-width="1"></path><path d="M234
      637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387
      683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650
      637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888
      672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453
      305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2
      151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221
      362L289 634Q287 635 234 637Z" id="E7-MJMATHI-4E"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E7-MJMAIN-31" y="0"></use><use x="778" xlink:href="#E7-MJAMS-2A7D"
      y="0"></use><g transform="translate(1834,0)"><use x="0"
      xlink:href="#E7-MJMATHI-41" y="0"></use><use transform="scale(0.707)" x="1061"
      xlink:href="#E7-MJMATHI-69" y="-213"></use></g><use x="3207"
      xlink:href="#E7-MJAMS-2A7D" y="0"></use><use x="4263" xlink:href="#E7-MJMATHI-4E"
      y="0"></use></g></svg><span class="MJX_Assistive_MathML"
      role="presentation" style="border: 0px !important; clip: rect(1px, 1px, 1px, 1px); display:
      block !important; height: 1px !important; left: 0px; overflow: hidden !important; padding: 1px
      0px 0px !important; position: absolute !important; top: 0px; transition: none 0s ease 0s;
      user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>⩽</mo><msub><mi>A</mi><mi>i</mi></msub><mo>⩽</mo><mi>N</mi></math></span></span>)
      denoting the&nbsp;elements of the array.<br />Note: It is guaranteed that all
      elements of array<span
      class="Apple-converted-space">&nbsp;</span><em><span
      class="mathjax-latex"><span class="MathJax_Preview" style="color:
      inherit;"></span><span class="MathJax_SVG" data-mathml="&lt;math
      xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;/math&gt;"
      id="MathJax-Element-8-Frame" role="presentation" style="border: 0px; direction: ltr; display:
      inline-block; float: none; font-size: 14px; font-style: normal; font-weight: normal;
      line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px;
      min-width: 0px; overflow-wrap: normal; padding: 0px; position: relative; white-space: nowrap;
      word-spacing: normal;" tabindex="0"><svg aria-hidden="true" focusable="false"
      height="2.143ex" role="img" style="vertical-align: -0.271ex;" viewbox="0 -805.7 750.5 922.5"
      width="1.743ex" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M208
      74Q208 50 254 46Q272 46 272 35Q272 34 270 22Q267 8 264 4T251 0Q249 0 239 0T205 1T141 2Q70 2 50
      0H42Q35 7 35 11Q37 38 48 46H62Q132 49 164 96Q170 102 345 401T523 704Q530 716 547
      716H555H572Q578 707 578 706L606 383Q634 60 636 57Q641 46 701 46Q726 46 726 36Q726 34 723
      22Q720 7 718 4T704 0Q701 0 690 0T651 1T578 2Q484 2 455 0H443Q437 6 437 9T439 27Q443 40 445
      43L449 46H469Q523 49 533 63L521 213H283L249 155Q208 86 208 74ZM516 260Q516 271 504 416T490
      562L463 519Q447 492 400 412L310 260L413 259Q516 259 516 260Z" id="E8-MJMATHI-41"
      stroke-width="1"></path></defs><g fill="currentColor" stroke-width="0"
      stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><use x="0"
      xlink:href="#E8-MJMATHI-41" y="0"></use></g></svg><span
      class="MJX_Assistive_MathML" role="presentation" style="border: 0px !important; clip:
      rect(1px, 1px, 1px, 1px); display: block !important; height: 1px !important; left: 0px;
      overflow: hidden !important; padding: 1px 0px 0px !important; position: absolute !important;
      top: 0px; transition: none 0s ease 0s; user-select: none; width: 1px !important;"><math
      xmlns="http://www.w3.org/1998/Math/MathML">A</math></span></span><span
      class="Apple-converted-space">&nbsp;</span>are
      different.</span></em></span></span></em></span></em></li>
      </ul>
      <em><span style="font-weight: 600;">Output format</span></em><br
      />
      <em><span style="font-weight: 600;">Print an integer that denotes the answer to
      the question.</span></em><br />
      <div class="less-margin-2 input-output-container" style="border-radius: 3px; border: 1px
      solid rgb(229, 231, 232); font-size: 14px; line-height: 21px; margin: 20px;">
      <div class="input-output right-border" style="border-right: 1px solid rgb(229, 231, 232);
      box-sizing: border-box; float: left; width: 448px;">
      <div class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); color: #252c33;
      padding: 6px 10px;">
      <div class="weight-600 less-margin-right light float-left small" style="color: #9ca3a8;
      float: left; font-size: 12px; font-weight: 600; margin-right: 5px;">
      <em>SAMPLE INPUT</em></div>
      <div class="input-output-opt float-right" style="float: right;">
      </div>
      <div class="clear" style="clear: both;">
      </div>
      </div>
      <div class="dark" style="color: #46535e;">
      <pre class="word-spacing-0" style="overflow-wrap: break-word; overflow-x: auto; padding:
      10px; white-space: pre-wrap;"><em><span style="font-weight: 600;">5
      1 3 2 5 4
      </span></em></pre>
      </div>
      </div>
      <div class="input-output" style="box-sizing: border-box; float: left; width: 448px;">
      <div class="form-label" style="border-bottom: 1px solid rgb(229, 231, 232); color: #252c33;
      padding: 6px 10px;">
      <div class="weight-600 float-left less-margin-right light small" style="color: #9ca3a8;
      float: left; font-size: 12px; font-weight: 600; margin-right: 5px;">
      <em>SAMPLE OUTPUT</em></div>
      <div class="input-output-opt float-right" style="float: right;">
      </div>
      <div class="clear" style="clear: both;">
      </div>
      </div>
      <div class="dark" style="color: #46535e;">
      <pre class="word-spacing-0" style="overflow-wrap: break-word; overflow-x: auto; padding:
      10px; white-space: pre-wrap;"><em><span style="font-weight: 600;">2
      </span></em></pre>
      </div>
      </div>
      <div class="clear" style="clear: both;">
      </div>
      </div>
      <em><span style="font-weight: 600;"><span
      class="mathjax-latex"></span></span></em><br />
      <div class="standard-margin" style="margin: 30px 0px 0px;">
      <em><strong style="font-weight: 600;"><em><strong style="font-weight:
      600;"><em><span class="weight-600 form-label" style="color: #252c33; font-size:
      14px; font-weight:
      600;">Explanation</span></em></strong></em></strong></em><br
      />
      <div class="less-margin" style="margin: 5px 0px 0px;">
      <em><strong style="font-weight: 600;"><em><strong style="font-weight:
      600;"><em>Answer is 2 (to verify this, you can simply implement this
      procedure)</em></strong></em></strong></em></div>
      <em><strong style="font-weight: 600;"><em><strong style="font-weight:
      600;"><em>
      </em></strong></em></strong></em></div>
      </div>
      <script
      src="https://gist.github.com/Svastikkka/ac4880bc54971f2345535ebf913913e6.js"></script>
      </div>


Write your content here...