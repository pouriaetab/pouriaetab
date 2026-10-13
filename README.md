<div align="center">

<img src="./assets/headline.svg" alt="Statistics · Data Science · Business · Product" width="720" />

<img src="https://komarev.com/ghpvc/?username=pouriaetab&color=58a6ff&style=flat-square&label=profile+views" alt="" width="1" height="1" />

</div>

---

### About me

```yaml
focus      : statistics · data science · business · product
degree     : M.S. Statistics (Data Science concentration)
experience : autonomous driving · automation · analytics
status     : open to new opportunities · open to relocation
```

- 📊 I turn messy data into clear reports and decisions people can act on
- ⚙️ I build lightweight web apps and automations that take manual work off people's plates

---

<!-- PINNED:START -->
### Pinned

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/pouriaetab/glassbox"><b>📌 glassbox</b></a><br>
<sub>A statistical decision pipeline with its validation, risk gates and failure history rendered live. Built as an engineering demonstration; the measured result is negative.</sub><br><br>
<img src="https://img.shields.io/badge/Python-3572A5?style=flat-square" alt="Python" />
</td>
<td width="50%" valign="top">
<a href="https://github.com/pouriaetab/av-fleet-evt"><b>📌 av-fleet-evt</b></a><br>
<sub>Generation aware extreme value estimation for AV fleet safety validation under heterogeneous sensor generation detection floors. Methods paper plus synthetic simulation.</sub><br><br>
<img src="https://img.shields.io/badge/TeX-3D6117?style=flat-square" alt="TeX" />
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/pouriaetab/tracebench"><b>📌 tracebench</b></a><br>
<sub>A verification and validation reference project: requirements traced to tests, known truth validation, calibration and an offline A/B test, run on live market data as a test bed.</sub><br><br>
<img src="https://img.shields.io/badge/Python-3572A5?style=flat-square" alt="Python" />
</td>
<td width="50%" valign="top">
<a href="https://github.com/pouriaetab/localdeck"><b>📌 localdeck</b></a><br>
<sub>A local control panel to start, stop, watch and open all your local web apps from one browser tab.</sub><br><br>
<img src="https://img.shields.io/badge/Python-3572A5?style=flat-square" alt="Python" />
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/pouriaetab/llmledger"><b>📌 llmledger</b></a><br>
<sub>   What happens to an LLM after it is added to LiteLLM&#x27;s price catalogue: competing risks survival analysis of price changes, retirements and removals.</sub><br><br>
<img src="https://img.shields.io/badge/Python-3572A5?style=flat-square" alt="Python" />
</td>
</tr>
</table>

---
<!-- PINNED:END -->

### More projects

<details>
<summary><b>AV safety tools and data science notebooks</b></summary>

<br>

| Project | What it does |
|:--|:--|
| 🛡️ **[av-safety-workbench](https://github.com/pouriaetab/av-safety-workbench)** | Risk assessment workbench where every number carries its method, assumptions, uncertainty and data source. Python + React, runs fully local, 86 tests. |
| 🤖 **[av-safety-triage-agent](https://github.com/pouriaetab/av-safety-triage-agent)** | LLM agent that investigates flagged events with read only tools and proposes a severity for human review, scored against hidden ground truth. |
| 🧰 **[ds-toolkit](https://github.com/pouriaetab/ds-toolkit)** · **[automate-eda](https://github.com/pouriaetab/automate-eda)** | Notebooks on statistical methods, ML and NLP, and a tool that generates EDA notebooks automatically. |

</details>

---

### In the lab (private builds)

- **Control deck.** One local launcher that starts, stops and assigns ports to all my webapps so they never collide.

---

### How I design systems

```mermaid
flowchart LR
    A[Synthetic data<br/>known ground truth] --> C[(Local store)]
    B[Real data<br/>CSV / SQL import] --> C
    C --> D[Estimators<br/>EVT · Bayesian · design effect]
    D --> E[Audit trail<br/>formula · n · assumptions · CI]
    E --> F[Dashboard]
    F --> G{Human sign off}
    H[Rule layer flags event] --> I[LLM agent<br/>read only tools]
    I --> J[Structured verdict<br/>with cited evidence]
    J --> G
```

1. No number without its sample size and its uncertainty.
2. When the evidence is thin, say "insufficient evidence" instead of guessing.
3. Deterministic rules decide what counts. LLMs investigate and explain. People sign off.
4. Test on synthetic data with known answers before trusting real data.
5. Local first. Nothing leaves the machine unless it has to.

---

### Tech stack

**Languages**
<br>
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white)

**Statistics and ML**
<br>
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189FDD?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

**Apps, data and AI**
<br>
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black)
![Claude](https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=anthropic&logoColor=white)

**Tools**
<br>
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Looker](https://img.shields.io/badge/Looker-4285F4?style=flat-square&logo=looker&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=flat-square&logo=jira&logoColor=white)
![Zenodo](https://img.shields.io/badge/Zenodo-1682D4?style=flat-square&logo=zenodo&logoColor=white)

---

### GitHub activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./profile-summary-card-output/github_dark/0-profile-details.svg">
  <img src="./profile-summary-card-output/github/0-profile-details.svg" alt="Contribution summary" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./profile-summary-card-output/github_dark/1-repos-per-language.svg">
  <img src="./profile-summary-card-output/github/1-repos-per-language.svg" alt="Repos per language" width="60%">
</picture>


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/pouriaetab/pouriaetab/output/github-snake-dark.svg">
  <img src="https://raw.githubusercontent.com/pouriaetab/pouriaetab/output/github-snake.svg" alt="Contribution snake" width="100%">
</picture>

</div>
