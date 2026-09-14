---
layout: homepage
description: Ahmad Amine is a PhD student at Penn researching data-driven safe iterative control of dynamical systems under uncertainty.
---

<section class="home-intro" aria-labelledby="intro-heading">
  <div class="identity">
    <div><p class="eyebrow">Learning &amp; control</p><h1 id="intro-heading">Ahmad Amine</h1><p class="affiliation">PhD student · Penn Engineering</p></div>
    <img class="portrait" src="{{ site.avatar | relative_url }}" alt="Ahmad Amine" width="1746" height="2616" fetchpriority="high">
  </div>
  <p class="lead-statement">Data-driven safe iterative control</p>
  <p>I am a PhD student in Electrical and Systems Engineering at the University of Pennsylvania, advised by <a href="https://www.seas.upenn.edu/~rahulm/">Rahul Mangharam</a>. My research focuses on learning and control of dynamical systems under uncertainty.</p>
  <p>I study how successful task executions can improve control performance and how failed executions can identify constraints and invariance-preserving control inputs. My work combines model predictive control, learning, and system identification, with autonomous vehicles and autonomous racing as an application domain.</p>
  <p>At Penn, I also teach control and robotics as a teaching assistant and help organize international Roboracer competitions.</p>
  <p>I have a Masters in Robotics from Penn. Before my PhD, I got a BE in Electrical and Computer Engineering, with a minor in Mathematics, at the American University of Beirut.</p>
  <div class="profile-links" aria-label="Academic profiles">
    <a class="social-link" href="{{ site.google_scholar }}">{% include icons/google-scholar.svg %}Google Scholar</a>
    <a class="social-link" href="{{ site.github_link }}">{% include icons/github.svg %}GitHub</a>
    <a class="social-link" href="{{ site.linkedin }}">{% include icons/linkedin.svg %}LinkedIn</a>
    <a href="{{ site.cv_link | relative_url }}">CV <span class="link-note">PDF ↗</span></a>
  </div>
</section>

<section class="section" aria-labelledby="updates-heading">
  <p class="eyebrow">Recently</p><h2 id="updates-heading">Research &amp; community news</h2>
  <ul class="updates-list">
    <li><p class="item-meta">2026 · Papers</p><p><a href="{{ '/research/' | relative_url }}#fail">FAIL</a> has been accepted to CDC 2026. <a href="{{ '/research/' | relative_url }}#ad-mpcc">AD-MPCC</a> and <a href="{{ '/research/' | relative_url }}#stl-svpio">STL-SVPIO</a> have been accepted to IROS 2026.</p></li>
    <li><p class="item-meta">June 2026 · Vienna &amp; Detroit</p><p>I helped organize the Roboracer competitions at ICRA, with 30 teams, and IV, with 14 teams. <a href="{{ '/journey/' | relative_url }}">Conference photos and notes <span aria-hidden="true">→</span></a></p></li>
    <li><p class="item-meta">Spring 2026 · Teaching</p><p>I served as lead teaching assistant for Penn’s autonomous racing course, giving lectures on optimal control, model predictive control, stochastic optimal control, and reinforcement learning. <a href="{{ '/teaching/' | relative_url }}">Courses and teaching roles <span aria-hidden="true">→</span></a></p></li>
  </ul>
</section>

<section id="peer-review" class="section" aria-labelledby="service-heading">
  <p class="eyebrow">Academic service</p><h2 id="service-heading">Peer review</h2>
  <p>I review for <a href="https://www.ieee-ras.org/publications/ra-l/"><em>IEEE Robotics and Automation Letters</em></a>, <a href="https://www.sciencedirect.com/journal/automatica"><em>Automatica</em></a>, and <a href="https://link.springer.com/journal/11081"><em>Optimization and Engineering</em></a>.</p>
  <p>My conference reviewing includes <a href="https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/">ICRA</a> (2025–2026), <a href="https://www.ieee-ras.org/conferences-workshops/financially-co-sponsored/iros/">IROS</a> (2023–2026), <a href="https://ro-man2026.org/">RO-MAN</a> (2023–2026), <a href="https://conferences.ifac-control.org/sysid2024/">SYSID</a> (2024), <a href="https://coinsconf.com/2025/">COINS</a> (2025), and <a href="https://ieee-iv.org/2026/">IV</a> (2026).</p>
</section>

<section id="contact" class="section contact" aria-labelledby="contact-heading">
  <h2 id="contact-heading">Contact</h2>
  <p>Got any questions about my research? Looking to collaborate on future research? Reach out!</p>
  <div class="contact-actions">
    <button type="button" class="button" id="reveal-email" aria-controls="email-details" aria-expanded="false" hidden>Show email <span aria-hidden="true">↗</span></button>
    <a class="social-link" href="{{ site.linkedin }}">{% include icons/linkedin.svg %}Connect on LinkedIn</a>
  </div>
  <div id="email-details" class="email-details" aria-live="polite" hidden><a id="email-link"></a></div>
  <noscript><p>You can contact me through LinkedIn.</p></noscript>
</section>
