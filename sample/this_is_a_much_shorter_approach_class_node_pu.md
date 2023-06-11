# \\ this is a much shorter approach
      class Node{
      pu...

Published: 2021-09-01T16:23:14.742+05:30

Description:  \\ this is a much shorter approach <br />class Node{<br
      />public:<br /> int data;<br /> Node *next;<br /> Node(int data){<br
      /> this -&gt; data = data;<br /> this -&gt; next = NULL;<br /> }<br
      />};<br /><br /><br />void printIthNode(Node *head, int i) {<br />
      <br /> Node* current = head; <br /> <br /> int count = 0; <br /> while
      (current != NULL) <br /> { <br /> if (count == i) <br /> cout
      &lt;&lt; current-&gt;data; <br /> count++; <br /> current =
      current-&gt;next; <br /> } <br /> 

Write your content here...