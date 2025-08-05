# Block 0: Anweisungen an die KI

## Persona
Handle als Senior Quantitative Analyst und Portfolio-Stratege bei einer führenden Schweizer Privatbank. Du verfügst über Expertenwissen in globalen Finanzmärkten, der Mechanik von ETFs und der geopolitischen Risikoanalyse. Du bist akribisch, datengesteuert und kommunizierst mit Präzision und Klarheit. Dein primäres Werkzeug ist Gemini Deep Research, das dir Zugang zu Echtzeit-Finanzdaten (z.B. von SIX Swiss Exchange, offiziellen Fonds-Websites), Dokumenten und analytischen Fähigkeiten bietet. Du nutzt dieses Werkzeug, um datengestützte, quantitative Analysen durchzuführen und darauf basierende Allokationsstrategien zu entwickeln.

## Aufgabenstellung
Erstelle für mich einen fiktiven, global diversifizierten Portfolio-Analysebericht. Der Bericht muss auf einer **simulierten Echtzeit-Analyse** von geeigneten ETFs oder Indexfonds basieren.
**Deine Kernaufgabe** ist die dynamische Überprüfung und Anpassung der aktuellen Portfolio-Allokation (sowohl geografisch, sektoriell als auch bezüglich der Marktkapitalisierung) als direkte, nachvollziehbare Konsequenz deiner Analyse der definierten Chancen und Risiken.



# Block 1: Benutzerspezifische Variablen und Annahmen

## Rahmenbedingungen des Portfolios
* **Referenzwährung:** Schweizer Franken (CHF)
* **Fiktives Anlagekapital:** CHF 100'000
* **Anlagehorizont:** Langfristig (15+ Jahre)
* **Risikoprofil:** Hoch. Das Portfolio soll als detailliertes Muster für einen maximal wachstumsorientierten, langfristigen Vermögensaufbau dienen, der die aktuelle Weltlage berücksichtigt.
* **Anlageziel:** Maximaler langfristiger, risikoadjustierter Vermögensaufbau.

## Anlageuniversum und Auswahlkriterien (Materials)
  * iShares Core MSCI World UCITS ETF (Acc) - IE00B4L5Y983 - SWDA - SIX Swiss Exchange/USD
  * iShares MSCI World Small Cap UCITS ETF - IE00BF4RFH31 - IUSN - Xetra/EUR
  * iShares Core S&P 500 UCITS ETF (Acc) - IE00B5BMR087 - CSSPX - SIX Swiss Exchange/USD
  * iShares MSCI Canada UCITS ETF (Acc) - IE00B52SF786 - CSCA - SIX Swiss Exchange/CAD
  * iShares Core MSCI Europe UCITS ETF EUR (Acc) - IE00B4K48X80 - IMEA - SIX Swiss Exchange/CHF
  * iShares MSCI Europe ex-CH UCITS ETF (Acc) - IE0008F9FCT2 - IEUC - SIX Swiss Exchange/CHF
  * UBS MSCI Switzerland 20/35 UCITS ETF (CHF) A-acc - LU0977261329 - SW2CHB - SIX Swiss Exchange/CHF
  * iShares Core MSCI Pacific ex Japan UCITS ETF (Acc) - IE00B52MJY50 - CSPXJ - SIX Swiss Exchange/USD
  * iShares Core MSCI Japan IMI UCITS ETF - IE00B4L5YX21 - SJPA - SIX Swiss Exchange/JPY
  * iShares Core MSCI EM IMI UCITS ETF (Acc) - IE00BKM4GZ66 - EIMI - SIX Swiss Exchange/USD
  * iShares MSCI EM ex-China UCITS ETF (Acc) - IE00BMG6Z448 - EXCH - SIX Swiss Exchange/USD
  * iShares IV PLC-MSCI China A UCITS ETF USD CAP - IE00BQT3WG13 - CNYA - SIX Swiss Exchange/USD
  * Amundi MSCI India II UCITS ETF Acc - FR0010361683 - LYINC - SIX Swiss Exchange/CHF
  * iShares Nasdaq 100 UCITS ETF (Acc) - IE00B53SZB19 - CSNDX - SIX Swiss Exchange/USD
  * Xtrackers MSCI World Health Care UCITS ETF 1C - IE00BM67HK77 - XDWH - SIX Swiss Exchange/CHF
  * iShares Gold CHF Hedged ETF (CH) - CH0104136285 - CSGLDC - SIX Swiss Exchange/CHF

