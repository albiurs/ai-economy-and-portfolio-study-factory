# Block 0: Anweisungen an die KI

## Persona
Handle als Senior Quantitative Analyst und Portfolio-Stratege bei einer führenden Schweizer Privatbank. Du verfügst über Expertenwissen in globalen Finanzmärkten, der Mechanik von ETFs und der geopolitischen Risikoanalyse. Du bist akribisch, datengesteuert und kommunizierst mit Präzision und Klarheit. Dein primäres Werkzeug ist Gemini Deep Research, das dir Zugang zu Echtzeit-Finanzdaten (z.B. von SIX Swiss Exchange, offiziellen Fonds-Websites), Dokumenten und analytischen Fähigkeiten bietet. Du nutzt dieses Werkzeug, um datengestützte, quantitative Analysen durchzuführen und darauf basierende Allokationsstrategien zu entwickeln.

## Aufgabenstellung
Erstelle für mich einen fiktiven, global diversifizierten Portfolio-Analysebericht im Format einer wissenschaftlichen Studie (IEEE-Stil). Der Bericht muss auf einer **simulierten Echtzeit-Analyse** von geeigneten ETFs oder Indexfonds basieren.
**Deine Kernaufgabe** ist die dynamische Ermittlung der Portfolio-Allokation (sowohl geografisch, sektoriell als auch bezüglich der Marktkapitalisierung) als direkte, nachvollziehbare Konsequenz deiner Analyse der definierten Chancen und Risiken.


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

## 1.3. Strategische Ziel-Parameter und zu ermittelnde Allokationen

* **Tabelle 1.3.1: Geografische Ziel-Allokation**

| Region                             | Ziel-Gewichtung % |
|:-----------------------------------|:------------------|
| Nordamerika: USA                   | 50%               |
| Nordamerika: Kanada                | [zu ermitteln]    |
| Europa: Schweiz (CH)               | 20%               |
| Europa: Europa ex. CH              | [zu ermitteln]    |
| Asien-Pazifik: Japan               | [zu ermitteln]    |
| Asien-Pazifik: ex. Japan           | [zu ermitteln]    |
| Emerging Markets: China (A-Aktien) | 0%                |
| Emerging Markets: ex. China        | 10%               |
| Indien                             | 10%               |
| **Total**                          | **100.0**         |

* **Tabelle 1.3.2: Sektorale Ziel-Allokation (als Resultat der Fondsauswahl)**

| Sektor                | Ziel-Gewichtung % |
|:----------------------|:------------------|
| Technologie           | 33%               |
| Finanzen              | [zu ermitteln]    |
| Gesundheitswesen      | 15%               |
| Industrie             | [zu ermitteln]    |
| Basiskonsumgüter      | [zu ermitteln]    |
| Zyklische Konsumgüter | [zu ermitteln]    |
| Energie               | [zu ermitteln]    |
| Edelmetalle: Gold     | 5%                |
| Andere                | [zu ermitteln]    |
| **Total**             | **100.0**         |

* **Tabelle 1.3.3: Ziel-Allokation nach Marktkapitalisierung (als Resultat der Fondsauswahl)**

| Marktkapitalisierung     | Ziel-Gewichtung % |
|:-------------------------|:------------------|
| Large Cap (>10 Mrd. USD) | 80%               |
| Mid Cap (2-10 Mrd. USD)  | [zu ermitteln]    |
| Small Cap (<2 Mrd. USD)  | [zu ermitteln]    |
| **Total**                | **100.0**         |

## 1.4. Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)
* **Anweisung:** Führe eine umfassende Analyse des globalen makroökonomischen und geopolitischen Umfelds (Stand: heute) durch. Identifiziere mindestens 3-5 zentrale **Gewinnchancen** (z.B. technologischer Fortschritt, demografische Entwicklungen) und 3-5 zentrale **Risikofaktoren** (z.B. geopolitische Spannungen, Zinsänderungsrisiko, Inflationstrends, regulatorische Risiken), die für das Portfolio relevant sind.



# Block 2: ALGORITHMISCHER WORKFLOW ZUR BERICHTERSTELLUNG (STUFE 1 & 2)


## Titel: `II. METHODS`

### Titel: `A. Materials and Selection Criteria`
Beschreibe das Anlageuniversum und die strengen, priorisierten Auswahlkriterien aus Abschnitt '1.2. Ausgewählte Anlageinstrumente'.

### Titel: `B. Target Allocation Strategy`
Präsentiere die in **Block 1** unter **'1.3. Strategische Zielparameter und zu ermittelnde Allokationen'** definierten Zielallokationen als die zu erreichenden Zielparameter des Modells. Verwende exakt die folgenden Tabellenstrukturen:

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

*   **Tabelle II-1: Geografische Zielallokation**

| Region | Ziel-Gewichtung % |
|:-------|:------------------|
  
* **Tabelle II-2: Sektorale Ziel-Allokation**

| Sektor | Ziel-Gewichtung % |
|:-------|:------------------|
  
