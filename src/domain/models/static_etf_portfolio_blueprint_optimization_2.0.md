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
  * iShares Core MSCI World UCITS ETF (Acc) - IE00B4L5Y983 - SWDA - SIX Swiss Exchange/USD
  * iShares MSCI World Small Cap UCITS ETF - IE00BF4RFH31 - IUSN - Xetra/EUR
  * iShares Nasdaq 100 UCITS ETF (Acc) - IE00B53SZB19 - CSNDX - SIX Swiss Exchange/USD
  * iShares MSCI Canada UCITS ETF (Acc) - IE00B52SF786 - CSCA - SIX Swiss Exchange/CAD
  * Xtrackers MSCI Europe UCITS ETF 1C - LU0274209237 - XMEU - SIX Swiss Exchange/CHF
  * UBS MSCI Switzerland 20/35 UCITS ETF (CHF) A-acc - LU0977261329 - SW2CHB - SIX Swiss Exchange/CHF
  * UBS ETF (CH) - SPI (CHF) A-acc - CH0131872431 - SPICHA - SIX Swiss Exchange/CHF
  * iShares Core MSCI Pacific ex Japan UCITS ETF (Acc) - IE00B52MJY50 - CSPXJ - SIX Swiss Exchange/USD
  * Xtrackers MSCI Japan UCITS ETF 1C - LU0274209740 - XMJP - SIX Swiss Exchange/JPY
  * iShares Core MSCI Japan IMI UCITS ETF - IE00B4L5YX21 - SJPA - SIX Swiss Exchange/JPY
  * iShares Nikkei 225 UCITS ETF (Acc) - IE00B52MJD48 - CSNKY - SIX Swiss Exchange/JPY
  * iShares Core MSCI EM IMI UCITS ETF (Acc) - IE00BKM4GZ66 - EIMI - SIX Swiss Exchange/USD
  * iShares MSCI EM ex-China UCITS ETF (Acc) - IE00BMG6Z448 - EXCH - SIX Swiss Exchange/USD
  * Amundi MSCI India II UCITS ETF Acc - FR0010361683 - LYINC - SIX Swiss Exchange/CHF

## 1.3. Strategische Ziel-Parameter und zu ermittelnde Allokationen

* **Tabelle 1.3.1: Geografische Ziel-Allokation**

| Region                      | Ziel-Gewichtung % |
|:----------------------------|:------------------|
| Nordamerika: USA            | 38%               |
| Nordamerika: Kanada         | 2%                |
| Europa: Schweiz (CH)        | 5%                |
| Europa: Europa ex. CH       | 25%               |
| Asien-Pazifik: Japan        | 5%                |
| Asien-Pazifik: ex. Japan    | 5%                |
| Emerging Markets: China     | 6%                |
| Emerging Markets: ex. China | 14%               |
| **Total**                   | **100.0**         |

* **Tabelle 1.3.2: Sektorale Ziel-Allokation (als Resultat der Fondsauswahl)**

| Sektor                 | Ziel-Gewichtung % |
|:-----------------------|:------------------|
| Technologie            | 27%               |
| Finanzen               | [zu ermitteln]    |
| Gesundheitswesen       | [zu ermitteln]    |
| Industrie              | [zu ermitteln]    |
| Basiskonsumgüter       | [zu ermitteln]    |
| Zyklische Konsumgüter  | [zu ermitteln]    |
| Energie                | [zu ermitteln]    |
| Andere                 | [zu ermitteln]    |
| **Total**              | **100.0**         |

* **Tabelle 1.3.3: Ziel-Allokation nach Marktkapitalisierung (als Resultat der Fondsauswahl)**

| Marktkapitalisierung     | Ziel-Gewichtung % |
|:-------------------------|:------------------|
| Large Cap (>10 Mrd. USD) | 75%               |
| Mid Cap (2-10 Mrd. USD)  | [zu ermitteln]    |
| Small Cap (<2 Mrd. USD)  | [zu ermitteln]    |
| **Total**                | **100.0**         |

## 1.4. Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)
* **Anweisung:** Führe eine umfassende Analyse des globalen makroökonomischen und geopolitischen Umfelds (Stand: heute) durch. Identifiziere mindestens 3-5 zentrale **Gewinnchancen** (z.B. technologischer Fortschritt, demografische Entwicklungen) und 3-5 zentrale **Risikofaktoren** (z.B. geopolitische Spannungen, Zinsänderungsrisiko, Inflationstrends, regulatorische Risiken), die für das Portfolio relevant sind.



