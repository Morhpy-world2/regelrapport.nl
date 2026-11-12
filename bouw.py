"""Bouwt de site: `python3 bouw.py` in de repo-root.

Ontwerp "Rapport" (12-11-2026), gekozen uit de varianten. Pas tekst hier aan, niet in de html. De pijlen in het
voorbeeld rekent script.js uit; de animaties in video/werkstuk/ en video/alinea/ worden ingesloten op de home en op
herkomst-en-controle. De oude animatie in schema/ blijft bestaan maar is nergens meer gelinkt.
"""
from pathlib import Path

DOEL = Path(__file__).parent
GEDEELD = ""   # fonts/, video/ en schema/ staan naast de pagina's
SITE = "https://regelrapport.nl"
DEELBEELD = "deel-regelrapport.png"   # 1200 x 630, voor LinkedIn en andere previews
NAAM = "Regelrapport"
EMAIL = "info@morphy.world"
MAILTO = f"mailto:{EMAIL}?subject=Kosteloze%20voorzet%20Regelrapport"

CUR = ' aria-current="page"'
MENU = [
    ("hoe-het-werkt", "Hoe het werkt"),
    ("herkomst-en-controle", "Herkomst en controle"),
    ("voor-wie", "Voor wie"),
    ("over-ons", "Over ons"),
]

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect x='4' y='2' width='24' height='28' rx='2' fill='%230e4a57'/%3E"
           "%3Cpath d='M9 10h14M9 15h14M9 20h9' stroke='%23fff' stroke-width='2.4'/%3E"
           "%3Ccircle cx='23' cy='21' r='3' fill='%23f0a35e'/%3E%3C/svg%3E")

MERK = ('<svg class="merk-icoon" viewBox="0 0 32 32" aria-hidden="true" focusable="false">'
        '<rect x="4" y="2" width="24" height="28" rx="2" fill="#0e4a57"/>'
        '<path d="M9 10h14M9 15h14M9 20h9" stroke="#fff" stroke-width="2.4"/>'
        '<circle cx="23" cy="21" r="3" fill="#f0a35e"/></svg>')


def pagina(slug, titel, omschrijving, inhoud):
    r = "" if slug == "" else "../"          # pad naar de root van de variant
    thuis = "./" if slug == "" else "../"
    schema = r + GEDEELD + "schema/"
    url = f"{SITE}/{slug}/" if slug else f"{SITE}/"
    menu = "".join(
        f'<li><a href="{r}{s}/"{CUR if s == slug else ""}>{t}</a></li>' for s, t in MENU)
    voorzet_cur = ' aria-current="page"' if slug == "voorzet" else ""
    kop = titel if slug == "" else f"{titel} · {NAAM}"
    html = f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{kop}</title>
<meta name="description" content="{omschrijving}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAAM}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{kop}">
<meta property="og:description" content="{omschrijving}">
<meta property="og:locale" content="nl_NL">
<meta property="og:image" content="{SITE}/{DEELBEELD}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Eén zin uit een rapport, met een pijl van elk gemarkeerd deel naar zijn bron.">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{FAVICON}">
<script>document.documentElement.classList.add("js")</script>
<link rel="preload" href="{r}{GEDEELD}fonts/kalam-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}stijl.css">
<script src="{r}script.js" defer></script>
</head>
<body>
<a class="overslaan" href="#inhoud">Naar de inhoud</a>
<header class="kop">
  <div class="kader kop-binnen">
    <a class="merk" href="{thuis}"{' aria-current="page"' if slug == "" else ""}>{MERK}<span>{NAAM}</span></a>
    <nav class="nav" aria-label="Hoofdmenu">
      <button class="menu-knop" type="button" aria-expanded="false" aria-controls="menu"><span class="menu-streepjes" aria-hidden="true"></span>Menu</button>
      <ul id="menu">{menu}</ul>
      <a class="knop knop-klein" href="{r}voorzet/"{voorzet_cur}>Kosteloze voorzet</a>
    </nav>
  </div>
</header>
<main id="inhoud">
{inhoud.strip().replace("{R}", r).replace("{SCHEMA}", schema).replace("{VIDEO}", r + GEDEELD + "video/")}
</main>
<footer class="voet">
  <div class="kader voet-binnen">
    <p class="voet-merk">{MERK}<span>{NAAM} is van Morphy B.V. · KVK 95783652</span></p>
    <ul>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="https://www.morphy.world">www.morphy.world</a></li>
    </ul>
  </div>
