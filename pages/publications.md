---
layout: publications
title: publications

permalink: /publications/
---

{:.alert .alert-warning}

<!-- This is a default page. See [configuration]({{ '/docs/configuration/' | relative_url }}) to learn more about **pages**.

To remove this page, you need to:

- Remove `pages/about.md`
- Update `_data/navigation.yml` to remove the link to this page from the top navigation. -->

## Publications

<div>
    <button id="toggleButton1">Toggle List 1 with Links</button>
    <button id="toggleButton2">Toggle List 2 with Links</button>
</div>

<ul id="listToToggle1" style="display: none;">
    <li><a href="https://example.com/link1">First linked item of list 1</a></li>
    <li><a href="https://example.com/link2">Second linked item of list 1</a></li>
    <li><a href="https://example.com/link3">Third linked item of list 1</a></li>
</ul>

<ul id="listToToggle2" style="display: none;">
    <li><a href="https://example.com/link4">First linked item of list 2</a></li>
    <li><a href="https://example.com/link5">Second linked item of list 2</a></li>
    <li><a href="https://example.com/link6">Third linked item of list 2</a></li>
</ul>

<script>
document.getElementById("toggleButton1").addEventListener("click", function() {
    var list1 = document.getElementById("listToToggle1");
    var list2 = document.getElementById("listToToggle2");
    list1.style.display = "block";
    list2.style.display = "none";
});

document.getElementById("toggleButton2").addEventListener("click", function() {
    var list1 = document.getElementById("listToToggle1");
    var list2 = document.getElementById("listToToggle2");
    list1.style.display = "none";
    list2.style.display = "block";
});
</script>
 

