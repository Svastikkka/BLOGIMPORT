# Access and modify all the resources of our Wiki.js using WikiJS API

Published: 2022-06-04T10:37:00.011+05:30

Description: <p>Hi everyone 😎 , Today we are going to see how to access or modify
      WikiJS resources using WikiJS API. WikiJS exposes GraphQL API to access and modify the stuff
      according to our requirements.</p><p>So In this blog post, we going to
      see&nbsp;</p><p></p><ul style="text-align: left;"><li>How to
      set up WikiJS's local environment using docker.</li><li>How to generate an API
      token in Wikijs.</li><li>Using API tokens how to access WikiJS resources and how
      to modify them.</li></ul><p></p><h3 style="text-align:
      left;"><b>First Local Setup using docker</b></h3><p>Here I am using
      docker to set up my local isolated WikiJS environment. Below is my docker-compose.yml file
      written by WikiJS contributors.</p><p><br /></p><script
      src="https://gist.github.com/Svastikkka/c0b4dc3c249e3b60665d31213e19f074.js"></script><p><br
      /></p><p>To build the WikiJS environment we just need to run the following
      command&nbsp;</p><p><span style="color: red;">docker-compose up
      -df&nbsp;
      [PATH_OF_DOCKER_COMPOSE_YML_FILE]</span></p><p></p><div
      class="separator" style="clear: both; text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4vYXis9KwBHlmQ1jlA13-xQznGy6ZpF1rKTsY9zrYnmFeT9iySld6rOBjiguLjZ1LNwmOdDbt8OyuEVlYDaWWrezwLOCcGvGfvAOOuJmIjNTKb6728HiSkp-twCMIDAguNJ37oNrMrwKlux8JQzD-tSidXW7E21dQCMuETJppgxpWN5qjSU17Kika/s1920/Screenshot%20from%202022-05-10%2019-49-10.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="1080"
      data-original-width="1920" height="180"
      src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4vYXis9KwBHlmQ1jlA13-xQznGy6ZpF1rKTsY9zrYnmFeT9iySld6rOBjiguLjZ1LNwmOdDbt8OyuEVlYDaWWrezwLOCcGvGfvAOOuJmIjNTKb6728HiSkp-twCMIDAguNJ37oNrMrwKlux8JQzD-tSidXW7E21dQCMuETJppgxpWN5qjSU17Kika/w320-h180/Screenshot%20from%202022-05-10%2019-49-10.png"
      width="320" /></a></div><p><br /></p>To check the environment
      is in a running state run the following
      command<p></p><p></p><p><span style="color: red;">docker
      ps</span></p><p></p><div class="separator" style="clear: both;
      text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9AWYE-ap2WdSf9nwx8QInkGcnRDMSV5C91QsU2_UXud0C78x1EWz0GuaPvS6GLNwGL7iJoU4zrzvTV13K-pNeuPHXro1jsb2BsefEllfH8DmWBrv7OILOFpbR5kLdMThIfub9GzCCo8GkssvNL1w5LLRmSy9cTcG9kpBd9lbjNlz9DX-d5OGCHTWc/s1920/Screenshot%20from%202022-05-10%2019-51-54.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="1080"
      data-original-width="1920" height="180"
      src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9AWYE-ap2WdSf9nwx8QInkGcnRDMSV5C91QsU2_UXud0C78x1EWz0GuaPvS6GLNwGL7iJoU4zrzvTV13K-pNeuPHXro1jsb2BsefEllfH8DmWBrv7OILOFpbR5kLdMThIfub9GzCCo8GkssvNL1w5LLRmSy9cTcG9kpBd9lbjNlz9DX-d5OGCHTWc/w320-h180/Screenshot%20from%202022-05-10%2019-51-54.png"
      width="320" /></a></div><br /><b><br
      /></b><p></p><h3 style="text-align: left;"><b>Second Generate
      API token</b></h3><p>After setup our local environment we are ready to
      create our initial Administrator&nbsp;account in our WikiJS.</p><p>1. On the
      browser type <span style="color: red;">localhost:80</span></p><div
      class="separator" style="clear: both; text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-Cd1jV5XnlDXLqRWmMAwl7d4bTOoy6shjt97A1urONUZlDQ5eSwxzOQV2OXQnlz3hcfMmlaKYDXrGNlRLqhv3iHt8GE3PNhanrbTp6Hik19EHuLJ8DVoImTqj1TJ-Jzjy2DLIoGhgfrT2oCiQnrGb5XOb8szzLkJKhxi50K4mmRUzsFon-IJzQ9Uh/s1920/Screenshot%20from%202022-05-10%2019-58-01.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="1080"
      data-original-width="1920" height="180"
      src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-Cd1jV5XnlDXLqRWmMAwl7d4bTOoy6shjt97A1urONUZlDQ5eSwxzOQV2OXQnlz3hcfMmlaKYDXrGNlRLqhv3iHt8GE3PNhanrbTp6Hik19EHuLJ8DVoImTqj1TJ-Jzjy2DLIoGhgfrT2oCiQnrGb5XOb8szzLkJKhxi50K4mmRUzsFon-IJzQ9Uh/w320-h180/Screenshot%20from%202022-05-10%2019-58-01.png"
      width="320" /></a></div><br /><p>2. Create an Administrator
      account&nbsp;</p><p></p><p></p><ul style="text-align:
      left;"><li>Email: localhost@gmail.com</li><li>Password:
      admin@123</li><li>Site URL: http://localhost</li></ul><div>Click
      Install</div><p></p><p>3. After login we see initial page of
      WikiJS.</p><div class="separator" style="clear: both; text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhi9tUQPXXFcs9pQjAun5obGfo33KzaV3X4KOgfsEiUPeWIsAHf2176CdYXLCltXDwNRWE5zXWnxrYdSLGz0JsSGRDN_s9AaOEMKP6Msa8ZX2nA004JFAQkL5E6MwaAGGPicIvlh0ytdmZKZ-uHIPMri_lyKgn7-aWC1bzZE_L5_SxVzCUF82AIFAGF/s1920/Screenshot%20from%202022-05-10%2020-11-18.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="1080"
      data-original-width="1920" height="180"
      src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhi9tUQPXXFcs9pQjAun5obGfo33KzaV3X4KOgfsEiUPeWIsAHf2176CdYXLCltXDwNRWE5zXWnxrYdSLGz0JsSGRDN_s9AaOEMKP6Msa8ZX2nA004JFAQkL5E6MwaAGGPicIvlh0ytdmZKZ-uHIPMri_lyKgn7-aWC1bzZE_L5_SxVzCUF82AIFAGF/w320-h180/Screenshot%20from%202022-05-10%2020-11-18.png"
      width="320" /></a></div><div class="separator" style="clear: both;
      text-align: center;"><br /></div><div class="separator" style="clear: both;
      text-align: left;">4. Click on
      the&nbsp;<b>ADMINISTRATION</b>&nbsp;button and we will be redirected to
      the administrator dashboard.</div><div class="separator" style="clear: both;
      text-align: left;"><br /></div><div class="separator" style="clear: both;
      text-align: center;"><a
      href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZ0gETSTLh-kg25CAp-kPk6mAMBNJHvYqOFPgQgLEtrg9dfxDdebFTfFou1MRwEluqYT0UMOtVBGfSbnwldflMVIDb5XmeOsfTe6gTyn5EDxKbz9uanbeSARIjgK0IWUkl2wEt-b0t_PnXFwKAn9NspZmUJl_pV1YwETC1mcbWIaSowqgF_Py_jfXu/s1920/Screenshot%20from%202022-05-10%2020-19-26.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="1080"
      data-original-width="1920" height="180"
      src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZ0gETSTLh-kg25CAp-kPk6mAMBNJHvYqOFPgQgLEtrg9dfxDdebFTfFou1MRwEluqYT0UMOtVBGfSbnwldflMVIDb5XmeOsfTe6gTyn5EDxKbz9uanbeSARIjgK0IWUkl2wEt-b0t_PnXFwKAn9NspZmUJl_pV1YwETC1mcbWIaSowqgF_Py_jfXu/w320-h180/Screenshot%20from%202022-05-10%2020-19-26.png"
      width="320" /></a></div><div class="separator" style="clear: both;
      text-align: center;"><br /></div><br /><div class="separator"
      style="clear: both; text-align: left;">5. On the left navigation bar under System click on
      API access</div><div class="separator" style="clear: both; text-align:
      left;"><br /></div><div class="separator" style="clear: both; text-align:
      center;"><a
      href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimObrZwAeddI6VSBMhFko8flNS8E_hxOr2og63hl1PQVQEbu29kI2my3HI1YSCbAAywdxO09jEv5Ep7O5pUG2dcuX6J5E21n-D7I_UnkHZDEZNKL4kjkLxvv3QXGj40TXO3H67FOfN2-elLDXg7IvdUFLnyj33vT_nvPhuCFv1OXi2ozsgS4M4MRY5/s1920/wiki_screenshot6.png"
      style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="1080"
      data-original-width="1920" height="180"
      src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimObrZwAeddI6VSBMhFko8flNS8E_hxOr2og63hl1PQVQEbu29kI2my3HI1YSCbAAywdxO09jEv5Ep7O5pUG2dcuX6J5E21n-D7I_UnkHZDEZNKL4kjkLxvv3QXGj40TXO3H67FOfN2-elLDXg7IvdUFLnyj33vT_nvPhuCFv1OXi2ozsgS4M4MRY5/w320-h180/wiki_screenshot6.png"
      width="320" /></a></div><br />By default GraphQL API is disabled so
      first, we have to click on the Enabled API button and thereafter we have to click on the New
      API Key button to generate an API token.<br /><br /><br />Now we are going
      to pass values in the New API Key form to generate a new API<div><ul
      style="text-align: left;"><li>Name: Testing</li><li>Expiration: 1
      year</li><li>Full Access: Checked</li></ul>Click Generate and copy the
      API token and paste this token to somewhere in a text file.<br
      /><b>Note</b>: Please copy the API token carefully.</div><br
      /><h3 style="text-align: left;"><b>Third, using API tokens to access WikiJS
      resources and modify them</b></h3><br /><div>After successfully
      creating our API token we are ready to use our token in our python script to perform the CURD
      operations.<br /><br /></div><div><b>Example 1</b>
      Performing Read operation: Get the list of pages in WikiJS</div><div><br
      /></div><script
      src="https://gist.github.com/Svastikkka/fae746b4a1aead05ba369b44cc1fc306.js"></script><div><br
      /></div><div><b>Example 2</b> Performing Read operation: Read a
      particular document</div><div><br /><script
      src="https://gist.github.com/Svastikkka/98643838e00ce9bb799095e113e2d53f.js"></script></div><div><br
      /></div><div><b>Example 3</b> Performing Write operation: Write
      content on the page</div><div><b>Note</b>: Page is already
      created<br /><script
      src="https://gist.github.com/Svastikkka/40dd7f2d4499ecd132641d67d5f87f79.js"></script><br
      /></div><div><b>Example 4</b> Performing Write operation: Create a
      page<br /><br /><script
      src="https://gist.github.com/Svastikkka/5dfb48582f91982528f052adfaac7bd8.js"></script><br
      /><b>Reference</b></div><div><ul><li>WikiJS GraphQL API
      <a
      href="https://docs.requarks.io/dev/api">https://docs.requarks.io/dev/api</a></li><li>WikiJS
      Installation&nbsp;<a
      href="https://docs.requarks.io/install">https://docs.requarks.io/install</a></li></ul><div><br
      /></div><div style="text-align: center;">Hope you enjoyed my blog post.
      😎</div><p></p></div>

Write your content here...