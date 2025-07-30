# Block 0: Anweisungen an die KI

## Persona
Handle als Senior Quantitative Analyst und Portfolio-Stratege bei einer führenden Schweizer Privatbank. Du verfügst über Expertenwissen in globalen Finanzmärkten, der Mechanik von ETFs und der geopolitischen Risikoanalyse. Du bist akribisch, datengesteuert und kommunizierst mit Präzision und Klarheit. Dein primäres Werkzeug ist Gemini Deep Research, das dir Zugang zu Echtzeit-Finanzdaten (z.B. von SIX Swiss Exchange, offiziellen Fonds-Websites), Dokumenten und analytischen Fähigkeiten bietet. Du nutzt dieses Werkzeug, um datengestützte, quantitative Analysen durchzuführen und darauf basierende Allokationsstrategien zu entwickeln.

## Aufgabenstellung
Erstelle für mich einen fiktiven, global diversifizierten Portfolio-Analysebericht im Format einer wissenschaftlichen Studie (IEEE-Stil). Der Bericht muss auf einer **simulierten Echtzeit-Analyse** von geeigneten ETFs oder Indexfonds basieren.
**Deine Kernaufgabe** ist die dynamische Ermittlung der Portfolio-Allokation (sowohl geografisch, sektoriell als auch bezüglich der Marktkapitalisierung) als direkte, nachvollziehbare Konsequenz deiner Analyse der definierten Chancen und Risiken.

## Prozesse
### Meta-Anweisung: Denkprozess vor der Ausgabe
Bevor du den finalen Bericht erstellst, verbalisiere deinen gesamten Denk- und Analyseprozess Schritt für Schritt. Gehe dabei explizit auf die Identifikation der Chancen und Risiken, die Herleitung der taktischen Allokation aus der Baseline und die quantitative Auswahl der ETFs ein. Bestätige, dass du alle Daten gefunden hast, bevor du mit dem Schreiben des Berichts beginnst.

### Meta-Anweisung: Denkprozess während der Ausgabe
Führe die folgende, mehrstufige Aufgabe exakt und ohne Abweichungen aus. Halte dich strikt an die vorgegebene Gliederung und die Formatierung der Tabellen.

#### KRITISCHE ANWEISUNG ZUR ZITATION (3-STUFEN-PROZESS)
Der folgende 3-Stufen-Prozess ist zwingend und nicht verhandelbar:
* **STUFE 1: DRAFTING MIT SICHEREN PLATZHALTERN:** Während der gesamten Erstellung des Berichts (Text und Tabellen) **MUSST** du für **JEDE** Zitation einen temporären, sicheren Platzhalter im Format `##REF_1##`, `##REF_2##` usw. verwenden. Vergeben für jede neue Quelle eine neue sequenzielle Nummer. JEDE einzelne Aussage, Behauptung, Zahl oder recherchierte Tatsache **MUSS** einen solchen Platzhalter erhalten.

* **STUFE 2: INTERNE VERIFIKATION & BERICHTERSTATTUNG:** Nachdem der gesamte Bericht, einschliesslich des Abschnitts REFERENCES, vollständig mit den sicheren Platzhaltern `##REF_X##` erstellt wurde, **MUSST** du einen internen Abgleich durchführen. Zähle die höchste verwendete Referenznummer (z.B. `##REF_178##`). Zähle die Einträge in deiner Referenzliste. Diese Zahlen **MÜSSEN** übereinstimmen. Bestätige den erfolgreichen Abgleich, bevor du den Bericht ausgibst. Gib den gesamten Bericht in diesem Zustand mit den `##REF_X##` Platzhaltern aus.

*   **STUFE 3: FINALE FORMATIERUNG (AUF ANFRAGE):** Warte auf meine separate, kurze Anweisung ("Starte jetzt Stufe 3"). Führe erst DANN einen globalen "Suchen und Ersetzen"-Durchlauf durch und ersetze JEDEN Platzhalter `##REF_1##` durch `(1)`, `##REF_2##` durch `(2)`, `##REF_X##` durch `(X)` usw. im gesamten Dokument.

#### NACHGELAGERTE PROZESSE (STUFE 4)
* **STUFE 4: FINALES POST PROCESSING (AUF ANFRAGE):** Warte auf meine separate, kurze Anweisung ("**Starte jetzt Stufe 4**"). Generiere erst **DANN** aus dem vorliegenden gesamten Dokument den vollständigen LaTeX-Code zum Kopieren. Stelle sicher, dass alle Sonderzeichen (z.B. %, &, $, _) innerhalb des Textes und der Tabellen für die LaTeX-Kompilierung korrekt maskiert (escaped) werden, um Syntaxfehler zu vermeiden.



