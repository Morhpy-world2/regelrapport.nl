"""Bouwt deze variant van regelrapport.nl: `python3 bouw.py` (in deze map).

Zelfde opzet als de bouw.py in de repo-root: de tekst van elke pagina staat hieronder; kop, menu en voet staan
één keer in `pagina()`. Alle links zijn relatief, zodat de site in een submap en in de root werkt.
Verhuist de inhoud van deze map naar de root, zet SCHEMA dan op "schema/".
"""
from pathlib import Path

HIER = Path(__file__).parent
NAAM = "Regelrapport"
EMAIL = "info@morphy.world"
ONDERWERP = "Kosteloze%20voorzet%20Regelrapport"
MAILTO = f"mailto:{EMAIL}?subject={ONDERWERP}"
SCHEMA = "../../schema/"  # vanaf de home van deze map

MENU = [
    ("hoe-het-werkt/", "Hoe het werkt"),
    ("herkomst-en-controle/", "Herkomst en controle"),
    ("voor-wie/", "Voor wie"),
]

MERK = ('<svg class="merk" viewBox="0 0 28 28" aria-hidden="true"><path d="M3 6h15M3 14h15M3 22h9" stroke="#15181d" '
        'stroke-width="3"/><rect x="21" y="3.5" width="5" height="5" fill="#b83a16"/><rect x="21" y="11.5" width="5" '
        'height="5" fill="#b83a16"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 28 28'%3E%3Cpath d='M3 6h15M3 14h15"
           "M3 22h9' stroke='%2315181d' stroke-width='3'/%3E%3Crect x='21' y='3.5' width='5' height='5' fill='%23b83a16'/%3E"
           "%3Crect x='21' y='11.5' width='5' height='5' fill='%23b83a16'/%3E%3C/svg%3E")


def pagina(pad, titel, omschrijving, inhoud):
    """pad: "" voor de home, anders "map/". In de inhoud staat {P} voor het pad terug naar de home."""
    p = "" if pad == "" else "../"
    thuis = "./" if pad == "" else "../"
    hier = ' aria-current="page"'
    menu = "".join(f'<li><a href="{p}{h}"{hier if h == pad else ""}>{t}</a></li>' for h, t in MENU)
    hier_naam = hier if pad == "" else ""
    hier_knop = hier if pad == "voorzet/" else ""
    kop = titel if pad == "" else f"{titel} · {NAAM}"
    inhoud = inhoud.replace("{P}", p).replace("{SCHEMA}", p + SCHEMA).strip()
    html = f"""<!doctype html>
<!-- Gemaakt door bouw.py in deze map. Pas de tekst daar aan en draai `python3 bouw.py`. -->
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{kop}</title>
<meta name="description" content="{omschrijving}">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="{p}stijl.css">
</head>
<body>
<a class="spring" href="#inhoud">Naar de inhoud</a>
<header class="kop"><div class="breed kop-in">
  <a class="naam" href="{thuis}"{hier_naam}>{MERK}{NAAM}</a>
  <nav aria-label="Hoofdmenu"><ul class="menu">{menu}
    <li class="menu-knop"><a class="knop klein" href="{p}voorzet/"{hier_knop}>Kosteloze voorzet</a></li></ul></nav>
</div></header>
<main id="inhoud">
{inhoud}
</main>
<footer class="voet"><div class="breed voet-in">
  <p>{NAAM} is van Morphy B.V. · KVK 95783652</p>
  <ul>
    <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
    <li><a href="{p}{SCHEMA}">Het schema</a></li>
    <li><a href="https://www.morphy.world">www.morphy.world</a></li>
  </ul>
</div></footer>
</body>
</html>
"""
    doel = HIER / pad / "index.html"
    doel.parent.mkdir(parents=True, exist_ok=True)
    doel.write_text(html, encoding="utf-8")
    print("geschreven:", doel.relative_to(HIER))


def sectie(nr, kop, inhoud, anker):
    """Een genummerde sectie: links nummer en kop, rechts de inhoud."""
    return f"""
<section class="sectie" aria-labelledby="{anker}"><div class="breed sectie-in">
  <div class="sectie-kop"><span class="nr" aria-hidden="true">{nr}</span><h2 id="{anker}">{kop}</h2></div>
  <div class="sectie-inhoud">
{inhoud.strip()}
  </div>
</div></section>
"""


