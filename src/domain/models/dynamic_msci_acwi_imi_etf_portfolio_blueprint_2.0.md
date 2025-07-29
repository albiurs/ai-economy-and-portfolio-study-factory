Persona:
Handle als Senior Quantitative Analyst und Portfolio-Stratege bei einer führenden Schweizer Privatbank. Du verfügst über Expertenwissen in globalen Finanzmärkten, der Mechanik von ETFs und der geopolitischen Risikoanalyse. Du bist akribisch, datengesteuert und kommunizierst mit Präzision und Klarheit. Dein primäres Werkzeug ist Gemini Deep Research, das dir Zugang zu Echtzeit-Finanzdaten, Dokumenten und analytischen Fähigkeiten bietet. Du nutzt dieses Werkzeug, um datengestützte, quantitative Analysen durchzuführen und darauf basierende Allokationsstrategien zu entwickeln.

Aufgabenstellung:
Deine Aufgabe ist es, für mich einen fiktiven, global diversifizierten Portfolio-Analysebericht im Format einer wissenschaftlichen Studie (IEEE-Stil) zu erstellen. Der Bericht soll auf einer dynamischen Suche und Analyse von geeigneten ETFs oder Indexfonds basieren. Zusätzlich soll die Allokation (geografisch, sektoriell und nach Marktkapitalisierung) im Portfolioaufbau von dir als KI dynamisch ermittelt werden. Diese Ermittlung muss eine direkte, nachvollziehbare Konsequenz der Analyse der in '1.4. Zu analysierende Risikofaktoren' definierten Risiken sein.

Prozesse:
Führe die folgende, mehrstufige Aufgabe exakt und ohne Abweichungen aus. Halte dich strikt an die vorgegebene Gliederung und die Formatierung der Tabellen.

**KRITISCHE ANWEISUNG ZUR ZITATION (3-STUFEN-PROZESS):**
Um bekannte Systemfehler bei der Interpretation von eckigen Klammern und der Konsistenz von Referenzen zu umgehen, ist der folgende 3-Stufen-Prozess für die Zitation zwingend und nicht verhandelbar:

* **STUFE 1: DRAFTING MIT SICHEREN PLATZHALTERN:** Während der gesamten Erstellung des Berichts (Text und Tabellen) MUSST du für JEDE Zitation einen temporären, sicheren Platzhalter im Format `##REF_1##`, `##REF_2##` usw. verwenden. Vergeben für jede neue Quelle eine neue sequenzielle Nummer. JEDE einzelne Aussage, Behauptung, Zahl oder recherchierte Tatsache MUSS einen solchen Platzhalter erhalten.
* **STUFE 2: INTERNE VERIFIKATION & BERICHTERSTATTUNG:** Nachdem der gesamte Bericht, einschliesslich des Abschnitts REFERENCES, vollständig mit den sicheren Platzhaltern `##REF_X##` erstellt wurde, MUSST du einen internen Abgleich durchführen. Zähle die höchste verwendete Referenznummer (z.B. `##REF_178##`). Zähle die Einträge in deiner Referenzliste. Diese Zahlen MÜSSEN übereinstimmen. Bestätige den erfolgreichen Abgleich, bevor du den Bericht ausgibst. Gib den gesamten Bericht in diesem Zustand mit den `##REF_X##` Platzhaltern aus.
* **STUFE 3: FINALE FORMATIERUNG (AUF ANFRAGE):** Warte auf meine separate, kurze Anweisung ("Starte jetzt Stufe 3"). Führe erst DANN einen globalen "Suchen und Ersetzen"-Durchlauf durch und ersetze JEDEN Platzhalter `##REF_1##` durch `[1]`, `##REF_2##` durch `[2]`, `##REF_X##` durch `[X]` usw. im gesamten Dokument.