</footer>
</body>
</html>
"""
    pad = DOEL / slug / "index.html" if slug else DOEL / "index.html"
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(html, encoding="utf-8")
    print("geschreven:", pad.relative_to(DOEL))


VOORBEELD_ZIN = """<p class="fragment-zin">Op de gevel aan de <mark class="m1">Beukenlaan</mark><sup>1</sup> is de
      geluidbelasting <mark class="m2">54 dB</mark><sup>2</sup>, en daarmee <mark class="m3">hoger dan de
      standaardwaarde</mark><sup>3</sup>.</p>"""

BRONNEN = [
    ("offerte", "Uit de offerte, met het letterlijke citaat. Door jou bevestigd."),
    ("rekenresultaten", "Uit de rekenresultaten, met de plek in het bestand."),
    ("wetsartikel", "Uitgerekend volgens de regel, met het wetsartikel erbij."),
]


def scene(soort, titel_id="", onderschrift=""):
    """De kern: het rapportvel met de zin, de bronvellen ernaast en een (in script.js berekende) pijl per bron."""
    lab = f' aria-labelledby="{titel_id}"' if titel_id else ""
    kid = f' id="{titel_id}"' if titel_id else ""
    vellen = "".join(f"""
          <li class="bronvel b{i}"><span class="vel-naam" aria-hidden="true">{naam}</span><span class="vel-regels" aria-hidden="true"></span><span class="vel-tekst"><span class="nr">{i}</span><span>{tekst}</span></span></li>"""
                     for i, (naam, tekst) in enumerate(BRONNEN, 1))
    return f"""<figure class="scene scene-{soort}"{lab}>
      <div class="scene-raster">
        <div class="rapportvel">
          <p class="fragment-kop"{kid}><span>Uit een rapport</span><span>één zin</span></p>
          {VOORBEELD_ZIN}
        </div>
        <ol class="bronvellen">{vellen}
        </ol>
        <svg class="pijlen" aria-hidden="true" focusable="false"></svg>
      </div>
      <figcaption>Fictief voorbeeld.{onderschrift}</figcaption>
    </figure>"""


def film(id_, kop, intro, map_, titel):
    """Een animatie uit /video/, over de volle breedte. De hoogte zet script.js (bericht uit het iframe)."""
    intro = f'\n    <p class="tekst">{intro}</p>' if intro else ""
    return f"""
<section class="film-sectie" aria-labelledby="{id_}">
  <div class="kader">
    <h2 id="{id_}">{kop}</h2>{intro}
    <iframe class="film" src="{{VIDEO}}{map_}/?embed=1" title="{titel}" loading="lazy"></iframe>
  </div>
</section>"""


def sectie(nr, label, id_, kop, inhoud, extra=""):
    return f"""
<section class="sectie{extra}" aria-labelledby="{id_}">
  <div class="kader sectie-raster">
    <p class="marge"><span>{nr}</span>{label}</p>
    <div class="sectie-inhoud">
      <h2 id="{id_}">{kop}</h2>
      {inhoud}
    </div>
  </div>
</section>"""


def oproep():
    return """
<section class="oproep" aria-labelledby="oproep-kop">
  <div class="kader oproep-binnen">
    <div>
      <h2 id="oproep-kop">Bekijk het op een aantal van jullie eigen rapporten</h2>
      <p>We maken kosteloos een voorzet voor jullie omgeving, op basis van een aantal van jullie eigen rapporten.
      Daarna komen we hem graag laten zien.</p>
    </div>
    <a class="knop knop-licht" href="{R}voorzet/">Naar de kosteloze voorzet</a>
  </div>
</section>"""


def stappen(items, start=1, prefix=""):
    rijen = "".join(
        f"""
        <li><span class="stap-nr" aria-hidden="true">{prefix}{i}</span><div><h3>{h}</h3>{p}</div></li>"""
        for i, (h, p) in enumerate(items, start))
    return f'<ol class="stappen">{rijen}\n      </ol>'


def tabel(items):
    rijen = "".join(f"""
        <li><h3>{h}</h3><p>{p}</p></li>""" for h, p in items)
    return f'<ul class="punten">{rijen}\n      </ul>'


# ------------------------------------------------------------------ home
pagina("", "Regelrapport: van onderzoeken naar rapport",
       "Regelrapport zet uit jullie onderzoeken en documenten een rapport op, volgens een sjabloon dat uit jullie "
       "eigen rapporten komt. Bij elk stuk tekst zie je waar het op rust.",
       f"""
