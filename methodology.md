# Methodology — news-image-20261125

## What this entry is

A one-page newspaper poster of **Wednesday 25 November 2026** — a single
1024×1024 PNG (`entry.png`), produced by `draw_poster.py` (Pillow +
DejaVu, run locally) and shipped by `main.py`, which only copies the
finished PNG. Layout: masthead ("WEDNESDAY 25 NOVEMBER 2026" + "40
STORIES · 7 REGIONS · EVERY FIGURE DATED + SOURCED") + 3 hero stories
with drawn scenes + 10 grid stories with drawn vector scenes + 14
text-only grid stories + 13 "Also on" stories + a 12-pin world map + a
DATE CHECK box + a sources footer. **40 distinct stories in total**
(3 + 10 + 14 + 13 = 40).

## The event-date rule

A story belongs on this poster only if its event **happened on, or was
first reported on, Wednesday 25 November 2026 in some timezone**,
verified against the source article's own body/dateline or a primary
wire — never against an aggregator listing date. Overnight items are
kept only when first reported on Wednesday, and are labelled honestly:
the Cartagena rescue (siege began Tuesday, rescue early Wednesday),
the Savasleyka strike (overnight 24–25 Nov, announced Wednesday) and
the RSF strikes (overnight, reported Wednesday) all say so on the
poster. Stories whose true event date was not Wed 25 Nov were dropped
and are listed with their correct dates in the DATE CHECK box.

## The badge system

Four levels, shown as a chip on every illustrated story (heroes 1–3
and grid 4–13) plus a legend on the poster:

- **CONFIRMED** — verified by 2+ wires / primary sources.
- **OFFICIAL** — on the record (company, government or court release).
- **REPORTED** — one outlet.
- **CLAIM** — one side says; not independently verified.

Badge assignments (illustrated stories):

| # | Story | Badge |
|---|-------|-------|
| 1 | US proposes tariffs on 14 economies | CONFIRMED |
| 2 | Hormuz mine claims go to gas + Ras Tanura hit claim | CLAIM |
| 3 | Pakistan's first astronaut reaches Tiangong | CONFIRMED |
| 4 | US inflation 3.8% in October | OFFICIAL |
| 5 | Army blows up lead-azide stockpile | OFFICIAL |
| 6 | Second judge blocks birthright order | CONFIRMED |
| 7 | Wall Street stages late comeback | CONFIRMED |
| 8 | Cartagena hostages all freed | CONFIRMED |
| 9 | Brazil's real rallies as bank sells $2bn | REPORTED |
| 10 | Ecuador campaign ends | REPORTED |
| 11 | Bolivia ex-oil chief testifies twice | REPORTED |
| 12 | Ukraine hits Savasleyka air base | OFFICIAL (Ukrainian claim on damage) |
| 13 | Merz: "Russia wants more than Ukraine" | OFFICIAL |

## Region split (must sum to 40)

| Region | Count | Stories |
|---|---|---|
| North America | 7 | 1 tariffs, 4 inflation, 5 stockpile, 6 birthright, 7 Wall St, 37 Macy's parade, 38 Mississippi plane crash |
| Latin America | 4 | 8 Cartagena, 9 Brazil real, 10 Ecuador, 11 Bolivia |
| Europe | 7 | 12 Savasleyka, 13 Merz, 14 Murmansk, 15 riot gas, 16 Europe shares, 17 Champions League, 18 Top Gear |
| Middle East | 6 | 2 Hormuz, 19 Hamas security chief, 20 Netanyahu judges, 21 Knesset inquiry, 22 oil, 39 Lebanon airport |
| Africa | 6 | 23 Cairo fire, 24 Sudan strikes, 25 Ramaphosa, 26 Mackenzie, 27 Ebola evacuation, 28 Edochie |
| Asia | 7 | 3 Shenzhou-24, 29 Asia AI rout, 30 North Korea, 31 Xiaomi/Shanghai, 32 Sri Lanka cricket, 33 India hockey, 34 Gukesh–Sindarov |
| Oceania | 3 | 35 Solomons pact, 36 Australia CPI, 40 Blyth defection |
| **Total** | **40** | 7 + 4 + 7 + 6 + 6 + 7 + 3 = 40 |

## The full 40-story list (source + event date each)

### Heroes (1–3)

| # | Story | Source | Event date |
|---|-------|--------|------------|
| 1 | US proposes tariffs on 14 economies — China up to 20% (40% if talks fail), EU 15%, India up to 25%, Vietnam up to 35%; hearings 25 Jan 2027 | USTR / Reuters / AP | Wed 25 Nov 2026 (Section 301 findings) |
| 2 | Hormuz mine claims go to gas + Ras Tanura hit claim — IRGC claims 2 tankers + 1 LNG carrier hit mines Wed evening (unverified, no vessel names); Houthis claim Ras Tanura refinery attack, 4 drones intercepted; Brent +3.5% | Reuters | Wed 25 Nov 2026 (claims; NOT verified fact) |
| 3 | Shenzhou-24: Pakistan's first astronaut reaches Tiangong — launch 00:18 UTC, dock 03:56 UTC; Muhammad Zeeshan Ali first foreign astronaut on Tiangong | Xinhua / CMSA / Reuters | Wed 25 Nov 2026 |

### Grid, illustrated (4–13)

| # | Story | Source | Event date |
|---|-------|--------|------------|
| 4 | US inflation 3.8% in October — PCE +3.8% y/y, core 3.3%; real spending −$5.8bn; far above Fed 2% target | BEA via AP | Wed 25 Nov 2026 |
| 5 | Army blows up entire lead-azide stockpile in Iowa — ~5 tons / 68 barrels detonated 10:08 ET Wed in Middletown; shelter-in-place until all-clear | AP / US Army | Wed 25 Nov 2026 |
| 6 | Second judge blocks Trump's birthright order — Judge Christopher Cooper, Washington DC, 67-page preliminary injunction vs August executive order | AP / Bloomberg Law | Wed 25 Nov 2026 |
| 7 | Wall Street stages late comeback — CLOSE Wed: Dow 50,182.95 +0.33%, S&P 500 7,182.78 −0.25%, Nasdaq 23,585.80 −0.62% (S&P was −3.2% intraday, Dow erased a 1,100-pt fall); Russell 2000 +0.71% | AP / Reuters | Wed 25 Nov 2026 (closes) |
| 8 | Cartagena hostages all freed after 17 hours — security forces stormed Éxito supermarket early Wed; ~30 taken Tue after failed armoured-car robbery, ~20 rescued in raid, 1 captor killed | Reuters / AFP | Rescue Wed 25 Nov 2026 (siege began Tue) |
| 9 | Brazil's real rallies as central bank sells $2bn — real gained Wed, dollar −1.5%; spending-cut talks continue | Rio Times | Wed 25 Nov 2026 |
| 10 | Ecuador election campaign ends — campaign ends Thu, then silence + 72-hour alcohol ban, $241 fines, ahead of Sunday local vote | Rio Times | Wed 25 Nov 2026 |
| 11 | Bolivia ex-oil chief testifies twice — former state oil chief Yussef Akly gave statements twice Wed to La Paz prosecutors as a witness in gasoline case; not charged | Rio Times | Wed 25 Nov 2026 |
| 12 | Ukraine hits Savasleyka air base, 5 planes damaged — strike overnight 24–25 Nov, announced Wed by Ukrainian General Staff: 3 MiG-31s + 2 Su-34s "knocked out for some time"; also 2 Samara refineries hit | Reuters / Ukrainian General Staff | Wed 25 Nov 2026 (announced; strike overnight) |
| 13 | Merz: "Russia wants more than Ukraine" — German Chancellor tells Bundestag Wed, defending defence spending + Ukraine aid | Reuters | Wed 25 Nov 2026 |

### Grid, text-only (14–27)

| # | Story | Source | Event date |
|---|-------|--------|------------|
| 14 | Murmansk governor held in corruption probe — head of Russia's Murmansk region placed in pre-trial detention for 2 months Wed, Moscow court | Reuters | Wed 25 Nov 2026 |
| 15 | 34 countries + EU tell Russia to stop riot gas in Ukraine — joint call Wed after chemical-weapons watchdog confirmed tear-gas traces in a trench Kyiv said was hit by a Russian grenade | Reuters | Wed 25 Nov 2026 |
| 16 | Europe shares fall as AI fears return — CLOSE Wed: Euro Stoxx 50 5,894.46 −1.82%, DAX 24,702.13 −1.26%, FTSE 100 10,427 −0.38% | Morningstar / Dow Jones | Wed 25 Nov 2026 (closes) |
| 17 | Champions League, Wed night — PSG 2–2 Roma, Sporting 2–2 Man Utd (Fernandes double; Tielemans sent off), Liverpool 3–0 Club Brugge, Bayern lose 2–1 at Lille, Inter 2–0 Stuttgart, Barcelona 4–1 Sabah, Atlético 2–0 Viking | UEFA / Flashscore | Wed 25 Nov 2026 (evening) |
| 18 | Gordon Ramsay to lead Top Gear revival — BBC flagship motoring show revival announced Wed | AP / BBC | Wed 25 Nov 2026 |
| 19 | Israel kills Hamas security chief in Gaza — Mohammad Abuelouf, head of Hamas interior security, killed Wed with his wife + 2 children in Beach camp strike; IDF said it "targeted several military operatives" | Reuters / Gaza medics | Wed 25 Nov 2026 |
| 20 | Israeli judges urge dropping Netanyahu bribery charge — Jerusalem judges tell attorney general Wed: little chance of conviction in Case 4,000; question criminality in Case 2,000; suggest plea deal in Case 1,000 | Al Jazeera / BBC | Wed 25 Nov 2026 |
| 21 | Knesset takes first step to Oct 7 inquiry — Israel's parliament Wed took initial step toward a state commission of inquiry into security failures of 7 Oct 2023; caretaker PM Netanyahu long opposed it | AP | Wed 25 Nov 2026 |
| 22 | Oil jumps: Brent $94.61, +3.5% — Brent settled $94.61/bbl (+3.5%), WTI $83.68 (+2.0%) Wed on Hormuz/Ras Tanura disruption fears | Rigzone / CNBC | Wed 25 Nov 2026 |
| 23 | Cairo ring-road fire kills 31 — fuel tanker overturned Wed evening on Warraq ring road, fire killed 31, injured 21 (Reuters; AP said "at least 30" — Reuters 31 used) | Reuters / Egypt Health Ministry | Wed 25 Nov 2026 |
| 24 | RSF drone strikes kill 19 civilians in Sudan — overnight strikes Wed on Damazin + Roseires, Blue Nile: 19 killed incl. 6 women, 20 wounded | Emergency Lawyers via Reuters | Wed 25 Nov 2026 (overnight, reported Wed) |
| 25 | Ramaphosa wins Phala Phala court battle — Western Cape High Court Wed set aside in its entirety the 2022 Section 89 panel report ($580,000 farm theft); impeachment inquiry falls away | Sowetan / Al Jazeera / Reuters | Wed 25 Nov 2026 |
| 26 | Kenya cult leader convicted again — Paul Mackenzie, serving 200 years for ~191 Shakahola deaths, convicted Wed on 5 counts cruelty to a child + 1 assault | Reuters | Wed 25 Nov 2026 |
| 27 | Ebola workers evacuated in eastern Congo — fighting forced WHO to move its Mongbwalu team + partners to Bunia Wed; monitoring of exposed people disrupted | AP / WHO | Wed 25 Nov 2026 |

### Also-on (28–40)

| # | Story | Source | Event date |
|---|-------|--------|------------|
| 28 | Nollywood legend Pete Edochie dies at 79 — died early Wed in Enugu after prolonged prostate cancer, family announced | OkayAfrica | Wed 25 Nov 2026 |
| 29 | Asia AI rout: KOSPI −6.16% — CLOSE Wed: KOSPI 4,697.51 −6.16% (Samsung −9.9%, SK Hynix −11.1%), Nikkei 57,011.62 −2.78% (SoftBank −14.8%), Taiex ~−4.9%, Shanghai 3,476.47 −2.03%, Hang Seng 21,966.01 −1.14%; India Nifty bucked trend +1.85% | AP / Reuters | Wed 25 Nov 2026 (closes) |
| 30 | North Korea expels Swiss diplomat — Pyongyang Wed ordered Swiss office closed, head of mission persona non grata, 48 hours to leave, over Swiss sanctions on Songdowon children's camp | KCNA via BBC | Wed 25 Nov 2026 |
| 31 | Xiaomi profit falls 68%, Shanghai at 1-year low — Shanghai Composite fell Wed to lowest in over a year as Xiaomi profit dropped 68% | AP | Wed 25 Nov 2026 |
| 32 | Sri Lanka women win Emerging Nations Trophy — beat Ireland by 6 wickets Wed (Ireland 96, Sri Lanka 99/4 in 12.4 overs) | RevSportz | Wed 25 Nov 2026 |
| 33 | India women thrash Japan 4–0 in hockey — completed clean sweep of Women's Asian Champions Trophy league stage Wed in Bhopal; India rose to career-best world No. 5 | The Hindu | Wed 25 Nov 2026 |
| 34 | Chess Game 2: Gukesh–Sindarov draw in 20 moves — World Championship, Geneva Wed: Gukesh (White, London System) drew Sindarov by threefold repetition in 1h57m; match level 1–1; prize fund $2.5m | ChessBase / FIDE | Wed 25 Nov 2026 |
| 35 | Australia–Solomon Islands security pact signed — Canberra Wed: Australia becomes defence partner of choice, Honiara bars foreign military bases; AU$740m over a decade (AFP) for education/health/policing; China pact reported scrapped, Wale declined to confirm (NDA) | Reuters / AFP | Wed 25 Nov 2026 |
| 36 | Australia inflation jumps to 4.9% — Oct CPI 4.9% y/y (from 4.3%, forecast ~4.7%), trimmed mean 3.8%; ASX 200 closed −0.39% at 8,692.4 Wed | ABS via Guardian / ABC | Wed 25 Nov 2026 |
| 37 | Macy's Thanksgiving Parade postponed to Saturday — bad weather expected Thu; milestone parade with Blue Hippo/Bluey floats | AP | Wed 25 Nov 2026 |
| 38 | Plane crash off Mississippi kills family of 6 — extended family on a fishing trip, killed Wed | AP | Wed 25 Nov 2026 |
| 39 | Lebanon to open second airport next month — Kleiat (Rene Mouawad) Airport to open next month, flights initially to Turkey, Egypt and Jordan; private sector to invest $5–6m; 4-year concession to Sky Lounge | Reuters (Kleiat dateline, Nov 25) | Wed 25 Nov 2026 |
| 40 | Australian senator defects to One Nation — SA Liberal senator Leah Blyth defected Wed, becoming One Nation's first upper-house member from the state | The Actual News summary | Wed 25 Nov 2026 |

## Story substitution

**#39 was swapped in after verification, #40 is the displaced story.**
The brief's #39 (Australian senator defects to One Nation, via The
Actual News summary) was flagged as the weakest link, with instructions
to swap it for Lebanon's second-airport announcement if verifiable.
A web search verified it: Reuters, dateline KLEIAT AIRPORT, Lebanon,
Nov 25 — "Lebanon plans to open a second international airport next
month", by Laila Bassam and Nazih Osseiran, with the transport
minister (Fayez Rasamny) on the record. The swap was made, and the
senator story was kept as #40 (the spare slot), so the poster still
carries 40 stories and the region split still sums to 40 (Middle East
6 with Lebanon, Oceania 3 with the senator).