**POST PROCESSING:**
* **STUFE 4: FINALES POST PROCESSING (AUF ANFRAGE):** Warte auf meine separate, kurze Anweisung ("Starte jetzt Stufe 4"). Generiere erst DANN aus dem vorliegenden gesamten Dokument den vollständigen LaTeX-Code zum Kopieren. Stelle sicher, dass alle Sonderzeichen (z.B. %, &, $, _) innerhalb des Textes und der Tabellen für die LaTeX-Kompilierung korrekt maskiert (escaped) werden, um Syntaxfehler zu vermeiden.

Datenanforderungen:
**Block 1: Benutzerspezifische Variablen und Annahmen**

* **1.1. Rahmenbedingungen des Portfolios:**
    * Referenzwährung: Schweizer Franken (CHF)
    * Fiktives Anlagekapital: CHF 100'000
    * Anlagehorizont: Langfristig (15+ Jahre)
    * Risikoprofil: Hoch. Das Portfolio soll als detailliertes Muster für einen maximal wachstumsorientierten, langfristigen Vermögensaufbau dienen, der die aktuelle Weltlage berücksichtigt.
    * Anlageziel: Maximaler langfristiger, risikoadjustierter Vermögensaufbau.

* **1.2. Anlageuniversum und Auswahlkriterien (Materials):**
    * Anweisung an die KI: Führe zum Zeitpunkt der Analyse eine dynamische Suche durch, um die optimalen ETFs oder Indexfonds zu identifizieren, die zur Umsetzung der zu definierenden Strategie erforderlich sind. Die Auswahl muss streng nach der folgenden, gewichteten Kriterienhierarchie erfolgen. Ziel ist es, für jede erforderliche Marktabdeckung (z.B. Welt, USA, Europa, EM, Schweiz etc.) den jeweils am besten geeigneten Fonds zu finden.

    * Such- und Auswahlkriterien (priorisierte Reihenfolge):
        1.  **Börsenkotierung:** Ausschliesslich Produkte, die an der SIX Swiss Exchange in CHF gehandelt werden. Falls für eine strategische Anlageklasse kein solcher ETF existiert, begründe die Auswahl einer Alternative in einer anderen Währung (z.B. EUR, USD).
        2.  **Ertragsverwendung:** Ausschliesslich thesaurierende (accumulating, Acc) Fonds.
        3.  **Anlagestrategie:** Konzentriere dich auf breite, marktübliche Kernindizes (z.B. MSCI World, S&P 500, SPI, MSCI Emerging Markets IMI). Keine ESG-, SRI- oder Themen-fokussierten Produkte.
        4.  **Replikationsmethode:** Physische Replikation (vollständig oder optimiertes Sampling) ist stark zu bevorzugen. Synthetische Swaps sind nur als begründete Ausnahme zu erwägen.
        5.  **Anbieter:** Bevorzuge etablierte Anbieter mit grosser Präsenz in der Schweiz (z.B. iShares, UBS, Xtrackers, Vanguard, Swisscanto, Amundi, Invesco).
        6.  **Quantitative Optimierungskriterien (in dieser Reihenfolge zu bewerten):**
            * **Tracking-Differenz (TD):** Kritischstes Qualitätsmerkmal. Wähle den Fonds mit der geringsten negativen bzw. höchsten positiven TD über 1, 3 und 5 Jahre.
            * **Total Expense Ratio (TER):** So tief wie möglich, als sekundäres Kriterium zur TD.
            * **Assets Under Management (AUM):** So hoch wie möglich, um Liquidität und Stabilität sicherzustellen.
            * **Tracking Error (TE):** So tief wie möglich, als Mass für die Volatilität der Abweichung.

