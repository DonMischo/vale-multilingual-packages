# Vale Multilingual Style Packages

Prose style rules for [Vale](https://vale.sh) covering German, English, and several other European languages. Installable as Vale packages via `vale sync` — the same way you install [write-good](https://github.com/errata-ai/write-good) or [proselint](https://github.com/errata-ai/proselint).

---

## Available packages

| Package | Language | Status |
|---|---|---|
| `Foliantica-DE` | German (Deutsch) | ✅ Complete (10 rules) |
| `Foliantica-EN` | English | ✅ Complete |
| `Foliantica-ES` | Spanish (Español) | ✅ Complete |
| `Foliantica-FR` | French (Français) | ✅ Complete |
| `Foliantica-PT` | Portuguese (Português) | ✅ Complete |
| `Foliantica-IT` | Italian (Italiano) | ✅ Complete |
| `Foliantica-SV` | Swedish (Svenska) | ✅ Complete |
| `Foliantica-DA` | Danish (Dansk) | ✅ Complete |
| `Foliantica-NO` | Norwegian (Norsk) | ✅ Complete |

All packages are complete with 8 rules each. Contributions to expand coverage are welcome.

> **Note on English:** `Foliantica-EN` focuses on gaps not covered by the popular [write-good](https://github.com/errata-ai/write-good) and [proselint](https://github.com/errata-ai/proselint) packages — specifically pleonasm/redundancy detection and nominalization. Use it alongside those packages for full coverage.

---

## Installation

### 1. Add the package URL to your `.vale.ini`

```ini
StylesPath = styles
MinAlertLevel = suggestion

# Replace Foliantica-DE with the package for your language
Packages = https://github.com/DonMischo/vale-multilingual/releases/latest/download/Foliantica-DE.zip

[*.md]
BasedOnStyles = Foliantica-DE
Vale.Spelling = NO
```

### 2. Run `vale sync`

```bash
vale sync
```

Vale downloads the ZIP and extracts it into your `StylesPath`. You're done.

### Combining with other packages

```ini
StylesPath = styles
Packages = write-good, proselint, https://github.com/DonMischo/vale-multilingual/releases/latest/download/Foliantica-DE.zip

[*.md]
BasedOnStyles = Vale, write-good, proselint, Foliantica-DE
Vale.Spelling = NO
```

> **Note:** `Vale.Spelling = NO` suppresses Vale's built-in English spell checker, which would flag most non-English words as errors.

---

## Rule descriptions

### WeaselWords *(existence)*
Flags vague or filler words that weaken prose — hedging adverbs (*eigentlich*, *irgendwie*, *sehr*), epistemic hedges (*anscheinend*, *vermeintlich*), bureaucratic filler (*diesbezüglich*, *dahingehend*), vague time expressions (*zeitnah*, *in absehbarer Zeit*), and relativising phrases (*sogenannte*, *im wahrsten Sinne des Wortes*).

### Redundancy *(substitution)*
Catches pleonasms — phrases where a modifier repeats information already in the noun. **German (DE):** adjective-in-noun tautologies (*tote Leiche*, *weißer Schimmel*, *neues Novum*), directional redundancies (*aufwärts steigen*, *wieder zurück*), RAS-syndrome acronyms (*PIN-Nummer*, *ADAC-Club*, *API-Schnittstelle*), and temporal redundancies (*vergangene Geschichte*, *künftige Zukunft*). **English (EN):** (*end result*, *unexpected surprise*, *past history*, *revert back*, *cooperate together*, *very unique*, *PIN number*, *ATM machine*).

### Passive *(existence)*  
Flags passive constructions (*wurde*, *wurden*, *worden*, sein+zu+Infinitiv) as suggestions to prefer active voice.

### NominalStyle *(substitution)*
Flags stretched noun-verb constructions — the "zombie noun" pattern described by Joseph M. Williams and Helen Sword. **German (DE):** *Funktionsverbgefüge* (*eine Entscheidung treffen* → *entscheiden*, *zur Kenntnis nehmen* → *beachten*). **English (EN):** function verb constructions (*make a decision* → *decide*, *conduct an analysis* → *analyze*, *be in possession of* → *possess*, *provide clarification* → *clarify*).

### WordyPhrases *(substitution, DE only)*
Flags inflated prepositional phrases from *Amtsdeutsch* (*im Hinblick auf* → *für*, *aufgrund der Tatsache dass* → *weil*, *in hohem Maße* → *sehr*). Based on the Bundesverwaltungsamt plain-language guide.

### ReflexiveVerbs *(substitution, DE only)*
Flags bloated reflexive constructions that can be replaced with a simpler verb (*befindet sich* → *ist*, *erweist sich als* → *ist*, *vollzieht sich* → *geschieht*). Based on Wolf Schneider's and Ludwig Reiners's critiques of *aufgeblähte Verben*.

### Klischees *(existence, DE only)*
Flags worn-out idioms, overused metaphors, and journalistic filler that signal lazy writing. Four categories: everyday idioms (*am Ende des Tages*, *ein Stück weit*, *ins Boot holen*, *in trockene Tücher bringen*); sports metaphors used outside sport (*am Ball bleiben*, *auf der Zielgeraden*, *ins eigene Tor schießen*); political boilerplate (*kein Denkverbot*, *konstruktiver Dialog*, *breiter Konsens*); journalistic clichés (*wie aus dem Nichts*, *totales Chaos*, *historischer Moment*, *neues Kapitel aufschlagen*). Based on Wolf Schneider's and Ludwig Reiners's catalogues of *abgedroschene Wendungen*.

---

## Attribution & sources

All rules are derived from the following authoritative style guides. All credit for the underlying guidance belongs to the original authors.

> **Note on AI-assisted content:** The rule entries in these packages were generated with the help of a large language model (Claude by Anthropic), working from the cited sources. Every source listed below is real and the underlying guidance is genuine — but individual entries have not been manually verified against the original texts one by one. If you spot an error or a false positive, please [open an issue](https://github.com/DonMischo/vale-multilingual/issues).

### German (Foliantica-DE)

| Author | Work | Year | Relevant rules |
|---|---|---|---|
| **Wolf Schneider** | *Deutsch fürs Leben* (Rowohlt) | 1994 | WeaselWords, NominalStyle, WordyPhrases |
| **Wolf Schneider** | *Deutsch! Das Handbuch für attraktives Schreiben* (Rowohlt) | 2005 | WeaselWords, WordyPhrases |
| **Bastian Sick** | *Der Dativ ist dem Genitiv sein Tod*, Bd. 1–3 (Kiepenheuer & Witsch) | 2004– | Redundancy, WeaselWords |
| **Bastian Sick** | Zwiebelfisch-Kolumnen (Spiegel Online) | 2003– | Redundancy, WeaselWords |
| **Ludwig Reiners** | *Stilkunst* (C.H. Beck) | 1944 / rev. 1991 | NominalStyle (Funktionsverbgefüge) |
| **Bundesverwaltungsamt** | *Leitfaden Bürgernahe Sprache* | 2002 | WordyPhrases, Passive |
| **Bundesministerium für Justiz** | *Handbuch der Rechtsförmlichkeit* (3. Aufl.) | 2008 | NominalStyle, WordyPhrases |
| **Duden** | *Richtiges und gutes Deutsch* (Bd. 9) / *Das Stilwörterbuch* (Bd. 2) | 2010 | Redundancy |
| **Institut für Deutsche Sprache** | Grammis-Datenbank, *Funktionsverbgefüge* | ongoing | NominalStyle |
| **Netzwerk Leichte Sprache** | *Regeln für Leichte Sprache* | 2013 | WeaselWords, WordyPhrases |
| **Wikipedia** | [Liste der Pleonasmen](https://de.wikipedia.org/wiki/Pleonasmus) | ongoing | Redundancy |
| **Wikipedia** | [RAS-Syndrom](https://de.wikipedia.org/wiki/RAS-Syndrom) | ongoing | Redundancy (acronyms) |

### English (Foliantica-EN)

| Author | Work | Year | Relevant rules |
|---|---|---|---|
| **William Strunk & E.B. White** | *The Elements of Style* (Macmillan) | 1959 | Redundancy |
| **William Zinsser** | *On Writing Well* (HarperCollins) | 1976 | Redundancy, NominalStyle |
| **Joseph M. Williams** | *Style: Lessons in Clarity and Grace* (Pearson) | 2014 | NominalStyle |
| **Helen Sword** | "Zombie Nouns" (New York Times Opinionator) | 2012 | NominalStyle |
| **Bryan A. Garner** | *Garner's Modern English Usage* (OUP, 4th ed.) | 2016 | Redundancy, NominalStyle |
| **Plain English Campaign** | *The A to Z of Alternative Words* | 2000 | NominalStyle |
| **UK Government Digital Service** | Content Design Guide | ongoing | NominalStyle |
| **Wikipedia** | [List of English pleonasms](https://en.wikipedia.org/wiki/Pleonasm) | ongoing | Redundancy |

### Spanish (Foliantica-ES)

| Author / Body | Work | Year | Relevant rules |
|---|---|---|---|
| **Real Academia Española** | *Diccionario panhispánico de dudas* | 2005 | Redundancy, ErroresComunes |
| **Real Academia Española** | *Ortografía de la lengua española* | 2010 | Redundancy |
| **Fundéu** | Style recommendations (fundeu.es) | ongoing | WeaselWords, WordyPhrases |
| **Manuel Seco** | *Diccionario de dudas y dificultades de la lengua española* (Espasa, 10th ed.) | 1998 | ErroresComunes |
| **Gobierno de España** | *Manual de estilo del lenguaje administrativo* (MAP) | 1990 | WordyPhrases, Passive |
| **Wikipedia** | [Pleonasmo (es)](https://es.wikipedia.org/wiki/Pleonasmo) | ongoing | Redundancy |

### French (Foliantica-FR)

| Author / Body | Work | Year | Relevant rules |
|---|---|---|---|
| **Académie française** | *Dictionnaire de l'Académie française* (9th ed.) | ongoing | Redundancy, FauxAmis |
| **Maurice Grevisse & André Goosse** | *Le bon usage* (De Boeck, 16th ed.) | 2016 | NominalStyle, WordyPhrases |
| **Office québécois de la langue française** | *Le grand dictionnaire terminologique* | ongoing | Anglicismes |
| **Michèle Lenoble-Pinson** | *Anglicismes et substituts français* (De Boeck) | 1991 | Anglicismes |
| **Gouvernement du Québec / OQLF** | *Guide du rédacteur* | 2011 | WordyPhrases, Passive |
| **Wikipedia** | [Pléonasme (fr)](https://fr.wikipedia.org/wiki/Pl%C3%A9onasme) | ongoing | Redundancy |

### Portuguese (Foliantica-PT)

| Author / Body | Work | Year | Relevant rules |
|---|---|---|---|
| **Secretaria de Comunicação Social (SECOM)** | *Manual de Redação da Presidência da República* (Brazil, 3rd ed.) | 2018 | WordyPhrases, Passive |
| **Pasquale Cipro Neto & Ulisses Infante** | *Gramática da língua portuguesa* (Scipione) | 2008 | NominalStyle, Redundancy |
| **Celso Cunha & Lindley Cintra** | *Nova Gramática do Português Contemporâneo* (Fundação Calouste Gulbenkian) | 2014 | NominalStyle |
| **Cândido de Figueiredo** | *Dicionário da língua portuguesa* | ongoing | FalsosAmigos |
| **Wikipedia** | [Estrangeirismo (pt)](https://pt.wikipedia.org/wiki/Estrangeirismo) | ongoing | Estrangeirismos |
| **Wikipedia** | [Pleonasmo (pt)](https://pt.wikipedia.org/wiki/Pleonasmo) | ongoing | Redundancy |

### Italian (Foliantica-IT)

| Author / Body | Work | Year | Relevant rules |
|---|---|---|---|
| **Luca Serianni** | *Grammatica italiana* (UTET) | 1989 | NominalStyle, Redundancy |
| **Accademia della Crusca** | Linguistic guidance (accademiadellacrusca.it) | ongoing | FalsiAmici, WeaselWords |
| **Presidenza del Consiglio dei Ministri** | *Manuale di stile* | 1997 | WordyPhrases, Passive |
| **Bice Mortara Garavelli** | *Manuale di retorica* (Bompiani) | 1988 | Redundancy |
| **Wikipedia** | [Forestierismo (it)](https://it.wikipedia.org/wiki/Forestierismo) | ongoing | Anglicismi |
| **Wikipedia** | [Pleonasmo (it)](https://it.wikipedia.org/wiki/Pleonasmo) | ongoing | Redundancy |

### Swedish (Foliantica-SV)

| Author / Body | Work | Year | Relevant rules |
|---|---|---|---|
| **Språkrådet** | *Svenska skrivregler* (Liber, 4th ed.) | 2017 | WordyPhrases, Passive, Redundancy |
| **Språkrådet** | *Myndigheternas skrivregler* (8th ed.) | 2014 | WordyPhrases, WeaselWords |
| **Svenska Akademien** | *Svenska Akademiens ordlista* (SAOL, 14th ed.) | 2015 | SprakFel |
| **Erik Wellander** | *Riktig svenska* (Esselte, 4th ed.) | 1973 | NominalStyle, Redundancy |
| **Wikipedia** | [Pleonasm (sv)](https://sv.wikipedia.org/wiki/Pleonasm) | ongoing | Redundancy |

### Danish (Foliantica-DA)

| Author / Body | Work | Year | Relevant rules |
|---|---|---|---|
| **Dansk Sprognævn** | *Retskrivningsordbogen* (4th ed.) | 2012 | SprogFejl |
| **Dansk Sprognævn** | Klarsprog recommendations (dsn.dk) | ongoing | WordyPhrases, WeaselWords, Passive |
| **Peter Becker-Christensen** | *Politikens Nudansk Ordbog* (20th ed.) | 2010 | Redundancy |
| **Wikipedia** | [Pleonasme (da)](https://da.wikipedia.org/wiki/Pleonasme) | ongoing | Redundancy |

### Norwegian (Foliantica-NO)

| Author / Body | Work | Year | Relevant rules |
|---|---|---|---|
| **Språkrådet** | *Bokmålsordboka / Nynorskordboka* | ongoing | SprakFeil |
| **Språkrådet** | Klarspråk guidelines (sprakradet.no/klarsprak) | ongoing | WordyPhrases, WeaselWords, Passive |
| **Erik Egeberg** | *Norsk stilistikk* (Universitetsforlaget) | 2003 | NominalStyle, Redundancy |
| **Wikipedia** | [Pleonasme (no)](https://no.wikipedia.org/wiki/Pleonasme) | ongoing | Redundancy |

---

## Using with Foliantica

These packages were created as part of the development of [Foliantica](https://github.com/DonMischo/foliantica), a writing app for authors — and are published here as a standalone resource for anyone who wants to use them with Vale directly. Foliantica injects the appropriate language package at request time based on the project's language setting.

---

## Contributing

1. Fork the repo and edit the YAML files in `styles/Foliantica-XX/`
2. Keep entries in categorised comment blocks with source attribution
3. Avoid entries that generate frequent false positives
4. Run `python tests/test_yaml_validity.py` before opening a PR — it checks every
   file parses, has the required Vale fields, and that `substitution` rules don't
   contain corrupted swap values (a real bug class found and fixed in this repo)
5. Open a PR describing the source for new entries

Vale rule format reference: [vale.sh/docs/topics/styles](https://vale.sh/docs/topics/styles/)

---

## License

MIT. Rule *content* is derived from published style guides; all intellectual credit for the underlying guidance belongs to the original authors listed above.
