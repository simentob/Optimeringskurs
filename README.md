<div align="center">

<img src="https://github.com/simentob.png" width="120" style="border-radius: 50%" />

# Optimeringskurs

**Matematisk optimering med Pyomo — lineær og ikke-lineær programmering**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pyomo](https://img.shields.io/badge/Pyomo-Optimering-orange?style=for-the-badge)](http://www.pyomo.org/)
[![GLPK](https://img.shields.io/badge/Solver-GLPK-green?style=for-the-badge)](https://www.gnu.org/software/glpk/)
[![IPOPT](https://img.shields.io/badge/Solver-IPOPT-blue?style=for-the-badge)](https://coin-or.github.io/Ipopt/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## Om prosjektet

Dette repoet inneholder oppgaver og løsninger fra **BRAINFood Optimeringskurs**. Koden bruker [Pyomo](http://www.pyomo.org/) — et kraftig Python-rammeverk for matematisk optimering — til å modellere og løse lineære og ikke-lineære optimeringsproblemer fra virkeligheten.

---

## Oppgaver

### 🏭 `fabrikk.py` — Produksjonsoptimering (LP)
Maksimering av fortjeneste i en fabrikk som produserer to produkter (A og B), med begrensninger på:
- Total produksjonskostnad
- CO₂-utslipp
- Tilgjengelige malingstimer

**Solver:** GLPK (lineær programmering med heltallsvariable)

---

### 📍 `optimering.py` — Lokasjonoptimering (NLP)
Finn den optimale plasseringen av et nytt kontor basert på vektede avstander til eksisterende kontorer i Pakistan (Lahore, Islamabad, Muzaffarabad, Peshawar).

**Solver:** IPOPT (ikke-lineær programmering)

---

### 💧 `hydro.py` — Legeringsoptimering for Norsk Hydro (LP)
Produksjonsplanlegging for aluminiumssmelteri. Finner den billigste blandingen av råmaterialer og skrapmetall for å oppfylle kjemiske krav (Si, Fe, Mg) til ønsket legering.

- **Del 1:** Optimaliser én charge på 20 tonn
- **Del 2:** Optimaliser alle ordre fra `orders.csv` samtidig, med delt lagerbeholdning på tvers

**Solver:** GLPK (lineær programmering)

---

## Kom i gang

### Krav
- Python 3.10+
- [Pyomo](http://www.pyomo.org/)
- GLPK og/eller IPOPT installert

### Installer avhengigheter

```bash
pip install pyomo
```

Installer solvere (macOS):
```bash
brew install glpk
brew install ipopt
```

### Kjør et eksempel

```bash
python fabrikk.py
python optimering.py
python hydro.py
```

---

## Data

| Fil | Beskrivelse |
|-----|-------------|
| `materials.csv` | Materialdata for produksjonsoppgaven |
| `orders.csv` | Ordredata |
| `BRAINFood___Optimering_oppgave_1.pdf` | Oppgavetekst 1 |
| `BRAINFood___Optimering_oppgave_2.pdf` | Oppgavetekst 2 |

---

<div align="center">
  <sub>Laget av <a href="https://github.com/simentob">simentob</a> · BRAINFood 2026</sub>
</div>
