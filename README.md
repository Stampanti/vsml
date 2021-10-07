<h1 align="center">VSML</h1>
<h3 align="center">VideoStampanti Website Generator</h3>
<br>
<h2 align="center">How it works</h2>
<h3 align="center">Scripts</h3>
<p>You can import scripts into your page by adding their URL in the <code>config/scripts/default.json</code> file.<br>
Scripts in the "headScript#" strings are put in the <head> section of the HTML file [TODO], while the ones in "bodyScript#" are put in the <body> section of the HTML file [Working].</p>
<h3 align="center">Styles</h3>
<p>You can import styles into your page by adding their URL in the <code>config/styles/default.json</code> file.<br>
If you want to apply styles to the body, you can either use an external CSS stylesheet or edit it in the <code>bodyCss</code> string in the <code>config/pages/metatags.json</code> file.</p>
<h3 align="center">Pages</h3>
<p>Create a file with the page's name at <code>config/pages/[pagename].vsml</code>, containing the body of the page. <a href="config/pages/page1.vsml">See an example</a>.<br>
To create the page, use <code>python3 generatePages.py [pagename]</code>.<br>
  If everything goes well, you should see a message like <code>VSML created the page [pagename] successfully!</code> in your terminal, and an HTML file with the page's name in the <code>out/</code> directory.
</p>
<h3 align="center">Navbar/Sidebar</h3>
<p>TODO</p>