# De inhoud volgt de bouw.py in de repo-root (stand 12-11-2026): een sjabloon is vaste tekst plus vragen, afgeleid
# uit rapporten; per rapport een voorzet met bron en citaat, die de ingenieur bevestigt. Beweer hier niets wat daar
# niet staat. Tijdwinst mag genoemd worden, zonder cijfers. Geen klantnamen, geen garanties, geen "elke regel heeft
# een bron".

OPROEP = """
<section class="oproep" aria-labelledby="voorzet"><div class="breed oproep-in">
  <div>
    <h2 id="voorzet">Een voorzet voor jullie omgeving</h2>
    <p>We maken kosteloos een voorzet, op basis van een aantal van jullie eigen rapporten. Daarna komen we hem
    graag laten zien.</p>
  </div>
  <a class="knop" href="{P}voorzet/">Kosteloze voorzet aanvragen</a>
</div></section>
"""

# ---------------------------------------------------------------- home
pagina("", "Regelrapport: van onderzoeken en documenten naar een rapport",
       "Regelrapport zet uit jullie onderzoeken en documenten een rapport op, volgens een sjabloon dat uit jullie "
       "eigen rapporten komt. Bij elk stuk tekst zie je waar het op rust.",
       f"""
<section class="opening"><div class="breed opening-in">
  <div>
    <p class="boven">Rapporten uit onderzoeken, berekeningen en documenten</p>
    <h1>{NAAM} zet je rapport op. Bij elk stuk tekst zie je waar het op rust.</h1>
    <p class="intro">Je verzamelt onderzoeken, berekeningen en documenten en schrijft daar een rapport van.
    {NAAM} zet dat rapport voor je op, volgens een sjabloon dat uit jullie eigen rapporten komt. Jij bevestigt en
    beslist.</p>
    <div class="acties">
      <a class="knop" href="{{P}}voorzet/">Kosteloze voorzet aanvragen</a>
      <a class="link" href="{{P}}hoe-het-werkt/">De werkwijze in stappen</a>
    </div>
  </div>
  <figure class="stroom">
    <figcaption>Van stukken naar rapport</figcaption>
    <ol>
      <li><span class="etiket">Jouw stukken</span>
        <ul class="stukken"><li>Onderzoeken</li><li>Berekeningen</li><li>Documenten</li></ul></li>
      <li><span class="etiket">{NAAM}</span>
        <p>Zet het rapport op volgens een sjabloon uit jullie eigen rapporten.</p></li>
      <li><span class="etiket">Het rapport</span>
        <p>Bij elk stuk tekst zie je waar het op rust.</p>
        <div class="regels" aria-hidden="true">
          <div><span><i style="width:100%"></i><i style="width:72%"></i></span><b>rust op</b></div>
          <div><span><i style="width:92%"></i><i style="width:100%"></i><i style="width:48%"></i></span><b>rust op</b></div>
        </div></li>
      <li><span class="etiket">Jij</span>
        <p>Bevestigt en beslist.</p></li>
    </ol>
  </figure>
</div></section>
""" + sectie("01", f"{NAAM} in het kort", """
    <ol class="punten">
      <li><h3>Het sjabloon komt uit jullie rapporten</h3>
        <p>We leggen een reeks van jullie rapporten naast elkaar. Wat steeds terugkomt, wordt de vaste tekst. Wat
        per project verschilt, wordt een vraag.</p></li>
      <li><h3>Elk rapport start bij de vragen</h3>
        <p>Per project beantwoord je de vragen van het sjabloon. Je antwoorden bepalen welke stukken in het
        rapport komen en wat erin staat.</p></li>
      <li><h3>Per vraag een voorstel, met bron en citaat</h3>
        <p>Het systeem leest de stukken van het project en stelt per vraag een antwoord voor, met de bron en het
        letterlijke citaat erbij. Jij bevestigt of past aan.</p></li>
      <li><h3>Vergelijkbare rapporten worden erbij gezocht</h3>
        <p>Het systeem zoekt rapporten over een situatie die op de jouwe lijkt: in jullie eigen archief en in de
        openbare rapporten die wij hebben verzameld.</p></li>
      <li><h3>Citaat, getal en regel worden nagekeken</h3>
        <p>Staat het citaat echt in de bron? Staan de getallen er ook? Zegt de tekst niets wat jij niet hebt
        geantwoord? Een eindcontrole legt het rapport tegen de wet en de rekenwaarden.</p></li>
      <li><h3>Zonder jouw bevestiging is niets definitief</h3>
        <p>Het systeem doet voorstellen. Er komt niets definitief in het rapport zonder dat jij het hebt
        bevestigd, en elke vorige versie blijft bewaard.</p></li>
    </ol>
""", "kort") + sectie("02", "Wat je eraan hebt", """
    <ol class="punten">
      <li><h3>Een rapport kost je minder tijd</h3>
        <p>Overtypen, nalopen en zoeken hoe je het de vorige keer deed, neemt het systeem over. Jouw tijd gaat
        naar het vakinhoudelijke oordeel.</p></li>
      <li><h3>Elk rapport komt op dezelfde manier tot stand</h3>
        <p>Dezelfde opbouw, dezelfde formuleringen en dezelfde vragen, wie het rapport ook maakt.</p></li>
      <li><h3>Je kunt het rapport uitleggen</h3>
        <p>Bij elk stuk tekst zie je waar het op rust. Dat scheelt bij de interne controle en bij vragen van de
        opdrachtgever of het bevoegd gezag.</p></li>
    </ol>
""", "oplevert") + sectie("03", "Het werk waar dit voor bedoeld is", """
    <ul class="streep">
      <li>Je schrijft steeds hetzelfde soort rapport, maar elk project is net anders.</li>
      <li>De inhoud komt uit losse stukken: onderzoeken, berekeningen, tekeningen, de offerte, mails van de
      opdrachtgever.</li>
      <li>Veel tijd gaat naar overtypen, nalopen en zoeken hoe je het de vorige keer deed.</li>
      <li>Je moet achteraf kunnen uitleggen waarom er staat wat er staat.</li>
    </ul>
    <p class="na"><a class="link" href="{P}voor-wie/">Kijk of het bij jullie past</a></p>
    <div class="kader">
      <div>
        <h3>Het geheel in één animatie</h3>
        <p>Drie onderzoeken, de documentgenerator en het rapport dat eruit komt.</p>
      </div>
      <a class="knop rand" href="{SCHEMA}">Open het schema</a>
    </div>
""", "werk") + sectie("04", "Er ligt al een verzameling openbare rapporten", """
    <p class="alinea">Wij hebben openbare rapporten verzameld en ingedeeld. Het systeem zoekt daarin naar
    situaties die op jouw project lijken, en we hebben er al eerste sjablonen uit afgeleid. Zo kunnen we voor
    jullie vakgebied snel een voorzet maken. Zit jouw vakgebied er nog niet bij, dan bouwen we die verzameling
    op.</p>
    <dl class="cijfers">
      <div><dt>akoestische rapporten</dt><dd>ruim 1.200</dd></div>
      <div><dt>stukken over stikstof</dt><dd>ruim 1.600</dd></div>
      <div><dt>verkeersonderzoeken</dt><dd>ruim 1.100</dd></div>
    </dl>
    <p class="noot">Openbare stukken onder de Omgevingswet, stand november 2026.</p>
""", "verzameling") + OPROEP)

