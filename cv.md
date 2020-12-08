---
layout: base
title: Curriculum vitae
---

<div id="cv-pdf" class="base">
  <object data="{{ site.baseurl }}/resume/cv.pdf" width="100%" height="800" type="application/pdf">
    <embed src="{{ site.baseurl }}/resume/cv.pdf" type='application/pdf'>
      Unable to display - <a href="{{ site.baseurl }}/resume/cv.pdf">Download</a>
    </embed>
  </object>
</div>

<script defer="defer" type="text/javascript">
var fullElementId = "cv-pdf"
var content = document.getElementById("content");
var fullElement = document.getElementById(fullElementId);
content.style.padding = 0;
content.style.margin = 0;
fullElement.style.height = content.scrollHeight + "px";
</script>
