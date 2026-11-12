"""Bouwt de pagina's van regelrapport.nl: `python3 bouw.py`.

De tekst van elke pagina staat hieronder; kop, menu en voet staan één keer in `pagina()`. De html-bestanden die
eruit komen staan in git (de site is statisch, de host bouwt niets). Pas tekst dus hier aan, niet in de html.
De animatie in schema/index.html is met de hand gemaakt en valt hierbuiten.
"""
from pathlib import Path

HIER = Path(__file__).parent
SITE = "https://regelrapport.nl"
NAAM = "Regelrapport"
EMAIL = "info@morphy.world"
VOORZET = "/voorzet/"

MENU = [
    ("/hoe-het-werkt/", "Hoe het werkt"),
    ("/herkomst-en-controle/", "Herkomst en controle"),
    ("/voor-wie/", "Voor wie"),
]

ICOON = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="6" y="3" width="20" height="26" rx="3" fill="#fff" '
         'stroke="#1f2b4f" stroke-width="2.5"/><path d="M11 10h10M11 15h10M11 20h6" stroke="#1f2b4f" '
         'stroke-width="2.5" stroke-linecap="round"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect x='6' y='3' "
           "width='20' height='26' rx='3' fill='%23fff' stroke='%231f2b4f' stroke-width='2.5'/%3E%3Cpath d='M11 10h10"
           "M11 15h10M11 20h6' stroke='%231f2b4f' stroke-width='2.5' stroke-linecap='round'/%3E%3C/svg%3E")


def pagina(pad, titel, omschrijving, inhoud):
    menu = "".join(
        f'<li><a href="{h}"{" aria-current=page" if h == pad else ""}>{t}</a></li>' for h, t in MENU)
    kop = titel if pad == "/" else f"{titel} · {NAAM}"
    html = f"""<!doctype html>
<!-- Gemaakt door bouw.py. Pas de tekst daar aan en draai `python3 bouw.py`. -->
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{kop}</title>
<meta name="description" content="{omschrijving}">
<link rel="canonical" href="{SITE}{pad}">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="/fonts/kalam-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/stijl.css">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{pad}">
<meta property="og:title" content="{kop}">
<meta property="og:description" content="{omschrijving}">
<meta property="og:locale" content="nl_NL">
<meta property="og:image" content="{SITE}/preview.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
</head>
<body>
<header class="kopbalk"><div class="breed">
  <a class="naam" href="/">{ICOON}{NAAM}</a>
  <nav aria-label="Hoofdmenu"><ul class="menu">{menu}
    <li><a class="knop klein" href="{VOORZET}">Kosteloze voorzet</a></li></ul></nav>
</div></header>
<main class="breed">
{inhoud.strip()}
</main>
<footer class="voet"><div class="breed">
  <p>{NAAM} is van Morphy B.V. · KVK 95783652</p>
  <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p><a href="/schema/">Het schema</a></p>
  <p><a href="https://www.morphy.world">www.morphy.world</a></p>
</div></footer>
</body>
</html>
"""
    doel = HIER / pad.strip("/") / "index.html"
    doel.parent.mkdir(parents=True, exist_ok=True)
    doel.write_text(html, encoding="utf-8")
    print("geschreven:", doel.relative_to(HIER))


OPROEP = f"""
<section class="oproep" aria-labelledby="voorzet">
  <h2 id="voorzet">Zien hoe dit er bij jullie uitziet?</h2>
  <p class="smal">We maken kosteloos een voorzet voor jullie omgeving, op basis van een paar van jullie eigen rapporten.
  Daarna komen we hem graag laten zien.</p>
  <div class="acties"><a class="knop" href="{VOORZET}">Vraag een kosteloze voorzet aan</a></div>
</section>
"""

