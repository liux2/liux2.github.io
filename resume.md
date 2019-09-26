---
layout: base
title: Resume
---

<div id="resume-pdf" class="base">
  <object data="{{ site.baseurl }}/resume/resume.pdf" type="application/pdf">
    <embed src="{{ site.baseurl }}/resume/resume.pdf" type='application/pdf'>
      Unable to display - <a href="{{ site.baseurl }}/resume/resume.pdf">Download</a>
    </embed>
  </object>
</div>

<script defer="defer" type="text/javascript">
var fullElementId = "resume-pdf"
var content = document.getElementById("content");
var fullElement = document.getElementById(fullElementId);
content.style.padding = 0;
content.style.margin = 0;
fullElement.style.height = content.scrollHeight + "px";
</script>
