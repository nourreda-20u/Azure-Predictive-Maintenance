# Target & Split Protocol (DRAFT)

Proposed binary label: any component failure in the future interval `(t, t+24h]` for each eligible machine-hour.

**Not approved until source audit.** Establish prediction timestamp semantics, failure/maintenance downtime exclusions, completeness of forward horizon, repeated failure-event counting, and cases of preventive maintenance. Only use error/maintenance records known at prediction time for features.

Design global chronological train/validation/test cutoffs. Include a sufficient boundary gap/purge for overlapping 24-hour label horizons. Record number of independent failure events in every split. Fit imputation/scaling/selection only within training data and CV folds. Never use test data for tuning or threshold selection. Consider holdout-machine generalization only as a separate evaluation.