<section class="held held-film">
  <div class="kader">
    <div class="held-tekst">
      <p class="boven">Voor bureaus die rapporten schrijven uit onderzoeken en documenten</p>
      <h1>Regelrapport zet jullie rapport op.</h1>
      <p class="intro">Je verzamelt onderzoeken, berekeningen en documenten en schrijft daar een rapport van.
      Regelrapport zet dat rapport voor je op, volgens een sjabloon dat uit jullie eigen rapporten komt. Jij
      bevestigt en beslist.</p>
      <div class="acties">
        <a class="knop" href="{{R}}voorzet/">Vraag een kosteloze voorzet aan</a>
        <a class="pijl" href="{{R}}hoe-het-werkt/">Zo werkt het</a>
      </div>
    </div>
    <iframe class="film" src="{{VIDEO}}werkstuk/?embed=1" title="Animatie: zo maak je een rapport"></iframe>
  </div>
</section>
<section class="sectie zin-sectie" aria-labelledby="zin-kop">
  <div class="kader">
    <h2 id="zin-kop">Bij elk stuk tekst zie je waar het op rust</h2>
    <p class="tekst">Eén zin uit een rapport. Elk gemarkeerd deel wijst terug naar het stuk waar het uit komt: de
    offerte, de rekenresultaten of het wetsartikel.</p>
    {scene("breed", "fragment-titel", '''
      <a href="{R}herkomst-en-controle/">Meer over herkomst</a>''')}
  </div>
</section>
""" + sectie("01", "In het kort", "kort", "Wat Regelrapport doet, in zes punten", tabel([
    ("Het sjabloon komt uit jullie rapporten",
     "We leggen een reeks van jullie rapporten naast elkaar. Wat steeds terugkomt, wordt de vaste tekst. Wat per "
     "project verschilt, wordt een vraag."),
    ("Elk rapport begint met vragen",
     "Per project beantwoord je de vragen van het sjabloon. Je antwoorden bepalen welke stukken in het rapport "
     "komen en wat erin staat."),
    ("Per vraag een voorstel, met bron en citaat",
     "Het systeem leest de stukken van het project en stelt per vraag een antwoord voor, met de bron en het "
     "letterlijke citaat erbij. Jij bevestigt of past aan."),
    ("Eerdere rapporten als voorbeeld erbij",
     "Het systeem zoekt rapporten over een situatie die op de jouwe lijkt: in jullie eigen archief en in de "
     "openbare rapporten die wij hebben verzameld."),
    ("Nagekeken op citaat, getal en regel",
     "Staat het citaat echt in de bron? Staan de getallen er ook? Zegt de tekst niets wat jij niet hebt "
     "geantwoord? Een eindcontrole legt het rapport tegen de wet en de rekenwaarden."),
    ("Bevestigen doe jij",
     "Het systeem doet voorstellen. Er komt niets definitief in het rapport zonder dat jij het hebt bevestigd, en "
     "elke vorige versie blijft bewaard."),
])) + sectie("02", "Opbrengst", "oplevert", "Wat je eraan hebt", """<ul class="drie">
        <li><h3>Minder tijd per rapport</h3>
          <p>Overtypen, nalopen en zoeken hoe je het de vorige keer deed, neemt het systeem over. Jouw tijd gaat
          naar het vakinhoudelijke oordeel.</p></li>
        <li><h3>Elk rapport volgens dezelfde opbouw</h3>
          <p>Dezelfde opbouw, dezelfde formuleringen en dezelfde vragen, wie het rapport ook maakt.</p></li>
        <li><h3>Uit te leggen, stuk voor stuk</h3>
          <p>Bij elk stuk tekst zie je waar het op rust. Dat scheelt bij de interne controle en bij vragen van de
          opdrachtgever of het bevoegd gezag.</p></li>
      </ul>""", " grijs") + sectie("03", "Herkenning", "nu", "Hoe rapporten nu vaak ontstaan", """<ul class="lijst">
          <li>Je schrijft steeds hetzelfde soort rapport, maar elk project is net anders.</li>
          <li>De inhoud komt uit losse stukken: onderzoeken, berekeningen, tekeningen, de offerte, mails van de
          opdrachtgever.</li>
          <li>Veel tijd gaat naar overtypen, nalopen en zoeken hoe je het de vorige keer deed.</li>
          <li>Je moet achteraf kunnen uitleggen waarom er staat wat er staat.</li>
        </ul>
      <p class="verder"><a class="pijl" href="{R}voor-wie/">Past het bij jullie bureau?</a></p>""") + sectie(
    "04", "Openbare rapporten", "kennis", "Een verzameling openbare rapporten om in te zoeken",
    """<p class="tekst">Wij hebben openbare rapporten verzameld en ingedeeld. Het systeem zoekt daarin naar
      situaties die op jouw project lijken, en we hebben er al eerste sjablonen uit afgeleid. Zo kunnen we voor
      jullie vakgebied snel een voorzet maken. Zit jouw vakgebied er nog niet bij, dan bouwen we die verzameling
      op.</p>
      <dl class="cijfers">
        <div><dt>akoestische rapporten</dt><dd>ruim 1.200</dd></div>
        <div><dt>stukken over stikstof</dt><dd>ruim 1.600</dd></div>
        <div><dt>verkeersonderzoeken</dt><dd>ruim 1.100</dd></div>
      </dl>
      <p class="noot">Openbare stukken onder de Omgevingswet, stand november 2026.</p>""", " grijs") + oproep())

# ------------------------------------------------------------------ hoe het werkt
pagina("hoe-het-werkt", "Hoe het werkt",
       "Eerst een sjabloon uit jullie eigen rapporten: vaste tekst en vragen. Daarna per rapport: stukken "
       "aanleveren, vragen bevestigen, tekst nalezen en een eindcontrole.",
       """
