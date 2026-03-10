<div align="center">

<img src="https://github.com/simentob.png" width="100" style="border-radius: 50%" />

# Optimeringskurs

**Matematisk optimering med Pyomo**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pyomo](https://img.shields.io/badge/Pyomo-Optimering-orange?style=for-the-badge)](http://www.pyomo.org/)
[![GLPK](https://img.shields.io/badge/Solver-GLPK-green?style=for-the-badge)](https://www.gnu.org/software/glpk/)
[![IPOPT](https://img.shields.io/badge/Solver-IPOPT-blue?style=for-the-badge)](https://coin-or.github.io/Ipopt/)

![Last commit](https://img.shields.io/github/last-commit/simentob/Optimeringskurs?style=flat-square&color=blueviolet)
![Repo size](https://img.shields.io/github/repo-size/simentob/Optimeringskurs?style=flat-square&color=blueviolet)

</div>

<br>

> Løsninger på reelle optimeringsproblemer med [Pyomo](http://www.pyomo.org/) - fra fabrikkstyring til aluminiumssmelting.

<br>

## Oppgaver

<details>
<summary><b>🏭 fabrikk.py -Produksjonsoptimering (LP)</b></summary>
<br>

Maksimerer fortjeneste i en fabrikk som produserer to produkter, med begrensninger på produksjonskostnad, CO₂-utslipp og malingstimer.

**Solver:** GLPK

</details>

<details>
<summary><b>📍 optimering.py -Lokasjonoptimering (NLP)</b></summary>
<br>

Finner den optimale plasseringen av et nytt kontor basert på vektede avstander til eksisterende kontorer i Pakistan.

**Solver:** IPOPT

</details>

<details>
<summary><b>💧 hydro.py -Legeringsoptimering (LP)</b></summary>
<br>

Produksjonsplanlegging for et aluminiumssmelteri. Finner den billigste blandingen av råmaterialer for å treffe kjemiske krav (Si, Fe, Mg).

- **Del 1:** Optimaliser én charge på 20 tonn
- **Del 2:** Optimaliser alle ordre fra `orders.csv` med delt lagerbeholdning

**Solver:** GLPK

</details>

<br>

## Kom i gang

```bash
pip install pyomo pandas
brew install glpk ipopt   # macOS
```

```bash
python fabrikk.py
python optimering.py
python hydro.py
```

<br>

## Data

| Fil | Beskrivelse |
|-----|-------------|
| `materials.csv` | Tilgjengelige råmaterialer med kjemisk sammensetning og lager |
| `orders.csv` | Ordre med vekt og kjemiske krav per legering |

<br>

<div align="center">
  <sub>av <a href="https://github.com/simentob">simentob</a> · 2026</sub>
</div>