# ---------------------------------------------------------------- home
pagina("/", "Regelrapport: van onderzoeken naar rapport",
       "Regelrapport zet uit jullie onderzoeken en documenten een rapport op, in jullie eigen sjabloon. "
       "Bij elke regel zie je uit welke bron hij komt.",
       f"""
<section>
  <p class="boven">Voor bureaus die rapporten schrijven</p>
  <h1 style="max-width:24ch">Van losse onderzoeken naar een rapport dat je regel voor regel kunt volgen.</h1>
  <p class="intro smal">Je verzamelt onderzoeken, berekeningen en documenten en schrijft daar een rapport van.
  {NAAM} zet dat rapport voor je op: in jullie eigen sjabloon, met bij elke regel de bron. Jij beoordeelt en beslist.</p>
  <div class="acties">
    <a class="knop" href="{VOORZET}">Vraag een kosteloze voorzet aan</a>
    <a class="link" href="/hoe-het-werkt/">Bekijk hoe het werkt</a>
  </div>
</section>

<section aria-labelledby="kort">
  <h2 id="kort">Wat het is, in vijf punten</h2>
  <ul class="rooster">
    <li class="kaart geel"><h3>Jullie eigen sjabloon</h3>
      <p>Het sjabloon maken we samen met jullie, uit jullie eigen rapporten: jullie opbouw, jullie formuleringen,
      jullie vakkennis.</p></li>
    <li class="kaart"><h3>Elke regel heeft een bron</h3>
      <p>Van elke regel in het rapport zie je waar hij vandaan komt: uit welk onderzoek, welk document of welk
      wetsartikel.</p></li>
    <li class="kaart blauw"><h3>Eerdere rapporten als voorbeeld</h3>
      <p>Het systeem zoekt in eerdere rapporten naar situaties die op de jouwe lijken: in jullie eigen archief en in
      duizenden openbare rapporten.</p></li>
    <li class="kaart"><h3>Controle aan het eind</h3>
      <p>Controles kijken het rapport na: staat elk citaat echt in de bron, kloppen de getallen, en klopt het met de
      geldende regels?</p></li>
    <li class="kaart groen"><h3>Jij beslist</h3>
      <p>Elke afweging komt bij jou terug, met de reden erbij. Er verandert niets aan het rapport zonder dat jij
      het ziet.</p></li>
  </ul>
</section>

<section class="twee">
  <div>
    <h2>Herken je dit?</h2>
    <ul class="lijst">
      <li>Je schrijft steeds hetzelfde soort rapport, maar elk project is net anders.</li>
      <li>De inhoud komt uit losse stukken: onderzoeken, berekeningen, tekeningen, mails van de opdrachtgever.</li>
      <li>Veel tijd gaat naar overtypen, nalopen en zoeken hoe je het de vorige keer deed.</li>
      <li>Je moet achteraf kunnen uitleggen waarom er staat wat er staat.</li>
    </ul>
    <p style="margin-top:18px"><a class="link" href="/voor-wie/">Voor wie het werkt</a></p>
  </div>
  <div class="kaart">
    <h3>Liever eerst het plaatje?</h3>
    <p>In één animatie: drie onderzoeken, de documentgenerator en het rapport dat eruit komt.</p>
    <div class="acties" style="margin-top:16px"><a class="knop licht" href="/schema/">Bekijk het schema</a></div>
  </div>
</section>

<section aria-labelledby="kennis">
  <h2 id="kennis">Je begint niet bij nul</h2>
  <p class="smal">Naast jullie eigen rapporten kan het systeem zoeken in openbare rapporten die wij al hebben
  verzameld en ingedeeld. Zit jouw vakgebied er nog niet bij, dan bouwen we die verzameling op.</p>
  <div class="cijfers">
    <div><b>ruim 1.200</b>akoestische rapporten</div>
    <div><b>ruim 1.600</b>stukken over stikstof</div>
    <div><b>ruim 1.100</b>verkeersonderzoeken</div>
  </div>
  <p class="voetnoot">Openbare stukken onder de Omgevingswet, stand november 2026.</p>
</section>
{OPROEP}
""")

