/* Regelrapport, variant rapport (ronde twee, B).
   - De kern: per scene worden de bronvellen op de hoogte van hun woord gezet en loopt van elk vel een pijl
     naar zijn markering. De pijl gaat door de witruimte tussen twee regels, nooit door tekst: vanaf het vel
     naar rechts van de zin, dan in het kanaal onder de regel van het woord naar links, en omhoog in de
     markering. Alle bochten delen dezelfde x-verloop, dus pijlen met oplopende begin- en eindhoogte kruisen
     niet. Lukt dat niet (twee woorden op één regel), dan geen pijlen: kleur en nummer leggen het verband.
   - Beweging: de held start na het laden van het font, de scene op herkomst-en-controle als hij in beeld
     komt. Secties komen één keer zacht in beeld, de cijfers tellen één keer op. Daarna staat alles stil.
   - prefers-reduced-motion: alles direct in de eindtoestand. */
(function () {
  "use strict";
  var d = document;
  var stil = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var NS = "http://www.w3.org/2000/svg";
  var scenes = [].slice.call(d.querySelectorAll(".scene"));

  function r1(v) { return Math.round(v * 10) / 10; }
  function maak(svg, naam, attrs) {
    var el = d.createElementNS(NS, naam);
    for (var k in attrs) el.setAttribute(k, attrs[k]);
    svg.appendChild(el);
    return el;
  }

  function leg(scene) {
    var raster = scene.querySelector(".scene-raster");
    var svg = scene.querySelector(".pijlen");
    var zin = scene.querySelector(".fragment-zin");
    var kolom = scene.querySelector(".bronvellen");
    if (!raster || !svg || !zin || !kolom) return;
    var vellen = [].slice.call(kolom.children);
    vellen.forEach(function (v) { v.style.marginTop = ""; });
    while (svg.firstChild) svg.removeChild(svg.firstChild);

    var R = raster.getBoundingClientRect();
    var Z = zin.getBoundingClientRect();
    var K = kolom.getBoundingClientRect();
    if (K.left < Z.right + 16) { scene.classList.remove("zonder-pijlen"); return; }   /* smal: vellen eronder */

    var lh = parseFloat(getComputedStyle(zin).lineHeight) || 40;
    var doelen = [];
    for (var i = 1; i <= 3; i++) {
      var m = zin.querySelector(".m" + i);
      if (!m) return;
      var rects = m.getClientRects();
      var M = rects[rects.length - 1];
      var onder = M.bottom - R.top;
      doelen.push({
        x: Math.max(M.left + 10, M.right - 16) - R.left,
        y: onder + 1,
        kanaal: onder + Math.max(6, (lh - M.height) / 2)
      });
    }
    for (var j = 1; j < doelen.length; j++) {
      if (doelen[j].kanaal - doelen[j - 1].kanaal < lh * 0.6) { scene.classList.add("zonder-pijlen"); return; }
    }
    scene.classList.remove("zonder-pijlen");

    /* vellen op de hoogte van hun woord, waar dat past (offsetTop negeert de lichte draaiing) */
    var ankers = [];
    vellen.forEach(function (v, n) {
      var regels = v.querySelector(".vel-regels");
      var binnen = regels.offsetTop + regels.offsetHeight / 2;
      var gewenst = doelen[n].kanaal - binnen;
      var extra = Math.max(0, Math.round(gewenst - v.offsetTop));
      if (extra) v.style.marginTop = extra + "px";
      ankers.push(v.offsetTop + binnen);
    });

    var R2 = raster.getBoundingClientRect();
    var Z2 = zin.getBoundingClientRect();
    var sx = kolom.getBoundingClientRect().left - R2.left - 4;
    var ex = Z2.right - R2.left + 8;
    var k = (sx - ex) * 0.5;
    svg.setAttribute("viewBox", "0 0 " + r1(R2.width) + " " + r1(R2.height));

    doelen.forEach(function (t, n) {
      var cls = "p" + (n + 1);
      var sy = ankers[n], ky = t.kanaal;
      var bocht = Math.max(2, Math.min(6, (ky - t.y) * 0.7));
      var dstr = "M" + r1(sx) + " " + r1(sy) +
        " C" + r1(sx - k) + " " + r1(sy) + " " + r1(ex + k) + " " + r1(ky) + " " + r1(ex) + " " + r1(ky) +
        " L" + r1(t.x + bocht) + " " + r1(ky) +
        " Q" + r1(t.x) + " " + r1(ky) + " " + r1(t.x) + " " + r1(ky - bocht) +
        " L" + r1(t.x) + " " + r1(t.y);
      maak(svg, "circle", { cx: r1(sx), cy: r1(sy), r: "2.8", "class": cls });
      maak(svg, "path", { d: dstr, pathLength: "1", "class": cls + " lijn" });
      maak(svg, "path", {
        d: "M" + r1(t.x - 5) + " " + r1(t.y + 6.5) + " L" + r1(t.x) + " " + r1(t.y) + " L" + r1(t.x + 5) + " " + r1(t.y + 6.5),
        "class": cls + " kopje"
      });
    });
  }

  function legAlles() { scenes.forEach(leg); }

  /* ------------------------------------------------ starten */
  function aan(el) { el.classList.add("aan"); }

  var held = d.querySelector(".scene-held");
  var anderen = scenes.filter(function (s) { return s !== held; });

  legAlles();
  var gestart = false;
  function startHeld() {
    if (gestart) return;
    gestart = true;
    legAlles();
    if (held) requestAnimationFrame(function () { requestAnimationFrame(function () { aan(held); }); });
  }
  if (stil) { scenes.forEach(aan); }
  if (d.fonts && d.fonts.ready) d.fonts.ready.then(function () { legAlles(); startHeld(); });
  setTimeout(startHeld, 1200);
  window.addEventListener("load", legAlles);
  var wacht;
  window.addEventListener("resize", function () { clearTimeout(wacht); wacht = setTimeout(legAlles, 100); });

  /* ------------------------------------------------ één keer in beeld */
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, "."); }
  function tel(dd) {
    var m = /^(\D*)([\d.]+)(.*)$/.exec(dd.textContent);
    if (!m) return;
    var doel = parseInt(m[2].replace(/\./g, ""), 10), t0 = null, duur = 1400;
    function stap(t) {
      if (t0 === null) t0 = t;
      var p = Math.min(1, (t - t0) / duur), e = 1 - Math.pow(1 - p, 3);
      dd.textContent = m[1] + fmt(p < 1 ? Math.round(doel * e / 10) * 10 : doel) + m[3];
      if (p < 1) requestAnimationFrame(stap);
    }
    requestAnimationFrame(stap);
  }

  var secties = [].slice.call(d.querySelectorAll(".sectie"));
  var cijfers = [].slice.call(d.querySelectorAll(".cijfers"));
  if (stil || !("IntersectionObserver" in window)) {
    secties.forEach(function (s) { s.classList.add("in"); });
    anderen.forEach(aan);
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      var el = en.target;
      io.unobserve(el);
      if (el.classList.contains("sectie")) el.classList.add("in");
      else if (el.classList.contains("scene")) aan(el);
      else if (el.classList.contains("cijfers")) [].forEach.call(el.querySelectorAll("dd"), tel);
    });
  }, { rootMargin: "0px 0px -10% 0px", threshold: 0.12 });
  secties.forEach(function (s) { io.observe(s); });
  cijfers.forEach(function (c) { io.observe(c); });
  var io2 = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { io2.unobserve(en.target); aan(en.target); }
    });
  }, { threshold: 0.4 });
  anderen.forEach(function (s) { io2.observe(s); });
})();

/* de ingesloten animaties melden hun hoogte */
addEventListener("message", function (e) {
  var h = e.data && e.data.regelrapportHoogte;
  if (!h) return;
  document.querySelectorAll("iframe.film").forEach(function (f) {
    if (f.contentWindow === e.source) { f.style.aspectRatio = "auto"; f.style.height = h + "px"; }
  });
});
