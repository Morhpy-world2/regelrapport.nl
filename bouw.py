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
  <p><a href="/video/">In beeld</a></p>
  <p><a href="https://www.morphy.world">www.morphy.world</a></p>
</div></footer>
</body>
</html>
"""
    doel = HIER / pad.strip("/") / "index.html"
    doel.parent.mkdir(parents=True, exist_ok=True)
    doel.write_text(html, encoding="utf-8")
    print("geschreven:", doel.relative_to(HIER))


# De inhoud volgt de werkstuk-proeftuin (werkwijze 3.0, stand 12-11-2026): een sjabloon is vaste tekst plus
# vragen, afgeleid uit rapporten; per rapport een voorzet met bron en citaat, die de ingenieur bevestigt.
# Huub, 12-11-2026: de site mag vooruitlopen op de proeftuin wat betreft het zoeken in de openbare rapporten en
# de resultaten, en tijdwinst mag genoemd worden. Geen cijfers over tijdwinst (niet gemeten) en geen klantnamen.

OPROEP = f"""
<section class="oproep" aria-labelledby="voorzet">
  <h2 id="voorzet">Zien hoe dit er bij jullie uitziet?</h2>
  <p class="smal">We maken kosteloos een voorzet voor jullie omgeving, op basis van een aantal van jullie eigen
  rapporten. Daarna komen we hem graag laten zien.</p>
  <div class="acties"><a class="knop" href="{VOORZET}">Vraag een kosteloze voorzet aan</a></div>
</section>
"""

# ---------------------------------------------------------------- home
pagina("/", "Regelrapport: van onderzoeken naar rapport",
       "Regelrapport zet uit jullie onderzoeken en documenten een rapport op, volgens een sjabloon dat uit jullie "
       "eigen rapporten komt. Bij elk stuk tekst zie je waar het op rust.",
       f"""
<section>
  <p class="boven">Voor bureaus die rapporten schrijven</p>
  <h1 style="max-width:24ch">Van losse onderzoeken naar een rapport dat je stuk voor stuk kunt volgen.</h1>
  <p class="intro smal">Je verzamelt onderzoeken, berekeningen en documenten en schrijft daar een rapport van.
  {NAAM} zet dat rapport voor je op, volgens een sjabloon dat uit jullie eigen rapporten komt. Bij elk stuk tekst
  zie je waar het op rust. Jij bevestigt en beslist.</p>
  <div class="acties">
    <a class="knop" href="{VOORZET}">Vraag een kosteloze voorzet aan</a>
    <a class="link" href="/hoe-het-werkt/">Bekijk hoe het werkt</a>
  </div>
</section>

<section aria-labelledby="kort">
  <h2 id="kort">Wat het is, in zes punten</h2>
  <ul class="rooster">
    <li class="kaart geel"><h3>Een sjabloon uit jullie eigen rapporten</h3>
      <p>We leggen een reeks van jullie rapporten naast elkaar. Wat steeds terugkomt, wordt de vaste tekst. Wat
      per project verschilt, wordt een vraag.</p></li>
    <li class="kaart"><h3>Een rapport begint met vragen</h3>
      <p>Per project beantwoord je de vragen van het sjabloon. Je antwoorden bepalen welke stukken in het rapport
      komen en wat erin staat.</p></li>
    <li class="kaart blauw"><h3>Een voorzet met bron en citaat</h3>
      <p>Het systeem leest de stukken van het project en stelt per vraag een antwoord voor, met de bron en het
      letterlijke citaat erbij. Jij bevestigt of past aan.</p></li>
    <li class="kaart geel"><h3>Eerdere rapporten erbij</h3>
      <p>Het systeem zoekt rapporten over een situatie die op de jouwe lijkt: in jullie eigen archief en in de
      openbare rapporten die wij hebben verzameld.</p></li>
    <li class="kaart"><h3>Nagekeken op bron, getal en regel</h3>
      <p>Staat het citaat echt in de bron? Staan de getallen er ook? Zegt de tekst niets wat jij niet hebt
      geantwoord? Een eindcontrole legt het rapport tegen de wet en de rekenwaarden.</p></li>
    <li class="kaart groen"><h3>Jij beslist</h3>
      <p>Het systeem doet voorstellen. Er komt niets definitief in het rapport zonder dat jij het hebt bevestigd,
      en elke vorige versie blijft bewaard.</p></li>
  </ul>