# ---------------------------------------------------------------- hoe het werkt
pagina("hoe-het-werkt/", "Hoe het werkt",
       "Eerst een sjabloon uit jullie eigen rapporten: vaste tekst en vragen. Daarna per rapport: stukken "
       "aanleveren, vragen bevestigen, tekst nalezen en een eindcontrole.",
       """
<section class="opening"><div class="breed">
  <p class="boven">Werkwijze</p>
  <h1>Eén keer het sjabloon vastleggen. Daarna dezelfde stappen voor elk rapport.</h1>
  <p class="intro">Een sjabloon bestaat bij ons uit twee delen: de vaste tekst van jullie rapporten, en de vragen
  die bepalen wat er in een rapport komt. Dat leggen we één keer goed vast. Daarna doorloopt elk nieuw rapport
  dezelfde stappen, en kost een rapport je minder tijd.</p>
  <div class="acties"><a class="knop rand" href="{SCHEMA}">Open het schema als animatie</a></div>
</div></section>
""" + sectie("A", "Het sjabloon, één keer", """
    <ol class="stappen fase-a">
      <li><h3>Jullie rapporten gaan naast elkaar</h3>
        <p>Jullie leveren een reeks bestaande rapporten van één soort aan. We zoeken eerst welke tekst letterlijk
        terugkomt, en in welke situatie. Dat wordt de vaste tekst, met bij elk stuk de rapporten waar het uit
        komt.</p></li>
      <li><h3>Verschillen worden vragen</h3>
        <p>Staat een stuk niet in elk rapport, dan zoeken we de projectsituatie die dat verklaart. Daar komt een
        vraag uit, zoals je die als vakmens zou stellen: gaat het om nieuwbouw, wordt er gesloopt, welke bronnen
        spelen mee. Per vraag zie je hoe jullie eerdere rapporten hem beantwoordden.</p>
        <p class="bij">Drie AI-modellen doen dit los van elkaar en moeten het daarna eens worden.</p></li>
      <li><h3>Uitspraken over de wet gaan naast de geldende tekst</h3>
        <p>Elke bewering over regelgeving in het sjabloon wordt naast de tekst gelegd die nu geldt, met het
        citaat erbij. In onze proeven kwamen zo verwijzingen boven naar regels die inmiddels zijn gewijzigd.</p></li>
      <li><h3>De open punten zijn aan jullie</h3>
        <p>Waar de rapporten elkaar tegenspreken of de wet iets anders zegt, komt een beslispunt met de keuzes
        erbij. Jullie vakkennis bepaalt wat het sjabloon wordt.</p></li>
    </ol>
""", "sjabloon") + sectie("B", "Elk nieuw rapport", """
    <ol class="stappen fase-b">
      <li><h3>Jij levert de projectstukken</h3>
        <p>De offerte, de rekenresultaten en de andere stukken waar het rapport op rust. Wat jij zelf weet, voeg
        je toe: jij bent ook een bron.</p></li>
      <li><h3>Vergelijkbare rapporten worden erbij gezocht</h3>
        <p>Het systeem zoekt rapporten over een vergelijkbare situatie, in jullie eigen archief en in de openbare
        rapporten die wij hebben verzameld. Je ziet waarin ze op jouw project lijken en waarin ze verschillen, en
        jij kiest welk rapport als voorbeeld dient.</p></li>
      <li><h3>Per vraag komt er een voorstel</h3>
        <p>Het systeem leest de stukken en stelt per vraag een antwoord voor, met de bron en het letterlijke
        citaat. Staat het citaat niet in de bron, of klopt een getal niet, dan vervalt het voorstel en blijft de
        vraag open voor jou.</p></li>
      <li><h3>Jij bevestigt het voorstel of past het aan</h3>
        <p>Een voorstel blijft geel tot jij het bevestigt. Na elk antwoord zie je welke stukken er in het rapport
        bij komen of wegvallen. Wat uit de regels te berekenen is, zoals een toets aan een grenswaarde, rekent
        het systeem uit met het wetsartikel erbij.</p></li>
      <li><h3>De tekst wordt ingevuld en geschreven</h3>
        <p>De vaste tekst wordt ingevuld met jouw antwoorden. Alleen de beschrijvende delen worden geschreven, en
        alleen uit wat jij hebt geantwoord. Een tweede lezer kijkt of er niets is bijverzonnen.</p></li>
      <li><h3>Jij leest na en bewerkt</h3>
        <p>Je past de tekst zelf aan of geeft een opdracht. Elke versie blijft bewaard en is terug te zetten.</p></li>
      <li><h3>Eindcontrole, als jij erom vraagt</h3>
        <p>Op jouw verzoek legt een controle het rapport tegen de wet en de rekenwaarden. Je krijgt meldingen met
        een voorstel, en je ziet wat wel en niet is getoetst. Jij handelt elke melding af.</p>
        <p class="bij"><a class="link" href="{P}herkomst-en-controle/">Lees verder over herkomst en controle</a></p></li>
    </ol>
""", "rapport") + sectie("C", "Het vakinhoudelijke oordeel houd jij", """
    <p class="alinea">Het systeem doet het lees-, zoek- en schrijfwerk en legt vast waar alles vandaan komt.</p>
    <p class="alinea">Tijdens het werk kun je het ook iets vragen: hoe deden eerdere rapporten dit, wat zegt de wet
    hierover. Het antwoord komt met bronnen, en wat je overneemt blijft een voorstel tot jij het bevestigt.</p>
""", "oordeel") + OPROEP)

