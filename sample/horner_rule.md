# Horner rule

Published: 2020-08-25T14:46:00.000+05:30

Description: <div dir="ltr" style="text-align: left;" trbidi="on">
      <div dir="ltr" style="text-align: left;" trbidi="on">
      Given a polynomial of the form <span style="background-color: white; color: rgba(0 , 0 , 0
      , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size:
      16px;">c</span><span style="background-color: white; border: 0px; bottom: -0.25em;
      color: rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif;
      font-size: 12px; line-height: 0; margin: 0px; padding: 0px; position: relative;
      vertical-align: baseline;">n</span><span style="background-color: white; color:
      rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size:
      16px;">x</span><span style="background-color: white; border: 0px; color: rgba(0 ,
      0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size: 12px;
      line-height: 0; margin: 0px; padding: 0px; position: relative; top: -0.5em; vertical-align:
      baseline;">n</span><span style="background-color: white; color: rgba(0 , 0 , 0 ,
      0.84); font-family: &quot;roboto&quot; , sans-serif; font-size: 16px;">&nbsp;+
      c</span><span style="background-color: white; border: 0px; bottom: -0.25em; color:
      rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size: 12px;
      line-height: 0; margin: 0px; padding: 0px; position: relative; vertical-align:
      baseline;">n-1</span><span style="background-color: white; color: rgba(0 , 0 , 0 ,
      0.84); font-family: &quot;roboto&quot; , sans-serif; font-size:
      16px;">x</span><span style="background-color: white; border: 0px; color: rgba(0 ,
      0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size: 12px;
      line-height: 0; margin: 0px; padding: 0px; position: relative; top: -0.5em; vertical-align:
      baseline;">n-1</span><span style="background-color: white; color: rgba(0 , 0 , 0 ,
      0.84); font-family: &quot;roboto&quot; , sans-serif; font-size: 16px;">&nbsp;+
      c</span><span style="background-color: white; border: 0px; bottom: -0.25em; color:
      rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size: 12px;
      line-height: 0; margin: 0px; padding: 0px; position: relative; vertical-align:
      baseline;">n-2</span><span style="background-color: white; color: rgba(0 , 0 , 0 ,
      0.84); font-family: &quot;roboto&quot; , sans-serif; font-size:
      16px;">x</span><span style="background-color: white; border: 0px; color: rgba(0 ,
      0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size: 12px;
      line-height: 0; margin: 0px; padding: 0px; position: relative; top: -0.5em; vertical-align:
      baseline;">n-2</span><span style="background-color: white; color: rgba(0 , 0 , 0 ,
      0.84); font-family: &quot;roboto&quot; , sans-serif; font-size: 16px;">&nbsp;+
      … + c</span><span style="background-color: white; border: 0px; bottom: -0.25em;
      color: rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif;
      font-size: 12px; line-height: 0; margin: 0px; padding: 0px; position: relative;
      vertical-align: baseline;">1</span><span style="background-color: white; color:
      rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size:
      16px;">x + c</span><span style="background-color: white; border: 0px; bottom:
      -0.25em; color: rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif;
      font-size: 12px; line-height: 0; margin: 0px; padding: 0px; position: relative;
      vertical-align: baseline;">0</span><span style="background-color: white; color:
      rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size:
      16px;">&nbsp;</span>and a value of x, find the value of polynomial for a given
      value of x. Here<span style="background-color: white; color: rgba(0 , 0 , 0 , 0.84);
      font-family: &quot;roboto&quot; , sans-serif; font-size:
      16px;">&nbsp;c</span><span style="background-color: white; border: 0px;
      bottom: -0.25em; color: rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; ,
      sans-serif; font-size: 12px; line-height: 0; margin: 0px; padding: 0px; position: relative;
      vertical-align: baseline;">n</span><span style="background-color: white; color:
      rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size:
      16px;">, c</span><span style="background-color: white; border: 0px; bottom:
      -0.25em; color: rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif;
      font-size: 12px; line-height: 0; margin: 0px; padding: 0px; position: relative;
      vertical-align: baseline;">n-1</span><span style="background-color: white; color:
      rgba(0 , 0 , 0 , 0.84); font-family: &quot;roboto&quot; , sans-serif; font-size:
      16px;">, ..&nbsp;</span>are integers (may be negative) and n is a positive
      integer.</div>
      <script
      src="https://gist.github.com/Svastikkka/71a7f037084608d626f5d806c1e64976.js"></script>
      </div>


Write your content here...