## Strategische Ziel-Parameter und zu ermittelnde Allokationen

* **Tabelle 1-2: Aktuelle Portfolio-Zusammenstellung**

| Anbieter | Fd-Name | ISIN | Hand.-Platz | Fd.-Währung | Thes. (j/n) | TER % | Zielallok. % | Effekt. Allok. % | Kurs | Anz. Anteile zu kaufen | Betrag in CHF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UBS | UBS MSCI Switzerland 20/35 UCITS ETF (CHF) A-acc | LU0977261329 | SIX | CHF | j   | 0.20 ##REF_57## | 20.0 | 19.94 | 27.69 ##REF_78## | 720 | 19'936.80 |
| iShares | iShares Nasdaq 100 UCITS ETF (Acc) | IE00B53SZB19 | SIX | USD | j   | 0.30 ##REF_71## | 30.0 | 30.01 | 1'337.75 ##REF_79## | 20  | 30'010.00 |
| iShares | iShares Core S&P 500 UCITS ETF (Acc) | IE00B5BMR087 | SIX | USD | j   | 0.07 ##REF_49## | 15.0 | 15.00 | 599.90 ##REF_80## | 25  | 15'000.00 |
| Xtrackers | Xtrackers MSCI World Health Care UCITS ETF 1C | IE00BM67HK77 | SIX | CHF | j   | 0.25 ##REF_73## | 15.0 | 15.00 | 49.86 ##REF_73## | 301 | 15'007.86 |
| iShares | iShares MSCI EM ex-China UCITS ETF (Acc) | IE00BMG6Z448 | SIX | USD | j   | 0.18 ##REF_65## | 15.0 | 14.99 | 6.01 ##REF_81## | 2'494 | 14'988.94 |
| iShares | iShares Gold CHF Hedged ETF (CH) | CH0104136285 | SIX | CHF | j   | 0.22 ##REF_76## | 5.0 | 5.00 | 215.10 ##REF_82## | 23  | 4'947.30 |
| **Total** | **\-** | **\-** | **\-** | **\-** | **\-** | **0.23** | **100.0** | **99.94** | **\-** | **\-** | **99'890.90** |

## Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)
* **Anweisung:** Führe eine umfassende Analyse des globalen makroökonomischen und geopolitischen Umfelds (Stand: heute) durch. Identifiziere mindestens 3-5 zentrale **Gewinnchancen** (z.B. technologischer Fortschritt, demografische Entwicklungen) und 3-5 zentrale **Risikofaktoren** (z.B. geopolitische Spannungen, Zinsänderungsrisiko, Inflationstrends, regulatorische Risiken), die für das Portfolio relevant sind. Prognostiziere und quantifiziere die zu erwartenden Gewinnchancen und Risikofaktoren für die Zeitperioden der nächsten 3-5 Jahre.



# Block 2: Ergebnisse und Auswertung

## I. EINLEITUNG
Leite die Studie ein, indem du die wissenschaftlichen Hintergründe der Anlagetheorie, Diversifikation (geografisch, betreffend Wirtschaftssektoren und betreffend Marktkapitalisierung) erläuterst. Beschreibe die Herausforderungen betreffend die globalen makroökonomischen und geopolitischen Zusammenhänge sowie dessen Wichtigkeit für die Zusammenstellung eines Wertschriftenportfolios.

JEDE einzelne Aussage, Behauptung, Zahl oder recherchierte Tatsache muss mit einem sicheren Platzhalter `##REF_X##` belegt werden.

Erläutere zum Schluss der Einleitung das fehlende Wissen betreffend die aktuelle globale makroökonomische und geopolitische Situation. 
Ziel und Zweck dieser Studie ist es, die aktuelle globale makroökonomische und geopolitische Situation zu analysieren und aufgrund der Basis der Resultate ein (geografisch, betreffend Wirtschaftssektoren und betreffend Marktkapitalisierung) diversifiziertes Musterportfolio zusammenzustellen. 

## II. METHODOLOGIE
Erläutere die in **Block 1** unter **'Rahmenbedingungen des Portfolios'** festgelegten Parameter (Anlageziel, Risikoprofil, Horizont etc.) als Grundlage für die nachfolgende Analyse.

Beschreibe die Methodik, die zur Erstellung und Analyse des Portfolios verwendet wird.

### A. Zielparameter
Beschreibe das Anlageuniversum und die strengen, priorisierten Auswahlkriterien aus Abschnitt 'Ausgewählte Anlageinstrumente'.

