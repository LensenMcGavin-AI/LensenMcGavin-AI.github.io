---
layout: page
title: Our Writing
permalink: /writing/
description: "Op-eds and articles on AI policy, regulation, and responsible AI in Aotearoa New Zealand, written by LensenMcGavin AI."
---

Op-eds and articles written by us. Where a piece was first published elsewhere, we include the original version here with full references.

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }}){% if post.published_in %} — published by [{{ post.published_in }}]({{ post.published_url }}){% endif %}, {{ post.date | date: "%-d %B %Y" }}
{% endfor %}