# ---------------------------------------------------------------- hoe het werkt
pagina("/hoe-het-werkt/", "Hoe het werkt",
       "In vijf stappen van jullie eigen rapporten naar een sjabloon, en van de stukken van een project naar een "
       "rapport dat is nagekeken.",
       f"""
<section>
  <p class="boven">Hoe het werkt</p>
  <h1 style="max-width:20ch">Eerst het sjabloon, daarna elk rapport.</h1>
  <p class="intro smal">Het begint met één keer goed vastleggen hoe jullie een rapport opbouwen. Daarna doorloopt
  elk nieuw rapport dezelfde stappen, en zit jij op de plek waar het om jouw oordeel gaat.</p>
  <div class="acties"><a class="knop licht" href="/schema/">Bekijk het als animatie</a></div>
</section>

<section aria-labelledby="eenmalig">
  <h2 id="eenmalig">Eenmalig: jullie sjabloon</h2>
  <ol class="stappen">
    <li><h3>We lezen jullie rapporten</h3>
      <p>Jullie leveren een aantal bestaande rapporten van één soort aan. Daaruit halen we de vaste opbouw: welke
      hoofdstukken, welke tekst steeds terugkomt, wat per project verschilt en onder welke voorwaarde iets er wel of
      niet in staat.</p></li>
    <li><h3>Samen maken we het sjabloon af</h3>
      <p>Dat wordt jullie sjabloon, helemaal voor jullie omgeving. Jullie vakkennis bepaalt wat erin komt. Waar het
      helpt, lenen we uit openbare rapporten of uit wat wij al voor hetzelfde vakgebied hebben gemaakt.</p>
      <p class="wie">Elk stuk tekst in het sjabloon weet uit welke rapporten het komt.</p></li>
  </ol>
</section>

<section aria-labelledby="perrapport">
  <h2 id="perrapport">Per rapport</h2>
  <ol class="stappen">
    <li><h3>Je levert de stukken van het project aan</h3>
      <p>De onderzoeken, berekeningen en documenten waar het rapport op moet rusten. Wat jij zelf weet, voeg je
      toe: jij bent ook een bron.</p></li>
    <li><h3>De gegevens worden uit de stukken gehaald</h3>
      <p>Bij elk gegeven hoort een citaat of een plek in de bron. Staat het er niet letterlijk, of klopt een getal
      niet, dan komt het er niet in. Wat ontbreekt, wordt een vraag aan jou.</p></li>
    <li><h3>Eerdere rapporten worden ernaast gelegd</h3>
      <p>Het systeem zoekt rapporten over een vergelijkbare situatie en laat zien wat die anders of extra doen.
      Bij elk verschil staat of het in dit project van toepassing is, en waarom.</p></li>
    <li><h3>Het rapport wordt opgebouwd</h3>
      <p>Volgens jullie sjabloon, in jullie formuleringen. Alleen de onderdelen die bij dit project horen, komen
      erin.</p></li>
    <li><h3>Het rapport wordt nagekeken en jij beslist</h3>
      <p>Controles lopen het rapport na op bronnen, getallen en regelgeving. Wat twijfel geeft, krijg jij als vraag
      of als voorstel. Jij keurt goed, past aan of wijst af.</p>
      <p class="wie"><a href="/herkomst-en-controle/">Meer over herkomst en controle</a></p></li>
  </ol>
</section>

<section class="tekst" aria-labelledby="blijft">
  <h2 id="blijft">Wat bij jou blijft</h2>
  <p class="smal">Het vakinhoudelijke oordeel. Het systeem doet het zoek-, lees- en schrijfwerk en legt vast waar
  alles vandaan komt. De afwegingen maak jij, en ze worden bewaard, zodat een volgend rapport erop kan
  voortbouwen.</p>
</section>
{OPROEP}
""")