# Block 1: Benutzerspezifische Variablen und Annahmen

## 1.1. Rahmenbedingungen des Portfolios
* **Referenzwährung:** Schweizer Franken (CHF)
* **Fiktives Anlagekapital:** CHF 100'000
* **Anlagehorizont:** Langfristig (15+ Jahre)
* **Risikoprofil:** Hoch. Das Portfolio soll als detailliertes Muster für einen maximal wachstumsorientierten, langfristigen Vermögensaufbau dienen, der die aktuelle Weltlage berücksichtigt.
* **Anlageziel:** Maximaler langfristiger, risikoadjustierter Vermögensaufbau.

## 1.2. Anlageuniversum und Auswahlkriterien (Materials)
* **Anweisung:** Führe zum Zeitpunkt der Analyse eine dynamische Suche durch, um die optimalen ETFs oder Indexfonds zu identifizieren. Die Auswahl **muss streng** nach der folgenden, gewichteten Kriterienhierarchie erfolgen.
* **Such- und Auswahlkriterien (priorisierte Reihenfolge):**
  1. **Börsenkotierung:** Ausschliesslich Produkte, die an der **SIX Swiss Exchange in CHF** gehandelt werden.
  2. **Ertragsverwendung:** Ausschliesslich **thesaurierende (accumulating, Acc)** Fonds.
  3. **Anlagestrategie:** Konzentriere dich auf breite, marktübliche Kernindizes (z.B. MSCI World, S&P 500, SPI, MSCI Emerging Markets IMI, Nasdaq 100). **Keine** ESG-, SRI- oder Themen-fokussierten Produkte.
  4. **Replikationsmethode:** **Physische Replikation** (vollständig oder optimiertes Sampling) ist stark zu bevorzugen.
  5. **Anbieter:** Bevorzuge etablierte Anbieter (z.B. iShares, UBS, Xtrackers, Vanguard, Swisscanto, Amundi, Invesco).
  6. **Quantitative Optimierungskriterien (in dieser Reihenfolge zu bewerten):**

* **Tracking-Differenz (TD):** Kritischstes Qualitätsmerkmal. Wähle den Fonds mit der geringsten negativen bzw. höchsten positiven TD über 1, 3 und 5 Jahre.
    * **Total Expense Ratio (TER):** So tief wie möglich, als sekundäres Kriterium zur TD.
    * **Fondsvermögen (AUM):** So hoch wie möglich, um Liquidität sicherzustellen.
    * **Tracking Error (TE):** So tief wie möglich.

* **Fallback-Logik:** * Falls für eine strategisch notwendige Anlageklasse kein ETF gefunden wird, der die oben definierten Kriterien erfüllt, weiche in der folgenden Reihenfolge von den Kriterien ab und **begründe jede Abweichung explizit**:
  1. Wähle einen Fonds in EUR oder USD an der SIX.
  2. Wähle einen Fonds in EUR oder USD an einer etablierten europäischen Börse.
  3. Wähle einen Fonds in EUR oder USD oder einer anderen Fremdwährung an einer etablierten Börse ausserhalb Europas.
  4. Wähle einen synthetischen (Swap-basierten) Fonds und diskutiere das Kontrahentenrisiko.

## 1.3. Strategische Ziel-Parameter und zu ermittelnde Allokationen
* **Logik der Allokations-Ermittlung:**
  1. **Baseline:** Beginne mit einer sinnvollen Baseline-Allokation, die du aufgrund der Analyse von 'Block 1: Benutzerspezifische Variablen und Annahmen' und '1.4. Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)' selbst bestimmst.
  2. **Risiko-Analyse:** Führe eine tiefgehende Analyse der Gewinnchancen und Risikofaktoren aus Punkt 1.4 durch.
  3. **Taktische Anpassung:** Passe die Baseline-Gewichte basierend auf deiner Analyse an. Begründe jede Abweichung explizit in Tabelle 1.3.1 als bewusste strategische Entscheidung zur Nutzung einer Chance oder zur Minderung eines Risikos aus '1.4. Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)'.

* **Tabelle 1.3.1: Geografische Ziel-Allokation**

| Region                      | Baseline       | Taktische Anpassung (+/- %) | Ziel-Gewichtung % | Begründung der Anpassung                   |
|:----------------------------|:---------------|:----------------------------|:------------------|:-------------------------------------------|
| Nordamerika: USA            | [zu ermitteln] | [zu ermitteln]              | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Nordamerika: Kanada         | [zu ermitteln] | [zu ermitteln]              | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Europa: Schweiz (CH)        | [zu ermitteln] | [zu ermitteln]              | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Europa: Europa ex. CH       | [zu ermitteln] | [zu ermitteln]              | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Asien-Pazifik: Japan        | [zu ermitteln] | [zu ermitteln]              | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Asien-Pazifik: ex. Japan    | [zu ermitteln] | [zu ermitteln]              | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Emerging Markets: China     | [zu ermitteln] | [zu ermitteln]              | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Emerging Markets: ex. China | [zu ermitteln] | [zu ermitteln]              | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| **Total**                   | **100.0**      | **-**                       | **100.0**         | **-**                                      |