# Block 2: ALGORITHMISCHER WORKFLOW ZUR BERICHTERSTELLUNG (STUFE 1 & 2)

## Executive Summary
Erstelle zu Beginn eine kurze, prägnante Zusammenfassung als eigenständige Übersicht für einen zeitkritischen Entscheidungsträger. Nenne das Anlageziel, die in Abschnitt 'III. RESULTS' und 'IV. DISCUSSION' präsentierte und begründete prozentuale Allokation zwischen den ETFs und die wichtigsten quantitativen Merkmale des resultierenden Portfolios.

JEDE einzelne Aussage, Behauptung, Zahl oder recherchierte Tatsache muss mit einem sicheren Platzhalter `##REF_X##` belegt werden.

## I. INTRODUCTION
Leite die Studie ein, indem du die wissenschaftlichen Hintergründe der Anlagetheorie, Diversifikation (geografisch, betreffend Wirtschaftssektoren und betreffend Marktkapitalisierung) erläuterst. Beschreibe die Herausforderungen betreffend die globalen makroökonomischen und geopolitischen Zusammenhänge sowie dessen Wichtigkeit für die Zusammenstellung eines Wertschriftenportfolios.

JEDE einzelne Aussage, Behauptung, Zahl oder recherchierte Tatsache muss mit einem sicheren Platzhalter `##REF_X##` belegt werden.

Erläutere zum Schluss der Einleitung das fehlende Wissen betreffend die aktuelle globale makroökonomische und geopolitische Situation. 
Ziel und Zweck dieser Studie ist es, die aktuelle globale makroökonomische und geopolitische Situation zu analysieren und aufgrund der Basis der Resultate ein (geografisch, betreffend Wirtschaftssektoren und betreffend Marktkapitalisierung) diversifiziertes Musterportfolio zusammenzustellen. 

## II. METHODS

Erläutere die in **Block 1** unter **'1.1. Rahmenbedingungen des Portfolios'** festgelegten Parameter (Anlageziel, Risikoprofil, Horizont etc.) als Grundlage für die nachfolgende Analyse.

Beschreibe die Methodik, die zur Erstellung und Analyse des Portfolios verwendet wird.
*   **A. Materials:** Liste die in **Block 1** unter **'1.2. Ausgewählte Anlageinstrumente'** definierten ETFs als die für die Studie zur Verfügung stehenden Materialien auf.
*   **B. Target Parameters:** Präsentiere die vom Benutzer in **Block 1** unter **'1.3. Strategische Ziel-Parameter und zu ermittelnde Allokationen'** definierten Ziel-Gewichtungen als die zu erreichenden Zielparameter des Modells. Verwende exakt die folgenden Tabellenstrukturen:
    *   **Tabelle II-1: Geografische Ziel-Allokation**

| Region | Ziel-Gewichtung % |
| :--- | :--- |

    *   **Tabelle II-2: Sektorale Ziel-Allokation**

| Sektor | Ziel-Gewichtung % |
| :--- | :--- |

    *   **Tabelle II-3: Ziel-Allokation nach Marktkapitalisierung**

| Marktkapitalisierung | Ziel-Gewichtung % |
| :--- | :--- |

*   **C. Analytical Process:** Beschreibe den analytischen Prozess. Erkläre, dass eine vergleichende Analyse der Instrumente durchgeführt wird, um eine optimale Allokation zur Erreichung der Zielparameter zu bestimmen. Detailliere hier die Methodik zur Ermittlung von Tracking-Differenz (TD) und Tracking Error (TE) wie folgt:
    *   **Tracking-Differenz (TD):** Die Angabe der TD ist für alle Zeiträume (1, 3, 5, 10 Jahre) zwingend erforderlich. Falls die TD für einen Zeitraum nicht direkt publiziert ist, **musst du sie berechnen**. Greife dazu auf das offizielle, aktuellste Factsheet des Fonds zu. Finde eine einzelne Tabelle, die sowohl die kumulierte Wertentwicklung des Fonds als auch die des Benchmarks für den exakt gleichen Zeitraum mit identischem Enddatum ausweist. Berechne die TD mit der Formel: $TD = \text{Fonds-Gesamtrendite in \%} - \text{Benchmark-Gesamtrendite in \%}$. Falls für einen Zeitraum keine Daten oder keine direkt vergleichbaren Daten aus einer einzigen Quelle verfügbar sind, markiere dies mit "n.v." und begründe es kurz.
    *   **Tracking Error (TE):** Gib für die Zeiträume 1, 3, 5 und 10 Jahre den publizierten Tracking Error an. Falls der TE für einen bestimmten Zeitraum nicht in offiziellen Dokumenten publiziert ist, gib "n.v." (nicht verfügbar) an. **Versuche unter keinen Umständen, den TE selbst zu berechnen.**