<section class="held held-smal">
  <div class="kader">
    <p class="boven">Werkwijze</p>
    <h1>Eerst het sjabloon, daarna elk rapport in dezelfde stappen.</h1>
    <p class="intro">Een sjabloon bestaat bij ons uit twee delen: de vaste tekst van jullie rapporten, en de vragen
    die bepalen wat er in een rapport komt. Dat leggen we één keer goed vast. Daarna doorloopt elk nieuw rapport
    dezelfde stappen, en kost een rapport je minder tijd.</p>
  </div>
</section>
""" + sectie("A", "Eenmalig", "eenmalig", "Vooraf: het sjabloon van jullie bureau", stappen([
    ("Wat steeds terugkomt, wordt vaste tekst",
     "<p>Jullie leveren een reeks bestaande rapporten van één soort aan. We zoeken eerst welke tekst letterlijk "
     "terugkomt, en in welke situatie. Dat wordt de vaste tekst, met bij elk stuk de rapporten waar het uit "
     "komt.</p>"),
    ("Wat per project verschilt, wordt een vraag",
     "<p>Staat een stuk niet in elk rapport, dan zoeken we de projectsituatie die dat verklaart. Daar komt een vraag "
     "uit, zoals je die als vakmens zou stellen: gaat het om nieuwbouw, wordt er gesloopt, welke bronnen spelen "
     "mee. Per vraag zie je hoe jullie eerdere rapporten hem beantwoordden.</p>"
     '<p class="opm">Drie AI-modellen doen dit los van elkaar en moeten het daarna eens worden.</p>'),
    ("Uitspraken over de wet, naast de tekst die nu geldt",
     "<p>Elke bewering over regelgeving in het sjabloon wordt naast de tekst gelegd die nu geldt, met het citaat "
     "erbij. In onze proeven kwamen zo verwijzingen boven naar regels die inmiddels zijn gewijzigd.</p>"),
    ("Over de open punten beslissen jullie",
     "<p>Waar de rapporten elkaar tegenspreken of de wet iets anders zegt, komt een beslispunt met de keuzes "
     "erbij. Jullie vakkennis bepaalt wat het sjabloon wordt.</p>"),
], prefix="A")) + sectie("B", "Per rapport", "perrapport", "Daarna: zo ontstaat elk nieuw rapport", stappen([
    ("Jij levert de projectstukken aan",
     "<p>De offerte, de rekenresultaten en de andere stukken waar het rapport op rust. Wat jij zelf weet, voeg je "
     "toe: ook jij bent een bron.</p>"),
    ("Vergelijkbare rapporten worden erbij gezocht",
     "<p>Het systeem zoekt rapporten over een vergelijkbare situatie, in jullie eigen archief en in de openbare "
     "rapporten die wij hebben verzameld. Je ziet waarin ze op jouw project lijken en waarin ze verschillen, en jij "
     "kiest welk rapport als voorbeeld dient.</p>"),
    ("Per vraag een voorgesteld antwoord",
     "<p>Het systeem leest de stukken en stelt per vraag een antwoord voor, met de bron en het letterlijke citaat. "
     "Staat het citaat niet in de bron, of klopt een getal niet, dan vervalt het voorstel en blijft de vraag open "
     "voor jou.</p>"),
    ("Jij bevestigt of past aan",
     "<p>Een voorstel blijft geel tot jij het bevestigt. Na elk antwoord zie je welke stukken er in het rapport bij "
     "komen of wegvallen. Wat uit de regels te berekenen is, zoals een toets aan een grenswaarde, rekent het "
     "systeem uit met het wetsartikel erbij.</p>"),
    ("De tekst wordt ingevuld",
     "<p>De vaste tekst wordt ingevuld met jouw antwoorden. Alleen de beschrijvende delen worden geschreven, en "
     "alleen uit wat jij hebt geantwoord. Een tweede lezer kijkt of er niets is bijverzonnen.</p>"),
    ("Jij leest na en bewerkt",
     "<p>Je past de tekst zelf aan of geeft een opdracht. Elke versie blijft bewaard en is terug te zetten.</p>"),
    ("Eindcontrole, als jij erom vraagt",
     "<p>Op jouw verzoek legt een controle het rapport tegen de wet en de rekenwaarden. Je krijgt meldingen met een "
     "voorstel, en je ziet wat wel en niet is getoetst. Jij handelt elke melding af.</p>"
     '<p class="opm"><a class="pijl" href="{R}herkomst-en-controle/">Hoe herkomst en controle werken</a></p>'),
], prefix="B"), " grijs") + sectie("C", "Jouw rol", "blijft", "Het vakinhoudelijke oordeel blijft van jou",
    """<p class="tekst">Het systeem doet het lees-, zoek- en schrijfwerk en legt vast waar alles vandaan komt.
      Tijdens het werk kun je het ook iets vragen: hoe deden eerdere rapporten dit, wat zegt de wet hierover. Het
      antwoord komt met bronnen, en wat je overneemt blijft een voorstel tot jij het bevestigt.</p>""") + oproep())

# ------------------------------------------------------------------ herkomst en controle
pagina("herkomst-en-controle", "Herkomst en controle",
       "Bij elk stuk tekst zie je waar het op rust: jullie sjabloon, een citaat uit een projectstuk, een "
       "wetsartikel of jouw eigen antwoord. Controles kijken citaten, getallen en regelgeving na.",
       f"""
