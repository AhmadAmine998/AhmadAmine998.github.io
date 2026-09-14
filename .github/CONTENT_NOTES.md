# Content review — September 2026

The recent corrections and revised CV take precedence over older CVs. The old
CVs supplied on September 14 add historical background, not current positions.

## Sources and decisions

- Teaching semesters and titles: revised CV. Penn ESE 6150 is Lead TA; all other
  listed courses are TA roles. MEAM 5200's AprilTag/Gazebo work is from the revised CV.
- Band Industries internship (Jun–Aug 2019),
  Berkeley Summer 2018, AUB Robotics Club, and NXP Cup/Coder Maker: uploaded older CVs.
- Kept the recent Jun 2020–Aug 2021 dates for Band Industries and AUB research.
- An older CV mentions remote, part-time Band Industries work from September 2021
  without an end date. Do not describe this as ongoing without confirmation.
- Semester/month-only dates do not invent a precise travel day. Month-only entries
  can overlap conference dates, e.g., the TIER IV internship and IFAC.
- Do not add RO-MAN 2023 attendance based only on the VAHR publication. IROS 2026
  is upcoming and is not listed as a completed journey.
- ACC 2026: attendance confirmed by Ahmad. The exact role beyond attendance has
  not been supplied; do not label him an organizer or speaker.
- All newer publication acceptances and event participation counts come from Ahmad.
- The publication list combines journal, conference, and workshop records by citation
  year, newest first. The display does not invent month or day precision for records
  that contain only a year. Venue names and acceptance labels remain explicit.
- No generated photos; group images use their complete frame.
- Research scope follows Ahmad's supplied description of data-driven safe iterative
  control. Autonomous vehicles are applications, not the scope of the methods.
- SIT-LMPC addresses nonlinear stochastic systems; FAIL's convergence result is
  scoped to deterministic LTI systems with unknown dynamics and polytopic constraints.
  Failure-efficient identification and integration of the two approaches are ongoing
  research objectives, not completed results or established guarantees.

## Event dates

- ICRA 2024 (May 13–17, Yokohama):
  https://www.tuwien.at/inf/scuderia-segfault/news-detail/15th-grand-prix/
- CDC 2024 (Dec 16–19, Milan):
  https://www.tuwien.at/inf/scuderia-segfault/news-detail/victory-at-roboracer-autonomous-grand-prix-in-milano/
- ICRA 2025 (May 19–23, Atlanta):
  https://www.tuwien.at/inf/scuderia-segfault/
- MAD-Games at ACC 2026 (May 26, New Orleans):
  https://acc26-madgames.roboracer.ai/
- ICRA 2026 (June 1–5, Vienna): https://2026.ieee-icra.org/about/
- IV 2026 (June 22–25, Detroit): https://ieee-iv.org/
- IFAC 2023 (July 9–14, Yokohama): https://ifac2023.org/index.html

## Photos

- IV 2026, ICRA 2025, ICRA 2026: Ahmad's uploaded originals.
- ICRA 2024: Ahmad identified the previously selected photograph as Scuderia TU Wien,
  not all participating teams. That image and its caption have been removed. Keep
  the conference entry without a photo until the correct photograph is supplied.
- CDC 2024: Ahmad supplied `together-2.JPG` and identified it as the competition
  group photo. `assets/img/events/cdc-2024.jpg` retains the original 2048 × 1365
  image without cropping or retouching. This replaces the earlier missing-photo note.

## September 2026 website additions

- Changes build on Ahmad’s writing and Gemfile fixes in `c89a5a2`.
- MEAM 5200 and ESE 6150: Ahmad’s supplied original photographs, shown without
  cropping. The source filenames were `8520b50e-7aea-452f-9701-3f10120a7a4a.png`
  and `ADT06125.png`, respectively. No semester or event date is inferred.
- `IFAC2023.svg` is the existing ensemble Gaussian process architecture figure.
  The caption describes model weighting from recent measurements and links to
  the associated paper. Research diagrams link to their full-size originals.
- R5 repository: https://github.com/mlab-upenn/f1-fifth
- AUB Robotics Club: https://sites.aub.edu.lb/aubrobotics/ (provided by Ahmad).
- NXP article: https://www.aub.edu.lb/msfea/news/Pages/winning-nxp-competition.aspx
  This article concerns AUB’s 2024 team. It is linked as an example of the event,
  not as evidence of Ahmad’s participation in that edition or of his 2021 role.
- Peer-review links point to official publisher, society, or conference pages.
  The linked RO-MAN page is the 2026 edition; the recorded review years remain
  2023–2026. Links do not imply attendance or an editorial appointment.
- Brand icons: Font Awesome Free 6.7.2, `svgs/brands/{github,linkedin,google-scholar}.svg`
  from https://github.com/FortAwesome/Font-Awesome/tree/6.7.2/svgs/brands
  Icons are licensed CC BY 4.0. Source comments and the upstream license are
  retained. Added attributes size them, inherit link color, and hide redundant
  icon information from assistive technology; visible text labels remain.

## Research media and citations

- Ahmad supplied `FAIL-Website.html` and `SIT-LMPC-Website.html` as sources for
  animations and figures. Their full explanatory text is not republished.
- The FAIL animation uses the original explainer's numerical and Canvas drawing
  code for its seeded constrained double-integrator example (`runFAIL(2, 15)`).
  The state constraints are |x₁| ≤ 15, |x₂| ≤ 10, and the input constraint is
  |u| ≤ 5. It shows the initial set followed by eight halfspace updates, using
  the original slider states. No intermediate geometry is synthesized. The
  reported eight learned halfspaces and six trajectories describe this example,
  not a general bound. Numerical results are inherited from the supplied source.
- The nine FAIL frames were extracted with a DOM/Canvas renderer using the
  original script. The frames include a title and the original slider readout.
  The GIF holds each update for 1.4 seconds and the last frame for 2.8 seconds.
  The silent MP4 uses the same frames; its first frame is the reduced-motion poster.
- `r5-platform.jpg`, `sit-lmpc-hardware-lap-times.png`, and
  `sit-lmpc-hardware-boundary-violations.png` are byte-for-byte extractions of the
  embedded hardware photograph and two hardware plots in `SIT-LMPC-Website.html`.
  Figure dimensions and complete frames are retained. Captions describe the
  plotted experiment without making a general claim of zero violations or
  monotonic improvement.
- SIT-LMPC video URL supplied by Ahmad:
  https://pub-33ab648a62794a59a34293b3fe2bd3cd.r2.dev/SIT-LMPC/Sit_optimized.mp4
  It is embedded directly without transcoding. Both Research animations autoplay
  silently and loop without visible controls, as requested. System reduced-motion
  settings pause the videos and display still images. External video playback
  could not be verified in the editing environment.
- Source SHA-256 values:
  - FAIL HTML: `794989c6a16cc9cefe3a6b2afea1d848537b2d2f0064324b88d1681b58f7f030`
  - SIT-LMPC HTML: `6d8a73883a29e4161f06d384afcc6398a4685f7baced82c381785f7d283e9848`
- BibTeX download links are conditional on a `bibtex` file path in each publication
  record. No links are displayed until citation files are supplied. A Zotero BibTeX
  export from Ahmad can provide these files without inventing publication metadata.

## Potential additions from Ahmad

An ICRA 2024 photo or post/album link; a BibTeX export of the listed publications;
one short personal recollection from selected
trips (especially Japan, Milan, or Berkeley); any additional conferences actually
attended; details of the ACC workshop role if more than attendance; end date for
remote Band Industries work if it should be part of the public timeline.