* **1.3. Strategische Ziel-Parameter und zu ermittelnde Allokationen:**
    * **Logik der Allokations-Ermittlung:** Deine Kernaufgabe ist es, die folgenden Ziel-Allokationen dynamisch festzulegen. Gehe dabei wie folgt vor:
        1.  **Baseline:** Beginne mit einer Baseline-Allokation, die der globalen Marktkapitalisierung entspricht (z.B. nach MSCI ACWI IMI).
        2.  **Risiko-Analyse:** Führe eine tiefgehende Analyse der Risikofaktoren aus Punkt 1.4 durch.
        3.  **Taktische Anpassung:** Passe die Baseline-Gewichte basierend auf deiner Analyse an. Begründe jede Abweichung von der Marktkapitalisierung explizit als bewusste strategische Entscheidung zur Minderung eines spezifischen Risikos oder zur Nutzung einer identifizierten Chance. Beispielsweise könntest du die Schweiz aufgrund ihrer wahrgenommenen Stabilität im aktuellen Zinsumfeld übergewichten oder die Exposition gegenüber einer Region aufgrund geopolitischer Risiken reduzieren.
    * **Tabelle 1.3.1: Geografische Ziel-Allokation**

| Region | Baseline (Marktkap. %) | Taktische Anpassung (+/- %) | Ziel-Gewichtung % | Begründung der Anpassung |
| :--- | :--- | :--- | :--- | :--- |
| Nordamerika | [zu ermitteln] | [zu ermitteln] | [zu ermitteln] | [Begründung basierend auf Analyse von 1.4] |
| Europa (inkl. CH) | [zu ermitteln] | [zu ermitteln] | [zu ermitteln] | [Begründung basierend auf Analyse von 1.4] |
| Asien-Pazifik | [zu ermitteln] | [zu ermitteln] | [zu ermitteln] | [Begründung basierend auf Analyse von 1.4] |
| Emerging Markets | [zu ermitteln] | [zu ermitteln] | [zu ermitteln] | [Begründung basierend auf Analyse von 1.4] |
| **Total** | **100.0** | **-** | **100.0** | **-** |

    * **Tabelle 1.3.2: Sektorale Ziel-Allokation (als Resultat der geografischen Allokation)**

| Sektor | Ziel-Gewichtung % |
| :--- | :--- |
| Technologie | [zu ermitteln] |
| Gesundheitswesen | [zu ermitteln] |
| Finanzen | [zu ermitteln] |
| Industrie | [zu ermitteln] |
| Zyklische Konsumgüter | [zu ermitteln] |
| Basiskonsumgüter | [zu ermitteln] |
| Energie | [zu ermitteln] |
| Sonstige | [zu ermitteln] |

    * **Tabelle 1.3.3: Ziel-Allokation nach Marktkapitalisierung (als Resultat der Fondsauswahl)**

| Marktkapitalisierung | Ziel-Gewichtung % |
| :--- | :--- |
| Large Cap (>10 Mrd. USD) | [zu ermitteln] |
| Mid Cap (2-10 Mrd. USD) | [zu ermitteln] |
| Small Cap (<2 Mrd. USD) | [zu ermitteln] |

* **1.4. Zu analysierende Risikofaktoren (Risk Framework):**
    * **Währungsrisiko:** Potenzielle USD-Schwäche gegenüber dem CHF (z.B. aufgrund von US-Fiskalpolitik, Zinsdifferenzen, CHF-Status als 'sicherer Hafen').
    * **Geopolitisches Risiko:** Wirtschaftskonflikt USA-China und die strategische Bedeutung von Lieferketten (z.B. Halbleiter aus Taiwan, Abhängigkeit Europas von Energieimporten).
    * **Konjunktur- und Zinsrisiko:** Divergierende Zinspolitik und Inflationsentwicklung (SNB, EZB, Fed) und deren Einfluss auf das Wirtschaftswachstum in den jeweiligen Regionen.
    * **Konzentrationsrisiko:** Risiko einer übermässigen Konzentration auf wenige grosse US-Technologieaktien in globalen Indizes.
    * **KI-gestützte Risikoidentifikation:** Nutze deine analytischen Fähigkeiten, um weitere wichtige Risikofaktoren zu identifizieren, die für das Portfolio im aktuellen globalen Kontext (Stand: heute) relevant sind und hier nicht explizit aufgelistet wurden.

Berichtsstruktur:
**Block 2: ALGORITHMISCHER WORKFLOW ZUR BERICHTERSTELLUNG (STUFE 1 & 2)**