<section class="held held-smal">
  <div class="kader">
    <p class="boven">Herkomst en controle</p>
    <h1>Van elk stuk tekst is te volgen waar het op rust.</h1>
    <p class="intro">Een rapport waar je naam onder staat, moet je kunnen uitleggen. Daarom is het van begin tot
    eind te volgen: van de tekst in het rapport terug naar het antwoord, en van het antwoord terug naar de
    bron.</p>
  </div>
</section>
""" + sectie("01", "Voorbeeld", "volgen", "Eén zin uit een rapport, met drie herkomsten",
             scene("breed")) + film("film-alinea", "Wat er achter één alinea zit", "", "alinea",
                                    "Animatie: wat er achter één alinea zit") + sectie("02", "Herkomst", "bronnen", "Vier soorten tekst, elk met een eigen herkomst", tabel([
    ("Vaste tekst", "Komt uit het sjabloon. Bij elk stuk staat uit welke van jullie rapporten het komt."),
    ("Gegevens van het project",
     "Komen uit de stukken die jij aanlevert, met bron en citaat, of van jou zelf. Nooit uit een ander rapport en "
     "nooit uit de wet."),
    ("Geschreven passages",
     "Worden geschreven uit jouw antwoorden. Bij elke passage zie je welke antwoorden erin zitten. Eerdere "
     "rapporten, uit jullie archief en uit de openbare verzameling, bepalen alleen de vorm. De feiten komen uit jouw antwoorden."),
    ("Wet- en regelgeving",
     "De geldende tekst, zoals de Omgevingswet, het Bkl en het Bbl, met de toelichting erbij."),
]), " grijs") + sectie("03", "Controle", "controle", "Zes punten die worden nagekeken", """<ol class="vragen">
        <li>Staat elk citaat letterlijk in de bron?</li>
        <li>Staat elk getal in het antwoord ook in de bron?</li>
        <li>Draagt de bron het voorgestelde antwoord helemaal, deels of niet?</li>
        <li>Staat er in een geschreven passage iets wat jij niet hebt geantwoord, of ontbreekt er iets?</li>
        <li>Kies je een antwoord dat in geen van jullie eerdere rapporten voorkwam? Dan staat erbij dat dit niet is
        getest, tot jij akkoord geeft.</li>
        <li>Klopt het rapport met de wet en met de rekenwaarden? Dat doet de eindcontrole.</li>
      </ol>
      <p class="nadruk">De eindcontrole kijkt als tweede beoordelaar mee, maar garandeert niets. Hij laat zien wat hij heeft
      getoetst. Wat niet is beoordeeld, telt niet als akkoord.</p>""") + sectie(
    "04", "Vastleggen", "afwegingen", "Elke keuze is zichtbaar en alles blijft bewaard", """<div class="twee">
        <p class="tekst">Bij twijfel krijg jij een vraag. Wat het systeem niet kan vinden,
        blijft open, met de reden erbij. Jouw besluiten worden vastgelegd, met wie en wanneer.</p>
        <p class="tekst">Alles wat het systeem heeft gedaan, blijft bewaard: wat het las, wat het voorstelde en wat
        jij ermee deed. Zo kun je later nagaan waarom er staat wat er staat.</p>
      </div>""", " grijs") + oproep())

# ------------------------------------------------------------------ voor wie
pagina("voor-wie", "Voor wie",
       "Voor iedereen die uit onderzoeken en documenten een rapport maakt. Het verst zijn we met akoestisch "
       "onderzoek; voor stikstof en verkeer ligt er een eerste sjabloon.",
       """