# ---------------------------------------------------------------- herkomst en controle
pagina("/herkomst-en-controle/", "Herkomst en controle",
       "Van elke regel in het rapport zie je uit welke bron hij komt. Controles kijken citaten, getallen en "
       "regelgeving na, en elke afweging komt bij jou terug.",
       f"""
<section>
  <p class="boven">Herkomst en controle</p>
  <h1 style="max-width:20ch">Bij elke regel zie je waar hij vandaan komt.</h1>
  <p class="intro smal">Een rapport waar je naam onder staat, moet je kunnen uitleggen. Daarom is alles van begin
  tot eind te volgen: van de regel in het rapport terug naar de bron.</p>
</section>

<section aria-labelledby="volgen">
  <h2 id="volgen">Eén regel, drie bronnen</h2>
  <div class="spoor">
    <p class="zin">Op de gevel aan de <mark>Dorpsstraat</mark> is de geluidbelasting <mark class="b">54 dB</mark>,
    en daarmee <mark class="g">hoger dan de standaardwaarde</mark>.</p>
    <ul>
      <li><span style="background:var(--geel)"></span>Uit de opdracht van de opdrachtgever, met het citaat erbij.</li>
      <li><span style="background:var(--blauw)"></span>Uit de rekenresultaten, met de plek in het bestand.</li>
      <li><span style="background:var(--groen-licht)"></span>Uit de regelgeving, met het artikel en de geldende tekst.</li>
    </ul>
  </div>
  <p class="voorbeeld">Verzonnen voorbeeld, om te laten zien hoe het werkt.</p>
</section>

<section aria-labelledby="bronnen">
  <h2 id="bronnen">Waar de inhoud uit komt</h2>
  <ul class="rooster">
    <li class="kaart geel"><h3>De stukken van het project</h3>
      <p>Onderzoeken, berekeningen en documenten die jij aanlevert. Een gegeven over dit project komt alleen
      hieruit, of van jou.</p></li>
    <li class="kaart"><h3>Jullie sjabloon</h3>
      <p>De opbouw en de vaste tekst, afgeleid uit jullie eigen rapporten.</p></li>
    <li class="kaart blauw"><h3>Eerdere rapporten</h3>
      <p>Jullie archief en openbare rapporten, als voorbeeld van hoe een vergelijkbare situatie is beschreven.
      Nooit als bron voor de gegevens van dit project.</p></li>
    <li class="kaart groen"><h3>Wet- en regelgeving</h3>
      <p>De geldende tekst, zoals de Omgevingswet, het Bkl en het Bbl, met de toelichting erbij.</p></li>
  </ul>
</section>

<section aria-labelledby="controle">
  <h2 id="controle">Wat er wordt nagekeken</h2>
  <ul class="lijst smal">
    <li>Staat elk citaat letterlijk in de bron waar het naar verwijst?</li>
    <li>Staan de getallen in het rapport ook zo in de berekening?</li>
    <li>Geldt wat uit een eerder rapport is overgenomen ook in dit project?</li>
    <li>Klopt wat het rapport over de regels zegt met de tekst die nu geldt?</li>
  </ul>
  <p class="smal" style="margin-top:18px">Twijfel wordt nooit stil opgelost. Het wordt een vraag aan jou.</p>
</section>

<section class="tekst" aria-labelledby="afwegingen">
  <h2 id="afwegingen">Afwegingen komen bij jou terug</h2>
  <p class="smal">Waar een keuze gemaakt moet worden, doet het systeem een voorstel met de reden erbij. Jij legt
  de afweging vast of verwerpt haar. Wat niet van toepassing is, blijft zichtbaar, met de reden waarom niet.</p>
  <p class="smal">Alles wat het systeem heeft gedaan, blijft bewaard: wat het las, wat het voorstelde en wat jij
  ermee deed. Zo kun je later nagaan waarom er staat wat er staat.</p>
</section>
{OPROEP}
""")

