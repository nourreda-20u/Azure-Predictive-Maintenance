"""Minimal modeling schema checks (not a data audit)."""
REQUIRED_MODEL_COLUMNS = ("machineID", "datetime", "target")

def missing_required_columns(columns, required=REQUIRED_MODEL_COLUMNS):
    """Return modeling columns absent from the supplied names."""
    return [name for name in required if name not in columns]