# ---------------------------------------------------------------- herkomst en controle
pagina("herkomst-en-controle/", "Herkomst en controle",
       "Bij elk stuk tekst zie je waar het op rust: jullie sjabloon, een citaat uit een projectstuk, een "
       "wetsartikel of jouw eigen antwoord. Controles kijken citaten, getallen en regelgeving na.",
       """
<section class="opening"><div class="breed">
  <p class="boven">Bronnen en nakijken</p>
  <h1>Van elk stuk tekst terug naar het antwoord, en van het antwoord naar de bron.</h1>
  <p class="intro">Een rapport waar je naam onder staat, moet je kunnen uitleggen. Daarom zie je bij elk stuk
  tekst waar het op rust, en is het rapport van begin tot eind te volgen.</p>
</div></section>
""" + sectie("01", "Voorbeeld: één regel, drie bronnen", """
    <figure class="spoor">
      <p class="zin">Op de gevel aan de <mark class="m1">Beukenlaan<sup>1</sup></mark> is de geluidbelasting
      <mark class="m2">54 dB<sup>2</sup></mark>, en daarmee
      <mark class="m3">hoger dan de standaardwaarde<sup>3</sup></mark>.</p>
      <table>
        <thead><tr><th scope="col">Nr.</th><th scope="col">Deel van de regel</th><th scope="col">Herkomst</th></tr></thead>
        <tbody>
          <tr><td>1</td><td><span class="m1">Beukenlaan</span></td>
            <td>Uit de offerte, met het letterlijke citaat. Door jou bevestigd.</td></tr>
          <tr><td>2</td><td><span class="m2">54 dB</span></td>
            <td>Uit de rekenresultaten, met de plek in het bestand.</td></tr>
          <tr><td>3</td><td><span class="m3">hoger dan de standaardwaarde</span></td>
            <td>Uitgerekend volgens de regel, met het wetsartikel erbij.</td></tr>
        </tbody>
      </table>
      <figcaption>Verzonnen voorbeeld, om te laten zien hoe het werkt.</figcaption>
    </figure>
""", "voorbeeld") + sectie("02", "Vier soorten tekst en waar ze op rusten", """
    <ol class="punten">
      <li><h3>Vaste tekst uit het sjabloon</h3>
        <p>Komt uit het sjabloon. Bij elk stuk staat uit welke van jullie rapporten het komt.</p></li>
      <li><h3>Projectgegevens</h3>
        <p>Komen uit de stukken die jij aanlevert, met bron en citaat, of van jou zelf. Nooit uit een ander
        rapport en nooit uit de wet.</p></li>
      <li><h3>Passages die geschreven worden</h3>
        <p>Worden geschreven uit jouw antwoorden. Bij elke passage zie je welke antwoorden erin zitten. Eerdere
        rapporten, uit jullie archief en uit de openbare verzameling, geven de vorm, niet de feiten.</p></li>
      <li><h3>Geldende wet- en regelgeving</h3>
        <p>De geldende tekst, zoals de Omgevingswet, het Bkl en het Bbl, met de toelichting erbij.</p></li>
    </ol>
""", "bronnen") + sectie("03", "Dit lopen de controles na", """
    <ul class="streep vragen">
      <li>Staat elk citaat letterlijk in de bron?</li>
      <li>Staat elk getal in het antwoord ook in de bron?</li>
      <li>Draagt de bron het voorgestelde antwoord helemaal, deels of niet?</li>
      <li>Staat er in een geschreven passage iets wat jij niet hebt geantwoord, of ontbreekt er iets?</li>
      <li>Kies je een antwoord dat in geen van jullie eerdere rapporten voorkwam? Dan staat erbij dat dit niet is
      getest, tot jij akkoord geeft.</li>
      <li>Klopt het rapport met de wet en met de rekenwaarden? Dat doet de eindcontrole.</li>
    </ul>
    <p class="nadruk">De eindcontrole is een tweede beoordelaar, geen garantie. Hij laat zien wat hij heeft
    getoetst. Wat niet is beoordeeld, telt niet als akkoord.</p>
""", "controles") + sectie("04", "Geen stille keuzes, en alles blijft bewaard", """
    <p class="alinea">Twijfel wordt een vraag aan jou, geen stille keuze. Wat het systeem niet kan vinden, blijft
    open, met de reden erbij. Jouw besluiten worden vastgelegd, met wie en wanneer.</p>
    <p class="alinea">Alles wat het systeem heeft gedaan, blijft bewaard: wat het las, wat het voorstelde en wat
    jij ermee deed. Zo kun je later nagaan waarom er staat wat er staat.</p>
""", "keuzes") + OPROEP)

