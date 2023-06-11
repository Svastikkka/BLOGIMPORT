# MongoDB CheetSheet [In Progress]

Published: 2020-08-04T20:28:00.005+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      <div style="text-align: left;">
      This guide includes an introduction to MongoDB, a glossary of terms and lists of commonly used
      MongoDB commands with example.</div>
      <div style="text-align: left;">
      So here we go,&nbsp;</div>
      <h3 style="text-align: left;">
      Introduction</h3>
      <div style="text-align: left;">
      </div>
      <ol style="text-align: left;">
      <li>Mongodb is a non-relational database which means it&nbsp;does not use the
      tabular schema of rows and columns found in most traditional database systems<span face=""
      style="color: #222222; font-family: arial, sans-serif;"><span style="background-color:
      white;"> </span></span>like MySql.&nbsp;</li>
      <li>The second thing about mongodb is that it stores data in a key-value
      pair.&nbsp;</li>
      <li>The third thing about the mongodb is that the attribute<b> _id</b> which
      is unique and it is automatically created by Mongodb so chill&nbsp; 😎</li>
      </ol>
      <br />
      <h3 style="text-align: left;">
      MongoDB commands</h3>
      <ul style="text-align: left;">
      <li>Create Database:</li>
      <ul>
      <li>&nbsp; <span style="color: red; font-family: courier;">use
      &lt;Database Name&gt;</span></li>
      </ul>
      <li>Create Collection:&nbsp;</li><ul><li><span style="color:
      red; font-family:
      courier;">db.createCollection(&lt;"Name"&gt;,{&lt;Option&gt;})</span></li></ul>
      <li>Insert One document in collection:&nbsp;</li>
      <ul>
      <li><span style="color: red; font-family:
      courier;">db.&lt;Collection-Name&gt;.insertOne([{&lt;document&gt;}])</span></li>
      </ul>
      <li><span style="font-family: inherit;">Insert Many Documnets in
      Collection:&nbsp;</span></li>
      <ul>
      <li><span style="color: red; font-family:
      courier;">db.&lt;Collection-Name&gt;.insertMany([{&lt;document1&gt;},{&lt;document2&gt;}])</span></li>
      </ul>
      <li><span style="font-family: inherit;">Find a particular
      row:</span></li>
      <ul>
      <li><span style="color: red; font-family:
      courier;">db.getCollection("&lt;Collection-Name&gt;").find({&lt;column-name&gt;:"&lt;Unique
      Name/Id&gt;"})</span></li>
      </ul>
      <li><span style="font-family: inherit;">To check which db is
      selected:</span></li>
      <ul>
      <li><span style="color: red; font-family:
      courier;">&nbsp;db</span></li>
      </ul>
      <li><span style="font-family: inherit;">To check all databases who has at least
      one collection or document</span></li>
      <ul>
      <li><span style="color: red; font-family:
      courier;">showdbs</span></li>
      </ul>
      <li>To drop a database:</li>
      <ul>
      <li><span style="color: red; font-family:
      courier;">db.dropDatabase()</span></li>
      </ul>
      <li>To drop a collection in database:</li>
      <ul>
      <li><span style="color: red; font-family:
      courier;">db.&lt;collection-name&gt;.drop()</span></li>
      </ul>
      <li><span style="font-family: inherit;">To see collection:</span></li>
      <ul>
      <li><span style="color: red; font-family:
      courier;">db.&lt;collection-name&gt;.find()</span></li>
      </ul>
      <li><span style="font-family: inherit;">To check the version of
      mongodb:</span></li>
      <ul>
      <li><span style="color: red; font-family:
      courier;">db.version()</span></li></ul>
      </ul>
      <div>
      <br /></div>
      </div>


Write your content here...