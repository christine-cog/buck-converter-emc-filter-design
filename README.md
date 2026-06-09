# buck-converter-emc-filter-design
EMC analysis and filter design for a DC/DC buck converter with an LTspice simulation &amp; a Python FFT analysis. 
# Buck Converter — EMC Analysis & Filter Design

![Status](https://img.shields.io/badge/status-in%20progress-orange)
![Tools](https://img.shields.io/badge/tools-LTspice%20%7C%20Python-blue)

## Overview
Simulation and EMC compliance analysis of a DC/DC buck converter 
(48V → 12V, 100 kHz switching frequency).  
The project covers three phases:
- **Analysis** — identification of conducted EMI emissions via FFT
- **Design** — EMC filter dimensioning (common mode & differential mode)
- **Validation** — comparison against MIL-STD-461 limits before and after filtering

## Industrial Context
Power electronics converters are widely used in embedded systems and many industries (aerospace, defense, industrial power conversion, automotive). 
Their switching behavior generates electromagnetic perturbations that must be controlled to ensure coexistence with sensitive onboard equipment (sonar, radar, communication systems).

## Tools
| Tool | Purpose |
|------|---------|
| LTspice XVII | Circuit simulation |
| Python | FFT analysis & filter design |
| NumPy | Signal processing |
| Matplotlib | Results visualization |

## Project Structure
buck-converter-emc-filter-design/
├── ltspice/        # Circuit schematics (.asc files)
├── python/         # Analysis and design scripts (.py)
├── figures/        # Generated plots and screenshots
└── report/         # Final PDF report
## Roadmap
- [x] Theoretical study (buck converter, EMC fundamentals,  
      CM/DM modes, normative limits)
- [ ] Ideal buck converter simulation (LTspice)
- [ ] Real circuit with parasitic elements
- [ ] FFT analysis of input current (Python)
- [ ] EMC filter design and validation
- [ ] Final report

## Results
*Coming soon — project in progress*

## Author
Christine Senghor — ENSEM Nancy, Electrical Engineering  
Research intern at Laboratoire GREEN, Université de Lorraine