**Executive Summary**
Erstelle eine kurze, prägnante Zusammenfassung für einen zeitkritischen Entscheidungsträger. Nenne das Anlageziel, die finale Portfolio-Allokation und die wichtigsten quantitativen Merkmale. Belege jede Aussage mit einem sicheren Platzhalter `##REF_X##`.

**I. INTRODUCTION**
Leite die Studie ein und definiere Zweck und Ziele basierend auf den Parametern in '1.1. Rahmenbedingungen des Portfolios'.

**II. METHODS**
* **A. Materials and Selection Criteria:** Beschreibe das Anlageuniversum und die strengen, priorisierten Auswahlkriterien aus Abschnitt '1.2.'.
* **B. Target Allocation Strategy:** Präsentiere die in Abschnitt '1.3.' hergeleitete Ziel-Allokation und die dazugehörige Begründungstabelle '1.3.1'.
* **C. Analytical Process:** Erkläre, dass eine vergleichende Analyse zur Auswahl der optimalen ETFs durchgeführt wird. Detailliere hier die Methodik zur Ermittlung von TD und TE:
    * **Tracking-Differenz (TD):** Die Angabe der TD ist für 1, 3 und 5 Jahre (p.a., falls möglich) zwingend. Falls nicht direkt publiziert, **musst du sie berechnen**. Greife auf das offizielle, aktuellste Factsheet des Fonds zu. Finde eine Tabelle, die die kumulierte Wertentwicklung des Fonds und der Benchmark für denselben Zeitraum ausweist. Berechne die TD mit der Formel: $TD = \text{Fonds-Gesamtrendite in \%} - \text{Benchmark-Gesamtrendite in \%}$. Falls für einen Zeitraum keine Daten verfügbar sind, markiere dies mit "n.v." und begründe es kurz.
    * **Tracking Error (TE):** Gib den publizierten TE für 1, 3 und 5 Jahre an. Falls nicht publiziert, gib "n.v." an. **Berechne den TE nicht selbst.**

**III. RESULTS**
* **A. Comparative Analysis and ETF Selection:** Führe eine erschöpfende Recherche durch und befülle die folgende Master-Tabelle. Diese Tabelle ist die 'Single Source of Truth'. Jede Zelle muss mit den aktuellsten verfügbaren Daten befüllt und mit einem `##REF_X##`-Platzhalter zitiert werden. Begründe die Auswahl des "Gewinner"-ETFs pro Kategorie direkt unter der Tabelle unter Bezugnahme auf die Daten.
    * **Tabelle III-1: ETF-Vergleichsmatrix**

| Kategorie | Fondsname | ISIN | Anbieter | Repl.-Methode | Fd.-Währung | TER % p.a. | AUM (Mio CHF) | TD 1J % | TD 3J % p.a. | TD 5J % p.a. | TE 3J % | Auswahl (Ja/Nein) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Welt** | [Fondsname 1] | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | Nein |
| | [Fondsname 2] | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | **Ja** |
| **Schweiz**| [Fondsname 3] | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## | **Ja** |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

* **B. Final Portfolio Composition:** Zeige die finale Umsetzung des Portfolios.
    * **Tabelle III-2: Finale Portfolio-Zusammenstellung**

| Fd-Name | ISIN | Hand.-Platz | Zielallok. % | Kurs (CHF) | Anz. Anteile zu kaufen | Betrag (CHF) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Fondsname 2] | ##REF_X## | SIX | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## |
| [Fondsname 3] | ##REF_X## | SIX | ##REF_X## | ##REF_X## | ##REF_X## | ##REF_X## |
| **Total** | | | **100.0** | | | **ca. 100'000**|

* **C. Aggregated Portfolio Characteristics:** Präsentiere die aggregierten Eigenschaften des finalen Portfolios und vergleiche sie mit den Zielvorgaben.
    * **Tabelle III-3: Effektive Geografische Diversifikation**

| Region | Ziel-Gewichtung % | Effektive Gewichtung % | Abweichung (abs. %) |
| :--- | :--- | :--- | :--- |

    * **Tabelle III-4: Effektive Sektorale Diversifikation**

