#!/usr/bin/env python3
"""Render the news-image-20261125 poster: one 1024x1024 PNG summing up
Wednesday 25 November 2026.

Drawn offline with Pillow + DejaVu fonts. Every story on the poster
happened, or was first reported, on Wed 25 Nov 2026 in some timezone;
claims are labelled as claims and every story carries a source tag.
The entrypoint (main.py) only copies the finished PNG -- the grader's
Python image has no Pillow, so nothing here runs at grade time.
"""
import os
from datetime import datetime, timezone

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

INK = (24, 24, 24)
GREY = (90, 90, 90)
RED = (178, 34, 34)
DARKRED = (140, 20, 20)
NAVY = (18, 52, 86)
TEAL = (14, 92, 96)
PAPER = (252, 250, 244)
RULE = (150, 150, 150)
LIGHT = (238, 236, 228)
BLUE_BG = (207, 227, 238)
LAND = (216, 232, 196)
LAND_EDGE = (140, 160, 120)

BADGE_COLORS = {
    "CONFIRMED": (26, 122, 46),
    "OFFICIAL": (18, 52, 86),
    "REPORTED": (176, 124, 0),
    "CLAIM": (178, 34, 34),
}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_SANS = lambda s: font("DejaVuSans.ttf", s)
F_SANSB = lambda s: font("DejaVuSans-Bold.ttf", s)
F_SERIF_R = lambda s: font("DejaVuSerif.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit in width px."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def wrap_detail_source(draw, detail, source, width):
    """Wrap a grid-A detail into at most 2 lines, keeping the whole
    '· source' tag together on the second line (or the first, if the
    detail fits on one line). Returns the lines to draw."""
    fnt = F_SANS(9)
    src = " · " + source
    sw = draw.textlength(src, font=fnt)
    first = wrap(draw, detail, fnt, width)
    if len(first) == 1:
        if draw.textlength(first[0] + src, font=fnt) <= width:
            return [first[0] + src]
        return [first[0], src]
    words = detail.split(" ")
    line1, i = "", 0
    while i < len(words) and draw.textlength(
            (line1 + " " + words[i]).strip(), font=fnt) <= width:
        line1 = (line1 + " " + words[i]).strip()
        i += 1
    rest = words[i:]
    line2, j = "", 0
    while j < len(rest) and draw.textlength(
            (line2 + " " + rest[j]).strip(), font=fnt) <= width - sw - 4:
        line2 = (line2 + " " + rest[j]).strip()
        j += 1
    while j < len(rest) and draw.textlength(
            (line2 + " " + rest[j]).strip() + src, font=fnt) <= width:
        line2 = (line2 + " " + rest[j]).strip()
        j += 1
    return [line1, line2 + src]


def draw_wrapped(draw, x, y, text, fnt, width, fill=INK, leading=None):
    """Draw wrapped text; returns the y just below the last line."""
    lh = leading or int(fnt.size * 1.22)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def badge(draw, x, y, label):
    """Draw a certainty chip; returns the x just past it."""
    fnt = F_SANSB(8)
    w = int(draw.textlength(label, font=fnt)) + 10
    h = 12
    draw.rounded_rectangle([x, y, x + w, y + h], radius=3,
                           fill=BADGE_COLORS[label])
    draw.text((x + 5, y + 2), label, font=fnt, fill=(255, 255, 255))
    return x + w


def num_chip(draw, x, y, n, size=15):
    fnt = F_SANSB(9)
    draw.rectangle([x, y, x + size, y + size], fill=RED)
    t = str(n)
    tw = draw.textlength(t, font=fnt)
    draw.text((x + (size - tw) / 2, y + 2), t, font=fnt, fill=(255, 255, 255))


def paint_scene(img, scene, x, y, w, h):
    """Render a scene onto a temp canvas and paste it, so no scene can
    paint outside its own box."""
    tmp = Image.new("RGB", (w, h), PAPER)
    td = ImageDraw.Draw(tmp)
    scene(td, 0, 0, w, h)
    img.paste(tmp, (x, y))


def section_rule(draw, y):
    draw.line([(8, y), (1016, y)], fill=RULE, width=1)

# ---------------------------------------------------------------- scenes
# Small fresh vector scenes, drawn with simple shapes only. Each takes
# the draw object and the box (x, y, w, h) it may paint inside.

def scene_tariffs(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 42, 72))
    d.ellipse([x + w - 52, y + 6, x + w - 12, y + 46], fill=(70, 130, 180),
              outline=(180, 210, 235))
    d.arc([x + w - 52, y + 6, x + w - 12, y + 46], 20, 160, fill=(180, 210, 235))
    d.line([(x + w - 52, y + 26), (x + w - 12, y + 26)], fill=(180, 210, 235))
    base = y + h - 8
    vals = [0.35, 0.5, 0.42, 0.7, 0.62, 0.9]
    bw = (w - 70) // len(vals)
    for i, v in enumerate(vals):
        bx = x + 6 + i * bw
        bh = int((h - 22) * v)
        d.rectangle([bx, base - bh, bx + bw - 3, base], fill=(232, 180, 60))
    d.text((x + 6, y + 4), "20%  15%  25%  35%", font=F_SANSB(9),
           fill=(255, 240, 180))