</section>

<section aria-labelledby="oplevert">
  <h2 id="oplevert">Wat het je oplevert</h2>
  <ul class="rooster">
    <li class="kaart"><h3>Minder tijd per rapport</h3>
      <p>Overtypen, nalopen en zoeken hoe je het de vorige keer deed, neemt het systeem over. Jouw tijd gaat naar
      het vakinhoudelijke oordeel.</p></li>
    <li class="kaart"><h3>Elk rapport op dezelfde manier</h3>
      <p>Dezelfde opbouw, dezelfde formuleringen en dezelfde vragen, wie het rapport ook maakt.</p></li>
    <li class="kaart"><h3>Een rapport dat je kunt uitleggen</h3>
      <p>Bij elk stuk tekst zie je waar het op rust. Dat scheelt bij de interne controle en bij vragen van de
      opdrachtgever of het bevoegd gezag.</p></li>
  </ul>
</section>

<section class="twee">
  <div>
    <h2>Herken je dit?</h2>
    <ul class="lijst">
      <li>Je schrijft steeds hetzelfde soort rapport, maar elk project is net anders.</li>
      <li>De inhoud komt uit losse stukken: onderzoeken, berekeningen, tekeningen, de offerte, mails van de
      opdrachtgever.</li>
      <li>Veel tijd gaat naar overtypen, nalopen en zoeken hoe je het de vorige keer deed.</li>
      <li>Je moet achteraf kunnen uitleggen waarom er staat wat er staat.</li>
    </ul>
    <p style="margin-top:18px"><a class="link" href="/voor-wie/">Voor wie het werkt</a></p>
  </div>
  <div class="kaart">
    <h3>Liever eerst het plaatje?</h3>
    <p>Twee korte animaties: hoe je een rapport maakt, en wat er achter één alinea zit.</p>
    <div class="acties" style="margin-top:16px"><a class="knop licht" href="/video/">Bekijk de animatie</a></div>
  </div>
</section>