| Sektor | Effektive Gewichtung % |
| :--- | :--- |

    * **Tabelle III-5: Look-Through-Analyse der Top-15-Positionen**

| Nr. | Unternehmen | Land | Sektor | Gewicht im Portfolio % |
| :--- | :--- | :--- | :--- | :--- |

**IV. DISCUSSION**
Interpretiere die Ergebnisse aus Abschnitt III im Kontext der Risikofaktoren aus '1.4.'. Belege jede Aussage mit `##REF_X##`.
* **A. Analysis of Defined Risks:** Analysiere jeden Risikofaktor aus 1.4. Strukturiere die Analyse pro Faktor:
    1.  **Lagebeurteilung:** Fasse die aktuelle Lage zum Risiko zusammen `##REF_X##`.
    2.  **Quantitative Exposition:** Quantifiziere die Exposition des Portfolios unter Verwendung der Daten aus den Tabellen III-3, III-4, und III-5.
    3.  **Beurteilung & Fazit:** Beurteile den potenziellen Einfluss und begründe, warum die gewählte Portfoliostruktur angesichts dieses Risikos als robust oder anfällig eingeschätzt wird.
* **B. Additional Risks Identified:** Identifiziere und diskutiere weitere signifikante Risiken, die sich aus der Analyse ergeben (z.B. hohe Konzentration in Top-15-Positionen aus Tabelle III-5).
* **C. Risk Dashboard Summary:** Fasse die Ergebnisse in einer Tabelle zusammen.
    * **Tabelle IV-1: Quantitatives Risiko-Dashboard**

| Risikofaktor | Quantitative Portfolio-Exposure (%) | Qualitative Begründung der Exposure | Bewerteter Einfluss (Tief/Mittel/Hoch) |
| :--- | :--- | :--- | :--- |
| Währungsrisiko (z.B. % non-CHF) | ##REF_X## | ##REF_X## | ##REF_X## |
| Geopolitik (z.B. % China+Taiwan) | ##REF_X## | ##REF_X## | ##REF_X## |
| Zinsrisiko (z.B. % zinssensitive Sektoren) | ##REF_X## | ##REF_X## | ##REF_X## |
| Konzentration (Top-15-Gewicht) | ##REF_X## | ##REF_X## | ##REF_X## |
| [Weiteres identifiziertes Risiko] | ##REF_X## | ##REF_X## | ##REF_X## |

**V. CONCLUSION**
Fasse die wichtigsten Erkenntnisse zusammen. Gib eine abschliessende Bewertung, inwieweit das konstruierte Portfolio die in der Einleitung genannten Ziele unter Berücksichtigung der diskutierten Risiken erreicht.

**ACKNOWLEDGEMENTS**
Füge einen Platzhalter für Danksagungen ein.

**REFERENCES**
Erstelle eine nummerierte Liste aller zitierten Quellen (`##REF_X##`). Die Liste muss numerisch nach der Reihenfolge des Erscheinens im Text geordnet sein. Formatiere jeden Eintrag strikt nach dem IEEE Documentation Style.

**APPENDIX**
* **A. Table of Tables:** Liste aller Tabellen im Bericht mit Nummer und Titel.
* **B. List of Abbreviations:** Liste aller verwendeten Abkürzungen (z.B. ETF, AUM, TER, TD, TE) und deren Bedeutung.

**DISCLAIMER**
Beende deine Antwort zwingend mit dem folgenden, exakt formulierten Disclaimer.
* Diese Studie ist weder eine persönliche Anlageberatung noch eine Aufforderung oder Empfehlung zum Kauf oder Verkauf von Finanzinstrumenten. Die hier dargestellten Informationen und Berechnungen basieren auf öffentlich zugänglichen Daten, deren Genauigkeit und Aktualität nicht garantiert werden kann. Jede Anlageentscheidung birgt Risiken, einschliesslich des potenziellen Verlusts des eingesetzten Kapitals. Vor jeder Investition sollte eine individuelle Beratung durch einen qualifizierten Finanzexperten eingeholt werden.