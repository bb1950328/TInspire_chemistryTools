
# Chemie Abschlussprüfung 2021

[Datenquelle Periodensystem](https://www.data-explorer.com/data/)

[TI Nspire™ CX II Python docs](https://education.ti.com/en/products/calculators/graphing-calculators/ti-nspire-cx-ii-cx-ii-cas/programming-in-python)

## Wichtig
* **KEINE GARANTIE AUF KORREKTHEIT**
* Nehmt euch den Code nicht als Vorbild, er ist nicht besonders schön
* Die meisten Menüs können verlassen werden, indem man nichts eingibt (einfach `enter` drücken)
* Zum Teil können Sachen gemacht werden, die in Realität gar nicht gehen (z.B. organische Namen und Strukturen werden viel zu wenig validiert)

## Auf den Rechner laden
1. TI Nspire CX CAS Student Software starten
1. Neues Dokument
1. Neues Python-Skript, "main.py" nennen
1. Von [hier](https://raw.githubusercontent.com/bb1950328/ChemistryFinals2021/master/main.py) alles kopieren und einfügen
1. Menu "File" > "Save to Handheld"
1. Auf dem Rechner öffnen und Ctrl+R drücken zum ausführen

## 1 Element-Info
Elementsymbol oder Name eingeben. Vom besten Treffer werden Daten angezeigt:
```
Symbol oder Name eingeben: Au
Protonenzahl: 79
Name: Gold
Symbol: Au
Relative Atommasse: 196.966569
Periode: 6
Gruppe: 11
Zustand: solid
Typ: Übergangsmetall
Atomradius: 1.8
Elektronegativität: 2.54
Dichte: 19.282
Schmelzpunkt (K): 1337.73
Siedepunkt (K): 3129
Isotope: 21
Elektronenkonfiguration: [Xe] 4f14 5d10 6s1
Symbol oder Name eingeben: 58fe
⁵⁸Fe könnte ein Eisen-Isotop mit 26 Protonen und 32 Neutronen sein.
```

## 2 Bohr'sches Atommodell
Elementsymbol angeben. Es werden Infos angezeigt für das Bohr'sche Atommodell:
```
Elementsymbol eingeben: cl
Elektronenvereilung von Chlor
Schale K 2 von 2 Elektronen
Schale L 8 von 8 Elektronen
Schale M 7 von 18 Elektronen
Kern: 17 Protonen und ca. 18.453000000000003 Neutronen
```

## 3 Delta-EN
Es können zwei oder mehr Elementsymbole eingegeben werden. Bei zwei werden die Elektronegativitäten ausgegeben. Bei drei oder mehr wird eine Tabelle mit allen Kombinationen und deren EN-Deltas ausgegeben: 
```
Mehrere Elementsymbole eingeben (mit Abstand getrennt): H Li
ΔEN = 1.12 (EN von Wasserstoff = 2.1 und EN von Lithium = 0.98
```
```
Mehrere Elementsymbole eingeben (mit Abstand getrennt): H Li Na Ca
     H    Li   Na   Ca  
H    0.0  1.12 1.17 1.1 
Li   1.12 0.0  0.05 0.02
Na   1.17 0.05 0.0  0.07
Ca   1.1  0.02 0.07 0   
```

## 4 Organischer Namens-Decoder
Namen eines organischen Moleküls eingeben:
```
Name einer organischen Verbindung: >? 5-Ethyl-2,3-dimethyl-4-propylheptan
1  C
   |
2  C-C
   |
3  C-C
   |
4  C-C-C-C
   |
5  C-C-C
   |
6  C
   |
7  C
Summenformel: C₇H₁₆
```

## 5 Organischer Namens-Encoder
Umkehrfunktion von Tool 4. Interaktive Eingabe der Struktur und anschliessende Ausgabe der Summenformel und des Namens:
```
Stammlänge: 5
Index Seitenkette (leer lassen zum Beenden): 2
Länge der Seitenkette: 1
Index Seitenkette (leer lassen zum Beenden): 2
Länge der Seitenkette: 1
Index Seitenkette (leer lassen zum Beenden): 4
Länge der Seitenkette: 1
Index Seitenkette (leer lassen zum Beenden): 
Summenformel: C₈H₁₈
2,2,4-trimethylpentan
```

## 6 Reaktionsgleichung ausgleichen
Reaktionsgleichung eingeben (`->` als Reaktionspfeil). Tool berechnet die Koeffizienten automatisch. Redoxreaktionen o.ä. aktuell nicht unterstützt.
```
Bitte Reaktionsgleichung eingeben: CH4 + O2 -> CO2 + H2O
CH₄ + O₂ -> CO₂ + H₂O
CH₄ + 2O₂ -> CO₂ + 2H₂O
```
```
Bitte Reaktionsgleichung eingeben: CH3CH2OH + O2 -> CO2 + H2O
CH₃CH₂OH + O₂ -> CO₂ + H₂O
CH₃CH₂OH + 3O₂ -> 2CO₂ + 3H₂O
```
```
Bitte Reaktionsgleichung eingeben: Zn + AuCl3 -> ZnCl2 + Au
Zn + AuCl₃ -> ZnCl₂ + Au
3Zn + 2AuCl₃ -> 3ZnCl₂ + 2Au
```
