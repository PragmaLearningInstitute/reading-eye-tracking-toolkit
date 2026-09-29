# Reading eye-tracking toolkit

**An inspectable reading-experiment runner with OpenFace integration and exploratory gaze analysis.** The toolkit presents plain and formatted texts, records event markers and responses, and derives gaze-related summaries from OpenFace output. It accompanies the [RUMBA.RD project](https://pragmalearninginstitute.com/rumba-rd) at [Pragma Learning Institute](https://pragmalearninginstitute.com/).

[Guide français](docs/getting-started.fr.md) · [Protocol](docs/protocol.fr.md) · [Data and metrics](docs/analysis.fr.md) · [PLI documentation](https://pragmalearninginstitute.com/outils/documentation)

This is research software, not a validated clinical eye tracker. `metrics.csv` summarizes an entire OpenFace recording, including non-reading phases. It does **not** directly report an A/B treatment effect. The [analysis guide](docs/analysis.fr.md) explains the distinction.

## Install and run

Requires Python 3.11+, Tk and a separate [OpenFace installation](https://github.com/TadasBaltrusaitis/OpenFace). Review OpenFace and model licenses for your intended use. No OpenFace binaries or model weights are redistributed here.

```bash
git clone https://github.com/PragmaLearningInstitute/reading-eye-tracking-toolkit.git
cd reading-eye-tracking-toolkit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m tkinter
export OPENFACE_ROOT="/path/to/OpenFace"
python experiment_runner.py
```

The expected executable is `$OPENFACE_ROOT/build/bin/FeatureExtraction`. The placeholder path above must be replaced with your actual installation. Windows users can activate the environment with `.venv\Scripts\activate`; the OpenFace executable path must match the platform, and that integration has not been validated in this release.

Use a fictional participant code for a rehearsal. Camera collection starts only after pressing **Lancer OpenFace** and confirming the collection notice. `Escape` requests exit. Optional audio, screen luminance and a second camera remain disabled unless explicitly enabled.

## Repository map

| File | Purpose |
| --- | --- |
| `experiment_runner.py` | Full-screen protocol, OpenFace process, markers, responses and analysis |
| `safety.py` | Identifier validation and spreadsheet-safe CSV output |
| `plan.csv` | Ordered trials and paths to their materials |
| `materials/` | Example texts, questions and Likert items |
| `tests/` | Focused regression tests |
| `docs/` | Installation, protocol, metrics, privacy and provenance |

## What a session produces

Markers, behavioural responses, layout geometry, optional WAV files, OpenFace CSV files, a calibration report and normalized gaze files are saved under `data/` by default. These may contain sensitive research data. The directory is excluded from Git; never commit participant sessions. The [data guide](docs/analysis.fr.md) describes each output and its limitations.

The default plan presents A (plain), then B (formatted). It is an example sequence, not randomized allocation or a counterbalanced study. Two five-point calibration blocks occur before the first reading trial. Customize and document the protocol before using it in research.

## Tests and provenance

```bash
python -m unittest discover -s tests -v
```

This edition derives from TimTrinche's [Dyslexia-Focused-Study-Toolkit-Reading-Experiment](https://github.com/TimTrinche/Dyslexia-Focused-Study-Toolkit-Reading-Experiment), commit `a142ff991a45c49f77413beaa6052a2551d7b3ae`. It adds safer identifiers, neutralized CSV cells, opt-in auxiliary sensors and working material paths. See [provenance](docs/provenance.fr.md), [validation](VALIDATION.md), [security](SECURITY.md) and [MIT license](LICENSE).

Cite the software using [CITATION.cff](CITATION.cff). Related code: [RUMBA.RD](https://github.com/PragmaLearningInstitute/rumba-rd) · [RUMBA.EX](https://github.com/PragmaLearningInstitute/rumba-ex).