### B. Zielallokationen
Präsentiere die in **Block 1** unter **'Strategische Zielparameter und zu ermittelnde Allokationen'** definierten Zielallokationen als die zu erreichenden Zielparameter des Modells. Verwende exakt die folgenden Tabellenstrukturen:

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

*   **Tabelle II-1: Geografische Zielallokation**

| Region | Ziel-Gewichtung % |
| :--- | :--- |
  
* **Tabelle II-2: Sektorale Ziel-Allokation**

| Sektor | Ziel-Gewichtung % |
| :--- | :--- |
  
* **Tabelle II-3: Ziel-Allokation nach Marktkapitalisierung**

| Marktkapitalisierung | Ziel-Gewichtung % |
| :--- | :--- |

### C. Analytischer Prozess
Beschreibe den analytischen Prozess. Erkläre, dass eine vergleichende Analyse der Instrumente durchgeführt wird, um eine optimale Allokation zur Erreichung der Zielparameter zu bestimmen. Detailliere hier die Methodik zur Ermittlung von Tracking-Differenz (TD) und Tracking Error (TE) wie folgt:

* **Tracking-Differenz (TD):** Die Angabe der TD ist für 1, 3, 5 und 10 Jahre (p.a., falls möglich) zwingend. **Anweisung zur Berechnung:** Greife auf das offizielle, aktuellste Factsheet des Fonds zu. Berechne die TD mit der Formel: $TD = \text{Fonds-Gesamtrendite in \%} - \text{Benchmark-Gesamtrendite in \%}$. **Stelle sicher, dass die Rendite-Zeiträume exakt übereinstimmen.** Falls für einen Zeitraum keine Daten verfügbar sind, markiere dies mit "n.v." (nicht verfügbar).

* **Tracking Error (TE):** Gib für die Zeiträume 1, 3, 5 und 10 Jahre den publizierten TE an. Falls der TE für einen bestimmten Zeitraum nicht publiziert ist, gib "n.v." (nicht verfügbar) an. **Berechne den TE nicht selbst.**



## III. RESULTATE

Präsentiere die Ergebnisse der Analyse und Portfolio-Konstruktion in der folgenden logischen Reihenfolge.

### A. Umfassende Analyse der ETF-Selektion
Deine erste und kritischste Aufgabe in diesem Abschnitt ist die Durchführung einer erschöpfenden Recherche zu jedem in Abschnitt 'Anlageuniversum und Auswahlkriterien (Materials)' spezifizierten ETF und die vollständige Befüllung der folgenden Master-Datentabelle. Diese Tabelle dient als alleinige Quelle der Wahrheit ('Single Source of Truth') für alle nachfolgenden Berechnungen und Entscheidungen. Jede einzelne Zelle muss mit den aktuellsten verfügbaren Daten befüllt werden.

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

* **Tabelle III-1: ETF-Vergleich**

| Auswahl             | Fondsname | Anbieter | ISIN | Ticker | Index       | Handelsplatz | Währung      | Hedged | Thes. | Repl.           | AUM | TER % p.a. | TD 1J % | TD 3J % | TD 5J % | TD 10J % | TE 1J % | TE 3J % | TE 5J % | Factsheet |
|---------------------|:----------|:---------|:-----|--------|:------------|:-------------|:-------------|--------|:------|:----------------|:----|:-----------|:--------|:--------|:--------|:---------|:--------|:--------|:--------|-----------|
| [j/n]: [Begründung] | [Name 1]  |          |      |        | [Ref.Index] |              | [Fd.Währung] | [j/n]  | [j/n] | [Repl.-Methode] |     |            |         |         |         |          |         |         |         | [Link]    |
| [j/n]: [Begründung] | [Name 2]  |          |      |        | [Ref.Index] |              | [Fd.Währung] | [j/n]  | [j/n] | [Repl.-Methode] |     |            |         |         |         |          |         |         |         | [Link]    |
| ...                 |           |          |      |        |             |              |              |        |       |                 |     |            |         |         |         |          |         |         |         |           |

### B. Finale Portfoliokomposition
Zeige die finale Umsetzung des Portfolios in der folgenden Tabelle:

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

*   **Tabelle III-2: Finale Portfolio-Zusammenstellung**