**III. RESULTS**
Präsentiere die Ergebnisse der Analyse und Portfolio-Konstruktion in der folgenden logischen Reihenfolge.
*   **A. Master-Datenerfassung und vergleichende Analyse:** Deine erste und kritischste Aufgabe in diesem Abschnitt ist die Durchführung einer erschöpfenden Recherche zu jedem in Block 1.2 spezifizierten ETF und die vollständige Befüllung der folgenden Master-Datentabelle. Diese Tabelle dient als alleinige Quelle der Wahrheit ('Single Source of Truth') für alle nachfolgenden Berechnungen und Entscheidungen. Jede einzelne Zelle muss mit den aktuellsten verfügbaren Daten befüllt und mit einem `##REF_X##`-Platzhalter zitiert werden.
    *   **Tabelle III-1: ETF-Vergleich**

| Fondsname | Anbieter | ISIN | Ref.Index | Repl.-Methode | Fd.-Währung | Thes. (j/n) | TER % p.a. | AUM | Ant. EM % | TD 1J % | TD 3J % | TD 5J % | TD 10J % | TE 1J % | TE 3J % | TE 5J % | TE 10J % | Hand.-Platz | Kurs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Fondsname 1] | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## |
| [Fondsname 2] | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## |
|... | | | | | | | | | | | | | | | | | | | |

*   **B. Allokationsbegründung und ETF-Selektion:** Basierend auf den umfassenden Daten in Tabelle III-1, liefere eine detaillierte Begründung für die spezifischen ETFs, die zur Erfüllung der regionalen Allokationen aus Tabelle II-1 ausgewählt wurden. Für Regionen, in denen mehrere ETFs zur Verfügung stehen (z.B. MSCI Japan, MSCI World), lege explizit dar, warum ein ETF gegenüber den anderen bevorzugt wurde. Beziehe dich dabei auf Schlüsselkennzahlen wie TER, Tracking-Differenz, AUM und Replikationsmethode. Begründe ausserdem die gewählte prozentuale Aufteilung zwischen den ausgewählten ETFs, um die geografischen Zielparameter bestmöglich zu approximieren.

*   **C. Finale Portfolio-Zusammenstellung:** Zeige die finale Umsetzung des Portfolios in **Tabelle III-2**.
    *   **Tabelle III-2: Finale Portfolio-Zusammenstellung**

| Anbieter | Fd-Name | ISIN | Hand.-Platz | Fd.-Währung | Thes. (j/n) | TER % | Zielallok. % | Effekt. Allok. % | Kurs | Anz. Anteile zu kaufen | Betrag in CHF |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

*   **D. Aggregierte Portfolio-Eigenschaften:** Präsentiere die aggregierten, konsolidierten Eigenschaften des finalen Portfolios in den folgenden Tabellen und vergleiche sie mit den Zielvorgaben aus Abschnitt II.B.
    *   **Tabelle III-3: Effektive Geografische Diversifikation**

| Region | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung % |
| :--- | :--- | :--- | :--- |

    *   **Tabelle III-4: Effektive Sektorale Diversifikation**

| Sektor | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung % |
| :--- | :--- | :--- | :--- |

    *   **Tabelle III-5: Effektive Diversifikation nach Marktkapitalisierung**

| Marktkapitalisierung | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung % |
| :--- | :--- | :--- | :--- |

*   **E. Look-Through Analysis of Individual Holdings:** Führe für jedes einzelne Produkt aus Tabelle III-2 eine detaillierte "Look-Through"-Analyse durch. Nummeriere die Analyse für jeden ETF (E.1, E.2,...) und die dazugehörigen Tabellen (Tabelle III-6, Tabelle III-7,...) konsistent.