<section aria-labelledby="kennis">
  <h2 id="kennis">Je begint niet bij nul</h2>
  <p class="smal">Wij hebben openbare rapporten verzameld en ingedeeld. Het systeem zoekt daarin naar
  situaties die op jouw project lijken, en we hebben er al eerste sjablonen uit afgeleid. Zo kunnen we voor
  jullie vakgebied snel een voorzet maken. Zit jouw vakgebied er nog niet bij, dan bouwen we die verzameling
  op.</p>
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
       "Eerst een sjabloon uit jullie eigen rapporten: vaste tekst en vragen. Daarna per rapport: stukken "
       "aanleveren, vragen bevestigen, tekst nalezen en een eindcontrole.",
       f"""
<section>
  <p class="boven">Hoe het werkt</p>
  <h1 style="max-width:20ch">Eerst het sjabloon, daarna elk rapport.</h1>
  <p class="intro smal">Een sjabloon bestaat bij ons uit twee delen: de vaste tekst van jullie rapporten, en de
  vragen die bepalen wat er in een rapport komt. Dat leggen we één keer goed vast. Daarna doorloopt elk nieuw
  rapport dezelfde stappen, en kost een rapport je minder tijd.</p>
  <div class="acties"><a class="knop licht" href="/video/">Bekijk het als animatie</a></div>
</section>

<section aria-labelledby="eenmalig">
  <h2 id="eenmalig">Eenmalig: jullie sjabloon</h2>
  <ol class="stappen">
    <li><h3>We leggen jullie rapporten naast elkaar</h3>
      <p>Jullie leveren een reeks bestaande rapporten van één soort aan. We zoeken eerst welke tekst letterlijk
      terugkomt, en in welke situatie. Dat wordt de vaste tekst, met bij elk stuk de rapporten waar het uit
      komt.</p></li>
    <li><h3>Wat verschilt, wordt een vraag</h3>
      <p>Staat een stuk niet in elk rapport, dan zoeken we de projectsituatie die dat verklaart. Daar komt een
      vraag uit, zoals je die als vakmens zou stellen: gaat het om nieuwbouw, wordt er gesloopt, welke bronnen
      spelen mee. Per vraag zie je hoe jullie eerdere rapporten hem beantwoordden.</p>
      <p class="wie">Drie AI-modellen doen dit los van elkaar en moeten het daarna eens worden.</p></li>
    <li><h3>Wat het sjabloon over de wet zegt, leggen we naast de wet</h3>
      <p>Elke bewering over regelgeving wordt naast de tekst gelegd die nu geldt, met het citaat erbij. In onze
      proeven kwamen zo verwijzingen boven naar regels die inmiddels zijn gewijzigd.</p></li>
    <li><h3>Jullie beslissen over de open punten</h3>
      <p>Waar de rapporten elkaar tegenspreken of de wet iets anders zegt, komt een beslispunt met de keuzes
      erbij. Jullie vakkennis bepaalt wat het sjabloon wordt.</p></li>
  </ol>
</section>

<section aria-labelledby="perrapport">
  <h2 id="perrapport">Per rapport</h2>
  <ol class="stappen">
    <li><h3>Je levert de stukken van het project aan</h3>
      <p>De offerte, de rekenresultaten en de andere stukken waar het rapport op rust. Wat jij zelf weet, voeg
      je toe: jij bent ook een bron.</p></li>
    <li><h3>Eerdere rapporten worden erbij gezocht</h3>
      <p>Het systeem zoekt rapporten over een vergelijkbare situatie, in jullie eigen archief en in de openbare
      rapporten die wij hebben verzameld. Je ziet waarin ze op jouw project lijken en waarin ze verschillen, en
      jij kiest welk rapport als voorbeeld dient.</p></li>
    <li><h3>Het systeem doet per vraag een voorzet</h3>
      <p>Het leest de stukken en stelt per vraag een antwoord voor, met de bron en het letterlijke citaat. Staat
      het citaat niet in de bron, of klopt een getal niet, dan vervalt het voorstel en blijft de vraag open
      voor jou.</p></li>
    <li><h3>Jij bevestigt of past aan</h3>
      <p>Een voorstel blijft geel tot jij het bevestigt. Na elk antwoord zie je welke stukken er in het rapport
      bij komen of wegvallen. Wat uit de regels te berekenen is, zoals een toets aan een grenswaarde, rekent het
      systeem uit met het wetsartikel erbij.</p></li>
    <li><h3>De tekst komt te staan</h3>
      <p>De vaste tekst wordt ingevuld met jouw antwoorden. Alleen de beschrijvende delen worden geschreven, en
      alleen uit wat jij hebt geantwoord. Een tweede lezer kijkt of er niets is bijverzonnen.</p></li>
    <li><h3>Je leest na en bewerkt</h3>
      <p>Je past de tekst zelf aan of geeft een opdracht. Elke versie blijft bewaard en is terug te zetten.</p></li>
    <li><h3>Eindcontrole</h3>
      <p>Op jouw verzoek legt een controle het rapport tegen de wet en de rekenwaarden. Je krijgt meldingen met
      een voorstel, en je ziet wat wel en niet is getoetst. Jij handelt elke melding af.</p>
      <p class="wie"><a href="/herkomst-en-controle/">Meer over herkomst en controle</a></p></li>
  </ol>
</section>

<section class="tekst" aria-labelledby="blijft">
  <h2 id="blijft">Wat bij jou blijft</h2>
  <p class="smal">Het vakinhoudelijke oordeel. Het systeem doet het lees-, zoek- en schrijfwerk en legt vast waar
  alles vandaan komt. Tijdens het werk kun je het ook iets vragen: hoe deden eerdere rapporten dit, wat zegt de
  wet hierover. Het antwoord komt met bronnen, en wat je overneemt blijft een voorstel tot jij het bevestigt.</p>
</section>
{OPROEP}
""")

