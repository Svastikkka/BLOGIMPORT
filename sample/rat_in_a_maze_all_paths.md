# Rat In a Maze All Paths

Published: 2021-06-07T10:33:00.005+05:30

Description: 
      <h4
      id="you-are-given-a-n-n-maze-with-a-rat-placed-at-maze-0-0-find-and-print-all-paths-that-rat-can-follow-to-reach-its-destination-i-e-maze-n-1-n-1-rat-can-move-in-any-direc-tion-left-right-up-and-down"
      style="-webkit-font-smoothing: antialiased; background-color: white; color: #565656;
      font-family: Roboto, sans-serif; font-size: 14px; font-weight: 400; letter-spacing: 0.3px;
      line-height: 25px; margin: 0px; padding: 15px 0px 5px;">You are given a N*N maze with a rat
      placed at maze[0][0]. Find and print all paths that rat can follow to reach its destination
      i.e. maze[N-1][N-1]. Rat can move in any direc­tion ( left, right, up and
      down).</h4><h4
      id="value-of-every-cell-in-the-maze-can-either-be-0-or-1-cells-with-value-0-are-blocked-means-rat-can-not-enter-into-those-cells-and-those-with-value-1-are-open"
      style="-webkit-font-smoothing: antialiased; background-color: white; color: #565656;
      font-family: Roboto, sans-serif; font-size: 14px; font-weight: 400; letter-spacing: 0.3px;
      line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Value of every cell in the maze can
      either be 0 or 1. Cells with value 0 are blocked means rat can­not enter into those cells and
      those with value 1 are open.</h4><div><div _ngcontent-ffh-c133=""
      class="description ng-star-inserted" style="-webkit-font-smoothing: antialiased;
      background-color: white; font-family: Roboto, sans-serif; font-size: 16px; margin: 0px;
      padding: 0px;"><h5 id="input-format" style="-webkit-font-smoothing: antialiased; color:
      #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">Input
      Format</h5><pre style="-webkit-font-smoothing: antialiased; background-image:
      linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family:
      &quot;Open Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      20px; max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">The first line of
      input contains an integer 'N' representing
      the dimension of the maze.
      The next N lines of input contain N space-separated
      integers representing the type of the cell.
      </code></pre><h5 id="output-format" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Output Format :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">For each test case, print the path from start position to
      </code></pre><pre style="-webkit-font-smoothing: antialiased; background-image:
      linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family:
      &quot;Open Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      20px; max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">destination
      position and only cells that are part of the solution </code></pre><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">path should be 1,
      rest all cells should be 0.

      Output for every test case will be printed in a separate line.
      </code></pre><h5 id="note" style="-webkit-font-smoothing: antialiased; color:
      #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Note:</h5><pre style="-webkit-font-smoothing: antialiased; background-image:
      linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family:
      &quot;Open Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      20px; max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">You do not need to
      print anything, it has already been taken care of. </code></pre><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;">Just implement the given
      function.</pre><h5 id="constraints" style="-webkit-font-smoothing: antialiased;
      color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Constraints:</h5><p style="-webkit-font-smoothing: antialiased; color:
      #353535; font-size: 14px; letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 0px
      0px 5px;">0 &lt; N &lt; 11 0 &lt;= Maze[i][j] &lt;=1</p><pre
      style="-webkit-font-smoothing: antialiased; background-image: linear-gradient(-90deg,
      rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family: &quot;Open
      Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top: 20px;
      max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">Time Limit: 1sec
      </code></pre></div><div _ngcontent-ffh-c133="" class="description
      ng-star-inserted" style="-webkit-font-smoothing: antialiased; background-color: white;
      font-family: Roboto, sans-serif; font-size: 16px; margin: 0px; padding: 0px;"><h5
      id="sample-input-1" style="-webkit-font-smoothing: antialiased; color: #353535; font-size:
      14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px 0px;">Sample Input 1
      :</h5><pre style="-webkit-font-smoothing: antialiased; background-image:
      linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255, 0.35)); font-family:
      &quot;Open Sans&quot;, sans-serif; font-weight: 600; margin-bottom: 20px; margin-top:
      20px; max-width: 866px; overflow-x: hidden; padding: 25px;"><code
      style="-webkit-font-smoothing: antialiased; margin: 0px; padding: 0px;">3
      1 0 1
      1 0 1
      1 1 1
      </code></pre><h5 id="sample-output-1" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 1 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">1 0 0 1 0 0 1 1 1
      </code></pre><h4 id="sample-output-1-explanation"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Sample
      Output 1 Explanation :</h4><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">Only 1 path is possible

      1 0 0
      1 0 0
      1 1 1
      </code></pre><p style="-webkit-font-smoothing: antialiased; color: #353535;
      font-size: 14px; letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 0px 0px
      5px;">Which is printed from left to right and then top to bottom in one
      line.</p><h5 id="sample-input-2" style="-webkit-font-smoothing: antialiased; color:
      #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding: 15px 0px
      0px;">Sample Input 2 :</h5><pre style="-webkit-font-smoothing: antialiased;
      background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215, 193, 255,
      0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">3
      1 0 1
      1 1 1
      1 1 1
      </code></pre><h5 id="sample-output-2" style="-webkit-font-smoothing:
      antialiased; color: #353535; font-size: 14px; letter-spacing: 0.4px; margin: 0px; padding:
      15px 0px 0px;">Sample Output 2 :</h5><pre style="-webkit-font-smoothing:
      antialiased; background-image: linear-gradient(-90deg, rgba(255, 205, 242, 0.35), rgba(215,
      193, 255, 0.35)); font-family: &quot;Open Sans&quot;, sans-serif; font-weight: 600;
      margin-bottom: 20px; margin-top: 20px; max-width: 866px; overflow-x: hidden; padding:
      25px;"><code style="-webkit-font-smoothing: antialiased; margin: 0px; padding:
      0px;">1 0 0 1 1 1 1 1 1
      1 0 0 1 0 0 1 1 1
      1 0 0 1 1 0 0 1 1
      1 0 0 1 1 1 0 0 1
      </code></pre><h4 id="sample-output-2-explanation"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">Sample
      Output 2 Explanation :</h4><h4
      id="4-paths-are-possible-which-are-printed-in-the-required-format"
      style="-webkit-font-smoothing: antialiased; color: #565656; font-size: 14px; font-weight: 400;
      letter-spacing: 0.3px; line-height: 25px; margin: 0px; padding: 15px 0px 5px;">4 paths are
      possible which are printed in the required format.</h4></div></div>
      <script
      src="https://gist.github.com/Svastikkka/d0c407bab3084e3cc74b9e594992fee7.js"></script>

Write your content here...