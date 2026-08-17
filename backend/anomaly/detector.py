import numpy as np
from sklearn.ensemble import IsolationForest


def detect_anomalies_zscore(amounts: list[float], threshold: float = 3.0) -> list[bool]:
    """
    Returns a list of True/False for each amount - True means it's an anomaly.
    Z-score = (value - mean) / standard deviation
    """
    if len(amounts) < 2:
        return [False] * len(amounts)

    amounts_array = np.array(amounts)
    mean = amounts_array.mean()
    std = amounts_array.std()

    if std == 0:  # all amounts are identical, nothing is unusual
        return [False] * len(amounts)

    z_scores = np.abs((amounts_array - mean) / std)
    return (z_scores > threshold).tolist()


def detect_anomalies_isolation_forest(amounts: list[float]) -> list[bool]:
    """
    Returns a list of True/False for each amount - True means it's an anomaly.
    Isolation Forest isolates outliers using random splits.
    """
    if len(amounts) < 5:  # not enough data to train meaningfully
        return [False] * len(amounts)

    amounts_array = np.array(amounts).reshape(-1, 1)  # sklearn expects 2D input

    model = IsolationForest(contamination=0.1, random_state=42)
    predictions = model.fit_predict(amounts_array)

    # IsolationForest returns -1 for anomalies, 1 for normal points
    return (predictions == -1).tolist()