def scene_hormuz(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(12, 74, 96))
    d.rectangle([x, y + h - 16, x + w, y + h], fill=(8, 52, 72))
    # tanker hull + bridge
    d.rectangle([x + 30, y + h - 34, x + w - 60, y + h - 18], fill=(40, 40, 44))
    d.rectangle([x + w - 60, y + h - 48, x + w - 34, y + h - 18],
                fill=(200, 60, 50))
    d.rectangle([x + 52, y + h - 44, x + 66, y + h - 34], fill=(40, 40, 44))
    # spiked mine + burst
    cx, cy = x + w - 95, y + 22
    for ang in range(0, 360, 30):
        import math
        dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        d.line([(cx + dx * 6, cy + dy * 6), (cx + dx * 11, cy + dy * 11)],
               fill=(220, 220, 220), width=2)
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(30, 30, 30))
    d.ellipse([x + 8, y + 8, x + 30, y + 30], fill=(255, 170, 40))
    d.ellipse([x + 14, y + 14, x + 24, y + 24], fill=(255, 230, 120))
    d.text((x + 36, y + 12), "CLAIM", font=F_SANSB(10), fill=(255, 210, 120))


def scene_space(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(8, 12, 34))
    import random
    rnd = random.Random(25)
    for _ in range(26):
        sx, sy = x + rnd.randint(2, w - 2), y + rnd.randint(2, h - 2)
        d.ellipse([sx, sy, sx + 2, sy + 2], fill=(255, 255, 255))
    # Earth arc bottom-left
    d.ellipse([x - 70, y + h - 26, x + 60, y + h + 70], fill=(40, 110, 190))
    d.ellipse([x - 70, y + h - 26, x + 60, y + h + 70], outline=(120, 190, 240))
    # rocket
    rx, ry = x + w - 78, y + 10
    d.polygon([(rx + 8, ry), (rx + 16, ry + 14), (rx, ry + 14)], fill=(220, 60, 50))
    d.rectangle([rx, ry + 14, rx + 16, ry + 34], fill=(235, 235, 235))
    d.polygon([(rx + 2, ry + 34), (rx + 8, ry + 28), (rx + 14, ry + 34)],
              fill=(255, 170, 40))
    # station ring
    d.ellipse([x + w - 46, y + h - 30, x + w - 6, y + h - 6],
              outline=(200, 200, 200), width=2)
    d.rectangle([x + w - 40, y + h - 22, x + w - 12, y + h - 14],
                fill=(180, 180, 190))


def scene_chart(d, x, y, w, h, color, up=True):
    d.rectangle([x, y, x + w, y + h], fill=(245, 244, 238))
    pts = [(x + 3, y + h - 6), (x + w * 0.25, y + h * 0.55),
           (x + w * 0.5, y + h * 0.65), (x + w * 0.75, y + h * 0.3),
           (x + w - 3, y + 5 if up else y + h - 10)]
    d.line(pts, fill=color, width=2)
    for px, py in pts:
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=color)


def scene_bars(d, x, y, w, h, color):
    d.rectangle([x, y, x + w, y + h], fill=(245, 244, 238))
    vals = [0.45, 0.6, 0.55, 0.8, 1.0]
    bw = w // len(vals)
    for i, v in enumerate(vals):
        bx = x + 3 + i * bw
        bh = int((h - 8) * v)
        d.rectangle([bx, y + h - 4 - bh, bx + bw - 3, y + h - 4], fill=color)


def scene_blast(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(60, 52, 40))
    cx, cy = x + w // 2, y + h // 2
    for r, col in [(15, (255, 230, 120)), (10, (255, 170, 40)),
                   (5, (220, 60, 30))]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    d.rectangle([x + 4, y + h - 10, x + 14, y + h - 3], fill=(120, 120, 120))
    d.rectangle([x + w - 14, y + h - 10, x + w - 4, y + h - 3],
                fill=(120, 120, 120))