# ---------------------------------------------------------------- herkomst en controle
pagina("/herkomst-en-controle/", "Herkomst en controle",
       "Bij elk stuk tekst zie je waar het op rust: jullie sjabloon, een citaat uit een projectstuk, een "
       "wetsartikel of jouw eigen antwoord. Controles kijken citaten, getallen en regelgeving na.",
       f"""
<section>
  <p class="boven">Herkomst en controle</p>
  <h1 style="max-width:20ch">Bij elk stuk tekst zie je waar het op rust.</h1>
  <p class="intro smal">Een rapport waar je naam onder staat, moet je kunnen uitleggen. Daarom is het van begin
  tot eind te volgen: van de tekst in het rapport terug naar het antwoord, en van het antwoord terug naar de
  bron.</p>
</section>

<section aria-labelledby="volgen">
  <h2 id="volgen">Eén regel, drie bronnen</h2>
  <div class="spoor">
    <p class="zin">Op de gevel aan de <mark>Beukenlaan</mark> is de geluidbelasting <mark class="b">54 dB</mark>,
    en daarmee <mark class="g">hoger dan de standaardwaarde</mark>.</p>
    <ul>
      <li><span style="background:var(--geel)"></span>Uit de offerte, met het letterlijke citaat. Door jou bevestigd.</li>
      <li><span style="background:var(--blauw)"></span>Uit de rekenresultaten, met de plek in het bestand.</li>
      <li><span style="background:var(--groen-licht)"></span>Uitgerekend volgens de regel, met het wetsartikel erbij.</li>
    </ul>
  </div>
  <p class="voorbeeld">Verzonnen voorbeeld, om te laten zien hoe het werkt.</p>
</section>

<section aria-labelledby="bronnen">
  <h2 id="bronnen">Waar de tekst op rust</h2>
  <ul class="rooster">
    <li class="kaart"><h3>Vaste tekst</h3>
      <p>Komt uit het sjabloon. Bij elk stuk staat uit welke van jullie rapporten het komt.</p></li>
    <li class="kaart geel"><h3>Gegevens van het project</h3>
      <p>Komen uit de stukken die jij aanlevert, met bron en citaat, of van jou zelf. Nooit uit een ander
      rapport en nooit uit de wet.</p></li>
    <li class="kaart blauw"><h3>Geschreven passages</h3>
      <p>Worden geschreven uit jouw antwoorden. Bij elke passage zie je welke antwoorden erin zitten. Eerdere
      rapporten, uit jullie archief en uit de openbare verzameling, geven de vorm, niet de feiten.</p></li>
    <li class="kaart groen"><h3>Wet- en regelgeving</h3>
      <p>De geldende tekst, zoals de Omgevingswet, het Bkl en het Bbl, met de toelichting erbij.</p></li>
  </ul>
</section>

<section aria-labelledby="controle">
  <h2 id="controle">Wat er wordt nagekeken</h2>
  <ul class="lijst smal">
    <li>Staat elk citaat letterlijk in de bron?</li>
    <li>Staat elk getal in het antwoord ook in de bron?</li>
    <li>Draagt de bron het voorgestelde antwoord helemaal, deels of niet?</li>
    <li>Staat er in een geschreven passage iets wat jij niet hebt geantwoord, of ontbreekt er iets?</li>
    <li>Kies je een antwoord dat in geen van jullie eerdere rapporten voorkwam? Dan staat erbij dat dit niet is
    getest, tot jij akkoord geeft.</li>
    <li>Klopt het rapport met de wet en met de rekenwaarden? Dat doet de eindcontrole.</li>
  </ul>
  <p class="smal" style="margin-top:18px">De eindcontrole is een tweede beoordelaar, geen garantie. Hij laat zien
  wat hij heeft getoetst. Wat niet is beoordeeld, telt niet als akkoord.</p>
</section>

<section class="tekst" aria-labelledby="afwegingen">
  <h2 id="afwegingen">Niets gebeurt stil</h2>
  <p class="smal">Twijfel wordt een vraag aan jou, geen stille keuze. Wat het systeem niet kan vinden, blijft
  open, met de reden erbij. Jouw besluiten worden vastgelegd, met wie en wanneer.</p>
  <p class="smal">Alles wat het systeem heeft gedaan, blijft bewaard: wat het las, wat het voorstelde en wat jij
  ermee deed. Zo kun je later nagaan waarom er staat wat er staat.</p>
</section>
{OPROEP}
""")

