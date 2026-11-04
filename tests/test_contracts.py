from pm.contracts import missing_required_columns

def test_required_columns_present():
    assert missing_required_columns(["machineID", "datetime", "target", "volt"]) == []

def test_missing_target_is_detected():
    assert missing_required_columns(["machineID", "datetime"]) == ["target"]
