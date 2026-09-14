<section id="publications" class="section" aria-labelledby="publications-heading">
  <p class="eyebrow">Publications</p><h2 id="publications-heading">Papers &amp; preprints</h2>
  <p class="publication-note">* Equal contribution. <a href="{{ site.google_scholar }}">Google Scholar <span aria-hidden="true">↗</span></a></p>
  {% assign all_papers = site.data.publications.main | concat: site.data.publications.workshops %}
  {% assign years = all_papers | group_by: 'year' | sort: 'name' | reverse %}
  {% for year in years %}
  <div class="publication-group">
    <h3>{{ year.name }}</h3>
    <ol class="publication-list">
      {% for paper in year.items %}
      <li class="publication" id="{{ paper.id }}">
        <p class="item-meta">{{ paper.venue_short }} · {{ paper.year }}{% if paper.status %} · {{ paper.status }}{% endif %}</p>
        <h4><a href="{{ paper.url }}">{{ paper.title | escape }}</a></h4>
        <p class="pub-authors">{{ paper.authors }}</p>
        <p class="pub-venue">{{ paper.venue | escape }}, {{ paper.year }}.</p>
        <div class="pub-links"><a href="{{ paper.url }}">Paper <span aria-hidden="true">↗</span><span class="sr-only">: {{ paper.title | escape }}</span></a>{% if paper.pdf %}<a href="{{ paper.pdf }}">PDF <span aria-hidden="true">↗</span><span class="sr-only">: {{ paper.title | escape }}</span></a>{% endif %}{% if paper.code %}<a href="{{ paper.code }}">Code <span aria-hidden="true">↗</span><span class="sr-only">: {{ paper.title | escape }}</span></a>{% endif %}</div>
      </li>
      {% endfor %}
    </ol>
  </div>
  {% endfor %}
</section>