# ---------------------------------------------------------------- voor wie
pagina("/voor-wie/", "Voor wie",
       "Voor iedereen die uit onderzoeken en documenten een rapport maakt: akoestiek, stikstof, verkeer, ecologie, "
       "bodem en andere vakgebieden.",
       f"""
<section>
  <p class="boven">Voor wie</p>
  <h1 style="max-width:21ch">Voor wie uit onderzoeken en documenten een rapport maakt.</h1>
  <p class="intro smal">Het vakgebied maakt weinig uit. Het werkt als jullie rapporten een herkenbare opbouw hebben
  en de inhoud uit andere stukken komt.</p>
</section>

<section aria-labelledby="past">
  <h2 id="past">Het past als dit bij jullie klopt</h2>
  <ul class="lijst smal">
    <li>Jullie schrijven regelmatig rapporten van dezelfde soort.</li>
    <li>Er is een sjabloon, of een vaste manier van opbouwen die in de rapporten terug te zien is.</li>
    <li>De inhoud komt uit bronnen: onderzoeken, metingen, berekeningen, dossiers, regelgeving.</li>
    <li>Een vakinhoudelijke medewerker tekent voor het resultaat en moet het kunnen onderbouwen.</li>
  </ul>
</section>

<section aria-labelledby="vakgebieden">
  <h2 id="vakgebieden">Vakgebieden</h2>
  <p class="smal">We zijn begonnen bij onderzoeken voor de leefomgeving. De werkwijze zelf is niet aan één vak
  gebonden: wat per vakgebied verschilt, zit in het sjabloon en in de bronnen.</p>
  <ul class="rooster">
    <li class="kaart geel"><h3>Hier hebben we al een verzameling</h3>
      <p>Akoestisch onderzoek, stikstofonderzoek en verkeersonderzoek. Daarvoor hebben we openbare rapporten
      verzameld en ingedeeld waar het systeem in kan zoeken.</p></li>
    <li class="kaart"><h3>Hier bouwen we het met jullie op</h3>
      <p>Bijvoorbeeld ecologisch onderzoek, bodemonderzoek of luchtkwaliteit. We beginnen dan bij jullie eigen
      rapporten en vullen aan met wat openbaar is.</p></li>
    <li class="kaart blauw"><h3>Buiten de leefomgeving</h3>
      <p>Maak je op een andere plek rapporten uit onderzoeken en documenten? Leg het ons voor. In de voorzet zie
      je snel of het bij jullie werkt.</p></li>
  </ul>
</section>
{OPROEP}
""")

# ---------------------------------------------------------------- voorzet
ONDERWERP = "Kosteloze%20voorzet%20Regelrapport"
pagina(VOORZET, "Kosteloze voorzet",
       "We maken kosteloos een voorzet voor jullie omgeving, op basis van jullie eigen rapporten, en komen hem "
       "laten zien.",
       f"""
<section>
  <p class="boven">Kosteloze voorzet</p>
  <h1 style="max-width:20ch">We laten het zien op jullie eigen rapporten.</h1>
  <p class="intro smal">Een voorzet is een eerste versie van jullie sjabloon, gemaakt uit een paar van jullie
  rapporten. Je ziet meteen hoe het er voor jullie soort werk uitziet. Het kost niets en je zit nergens aan vast.</p>
  <div class="acties">
    <a class="knop" href="mailto:{EMAIL}?subject={ONDERWERP}">Mail ons voor een voorzet</a>
    <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>
  </div>
</section>

<section aria-labelledby="gaat">
  <h2 id="gaat">Zo gaat het</h2>
  <ol class="stappen">
    <li><h3>Je stuurt ons een bericht</h3>
      <p>Vertel kort wat voor rapporten jullie maken. We nemen contact op om af te spreken welke rapporten we
      mogen gebruiken.</p></li>
    <li><h3>Wij maken de voorzet</h3>
      <p>Uit jullie rapporten, aangevuld met openbare rapporten of met wat we voor jullie vakgebied al hebben.</p></li>
    <li><h3>We komen hem laten zien</h3>
      <p>Je ziet het sjabloon, een rapport dat eruit komt en bij elke regel de bron. Daarna beslis je zelf of je
      verder wilt.</p></li>
  </ol>
</section>

<section class="tekst" aria-labelledby="gebeld">
  <h2 id="gebeld">Heb je ons al gesproken?</h2>
  <p class="smal">Dan weet degene die je belde of mailde al waar het over gaat. Antwoord op dat bericht, of mail
  naar <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</section>
""")
