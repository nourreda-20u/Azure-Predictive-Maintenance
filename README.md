# Azure Predictive Maintenance

A four-person research project using **SQL Server, Python, and scikit-learn** to explore early industrial component-failure prediction from historical telemetry, errors, maintenance, and failure events.

> **Current status: dataset audit / feasibility.** The proposed target is *any component failure in the next 24 hours*. It is **not yet approved**. The Microsoft Azure PdM dataset is synthetic; no model performance or production deployment is claimed.

## Dataset
Source: https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance/data

Expected inputs (verify files and schemas after download): `PdM_telemetry.csv`, `PdM_errors.csv`, `PdM_maint.csv`, `PdM_failures.csv`, and `PdM_machines.csv`.

The raw datasets are **not included** in GitHub. Follow `data/README.md` to obtain them.

## Team responsibilities
| Role | Owns | Handover |
|---|---|---|
| Data Engineering & SQL Server | SQL schema, ingestion, integrity checks, time-safe extracts | SQL scripts, data dictionary, data-quality evidence |
| EDA & Data Preprocessing | EDA, cleaning decisions, features and labels, temporal splitting, transformations | Audited dataset contract, split manifest, preprocessing code |
| Decision Tree & Random Forest | Tree/forest baselines, entropy, pruning, tuning | Reproducible models and validation results |
| SVM & Model Evaluation | SVM experiments, scaling, comparable evaluation | Comparison report, ROC/PR curves, model-selection rationale |

Cross-role decisions are documented in `docs/HANDOVER_CONTRACT.md` and `docs/TARGET_AND_SPLIT_SPEC.md`.

## Repository structure
```text
.github/         PR/issue templates and Python checks
configs/         Experiment configuration examples
data/            Local data directories (actual CSVs ignored)
docs/            Target definition, data contract, decisions
notebooks/       EDA and modeling notebooks (added by each role)
reports/         Reproducible reports, figures and metrics
sql/             SQL Server scripts
src/pm/          Reusable Python functions
tests/           Data and pipeline contract tests
```

## Local setup
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pytest -q
```

## Collaboration
1. Select an Issue and work on your own `feature/...` branch.
2. Include validation evidence and changed-file descriptions in a Pull Request.
3. Have the downstream role review the handover before merging to `main`.
4. Never commit downloaded raw data, credentials, SQL backups, generated models, or giant notebook outputs.

**Scope:** Decision Tree, Random Forest, SVM, fair temporal validation, reproducible documentation. Deployment/dashboard work is postponed.