# ---------------------------------------------------------------- voor wie
pagina("voor-wie/", "Voor wie",
       "Voor iedereen die uit onderzoeken en documenten een rapport maakt. Het verst zijn we met akoestisch "
       "onderzoek; voor stikstof en verkeer ligt er een eerste sjabloon.",
       """
<section class="opening"><div class="breed">
  <p class="boven">Past het bij jullie</p>
  <h1>Voor rapporten met een herkenbare opbouw en inhoud uit andere stukken.</h1>
  <p class="intro">Het is voor wie uit onderzoeken en documenten een rapport maakt. Het vakgebied maakt weinig
  uit. Het werkt als jullie rapporten een herkenbare opbouw hebben en de inhoud uit andere stukken komt.</p>
</div></section>
""" + sectie("01", "Wanneer het past", """
    <ul class="streep">
      <li>Jullie schrijven regelmatig rapporten van dezelfde soort.</li>
      <li>Er is een reeks bestaande rapporten waar de vaste manier van opbouwen in terug te zien is. Een sjabloon
      in Word hoeft er niet te zijn.</li>
      <li>De inhoud komt uit bronnen: onderzoeken, metingen, berekeningen, dossiers, regelgeving.</li>
      <li>Een vakinhoudelijke medewerker tekent voor het resultaat en moet het kunnen onderbouwen.</li>
    </ul>
""", "past") + sectie("02", "Per vakgebied", """
    <p class="alinea">We zijn begonnen bij onderzoeken voor de leefomgeving. De werkwijze zelf is niet aan één vak
    gebonden: de vragen, de vaste tekst en de regels verschillen per vakgebied, de stappen niet.</p>
    <ul class="vakken">
      <li><span class="etiket">Hier zijn we het verst</span>
        <h3>Akoestisch onderzoek naar wegverkeer</h3>
        <p>Voor stikstofonderzoek en verkeersonderzoek ligt er een eerste sjabloon. Van alle drie hebben we
        openbare rapporten verzameld en ingedeeld.</p></li>
      <li><span class="etiket">Bouwen we met jullie op</span>
        <h3>Andere onderzoeken voor de leefomgeving</h3>
        <p>Bijvoorbeeld ecologisch onderzoek, bodemonderzoek of luchtkwaliteit. We beginnen dan bij jullie eigen
        rapporten en vullen aan met wat openbaar is.</p></li>
      <li><span class="etiket">Buiten de leefomgeving</span>
        <h3>Een ander soort rapport</h3>
        <p>Maak je op een andere plek rapporten uit onderzoeken en documenten? Leg het ons voor. In de voorzet zie
        je snel of het bij jullie werkt.</p></li>
    </ul>
""", "vakgebieden") + sectie("03", "Hoe ver we nu zijn", """
    <p class="alinea">We bouwen dit per vakgebied op, samen met het bureau. Elk sjabloon heeft punten waar jullie
    vakkennis en soms een jurist over beslissen. Die punten laten we zien; we lossen ze niet stil op.</p>
""", "stand") + OPROEP)