* **Tabelle II-3: Ziel-Allokation nach Marktkapitalisierung**

| Marktkapitalisierung | Ziel-Gewichtung % |
|:---------------------|:------------------|

### Titel: `C. Analytical Process`
Beschreibe den analytischen Prozess. Erkläre, dass eine vergleichende Analyse der Instrumente durchgeführt wird, um eine optimale Allokation zur Erreichung der Zielparameter zu bestimmen. Detailliere hier die Methodik zur Ermittlung von Tracking-Differenz (TD) und Tracking Error (TE) wie folgt:

* **Tracking-Differenz (TD):** Die Angabe der TD ist für 1, 3, 5 und 10 Jahre (p.a., falls möglich) zwingend. **Anweisung zur Berechnung:** Greife auf das offizielle, aktuellste Factsheet des Fonds zu. Berechne die TD mit der Formel: $TD = \text{Fonds-Gesamtrendite in \%} - \text{Benchmark-Gesamtrendite in \%}$. **Stelle sicher, dass die Rendite-Zeiträume exakt übereinstimmen.** Falls für einen Zeitraum keine Daten verfügbar sind, markiere dies mit "n.v." (nicht verfügbar).

* **Tracking Error (TE):** Gib für die Zeiträume 1, 3, 5 und 10 Jahre den publizierten TE an. Falls der TE für einen bestimmten Zeitraum nicht publiziert ist, gib "n.v." (nicht verfügbar) an. **Berechne den TE nicht selbst.**


## Titel: `III. RESULTS`
Präsentiere die Ergebnisse der Analyse und Portfolio-Konstruktion in der folgenden logischen Reihenfolge.

### Titel: `B. Final Portfolio Composition`
Zeige die finale Umsetzung des Portfolios in der folgenden Tabelle:

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

*   **Tabelle III-2: Finale Portfolio-Zusammenstellung**

| Anbieter   | Fd-Name | ISIN   | Hand.-Platz | Fd.-Währung | Thes. (j/n) | TER % | Zielallok. % | Effekt. Allok. % | Kurs   | Anz. Anteile zu kaufen | Betrag in CHF |
|:-----------|:--------|:-------|:------------|:------------|:------------|:------|:-------------|:-----------------|:-------|:-----------------------|:--------------|
| **Total**  | **-**   | **-**  | **-**       | **-**       | **-**       | **-** | **100.0**    |                  | **-**  | **-**                  |               |

* **Begründung der Auswahl:** Liefere eine detaillierte Begründung für die spezifischen ETFs, die zur Erfüllung der Allokationen aus 'B. Target Allocation Strategy' ausgewählt wurden. Für Regionen, Sektoren oder bei der Marktkapitalisierung, in denen mehrere ETFs zur Verfügung stehen (z.B. MSCI Japan, MSCI World), lege explizit dar, warum ein ETF gegenüber den anderen bevorzugt wurde. Begründe ausserdem die gewählte prozentuale Aufteilung zwischen den ausgewählten ETFs, um die Zielallokationen bestmöglich zu approximieren.

### Titel: `C. Aggregated Portfolio Characteristics`
Präsentiere die aggregierten, konsolidierten Eigenschaften des finalen Portfolios in den folgenden Tabellen und vergleiche sie mit den Zielvorgaben aus Abschnitt II.B.

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

* **Tabelle III-3: Effektive Geografische Diversifikation**

| Region | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung % |
|:-------|:------------------|:-----------------------|:-------------|

*   **Tabelle III-4: Effektive Sektorale Diversifikation**

| Sektor | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung % |
|:-------|:------------------|:-----------------------|:-------------|

*   **Tabelle III-5: Effektive Diversifikation nach Marktkapitalisierung**

| Marktkapitalisierung | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung % |
|:---------------------|:------------------|:-----------------------|:-------------|

### Titel: `D. Look-Through Analysis`
Führe für jedes einzelne Produkt aus 'Tabelle III-2: Finale Portfolio-Zusammenstellung' eine detaillierte "Look-Through"-Analyse durch. Ermittle für jeden einzelnen Fonds im Portfolio: 
1. die Allokation (prozentual innerhalb des Fonds und auch aggregiert im finalen Portfolio) bezüglich Geografie, Sektor und Marktkapitalisierung. 
2. Die Top 10 Positionen mit prozentualem Anteil im finalen Portfolio.

Nummeriere die Analyse für jeden ETF (E.1, E.2,...) und die dazugehörigen Tabellen (Tabelle III-6, Tabelle III-7,...) konsistent.


## Titel: `IV. DISCUSSION`
Interpretiere die in Abschnitt 'III. RESULTS' präsentierten Ergebnisse im Kontext der in 'Block 1: Benutzerspezifische Variablen und Annahmen' unter '1.4. Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)' definierten Chancen und Risiken. Jede Aussage und jeder Fakt muss mit einem sicheren Platzhalter `##REF_X##` belegt werden.

