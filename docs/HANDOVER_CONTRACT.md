# Stage Handover Contract

Every handover includes **artifact + reproducible code + data version + validation evidence + assumptions**.

## SQL Server → EDA / Preprocessing
Provide schema, raw-file checksums, import scripts, row/key/null reports, time semantics, validated source exports and join cardinality checks. Accept only if no unexplained missing machines/row multiplication.

## EDA / Preprocessing → Both ML Roles
Provide EDA and cleaning log, features and target policy, label-generation code, time-safe feature code, chronological split manifest, class/event counts per split, and unfitted sklearn pipeline definitions. Accept only after checking leakage, split boundaries and schema consistency.

## Decision Tree / Random Forest → Shared Evaluation
Provide experiment IDs, dataset/split versions, CV strategy, parameters, predictions/scores, timing, and reproducible model pipelines.

## SVM → Shared Evaluation
Provide equivalent records, scaling verification, linear/RBF trials, resource-use measurements, and decision scores.

## Final Gate
Compare all models on identical splits; choose threshold on validation only; evaluate untouched test once; report both row-level and event-level detection outcomes and limitations. Deployment is out of current scope.

## Shared decisions
Target/horizon: entire team. Temporal features: SQL + EDA. Split and leakage checks: EDA + both ML roles. Final model choice: both ML roles.