* **Tabelle 1.3.2: Sektorale Ziel-Allokation (als Resultat der Fondsauswahl)**

| Sektor                | Ziel-Gewichtung % | Begründung der Anpassung                   |
|:----------------------|:------------------|:-------------------------------------------|
| Technologie           | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Finanzen              | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Gesundheitswesen      | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Industrie             | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Basiskonsumgüter      | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Zyklische Konsumgüter | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Energie               | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Andere                | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| **Total**             | **100.0**         | **-**                                      |

* **Tabelle 1.3.3: Ziel-Allokation nach Marktkapitalisierung (als Resultat der Fondsauswahl)**

| Marktkapitalisierung     | Ziel-Gewichtung % | Begründung der Anpassung                   |
|:-------------------------|:------------------|:-------------------------------------------|
| Large Cap (>10 Mrd. USD) | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Mid Cap (2-10 Mrd. USD)  | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| Small Cap (<2 Mrd. USD)  | [zu ermitteln]    | [Begründung basierend auf Analyse von 1.4] |
| **Total**                | **100.0**         | **-**                                      |

## 1.4. Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)
* **Anweisung:** Führe eine umfassende Analyse des globalen makroökonomischen und geopolitischen Umfelds (Stand: heute) durch. Identifiziere mindestens 3-5 zentrale **Gewinnchancen** (z.B. technologischer Fortschritt, demografische Entwicklungen) und 3-5 zentrale **Risikofaktoren** (z.B. geopolitische Spannungen, Zinsänderungsrisiko, Inflationstrends, regulatorische Risiken), die für das Portfolio relevant sind.



# Block 2: ALGORITHMISCHER WORKFLOW ZUR BERICHTERSTELLUNG (STUFE 1 & 2)

## Executive Summary
Erstelle eine kurze, prägnante Zusammenfassung. Nenne das Anlageziel, die finale Portfolio-Allokation und die wichtigsten quantitativen Merkmale. Belege jede Aussage mit `##REF_X##`.


## I. INTRODUCTION
Leite die Studie ein und definiere Zweck und Ziele basierend auf '1.1. Rahmenbedingungen des Portfolios'.


## II. METHODS
* **A. Materials and Selection Criteria:** Beschreibe das Anlageuniversum und die strengen, priorisierten Auswahlkriterien aus Abschnitt '1.2.'. Erwähne die Fallback-Logik.

* **B. Target Allocation Strategy:** Präsentiere die in Abschnitt '1.3.' hergeleitete Ziel-Allokation und die dazugehörige Begründungstabelle '1.3.1'.

* **C. Analytical Process:** Erkläre die Methodik zur Auswahl der ETFs. Detailliere hier die Methodik zur Ermittlung von TD und TE:

* **Tracking-Differenz (TD):** Die Angabe der TD ist für 1, 3 und 5 Jahre (p.a., falls möglich) zwingend. **Anweisung zur Berechnung:** Greife auf das offizielle, aktuellste Factsheet des Fonds zu. Berechne die TD mit der Formel: $TD = \text{Fonds-Gesamtrendite in \%} - \text{Benchmark-Gesamtrendite in \%}$. **Stelle sicher, dass die Rendite-Zeitraeume exakt übereinstimmen.** Falls für einen Zeitraum keine Daten verfügbar sind, markiere dies mit "n.v." (nicht verfügbar).

* **Tracking Error (TE):** Gib den publizierten TE für 1, 3 und 5 Jahre an. Falls nicht publiziert, gib "n.v." an. **Berechne den TE nicht selbst.**


## III. RESULTS

### A. Comparative Analysis and ETF Selection
Führe eine erschöpfende Recherche durch und befülle die folgende Master-Tabelle. Jede Zelle muss mit den aktuellsten verfügbaren Daten befüllt und mit einem `##REF_X##`-Platzhalter zitiert werden.

* **Tabelle III-1: ETF-Vergleichsmatrix**

| Kategorie | Fondsname | ISIN | Anbieter | Repl.-Methode | Fd.-Währung | TER % p.a. | AUM (Mio CHF) | TD 1J % | TD 3J % p.a. | TD 5J % p.a. | TE 3J % | Auswahl (Ja/Nein) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Welt** | [Fondsname 1] | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | Nein |
| | [Fondsname 2] | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | **Ja** |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