###  Titel: `A. Analysis of Defined Risks`
Führe für jeden in Abschnitt '1.4. Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)' genannten Risikofaktor eine detaillierte Analyse durch. Strukturiere die Analyse für jeden Faktor wie folgt:
    1.  **Recherche-Zusammenfassung:** Fasse die aktuelle Lage zum jeweiligen Risikofaktor kurz zusammen und belege alle Fakten mit sicheren Zitations-Platzhaltern `##REF_X##`.
    2.  **Quantitative Exposition:** Quantifiziere die Exposition des Portfolios gegenüber dem Risiko, indem du die effektiven Gewichte aus den Tabellen 'Tabelle III-3: Effektive Geografische Diversifikation', 'Tabelle III-4: Effektive Sektorale Diversifikation' und 'Tabelle III-5: Effektive Diversifikation nach Marktkapitalisierung' zitierst und interpretierst.
    3.  **Qualitative Beurteilung:** Beurteile den potenziellen Einfluss des Risikos auf das Portfolio, basierend auf recherchierten Fakten `##REF_X##`.
    4.  **Fazit für das Portfolio:** Begründe, warum die gewählte Portfoliostruktur angesichts dieses Risikos und der quantifizierten Exposition als robust oder anfällig eingeschätzt wird.

###  Titel: `B. Risk Dashboard`
Fasse die Ergebnisse in einer zusammen:

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

*   **Tabelle IV-1: Quantitatives Risiko-Dashboard**

| Risikofaktor | Quantitative Portfolio-Exposure % | Art des Risikos / der Anfälligkeit | Bewerteter Einfluss (Tief/Mittel/Hoch) |
|:-------------|:----------------------------------|:-----------------------------------|:---------------------------------------|

###  Titel: `C. Additional Risks Identified Through Analysis`
Untersuche kritisch die aggregierten Portfolioeigenschaften aus Abschnitt 'III. RESULTS'. Identifiziere und diskutiere alle weiteren signifikanten Konzentrationsrisiken, die sich ergeben haben (z.B. übermässige Exposition gegenüber einem einzelnen Unternehmen, einem Sub-Sektor, einem spezifischen Währungsblock oder einem Segment der Marktkapitalisierung). Begründe, warum diese Konzentration ein bemerkenswertes Risiko darstellt.

###  Titel: `D. Analysis of Defined Chances`
Führe für jede in Abschnitt '1.4. Zu analysierende Gewinnchancen und Risikofaktoren (Gain and Risk Framework)' genannte Chance eine detaillierte Analyse durch. Strukturiere die Analyse für jeden Faktor wie folgt:
    1.  **Recherche-Zusammenfassung:** Fasse die aktuelle Lage zur jeweiligen Chance kurz zusammen und belege alle Fakten mit sicheren Zitations-Platzhaltern `##REF_X##`.
    2.  **Quantitative Exposition:** Quantifiziere die Exposition des Portfolios gegenüber der Chance, indem du die effektiven Gewichte aus den Tabellen 'Tabelle III-3: Effektive Geografische Diversifikation', 'Tabelle III-4: Effektive Sektorale Diversifikation' und 'Tabelle III-5: Effektive Diversifikation nach Marktkapitalisierung' zitierst und interpretierst.
    3.  **Qualitative Beurteilung:** Beurteile den potenziellen Einfluss jeder Chance auf das Portfolio, basierend auf recherchierten Fakten `##REF_X##`.
    4.  **Fazit für das Portfolio:** Begründe, warum die gewählte Portfoliostruktur angesichts dieser Chance und der quantifizierten Exposition als robust oder anfällig eingeschätzt wird.

###  Titel: `E. Chance Dashboard`
Fasse die Ergebnisse in einer zusammen:

* **Darstellung Tabellen:** Erstelle ausschliesslich vollständig ausgefüllte Tabellen mit der exakten Struktur. **Halte dich strikt an die vorgegebene Tabellenstruktur**:

*   **Tabelle IV-2: Quantitatives Gewinnchancen-Dashboard**

| Gewinnchance | Quantitative Portfolio-Exposure % | Art der Gewinnchance / Wachstumschance | Bewerteter Einfluss (Tief/Mittel/Hoch) |
|:-------------|:----------------------------------|:---------------------------------------|:---------------------------------------|

###  Titel: `F. Additional Chance Identified Through Analysis`
Untersuche kritisch die aggregierten Portfolioeigenschaften aus Abschnitt 'III. RESULTS'. Identifiziere und diskutiere alle weiteren signifikanten Konzentrationschancen, die sich ergeben haben (z.B. übermässige Exposition gegenüber einem einzelnen Unternehmen, einem Sub-Sektor, einem spezifischen Währungsblock oder einem Segment der Marktkapitalisierung). Begründe, warum diese Konzentration eine bemerkenswerte Gewinnchance bzw. Wachstumschance darstellt.


## Titel: `V. CONCLUSION`
Fasse die wichtigsten Erkenntnisse der Studie zusammen. Gib eine abschliessende Bewertung, inwieweit das konstruierte Portfolio die in der Einleitung genannten Ziele unter Berücksichtigung der diskutierten Risiken erreicht.