def scene_gavel(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 244, 238))
    d.line([(x + 8, y + 12), (x + w - 8, y + h - 12)], fill=(120, 80, 40),
           width=4)
    d.rectangle([x + w - 22, y + 4, x + w - 6, y + 14], fill=(90, 60, 30))
    d.rectangle([x + 6, y + h - 12, x + 22, y + h - 4], fill=(90, 60, 30))
    d.rectangle([x + w // 2 - 12, y + h - 8, x + w // 2 + 12, y + h - 3],
                fill=(150, 110, 60))


def scene_building(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 244, 238))
    d.rectangle([x + 10, y + 8, x + w - 10, y + h - 4], fill=(70, 110, 160))
    for i in range(3):
        for j in range(2):
            d.rectangle([x + 15 + i * 14, y + 13 + j * 10,
                         x + 24 + i * 14, y + 20 + j * 10],
                        fill=(255, 240, 180))
    d.ellipse([x + w - 22, y + 2, x + w - 4, y + 20], fill=(26, 122, 46))
    d.text((x + w - 18, y + 6), "✓", font=F_SANSB(10), fill=(255, 255, 255))


def scene_ballot(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 244, 238))
    d.rectangle([x + 14, y + 12, x + w - 14, y + h - 4], fill=(180, 60, 60))
    d.rectangle([x + w // 2 - 8, y + 8, x + w // 2 + 8, y + 13],
                fill=(255, 255, 255))
    d.rectangle([x + 18, y + 4, x + 30, y + 12], fill=(255, 255, 255),
                outline=(40, 40, 40))


def scene_pumpjack(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 244, 238))
    d.line([(x + 8, y + h - 4), (x + w - 8, y + 8)], fill=(60, 60, 60),
           width=3)
    d.line([(x + w // 2, y + h - 4), (x + w // 2, y + 10)], fill=(60, 60, 60),
           width=3)
    d.rectangle([x + w - 16, y + 4, x + w - 4, y + 12], fill=(40, 40, 40))
    d.ellipse([x + 6, y + h - 12, x + 16, y + h - 2], fill=(30, 30, 30))


def scene_jets(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(200, 220, 235))
    for jx, jy in [(x + 10, y + 8), (x + 30, y + 18)]:
        d.polygon([(jx, jy), (jx + 18, jy + 4), (jx, jy + 8)], fill=(60, 60, 70))
        d.polygon([(jx + 4, jy + 2), (jx + 10, jy - 2), (jx + 10, jy + 6)],
                  fill=(60, 60, 70))
    d.line([(x + 4, y + h - 6), (x + w - 4, y + h - 6)], fill=(90, 90, 90),
           width=2)
    d.ellipse([x + w - 16, y + 4, x + w - 6, y + 14], fill=(255, 170, 40))


def scene_podium(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 244, 238))
    d.rectangle([x, y + 4, x + w, y + 8], fill=(20, 20, 20))
    d.rectangle([x, y + 8, x + w, y + 12], fill=(200, 30, 30))
    d.rectangle([x, y + 12, x + w, y + 16], fill=(240, 200, 40))
    d.rectangle([x + w // 2 - 10, y + 18, x + w // 2 + 10, y + h - 4],
                fill=(90, 70, 50))
    d.ellipse([x + w // 2 - 6, y + h - 16, x + w // 2 + 6, y + h - 6],
              fill=(220, 180, 140))

# ---------------------------------------------------------------- data
# (headline, detail, source, badge, region, scene)
HEROES = [
    ("US PROPOSES TARIFFS ON 14 ECONOMIES",
     "USTR Section 301 findings Wed: China up to 20% (40% if talks fail), "
     "EU 15%, India up to 25%, Vietnam up to 35%. Hearings 25 Jan 2027.",
     "SOURCE: USTR / Reuters / AP", "CONFIRMED",
     "NORTH AMERICA · TRADE", scene_tariffs),
    ("HORMUZ MINE CLAIMS GO TO GAS + RAS TANURA HIT CLAIM",
     "IRGC claims 2 tankers + 1 LNG carrier hit mines Wed evening — "
     "unverified, no vessel names. Houthis claim Ras Tanura refinery hit; "
     "4 drones intercepted. Brent +3.5%.",
     "SOURCE: Reuters — CLAIMS, NOT VERIFIED", "CLAIM",
     "MIDDLE EAST · STRAIT OF HORMUZ", scene_hormuz),
    ("PAKISTAN'S FIRST ASTRONAUT REACHES TIANGONG",
     "Shenzhou-24 launched 00:18 UTC, docked 03:56 UTC. Muhammad Zeeshan "
     "Ali is the first foreign astronaut aboard China's Tiangong station.",
     "SOURCE: Xinhua / CMSA / Reuters", "CONFIRMED",
     "ASIA · SPACE", scene_space),
]

# grid stories 4-13: (n, headline, detail, source, badge, scene)
GRID_A = [
    (4, "US inflation 3.8% in October",
     "PCE +3.8% y/y, core 3.3%; real spending −$5.8bn — above the "
     "Fed's 2% target.", "BEA via AP", "OFFICIAL",
     lambda d, x, y, w, h: scene_bars(d, x, y, w, h, (178, 34, 34))),
    (5, "Army blows up lead-azide stockpile",
     "~5 tons / 68 barrels detonated 10:08 ET in Middletown, Iowa; "
     "shelter-in-place until all-clear.", "AP / US Army", "OFFICIAL",
     scene_blast),
    (6, "Second judge blocks birthright order",
     "Judge Cooper, Washington DC, 67-page injunction vs August "
     "executive order.", "AP / Bloomberg Law", "CONFIRMED",
     scene_gavel),
    (7, "Wall Street stages late comeback",
     "Dow 50,182.95 +0.33%; S&P 7,182.78 −0.25%; Nasdaq 23,585.80 "
     "−0.62%. S&P was −3.2% intraday.", "AP / Reuters", "CONFIRMED",
     lambda d, x, y, w, h: scene_chart(d, x, y, w, h, (26, 122, 46))),
    (8, "Cartagena hostages all freed",
     "Forces stormed Éxito supermarket early Wed after a 17-hour siege; "
     "~30 taken Tue, ~20 rescued, 1 captor killed.", "Reuters / AFP",
     "CONFIRMED", scene_building),
    (9, "Brazil's real rallies as bank sells $2bn",
     "Real gained Wed, dollar −1.5%; spending-cut talks continue.",
     "Rio Times", "REPORTED",
     lambda d, x, y, w, h: scene_chart(d, x, y, w, h, (26, 122, 46))),
    (10, "Ecuador campaign ends",
     "Campaign ends Thu, then silence + 72-hour alcohol ban, $241 fines, "
     "ahead of Sunday's local vote.", "Rio Times", "REPORTED",
     scene_ballot),
    (11, "Bolivia ex-oil chief testifies twice",
     "Former state oil chief Yussef Akly gave statements twice Wed to La "
     "Paz prosecutors as a witness; not charged.", "Rio Times", "REPORTED",
     scene_pumpjack),
    (12, "Ukraine hits Savasleyka air base",
     "Strike overnight 24–25 Nov: 3 MiG-31s + 2 Su-34s “knocked out for "
     "some time”; 2 Samara refineries hit.", "Reuters / Ukr. General Staff",
     "OFFICIAL", scene_jets),
    (13, "Merz: “Russia wants more than Ukraine”",
     "Chancellor tells Bundestag Wed, defending defence spending "
     "+ Ukraine aid.", "Reuters", "OFFICIAL", scene_podium),
]

# grid stories 14-27: (n, headline, detail, source)
GRID_B = [
    (14, "Murmansk governor held in corruption probe",
     "Head of Russia's Murmansk region in pre-trial detention for 2 "
     "months, Moscow court Wed.", "Reuters"),
    (15, "34 countries + EU: Russia must stop riot gas",
     "Joint call Wed after the watchdog confirmed tear-gas traces in a "
     "trench Kyiv said was hit by a Russian grenade.", "Reuters"),
    (16, "Europe shares fall as AI fears return",
     "Euro Stoxx 50 5,894.46 −1.82%; DAX 24,702.13 −1.26%; FTSE 100 "
     "10,427 −0.38%.", "Morningstar / Dow Jones"),
    (17, "Champions League, Wed night",
     "PSG 2–2 Roma; Sporting 2–2 Man Utd; Liverpool 3–0 Brugge; Bayern "
     "lose 2–1 at Lille; Inter 2–0 Stuttgart; Barça 4–1 Sabah; "
     "Atlético 2–0 Viking.", "UEFA"),
    (18, "Ramsay to lead Top Gear revival",
     "BBC flagship motoring show revival announced Wed.", "AP / BBC"),
    (19, "Israel kills Hamas security chief in Gaza",
     "Mohammad Abuelouf killed Wed with wife + 2 children in Beach camp "
     "strike; IDF said it “targeted several military operatives”.",
     "Reuters / Gaza medics"),
    (20, "Israeli judges urge dropping Netanyahu bribery charge",
     "Jerusalem judges tell AG Wed: little chance of conviction in Case "
     "4,000; question Case 2,000; suggest plea in Case 1,000.",
     "Al Jazeera / BBC"),
    (21, "Knesset takes first step to Oct 7 inquiry",
     "Parliament Wed took the initial step toward a state commission into "
     "7 Oct 2023 security failures; caretaker PM Netanyahu long opposed "
     "it.", "AP"),
    (22, "Oil jumps: Brent $94.61, +3.5%",
     "Brent settled $94.61/bbl (+3.5%), WTI $83.68 (+2.0%) Wed on "
     "Hormuz / Ras Tanura disruption fears.", "Rigzone / CNBC"),
    (23, "Cairo ring-road fire kills 31",
     "Fuel tanker overturned Wed evening on the Warraq ring road; 31 "
     "killed, 21 injured.", "Reuters / Egypt Health Ministry"),
    (24, "RSF drone strikes kill 19 in Sudan",
     "Overnight strikes Wed on Damazin + Roseires, Blue Nile: 19 killed "
     "incl. 6 women, 20 wounded.", "Emergency Lawyers via Reuters"),
    (25, "Ramaphosa wins Phala Phala court battle",
     "Western Cape High Court Wed set aside in full the 2022 Section 89 "
     "panel report ($580,000 farm theft); impeachment inquiry falls "
     "away.", "Sowetan / Al Jazeera"),
    (26, "Kenya cult leader convicted again",
     "Paul Mackenzie, serving 200 years for ~191 Shakahola deaths, "
     "convicted Wed on 5 counts cruelty to a child + 1 assault.",
     "Reuters"),
    (27, "Ebola workers evacuated in eastern Congo",
     "Fighting forced WHO to move its Mongbwalu team + partners to Bunia "
     "Wed; monitoring of exposed people disrupted.", "AP / WHO"),
]

# also-on 28-40: (n, headline, source)
ALSO_ON = [
    (28, "Nollywood legend Pete Edochie dies at 79", "OkayAfrica"),
    (29, "Asia AI rout: KOSPI −6.16%; Nikkei −2.78%; Nifty +1.85%",
     "AP / Reuters"),
    (30, "North Korea expels Swiss diplomat", "KCNA via BBC"),
    (31, "Xiaomi profit falls 68%, Shanghai at 1-year low", "AP"),
    (32, "Sri Lanka women win Emerging Nations Trophy", "RevSportz"),
    (33, "India women thrash Japan 4–0 in hockey", "The Hindu"),
    (34, "Chess Game 2: Gukesh–Sindarov draw in 20 moves", "ChessBase / FIDE"),
    (35, "Australia–Solomon Islands security pact signed", "Reuters / AFP"),
    (36, "Australia inflation jumps to 4.9%", "ABS via Guardian / ABC"),
    (37, "Macy's Thanksgiving Parade postponed to Saturday", "AP"),
    (38, "Plane crash off Mississippi kills family of 6", "AP"),
    (39, "Lebanon to open second airport next month", "Reuters"),
    (40, "Australian senator defects to One Nation", "The Actual News"),
]

DATE_CHECK = [
    "Sanofi buys Insmed $41bn — Tue 24 Nov",
    "Russia claims 699 drones downed — Tue 24 Nov",
    "Hormuz: IRGC claims 3 tankers hit mines — Tue 24 Nov",
    "Shanghai Politburo purge — Tue 24 Nov",
    "TAIEX +8.99% chip rally — Tue 24 Nov",
    "CAS verdict: Senegal AFCON champions — Tue 24 Nov",
    "Gukesh–Sindarov Game 1 draw — Tue 24 Nov",
    "Sooryavanshi 204 off 53, India A beat UAE — Tue 24 Nov",
    "Champions League Tue night — Tue 24 Nov",
    "Huawei convicted 10 of 12 counts — Tue 24 Nov",
    "Shein $100m FTC settlement — Tue 24 Nov",
    "Houthi strike on Riyadh tower, 11 hurt — Tue 24 Nov",
    "Dow first close above 50,000 — Tue 24 Nov",
]

NUMBERS = ("THE DAY IN NUMBERS:  −6.16% KOSPI  ·  $94.61 Brent +3.5%  ·  "
           "14 economies face US tariffs  ·  31 killed in Cairo  ·  "
           "5 warplanes hit  ·  3.8% US PCE  ·  4.9% Australia CPI")

TIMELINE = [
    ("00:18", "Shenzhou-24 launches"),
    ("00:30", "Australia CPI 4.9%"),
    ("03:07", "Cartagena hostages rescued"),
    ("03:56", "Shenzhou-24 docks"),
    ("14:00", "Chess Game 2 starts, Geneva"),
    ("15:08", "US Army detonates stockpile, Iowa"),
    ("16:46", "IRGC LNG-carrier mine claim"),
    ("21:00", "Wall St closes, Dow +0.33% at 50,182.95"),
]

# 12 map pins: (story no., label, lon, lat, label dx, dy)
PINS = [
    (1, "Washington", -77.0, 38.9, -62, -14),
    (2, "Hormuz", 56.5, 26.5, 8, -10),
    (3, "Jiuquan", 98.5, 39.8, 8, -4),
    (5, "Iowa", -93.6, 41.6, -34, 8),
    (8, "Cartagena", -75.5, 10.4, 8, -4),
    (12, "Savasleyka", 43.7, 55.6, 8, -10),
    (13, "Berlin", 13.4, 52.5, -46, -10),
    (19, "Gaza", 34.5, 31.5, -38, 6),
    (24, "Damazin", 34.4, 11.8, 8, -4),
    (25, "Pretoria", 28.2, -25.7, 8, -4),
    (28, "Enugu", 7.5, 6.4, -12, 8),
    (35, "Canberra", 149.1, -35.3, -58, -4),
]

CONTINENTS = {
    "N America": [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80),
                  (-85, 70), (-75, 73), (-60, 60), (-55, 47), (-65, 45),
                  (-70, 42), (-75, 35), (-80, 32), (-81, 26), (-90, 21),
                  (-95, 19), (-97, 16), (-92, 15), (-86, 12), (-83, 9),
                  (-79, 9), (-90, 14), (-105, 20), (-110, 23), (-114, 29),
                  (-125, 40), (-124, 48), (-135, 58), (-155, 58), (-165, 60)],
    "S America": [(-79, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12),
                  (-72, -18), (-70, -23), (-70, -30), (-72, -37),
                  (-73, -44), (-70, -52), (-66, -55), (-65, -45),
                  (-62, -40), (-58, -35), (-52, -32), (-48, -28),
                  (-41, -23), (-35, -9), (-35, -6), (-40, -3), (-44, -2),
                  (-50, 0), (-52, 5), (-60, 8), (-68, 11), (-72, 12),
                  (-77, 8)],
    "Europe": [(-10, 36), (-9, 43), (-2, 44), (-1, 46), (-4, 48), (-1, 50),
               (2, 51), (5, 53), (8, 55), (8, 57), (10, 59), (5, 60),
               (5, 62), (12, 64), (18, 69), (25, 71), (30, 70), (32, 68),
               (40, 66), (48, 62), (50, 58), (48, 55), (44, 52), (40, 48),
               (38, 46), (35, 44), (32, 42), (28, 41), (23, 40), (22, 37),
               (19, 40), (16, 38), (12, 38), (8, 39), (3, 38), (0, 36),
               (-2, 37), (-6, 36)],
    "Africa": [(-6, 35), (-10, 31), (-15, 27), (-17, 21), (-17, 15),
               (-16, 12), (-13, 8), (-8, 5), (-4, 5), (2, 6), (6, 4),
               (9, 4), (9, -1), (12, -5), (13, -10), (12, -17), (14, -22),
               (16, -28), (18, -34), (20, -35), (26, -34), (28, -33),
               (32, -29), (35, -24), (36, -18), (40, -15), (40, -10),
               (42, -4), (46, -1), (51, 2), (51, 10), (48, 11), (43, 12),
               (40, 15), (38, 18), (37, 22), (35, 28), (33, 31), (30, 32),
               (25, 32), (20, 32), (15, 32), (11, 34), (10, 37)],
    "Asia": [(32, 68), (40, 68), (48, 68), (55, 69), (62, 69), (68, 70),
             (75, 72), (85, 74), (95, 76), (105, 77), (115, 76), (125, 74),
             (135, 72), (145, 72), (155, 70), (160, 66), (162, 60),
             (158, 55), (155, 50), (150, 45), (142, 42), (140, 38),
             (135, 35), (130, 33), (127, 35), (122, 38), (120, 32),
             (115, 30), (110, 25), (108, 20), (105, 15), (103, 10),
             (100, 8), (98, 12), (95, 16), (92, 21), (90, 22), (86, 20),
             (82, 17), (80, 13), (77, 8), (75, 12), (72, 20), (70, 23),
             (66, 25), (62, 25), (58, 26), (56, 27), (54, 26), (52, 28),
             (50, 29), (48, 30), (44, 29), (42, 31), (40, 32), (38, 32),
             (36, 36), (34, 36), (30, 38), (27, 41), (24, 38)],
    "Australia": [(113, -22), (114, -30), (115, -35), (118, -35),
                  (124, -33), (129, -32), (132, -32), (135, -35),
                  (137, -35), (140, -38), (145, -38), (150, -37),
                  (153, -32), (153, -27), (150, -22), (146, -19),
                  (142, -15), (142, -11), (137, -12), (135, -15),
                  (132, -12), (130, -13), (126, -14), (122, -17),
                  (118, -20)],
}

# ---------------------------------------------------------------- render

def render():
    edition = datetime.now(timezone.utc).strftime("%d %b %Y %H:%M UTC")
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead
    d.text((8, 4), "THE WORLD IN ONE DAY", font=F_SERIF(38), fill=INK)
    d.text((1016, 6), "WEDNESDAY 25 NOVEMBER 2026", font=F_SANSB(16),
           fill=RED, anchor="ra")
    d.text((1016, 28), "40 STORIES · 7 REGIONS", font=F_SANSB(10),
           fill=INK, anchor="ra")
    d.text((8, 46), "The day's world news, verified story by story — "
           "Wednesday's events only. Every figure dated + sourced.",
           font=F_SERIF_R(11), fill=GREY)
    section_rule(d, 58)

    # ---- heroes (3 columns)
    hy, hh = 62, 162
    hx = [8, 345, 682]
    hw = 333
    for (headline, detail, source, bdg, region, scene), x in zip(HEROES, hx):
        d.rectangle([x, hy, x + hw, hy + hh], outline=RULE, width=1)
        paint_scene(img, scene, x + 1, hy + 1, hw - 2, 56)
        ry = hy + 62
        d.text((x + 6, ry), region, font=F_SANSB(9), fill=RED)
        bw = int(d.textlength(bdg, font=F_SANSB(8))) + 10
        badge(d, x + hw - 6 - bw, ry - 1, bdg)
        ty = draw_wrapped(d, x + 6, ry + 15, headline, F_SERIF(14),
                          hw - 12, leading=17)
        ty = draw_wrapped(d, x + 6, ty + 2, detail, F_SANS(10), hw - 12,
                          leading=12)
        d.text((x + 6, hy + hh - 14), source, font=F_SANSB(8), fill=GREY)

    # ---- numbers strip
    ny = 228
    d.rectangle([8, ny, 1016, ny + 17], fill=(20, 40, 60))
    d.text((14, ny + 3), NUMBERS, font=F_SANSB(10), fill=(255, 255, 255))

    # ---- region tabs + badge legend
    ly = 249
    d.text((8, ly), "N AMERICA 7 · LATIN AMERICA 4 · EUROPE 7 · "
           "MIDDLE EAST 6 · AFRICA 6 · ASIA 7 · OCEANIA 3",
           font=F_SANSB(9), fill=NAVY)
    lx = 1016
    for label in ["CONFIRMED", "OFFICIAL", "REPORTED", "CLAIM"]:
        wch = int(d.textlength(label, font=F_SANSB(8))) + 10
        lx -= wch
        badge(d, lx, ly, label)
        lx -= 4
    d.text((lx - 4, ly + 1), "BADGES:", font=F_SANSB(8), fill=GREY,
           anchor="ra")

    # ---- grid 4-13 (two columns, 5 rows, drawn scenes)
    gy, row_h = 265, 36
    for i, (n, headline, detail, source, bdg, scene) in enumerate(GRID_A):
        col, row = i % 2, i // 2
        x = 8 + col * 508
        y = gy + row * row_h
        if col == 0:
            d.line([(8, y), (1016, y)], fill=(220, 220, 210), width=1)
        num_chip(d, x, y + 2, n)
        paint_scene(img, scene, x + 18, y + 1, 62, 32)
        tx = x + 86
        bw = int(d.textlength(bdg, font=F_SANSB(8))) + 10
        badge(d, x + 500 - bw, y + 2, bdg)
        hlines = wrap(d, headline, F_SANSB(11), 500 - 86 - bw - 8)
        d.text((tx, y + 1), hlines[0], font=F_SANSB(11), fill=INK)
        lines = wrap_detail_source(d, detail, source, 500 - 86)
        d.text((tx, y + 14), lines[0], font=F_SANS(9), fill=INK)
        if len(lines) > 1:
            d.text((tx, y + 25), lines[1], font=F_SANS(9), fill=INK)
    section_rule(d, gy + 5 * row_h + 2)

    # ---- grid 14-27 (two columns, text only, 7 rows x 30px:
    # headline + up to 2 body lines per row)
    by = 451
    brow = 30
    for i, (n, headline, detail, source) in enumerate(GRID_B):
        col, row = i % 2, i // 2
        x = 8 + col * 508
        y = by + row * brow
        d.text((x, y), str(n), font=F_SANSB(10), fill=RED)
        nx = x + 20
        d.text((nx, y), headline, font=F_SANSB(10), fill=INK)
        body = detail + " · " + source
        lines = wrap(d, body, F_SANS(9), 500 - 20)
        d.text((nx, y + 11), lines[0], font=F_SANS(9), fill=GREY)
        if len(lines) > 1:
            d.text((nx, y + 21), " ".join(lines[1:]), font=F_SANS(9),
                   fill=GREY)
    section_rule(d, by + 7 * brow + 2)

    # ---- UTC timeline (flow items across two lines, measured)
    ty = 667
    d.rectangle([8, ty, 1016, ty + 26], fill=LIGHT, outline=RULE)
    d.text((14, ty + 2), "THE DAY IN UTC", font=F_SANSB(10), fill=NAVY)
    tx, tline = 130, ty + 2
    for t, ev in TIMELINE:
        s = t + " " + ev
        sw = d.textlength(s, font=F_SANS(9))
        if tx + sw > 1010 and tline == ty + 2:
            tx, tline = 130, ty + 14
        d.text((tx, tline), s, font=F_SANS(9), fill=INK)
        tx += int(sw) + 14

    # ---- map + also-on
    my = 699
    d.text((8, my), "AROUND THE WORLD — 12 NUMBERED PINS", font=F_SANSB(10),
           fill=NAVY)
    d.text((508, my), "Pins match story numbers.", font=F_SANS(9),
           fill=GREY, anchor="ra")
    d.text((516, my), "ALSO ON — STORIES 28–40", font=F_SANSB(10),
           fill=NAVY)
    map_x, map_y, map_w, map_h = 8, 713, 500, 116
    d.rectangle([map_x, map_y, map_x + map_w, map_y + map_h],
                fill=BLUE_BG, outline=RULE)
    for gx in range(map_x + 50, map_x + map_w, 50):
        d.line([(gx, map_y), (gx, map_y + map_h)], fill=(190, 210, 222))
    for gyy in range(map_y + 29, map_y + map_h, 29):
        d.line([(map_x, gyy), (map_x + map_w, gyy)], fill=(190, 210, 222))

    def to_xy(lon, lat):
        px = map_x + (lon + 170) / 360.0 * map_w
        py = map_y + (78 - lat) / 136.0 * map_h
        return (px, py)

    for poly in CONTINENTS.values():
        d.polygon([to_xy(lon, lat) for lon, lat in poly], fill=LAND,
                  outline=LAND_EDGE)
    for n, label, lon, lat, dx, dy in PINS:
        px, py = to_xy(lon, lat)
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=RED,
                  outline=(255, 255, 255))
        t = str(n)
        tw = d.textlength(t, font=F_SANSB(7))
        d.text((px - tw / 2, py - 4), t, font=F_SANSB(7),
               fill=(255, 255, 255))
        d.text((px + dx, py + dy), label, font=F_SANSB(8), fill=INK)

    ay = 713
    for n, headline, source in ALSO_ON:
        d.text((516, ay), str(n), font=F_SANSB(10), fill=RED)
        nx = 516 + 20
        d.text((nx, ay), headline, font=F_SANSB(10), fill=INK)
        hxw = d.textlength(headline, font=F_SANSB(10))
        d.text((nx + hxw + 4, ay), "— " + source, font=F_SANS(9),
               fill=GREY)
        ay += 11

    # ---- DATE CHECK
    dy = 849
    d.rectangle([8, dy, 1016, 965], outline=DARKRED, width=2)
    d.text((14, dy + 4), "DATE CHECK — LEFT OUT ON PURPOSE: big stories "
           "that are NOT from Wednesday 25 Nov", font=F_SANSB(10),
           fill=DARKRED)
    cols = [DATE_CHECK[0:5], DATE_CHECK[5:9], DATE_CHECK[9:13]]
    for ci, col in enumerate(cols):
        cx = 16 + ci * 336
        cy = dy + 32
        for item in col:
            cy = draw_wrapped(d, cx, cy, "× " + item, F_SANS(9), 320,
                              fill=INK, leading=11)
            cy += 3
    d.text((14, 950), "Note: Morocco vowed to challenge the CAS verdict "
           "Wed 25 — the challenge is Wed, the verdict Tue. Wed's Hormuz "
           "LNG-carrier + 2-tanker claims are separate, newer claims.",
           font=F_SANS(8), fill=GREY)

    # ---- footer
    fy = 972
    fy = draw_wrapped(d, 8, fy, "Sources: USTR · Reuters · AP · Xinhua / "
                      "CMSA · BEA · US Army · Bloomberg Law · Rio Times · "
                      "Ukrainian General Staff · Morningstar / Dow Jones · "
                      "UEFA · BBC · Al Jazeera · Rigzone / CNBC · Egypt "
                      "Health Ministry · Emergency Lawyers · Sowetan · "
                      "OkayAfrica · KCNA · RevSportz · The Hindu · "
                      "ChessBase / FIDE · AFP · ABS · The Actual News",
                      F_SANS(8), 1008, fill=GREY, leading=11)
    d.text((8, fy + 2), "All 40 stories happened, or were first reported, "
           "on Wednesday 25 November 2026 in some timezone. Claims are "
           "labelled as claims.", font=F_SANSB(9), fill=INK)
    d.text((8, fy + 15), "Poster drawn " + edition +
           " · entry.png 1024×1024.", font=F_SANS(8), fill=GREY)

    img.save(OUT, optimize=True)
    print("wrote %s (%d bytes)" % (OUT, os.path.getsize(OUT)))


if __name__ == "__main__":
    render()