<section class="held held-smal">
  <div class="kader">
    <p class="boven">Voor wie</p>
    <h1>Voor bureaus die hun rapporten opbouwen uit onderzoeken en documenten.</h1>
    <p class="intro">Het vakgebied maakt weinig uit. Het werkt als jullie rapporten een herkenbare opbouw hebben en de
    inhoud uit andere stukken komt.</p>
  </div>
</section>
""" + sectie("01", "Toets", "past", "Vier kenmerken van een bureau waar het past", """<ul class="vinken">
        <li>Jullie schrijven regelmatig rapporten van dezelfde soort.</li>
        <li>Er is een reeks bestaande rapporten waar de vaste manier van opbouwen in terug te zien is. Een sjabloon
        in Word hoeft er niet te zijn.</li>
        <li>De inhoud komt uit bronnen: onderzoeken, metingen, berekeningen, dossiers, regelgeving.</li>
        <li>Een vakinhoudelijke medewerker tekent voor het resultaat en moet het kunnen onderbouwen.</li>
      </ul>""") + sectie("02", "Vakgebieden", "vakgebieden", "Hoe ver we zijn per vakgebied", """<p class="tekst">We
      zijn begonnen bij onderzoeken voor de leefomgeving. De werkwijze zelf is niet aan één vak gebonden: de vragen,
      de vaste tekst en de regels verschillen per vakgebied, de stappen niet.</p>
      <ul class="drie">
        <li><p class="status s-klaar">Het verst</p><h3>Akoestiek, stikstof en verkeer</h3>
          <p>Akoestisch onderzoek naar wegverkeer. Voor stikstofonderzoek en verkeersonderzoek ligt er een eerste
          sjabloon. Van alle drie hebben we openbare rapporten verzameld en ingedeeld.</p></li>
        <li><p class="status s-bouw">Samen op te bouwen</p><h3>Andere vakken in de leefomgeving</h3>
          <p>Bijvoorbeeld ecologisch onderzoek, bodemonderzoek of luchtkwaliteit. We beginnen dan bij jullie eigen
          rapporten en vullen aan met wat openbaar is.</p></li>
        <li><p class="status s-open">Leg het ons voor</p><h3>Buiten de leefomgeving</h3>
          <p>Maak je op een andere plek rapporten uit onderzoeken en documenten? Leg het ons voor. In de voorzet zie
          je snel of het bij jullie werkt.</p></li>
      </ul>""", " grijs") + sectie("03", "Stand", "stand", "Per vakgebied opgebouwd, samen met het bureau",
    """<p class="tekst">We bouwen dit per vakgebied op, samen met het bureau. Elk sjabloon heeft punten waar jullie
      vakkennis en soms een jurist over beslissen. Die punten leggen we aan jullie voor.</p>""")
  + oproep())

# ------------------------------------------------------------------ voorzet
pagina("voorzet", "Kosteloze voorzet",
       "We maken kosteloos een voorzet voor jullie omgeving, op basis van jullie eigen rapporten, en komen hem "
       "laten zien.",
       f"""
