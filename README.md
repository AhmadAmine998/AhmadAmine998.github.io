# Ahmad Amine — academic website

A Jekyll website for GitHub Pages at https://ahmadamine998.github.io/.

## Content

- `index.md`: introduction, recent updates, peer review, and contact.
- `research.html`: explanations of the research themes.
- `_data/publications.yml`: all publication records, author order, and equal-contribution marks. The Research page combines the records into year groups, newest first.
- `_data/teaching.yml`: courses grouped by institution, role, semesters, and descriptions.
- `community.html`: Roboracer, open-source work, and outreach.
- `_data/journey.yml`: conferences, internships, and milestones, newest first.
- `_data/navigation.yml`: navigation links.
- `_layouts/homepage.html`: shared layout for every page.
- `assets/img/events/`: event photographs. Preserve each complete frame.
- `assets/img/teaching/`: original course photographs, with captions and alt text in `_data/teaching.yml`.
- `_includes/icons/`: self-hosted Font Awesome brand SVGs; their license is in `assets/licenses/font-awesome.txt`.
- `assets/fonts/`: self-hosted IBM Plex Sans with its license.
- `assets/js/theme.js`: Light, Dark, and System appearance selection.
- `assets/files/curriculum_vitae.pdf`: public CV. Keep the full application CV separately.

Course material links are intentionally absent until Ahmad is ready to share them.
Use `status: Accepted` for accepted conference papers until publication details
are available. Do not infer conference attendance from an authored paper.

## Research media and citation downloads

The Research page shows muted, looping videos without playback controls. The
SIT-LMPC video uses Ahmad's supplied public MP4 URL. FAIL has a local MP4 and a
downloadable GIF generated from the supplied explainer's eight learning updates.
Visitors who request reduced motion see the corresponding still image instead.
The hardware plots can be expanded below the SIT-LMPC demonstration.

To add a BibTeX download, save one exported citation as `assets/bib/<paper-id>.bib`
and set `bibtex: /assets/bib/<paper-id>.bib` in that paper's entry in
`_data/publications.yml`. The template then displays a download link beside Paper
and PDF. Leave the field absent until the corresponding file is ready. Use
Ahmad's Zotero export to preserve citation metadata and keys; do not invent
proceedings page numbers or DOIs for accepted papers.

## Contact

The email address is assembled after the visitor activates Show email, reducing
simple address harvesting. The script is public and browser bots can activate it;
this is a deterrent, not an access-control mechanism. The public PDF omits direct
email, phone, and street address. Academic pages remain searchable.

An external contact form would require a separate service with server-side bot
validation and rate limiting. Do not put service credentials in this repository.
Previously published contact details may remain in history, papers, or caches.

## Build

```sh
bundle install
bundle exec jekyll build
python3 .github/scripts/check_site.py
```

Pull requests build with GitHub Pages' Jekyll action and check local links,
publication and course coverage, navigation, contact exposure, and script syntax.
The workflow saves a compiled review artifact and does not deploy the site.

`assets/js/legacy-links.js` preserves the previous homepage's research and paper
anchors by routing visitors to the relevant new page. Course and publication
content renders without JavaScript; the email reveal and legacy redirects use it.

The header's Theme control defaults to System and follows changes to the operating
system appearance. A manual Light or Dark choice is saved locally across pages.
Without JavaScript or stored preferences, the CSS follows system appearance.
If local storage is unavailable, the control still works on the current page.

Historical content decisions and photo credits are recorded in
`.github/CONTENT_NOTES.md`. Those notes are not included in the public website.

The original site used [Minimal Light](https://github.com/yaoyao-liu/minimal-light).
The retained legacy theme files are not loaded by the current layout.