## Distinct-count check

3 heroes + 10 illustrated grid + 14 text grid + 13 Also-on = **40
distinct stories**. No duplicates:

- The Hormuz mine claims (#2, Wed) and the Hormuz claims in DATE
  CHECK (Tue) are two different days' claims, kept apart deliberately.
- The tariff proposal (#1) and the Wall Street close (#7) are two
  different events (a USTR finding vs a market close).
- The two Hormuz-adjacent oil items (#2 claims, #22 Brent price) are a
  claim and a market reaction, not the same story.
- Gukesh Game 2 (#34, Wed) vs Game 1 (Tue, DATE CHECK) are different
  games.
- The CAS verdict (Tue, DATE CHECK) vs Morocco's challenge (Wed) are
  different events; only the challenge is a Wednesday event, and it is
  noted in the DATE CHECK footnote rather than given its own story.

## Map-pin check (12 pins)

| Pin | Place | Story |
|-----|-------|-------|
| 1 | Washington | Tariffs (#1) |
| 2 | Strait of Hormuz | Hormuz claims (#2) |
| 3 | Jiuquan | Shenzhou-24 (#3) |
| 5 | Iowa | Lead-azide stockpile (#5) |
| 8 | Cartagena | Hostages freed (#8) |
| 12 | Savasleyka | Air base strike (#12) |
| 13 | Berlin | Merz speech (#13) |
| 19 | Gaza | Hamas security chief (#19) |
| 24 | Damazin | Sudan strikes (#24) |
| 25 | Pretoria | Ramaphosa (#25) |
| 28 | Enugu | Edochie dies (#28) |
| 35 | Canberra | Solomons pact (#35) |

Every pin's story is on the poster. Note: the Cairo fire (#23) has no
pin — Cairo and Gaza are ~200 km apart and their pins overlapped into
one blob at this scale, so the pin went to Enugu (#28) instead. The
Cairo story is still on the poster (grid #23) and in the numbers strip.

## "THE DAY IN UTC" — timeline strip (8 events, verified times only)

| UTC | Event |
|-----|-------|
| 00:18 | Shenzhou-24 launches from Jiuquan |
| 00:30 | Australia Oct CPI released, 4.9% |
| 03:07 | Cartagena hostages rescued |
| 03:56 | Shenzhou-24 docks with Tiangong |
| 14:00 | Chess Game 2 starts, Geneva |
| 15:08 | US Army detonates lead-azide stockpile, Iowa |
| 16:46 | IRGC LNG-carrier mine claim carried by Mehr |
| 21:00 | Wall Street closes, Dow +0.33% at 50,182.95 |

## "THE DAY IN NUMBERS" strip

−6.16% KOSPI (4,697.51) · $94.61 Brent crude +3.5% · 14 economies hit
by proposed US tariffs, China up to 20% · 31 killed in Cairo
ring-road tanker fire · 5 Russian warplanes Ukraine says it damaged
at Savasleyka · 3.8% US PCE inflation / 4.9% Australia CPI. Every
figure already appears on the poster or in this document.

## DATE CHECK — 13 entries

The box lists stories that were left out because their event was
**not** Wed 25 Nov 2026, with the correct date for each:

1. Sanofi buys Insmed $41bn — Tue 24 Nov
2. Russia claims 699 drones downed — Tue 24 Nov
3. Hormuz: IRGC claims 3 tankers hit mines under US escort — Tue 24 Nov (Wed's LNG-carrier + 2-tanker claims are separate, newer claims)
4. Shanghai Politburo purge — Tue 24 Nov
5. TAIEX +8.99% chip rally — Tue 24 Nov (Wed Taiex FELL ~4.9%)
6. CAS verdict restoring Senegal as AFCON champions — Tue 24 Nov (Morocco vowed to challenge it Wed 25 — the challenge is Wed, the verdict is Tue)
7. Gukesh–Sindarov Game 1 draw — Tue 24 Nov (Game 2 is Wed)
8. Vaibhav Sooryavanshi 204 off 53 balls, 28 sixes, India A beat UAE — Tue 24 Nov, Doha
9. Champions League Tue night (Real Madrid 5–1 PSV, Arsenal 1–1 Dortmund, Man City 2–2 Napoli, Galatasaray 1–0 Aston Villa) — Tue 24 Nov evening Europe
10. Huawei convicted 10 of 12 counts — Tue 24 Nov, Brooklyn jury
11. Shein agrees $100m FTC settlement — announced Tue 24 Nov
12. Houthi strike on Riyadh financial-district tower, 11 injured — Tue 24 Nov (Wed's Ras Tanura claim is separate)
13. Dow first close above 50,000 (50,018.70) — Tue 24 Nov (Wed close 50,182.95 is the Wed figure)

## Honesty notes and cautions applied

- **Hormuz is a daily-claims war.** Tuesday had a 3-tanker claim;
  Wednesday has a DIFFERENT 2-tanker + LNG-carrier claim. The poster
  says "IRGC CLAIMS" and dates it Wed 25 Nov, and never presents any
  Hormuz mine strike as verified fact. The hero badge is CLAIM and the
  source line reads "CLAIMS, NOT VERIFIED".
- **Egypt toll:** Reuters 31 is used, not AP's "at least 30".
- **Australia–Solomons money:** AFP's AU$740m only, not ~AU$980m.
- **Europe closes:** the final closes are used (Euro Stoxx 50
  5,894.46 −1.82%, DAX 24,702.13 −1.26%, FTSE 100 10,427 −0.38%);
  intraday reports differed.
- **Market figures are CLOSING figures** throughout (Wall Street,
  Europe, Asia).
- **Cartagena:** the siege began Tuesday; only the rescue is a
  Wednesday event, and the poster says so ("~30 taken Tue").
- **Savasleyka damage:** the "5 planes damaged" figure is a Ukrainian
  General Staff claim; the poster attributes it ("Ukraine hits…",
  badge OFFICIAL for the Ukrainian announcement, damage as their
  claim).
- **Ras Tanura:** the Houthi claim is a claim; the poster says
  "Houthis claim" and the 4 intercepted drones / smoke on imagery are
  reported as such.
- **Poster text trims:** a few poster lines shorten wording for fit
  ("Judge Cooper" for Judge Christopher Cooper; "above the Fed's 2%
  target"; the #29 Also-on line drops the Taiex figure, which is
  carried in full in this document). No figure was changed by trimming.

## What could not be verified

- **Hormuz (#2):** rests on the IRGC claim (via Reuters) and the Houthi
  claim alone. No tanker names, flags, owners, cargo or casualty
  figures were given for the mine claims; the claims are unconfirmed.
  Carried with a CLAIM badge and the caveat stated on the poster.
- **Ras Tanura (#2):** the refinery-attack claim is Houthi only; the
  interception of 4 drones and smoke on imagery are as reported.
- **Bolivia (#11), Ecuador (#10), Brazil (#9):** single-outlet (Rio
  Times) items, carried with REPORTED badges.
- **Senator defection (#40):** rests on a single summary (The Actual
  News); carried as REPORTED and placed last, as the weakest link.
- **Plane crash (#38):** single-outlet (AP) brief; carried as REPORTED.

## Build notes (how the poster was made)

`draw_poster.py` renders `entry.png` with Pillow + DejaVu
(DejaVuSerif-Bold for the masthead and headlines, DejaVuSans for body
text). Every scene is drawn fresh with simple shapes — bar and line
charts, a tanker and spiked mine, a rocket and station ring, a gavel,
a ballot box, a pumpjack, jets, a podium — no copied assets. Scenes
are painted onto a temporary canvas and pasted into their boxes, so no
scene can paint outside its own frame (an early version's Earth arc
spilled across two heroes; the paste-clip fixed it). Text is wrapped by
measurement, never by eye: grid-A details use a wrapper that keeps the
whole "· source" tag on one line, and the numbers strip, timeline and
Also-on lines were all measured to fit their columns before the final
render. The map is a simplified equirectangular world (rough continent
polygons) with pins at the stories' real coordinates; two pin
placements were changed after zoom checks — Cairo's pin overlapped
Gaza's, so the 12th pin went to Enugu (#28) instead, and the
Washington label was moved above its pin after Iowa's pin sat on it.
The edition timestamp in the masthead and footer is the render time
in UTC.

## Verification record

- SHA-256 of committed `entry.png`: `50902a2136d0ace37970ede7cf471b50b24f75f28726751ca579a17964c6c496`
- Size of committed `entry.png`: `254928` bytes (1024×1024 pixels)
- Two-run byte-compare (`MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py`
  and `/tmp/out2` from the entry dir, then compare): `PASS — both runs byte-identical (cmp clean), and both SHA-256s match the committed entry.png`

Checks run before submission:

1. Two independent runs of `main.py` produce byte-identical `entry.png`
   files, and the SHA-256 matches the committed `entry.png`.
2. `entry.png` is 1024×1024 pixels.
3. `entry.png` is under 1 MiB (< 1,048,576 bytes).
4. Distinct stories counted on the poster = 40; region tabs sum to 40.
5. Every figure on the poster matches a figure in this document; every
   story's event date is Wed 25 Nov 2026 under the event-date rule
   above (or labelled honestly as reported-Wed where it was an
   overnight event).
6. The poster was viewed at full size and in zoomed crops (heroes,
   grid A, grid B, map, DATE CHECK): all 40 numbers legible, no text
   overlaps, DATE CHECK legible, map pins correct, badges readable.

## Sources index (primary, in brief order)

USTR; Reuters; AP; Xinhua / CMSA; BEA; US Army; Bloomberg Law; Rio
Times; Ukrainian General Staff; Morningstar / Dow Jones; UEFA /
Flashscore; BBC; Al Jazeera; Rigzone / CNBC; Egypt Health Ministry;
Emergency Lawyers; Sowetan; OkayAfrica; KCNA; RevSportz; The Hindu;
ChessBase / FIDE; AFP; ABS; The Actual News.