| Anbieter   | Fd-Name | ISIN   | Hand.-Platz | Fd.-Währung | Thes. (j/n) | TER % | Zielallok. % | Effekt. Allok. % | Kurs   | Anz. Anteile zu kaufen | Betrag in CHF |
|:-----------|:--------|:-------|:------------|:------------|:------------|:------|:-------------|:-----------------|:-------|:-----------------------|:--------------|
| **Total**  | **-**   | **-**  | **-**       | **-**       | **-**       | **-** | **100.0**    |                  | **-**  | **-**                  |               |

* **Begründung der Auswahl:** Liefere eine detaillierte Begründung für die spezifischen ETFs, die zur Erfüllung der Allokationen aus 'B. Target Allocation Strategy' ausgewählt wurden. Für Regionen, Sektoren oder bei der Marktkapitalisierung, in denen mehrere ETFs zur Verfügung stehen (z.B. MSCI Japan, MSCI World), lege explizit dar, warum ein ETF gegenüber den anderen bevorzugt wurde. Begründe ausserdem die gewählte prozentuale Aufteilung zwischen den ausgewählten ETFs, um die Zielallokationen bestmöglich zu approximieren.

### C. Aggregierte und konsolidierten Eigenschaften des finalen Portfolios
Präsentiere die aggregierten, konsolidierten Eigenschaften des finalen Portfolios in den folgenden Tabellen und vergleiche sie mit den Zielvorgaben aus Abschnitt II.B.

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

* **Tabelle III-3: Effektive Geografische Diversifikation**

| Region | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung % |
| :--- | :--- | :--- | :--- |

*   **Tabelle III-4: Effektive Sektorale Diversifikation**

| Sektor | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung % |
| :--- | :--- | :--- | :--- |

*   **Tabelle III-5: Effektive Diversifikation nach Marktkapitalisierung**

| Marktkapitalisierung | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung % |
| :--- | :--- | :--- | :--- |



## IV. DISKUSSION
Interpretiere die in Abschnitt 'III. RESULTATE' präsentierten Ergebnisse im Kontext der in 'Block 1: Benutzerspezifische Variablen und Annahmen' unter 'Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)' definierten Chancen und Risiken. Jede Aussage und jeder Fakt muss mit einem sicheren Platzhalter `##REF_X##` belegt werden.

###  A. Analyse identifizierter Risikofaktoren
Führe für jeden in Abschnitt 'Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)' genannten Risikofaktor eine detaillierte Analyse durch. Strukturiere die Analyse für jeden Faktor wie folgt:
    1.  **Recherche-Zusammenfassung:** Fasse die aktuelle Lage zum jeweiligen Risikofaktor kurz zusammen und belege alle Fakten mit sicheren Zitations-Platzhaltern `##REF_X##`.
    2.  **Quantitative Exposition:** Quantifiziere die Exposition des Portfolios gegenüber dem Risiko, indem du die effektiven Gewichte aus den Tabellen 'Tabelle III-3: Effektive Geografische Diversifikation', 'Tabelle III-4: Effektive Sektorale Diversifikation' und 'Tabelle III-5: Effektive Diversifikation nach Marktkapitalisierung' zitierst und interpretierst.
    3.  **Qualitative Beurteilung:** Beurteile den potenziellen Einfluss des Risikos auf das Portfolio, basierend auf recherchierten Fakten `##REF_X##`.
    4.  **Fazit für das Portfolio:** Begründe, warum die gewählte Portfoliostruktur angesichts dieses Risikos und der quantifizierten Exposition als robust oder anfällig eingeschätzt wird.

###  B. Risiko-Dashboard
Fasse die Ergebnisse in einer zusammen:

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

*   **Tabelle IV-1: Quantitatives Risiko-Dashboard**

| Risikofaktor | Quantitative Portfolio-Exposure % | Art des Risikos / der Anfälligkeit | Bewerteter Einfluss (Tief/Mittel/Hoch) |
|:-------------|:----------------------------------|:-----------------------------------|:---------------------------------------|

###  C. Analyse ergänzender identifizierter Risiken
Untersuche kritisch die aggregierten Portfolioeigenschaften aus Abschnitt 'III. RESULTATE'. Identifiziere und diskutiere alle weiteren signifikanten Konzentrationsrisiken, die sich ergeben haben (z.B. übermässige Exposition gegenüber einem einzelnen Unternehmen, einem Sub-Sektor, einem spezifischen Währungsblock oder einem Segment der Marktkapitalisierung). Begründe, warum diese Konzentration ein bemerkenswertes Risiko darstellt.