**IV. DISCUSSION**
Interpretiere die in Abschnitt III präsentierten Ergebnisse im Kontext der in **Block 1** unter **'1.4. Zu analysierende Risikofaktoren'** definierten Risiken. Jede Aussage und jeder Fakt muss mit einem sicheren Platzhalter `##REF_X##` belegt werden.
*   **A. Analysis of Defined Risks:** Führe für jeden in Block 1.4 genannten Risikofaktor eine detaillierte Analyse durch. Strukturiere die Analyse für jeden Faktor wie folgt:
    1.  **Recherche-Zusammenfassung:** Fasse die aktuelle Lage zum jeweiligen Risikofaktor kurz zusammen und belege alle Fakten mit sicheren Zitations-Platzhaltern `##REF_X##`.
    2.  **Quantitative Exposition:** Quantifiziere die Exposition des Portfolios gegenüber dem Risiko, indem du die effektiven Gewichte aus den Tabellen III-3, III-4 und III-5 zitierst und interpretierst.
    3.  **Qualitative Beurteilung:** Beurteile den potenziellen Einfluss des Risikos auf das Portfolio, basierend auf recherchierten Fakten `##REF_X##`.
    4.  **Fazit für das Portfolio:** Begründe, warum die gewählte Portfoliostruktur angesichts dieses Risikos und der quantifizierten Exposition als robust oder anfällig eingeschätzt wird.
*   **B. Risk Dashboard:** Fasse die Ergebnisse in **Tabelle IV-1** zusammen.
    *   **Tabelle IV-1: Quantitatives Risiko-Dashboard**

| Risikofaktor | Quantitative Portfolio-Exposure % | Art des Risikos / der Anfälligkeit | Bewerteter Einfluss (Tief/Mittel/Hoch) |
| :--- | :--- | :--- | :--- |

*   **C. Additional Risks Identified Through Analysis:** Über die vom Benutzer vordefinierten Risiken hinaus, untersuche kritisch die aggregierten Portfolioeigenschaften aus Abschnitt III. Identifiziere und diskutiere alle weiteren signifikanten Konzentrationsrisiken, die sich ergeben haben (z.B. übermässige Exposition gegenüber einem einzelnen Unternehmen, einem Sub-Sektor oder einem spezifischen Währungsblock). Begründe, warum diese Konzentration ein bemerkenswertes Risiko darstellt.

**V. CONCLUSION**
Fasse die wichtigsten Erkenntnisse der Studie zusammen. Gib eine abschliessende Bewertung, inwieweit das konstruierte Portfolio die in der Einleitung genannten Ziele unter Berücksichtigung der diskutierten Risiken erreicht.

**ACKNOWLEDGEMENTS**
Füge einen Platzhalter für Danksagungen ein.

**REFERENCES**
Erstelle eine nummerierte Liste aller zitierten Quellen, die durch die `##REF_X##` Platzhalter im Text repräsentiert werden. Die Liste muss numerisch nach der Reihenfolge des Erscheinens im Text geordnet sein (NICHT alphabetisch). Stelle sicher, dass die Liste VOLLSTÄNDIG ist und für JEDEN `##REF_X##` Platzhalter im Text ein entsprechender Eintrag existiert. Formatiere jeden Eintrag strikt nach dem IEEE Documentation Style, unter korrekter Identifizierung des Quellentyps (z.B. Online-Artikel, technischer Bericht, Website) und Anwendung des entsprechenden Formats für Autoren, Titel, Daten und URLs.

**APPENDIX**
*   **A. Table of Tables:** Erstelle eine Liste aller Tabellen im Bericht mit ihrer Nummer und ihrem vollständigen Titel.
*   **B. List of Abbreviations:** Erstelle eine Liste aller im Bericht verwendeten Abkürzungen (z.B. ETF, AUM, TER) und deren vollständige Bedeutung.

**DISCLAIMER**
Beende deine Antwort zwingend mit dem folgenden, exakt formulierten Disclaimer.
*   Diese Studie ist weder eine persönliche Anlageberatung noch eine Aufforderung oder Empfehlung zum Kauf oder Verkauf von Finanzinstrumenten. Die hier dargestellten Informationen und Berechnungen basieren auf öffentlich zugänglichen Daten, deren Genauigkeit und Aktualität nicht garantiert werden kann. Jede Anlageentscheidung birgt Risiken, einschliesslich des potenziellen Verlusts des eingesetzten Kapitals. Vor jeder Investition sollte eine individuelle Beratung durch einen qualifizierten Finanzexperten eingeholt werden.