# ---------------------------------------------------------------- voor wie
pagina("/voor-wie/", "Voor wie",
       "Voor iedereen die uit onderzoeken en documenten een rapport maakt. Het verst zijn we met akoestisch "
       "onderzoek; voor stikstof en verkeer ligt er een eerste sjabloon.",
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
    <li>Er is een reeks bestaande rapporten waar de vaste manier van opbouwen in terug te zien is. Een sjabloon
    in Word hoeft er niet te zijn.</li>
    <li>De inhoud komt uit bronnen: onderzoeken, metingen, berekeningen, dossiers, regelgeving.</li>
    <li>Een vakinhoudelijke medewerker tekent voor het resultaat en moet het kunnen onderbouwen.</li>
  </ul>
</section>

<section aria-labelledby="vakgebieden">
  <h2 id="vakgebieden">Vakgebieden</h2>
  <p class="smal">We zijn begonnen bij onderzoeken voor de leefomgeving. De werkwijze zelf is niet aan één vak
  gebonden: de vragen, de vaste tekst en de regels verschillen per vakgebied, de stappen niet.</p>
  <ul class="rooster">
    <li class="kaart geel"><h3>Hier zijn we het verst</h3>
      <p>Akoestisch onderzoek naar wegverkeer. Voor stikstofonderzoek en verkeersonderzoek ligt er een eerste
      sjabloon. Van alle drie hebben we openbare rapporten verzameld en ingedeeld.</p></li>
    <li class="kaart"><h3>Hier bouwen we het met jullie op</h3>
      <p>Bijvoorbeeld ecologisch onderzoek, bodemonderzoek of luchtkwaliteit. We beginnen dan bij jullie eigen
      rapporten en vullen aan met wat openbaar is.</p></li>
    <li class="kaart blauw"><h3>Buiten de leefomgeving</h3>
      <p>Maak je op een andere plek rapporten uit onderzoeken en documenten? Leg het ons voor. In de voorzet zie
      je snel of het bij jullie werkt.</p></li>
  </ul>
</section>

<section class="tekst" aria-labelledby="stand">
  <h2 id="stand">Waar we nu staan</h2>
  <p class="smal">We bouwen dit per vakgebied op, samen met het bureau. Elk sjabloon heeft punten waar jullie
  vakkennis en soms een jurist over beslissen. Die punten laten we zien; we lossen ze niet stil op.</p>
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
  <p class="intro smal">Een voorzet is een eerste versie van jullie sjabloon, gemaakt uit een aantal van jullie
  rapporten: de vaste tekst en de vragen die we erin vinden. Je ziet meteen hoe het er voor jullie soort werk
  uitziet. Het kost niets en je zit nergens aan vast.</p>
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
      <p>Je ziet de vragen, de vaste tekst en per vraag hoe jullie eigen rapporten hem beantwoordden. Daarna
      beslis je zelf of je verder wilt.</p></li>
  </ol>
</section>

<section class="tekst" aria-labelledby="gebeld">
  <h2 id="gebeld">Heb je ons al gesproken?</h2>
  <p class="smal">Dan weet degene die je belde of mailde al waar het over gaat. Antwoord op dat bericht, of mail
  naar <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</section>
""")

# ---------------------------------------------------------------- in beeld
# Twee animaties onder elkaar, elk een eigen bestand in video/ (met de hand gemaakt, niet door dit script).
# De eerste animatie (schema/index.html) blijft staan en is hieronder gelinkt.
pagina("/video/", "In beeld",
       "Twee korte animaties: hoe je met Regelrapport een rapport maakt, en wat er achter één alinea zit.",
       f"""
<section>
  <p class="boven">In beeld</p>
  <h1 style="max-width:20ch">Zo maak je een rapport.</h1>
  <p class="intro smal">Van sjabloon tot eindcontrole, in een verzonnen project.</p>
  <iframe class="film" id="film-a" src="werkstuk/?embed=1" title="Animatie: zo maak je een rapport" loading="lazy"></iframe>
</section>

<section aria-labelledby="alinea">
  <h2 id="alinea">Wat er achter één alinea zit</h2>
  <p class="smal">Dezelfde alinea, nu van de andere kant: waar elk deel vandaan komt.</p>
  <iframe class="film" id="film-b" src="alinea/?embed=1" title="Animatie: wat er achter één alinea zit" loading="lazy"></iframe>
  <p class="voetnoot"><a href="/schema/">Bekijk ook de eerste animatie: van onderzoeken naar rapport</a></p>
</section>
<script>
addEventListener("message", e => {{
  const h = e.data && e.data.regelrapportHoogte;
  if (!h) return;
  for (const f of document.querySelectorAll("iframe.film")) if (f.contentWindow === e.source) f.style.height = h + "px";
}});
</script>
{OPROEP}
""")