<section class="held held-smal">
  <div class="kader">
    <p class="boven">Kosteloze voorzet</p>
    <h1>Een eerste sjabloon, gemaakt uit jullie eigen rapporten.</h1>
    <p class="intro">Een voorzet is een eerste versie van jullie sjabloon, gemaakt uit een aantal van jullie
    rapporten: de vaste tekst en de vragen die we erin vinden. Je ziet meteen hoe het er voor jullie soort werk
    uitziet. Het kost niets en je zit nergens aan vast.</p>
    <div class="acties">
      <a class="knop" href="{MAILTO}">Mail ons voor een voorzet</a>
      <a class="pijl" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</section>
""" + sectie("01", "Verloop", "gaat", "Van jouw bericht tot de presentatie", stappen([
    ("Je stuurt ons een bericht",
     "<p>Vertel kort wat voor rapporten jullie maken. We nemen contact op om af te spreken welke rapporten we mogen "
     "gebruiken.</p>"),
    ("Wij maken de voorzet",
     "<p>Uit jullie rapporten, aangevuld met openbare rapporten of met wat we voor jullie vakgebied al hebben.</p>"),
    ("We komen hem laten zien",
     "<p>Je ziet de vragen, de vaste tekst en per vraag hoe jullie eigen rapporten hem beantwoordden. Daarna beslis "
     "je zelf of je verder wilt.</p>"),
]), " grijs") + sectie("02", "Al contact", "gebeld", "Heb je ons al aan de lijn gehad?", f"""<p class="tekst">Dan
      weet degene die je belde of mailde al waar het over gaat. Antwoord op dat bericht, of mail naar
      <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      <div class="acties"><a class="knop" href="{MAILTO}">Mail ons voor een voorzet</a></div>"""))

# ------------------------------------------------------------------ over ons
# Voorzet (12-11-2026). Kenmerken en foto's uit website-transformatie (src/content/over-ons.ts, public/team/);
# de aanpak is hier die van Regelrapport.
def persoon(naam):
    return (f'<li><img src="{{R}}team/{naam.lower()}.jpg" alt="" width="400" height="400" loading="lazy">'
            f'<span>{naam}</span></li>')


pagina("over-ons", "Over ons",
       "Regelrapport is een product van Morphy, een techbedrijf uit 2024. Wij bouwen met AI en werken samen met "
       "de ingenieurs die het vak kennen.",
       """
<section class="held held-smal">
  <div class="kader">
    <p class="boven">Over ons</p>
    <h1>Wij zijn de AI-bouwers. De vakkennis komt van de ingenieurs.</h1>
    <p class="intro">Op dit moment onderzoeken we de ingenieurswereld, en daarbinnen één ding: rapporten maken uit
    onderzoeken en documenten. Dat doen we samen met de mensen die die rapporten schrijven. Zij weten wat er moet
    staan, wij bouwen de techniek eromheen.</p>
  </div>
</section>
""" + sectie("01", "Team", "team", "Jan, Frans en Huub", '<ul class="team">\n        '
             + "\n        ".join(persoon(n) for n in ("Jan", "Frans", "Huub")) + "\n      </ul>")
  + sectie("02", "Morphy", "morphy", "Regelrapport is een product van Morphy",
    """<p class="tekst">Morphy is een techbedrijf dat bedrijven transformeert voor AI. Regelrapport is het product
      dat we voor de ingenieurswereld bouwen.</p>
      <dl class="kenmerken">
        <div><dt>Opgericht</dt><dd>2024</dd></div>
        <div><dt>Type</dt><dd>Techbedrijf</dd></div>
        <div><dt>Focus</dt><dd>AI-transformatie</dd></div>
        <div><dt>Aanpak</dt><dd>Per vakgebied, samen met het bureau</dd></div>
      </dl>
      <p class="verder"><a class="pijl" href="https://www.morphy.world">www.morphy.world</a></p>""", " grijs")
  + oproep())