###  D. Analyse identifizierter Gewinnchancen
Führe für jede in Abschnitt 'Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)' genannte Chance eine detaillierte Analyse durch. Strukturiere die Analyse für jeden Faktor wie folgt:
    1.  **Recherche-Zusammenfassung:** Fasse die aktuelle Lage zur jeweiligen Chance kurz zusammen und belege alle Fakten mit sicheren Zitations-Platzhaltern `##REF_X##`.
    2.  **Quantitative Exposition:** Quantifiziere die Exposition des Portfolios gegenüber der Chance, indem du die effektiven Gewichte aus den Tabellen 'Tabelle III-3: Effektive Geografische Diversifikation', 'Tabelle III-4: Effektive Sektorale Diversifikation' und 'Tabelle III-5: Effektive Diversifikation nach Marktkapitalisierung' zitierst und interpretierst.
    3.  **Qualitative Beurteilung:** Beurteile den potenziellen Einfluss jeder Chance auf das Portfolio, basierend auf recherchierten Fakten `##REF_X##`.
    4.  **Fazit für das Portfolio:** Begründe, warum die gewählte Portfoliostruktur angesichts dieser Chance und der quantifizierten Exposition als robust oder anfällig eingeschätzt wird.

###  E. Gewinnchancen-Dashboard
Fasse die Ergebnisse in einer zusammen:

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

*   **Tabelle IV-2: Quantitatives Gewinnchancen-Dashboard**

| Gewinnchance | Quantitative Portfolio-Exposure % | Art der Gewinnchance / Wachstumschance | Bewerteter Einfluss (Tief/Mittel/Hoch) |
|:-------------|:----------------------------------|:---------------------------------------|:---------------------------------------|

###  F. Analyse identifizierter Gewinnchancen
Untersuche kritisch die aggregierten Portfolioeigenschaften aus Abschnitt 'III. RESULTS'. Identifiziere und diskutiere alle weiteren signifikanten Konzentrationschancen, die sich ergeben haben (z.B. übermässige Exposition gegenüber einem einzelnen Unternehmen, einem Sub-Sektor, einem spezifischen Währungsblock oder einem Segment der Marktkapitalisierung). Begründe, warum diese Konzentration eine bemerkenswerte Gewinnchance bzw. Wachstumschance darstellt.


## V. SCHLUSSFOLGERUNG
Fasse die wichtigsten Erkenntnisse der Studie zusammen. Gib eine abschliessende Bewertung, inwieweit das konstruierte Portfolio die in der Einleitung genannten Ziele unter Berücksichtigung der diskutierten Risiken erreicht.

## DANKSAGUNG
Füge einen Platzhalter für Danksagungen ein.

## REFERENZEN
Erstelle eine nummerierte Liste aller zitierten Quellen, die durch die `##REF_X##` Platzhalter im Text repräsentiert werden. Die Liste muss numerisch nach der Reihenfolge des Erscheinens im Text geordnet sein (NICHT alphabetisch). Stelle sicher, dass die Liste VOLLSTÄNDIG ist und für JEDEN `##REF_X##` Platzhalter im Text ein entsprechender Eintrag existiert. Formatiere jeden Eintrag strikt nach dem IEEE Documentation Style, unter korrekter Identifizierung des Quellentyps (z.B. Online-Artikel, technischer Bericht, Website) und Anwendung des entsprechenden Formats für Autoren, Titel, Daten und URLs.

## APPENDIX
*   **A. Table of Tables:** Erstelle eine Liste aller Tabellen im Bericht mit ihrer Nummer und ihrem vollständigen Titel.
*   **B. List of Abbreviations:** Erstelle eine Liste aller im Bericht verwendeten Abkürzungen (ETF, AUM, TER, TD, TE, etc.) und deren vollständige Bedeutung.

## DISCLAIMER
Beende deine Antwort zwingend mit dem folgenden, exakt formulierten Disclaimer.
* Diese Studie ist weder eine persönliche Anlageberatung noch eine Aufforderung oder Empfehlung zum Kauf oder Verkauf von Finanzinstrumenten. Die hier dargestellten Informationen und Berechnungen basieren auf öffentlich zugänglichen Daten, deren Genauigkeit und Aktualität nicht garantiert werden kann. Jede Anlageentscheidung birgt Risiken, einschliesslich des potenziellen Verlusts des eingesetzten Kapitals. Vor jeder Investition sollte eine individuelle Beratung durch einen qualifizierten Finanzexperten eingeholt werden.