# ---------------------------------------------------------------- voorzet
pagina("voorzet/", "Kosteloze voorzet",
       "We maken kosteloos een voorzet voor jullie omgeving, op basis van jullie eigen rapporten, en komen hem "
       "laten zien.",
       f"""
<section class="opening"><div class="breed">
  <p class="boven">Kosteloos, je zit nergens aan vast</p>
  <h1>Een eerste versie van jullie sjabloon, gemaakt uit jullie eigen rapporten.</h1>
  <p class="intro">Dat is de voorzet: de vaste tekst en de vragen die we in een aantal van jullie rapporten
  vinden. Je ziet meteen hoe het er voor jullie soort werk uitziet. Het kost niets en je zit nergens aan vast.</p>
  <div class="acties">
    <a class="knop" href="{MAILTO}">Mail ons over een voorzet</a>
    <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>
  </div>
</div></section>
""" + sectie("01", "Wat er na je mail gebeurt", """
    <ol class="stappen">
      <li><h3>Jij mailt wat jullie maken</h3>
        <p>Vertel kort wat voor rapporten jullie maken. We nemen contact op om af te spreken welke rapporten we
        mogen gebruiken.</p></li>
      <li><h3>Wij stellen de voorzet op</h3>
        <p>Uit jullie rapporten, aangevuld met openbare rapporten of met wat we voor jullie vakgebied al
        hebben.</p></li>
      <li><h3>Je krijgt hem te zien</h3>
        <p>We komen hem laten zien: de vragen, de vaste tekst en per vraag hoe jullie eigen rapporten hem
        beantwoordden. Daarna beslis je zelf of je verder wilt.</p></li>
    </ol>
""", "verloop") + sectie("02", "Al door ons gebeld of gemaild?", f"""
    <p class="alinea">Dan weet degene die je belde of mailde al waar het over gaat. Antwoord op dat bericht, of
    mail naar <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
""", "gesproken"))