* **Begründung der Auswahl:** Begründe **unmittelbar unter der Tabelle** für jede Kategorie die Auswahl des "Gewinner"-ETFs. Beziehe dich dabei explizit auf die Daten in der Tabelle und die priorisierten Kriterien aus Abschnitt 1.2.

### B. Final Portfolio Composition
* **Tabelle III-2: Finale Portfolio-Zusammenstellung**

| Fd-Name | ISIN | Hand.-Platz | Zielallok. % | Kurs (CHF) | Anz. Anteile | Invest.-Betrag (CHF) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Fondsname 2] | ##REF_X## | SIX | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## |
| ... | ##REF_X## | SIX | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## |
| **Total** | | | **100.0** | | | **ca. 100'000**|

### C. Aggregated Portfolio Characteristics

* **Tabelle III-3: Effektive Geografische Diversifikation**

* **Tabelle III-4: Effektive Sektorale Diversifikation**

* **Wichtige Anweisung für Tabelle III-5:** Diese Tabelle erfordert eine 'Look-Through'-Analyse. Du **musst** die Top-Positionen *jedes einzelnen ausgewählten ETFs* abrufen, deren jeweiliges Gewicht *innerhalb des Gesamtportfolios* berechnen (Formel: `Gewicht_final = Gewicht_pos_in_ETF * Allokation_etf_in_Portfolio`) und die Ergebnisse aggregieren. Zeige die 15 grössten, einzigartigen Unternehmenspositionen im finalen Portfolio.

* **Tabelle III-5: Look-Through-Analyse der Top-15-Positionen**

| Nr. | Unternehmen | Land | Sektor | Gewicht im Portfolio % |
| :--- | :--- | :--- | :--- | :--- |


## IV. DISCUSSION
Interpretiere die Ergebnisse aus Abschnitt III im Kontext der Risikofaktoren aus '1.4.'. Belege jede Aussage mit `##REF_X##`.

### A. Analysis of Defined Risks
Analysiere jeden in 1.4 identifizierten Risikofaktor.

### B. Additional Risks Identified
Diskutiere weitere Risiken (z.B. hohe Konzentration in Top-15-Positionen, Währungsrisiko).

### C. Risk Dashboard Summary
* **Tabelle IV-1: Quantitatives Risiko-Dashboard**

| Risikofaktor | Quantitative Portfolio-Exposure (%) | Qualitative Begründung der Exposure | Bewerteter Einfluss (Tief/Mittel/Hoch) |
| :--- | :--- | :--- | :--- |
| Währungsrisiko (% non-CHF) | ##REF_X## | ##REF_X## | ##REF_X## |
| Geopolitik (z.B. % China+Taiwan) | ##REF_X## | ##REF_X## | ##REF_X## |
| Zinsrisiko (% zinssensitive Sektoren) | ##REF_X## | ##REF_X## | ##REF_X## |
| Konzentration (Top-15-Gewicht) | ##REF_X## | ##REF_X## | ##REF_X## |
| Technologie-Konzentration (z.B. % "Magnificent 7") | ##REF_X## | ##REF_X## | ##REF_X## |


## V. CONCLUSION
Fasse die wichtigsten Erkenntnisse zusammen und bewerte, inwieweit das Portfolio die Ziele aus der Einleitung erreicht.


## ACKNOWLEDGEMENTS
Füge einen Platzhalter für Danksagungen ein.


## REFERENCES
Erstelle eine nummerierte Liste aller zitierten Quellen (`##REF_X##`). Die Liste muss numerisch nach der Reihenfolge des Erscheinens im Text geordnet sein. Formatiere jeden Eintrag strikt nach dem IEEE Documentation Style.


## APPENDIX
* **A. Table of Tables:** Liste aller Tabellen.

* **B. List of Abbreviations:** Liste aller Abkürzungen (ETF, AUM, TER, TD, TE, etc.).


## DISCLAIMER
Beende deine Antwort zwingend mit dem folgenden, exakt formulierten Disclaimer:
*Diese Studie ist weder eine persönliche Anlageberatung noch eine Aufforderung oder Empfehlung zum Kauf oder Verkauf von Finanzinstrumenten. Die hier dargestellten Informationen und Berechnungen basieren auf öffentlich zugänglichen Daten, deren Genauigkeit und Aktualität nicht garantiert werden kann. Jede Anlageentscheidung birgt Risiken, einschliesslich des potenziellen Verlusts des eingesetzten Kapitals. Vor jeder Investition sollte eine individuelle Beratung durch einen qualifizierten Finanzexperten eingeholt werden.*