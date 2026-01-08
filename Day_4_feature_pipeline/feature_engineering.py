def prepare_features(records):
    features = []

    for row in records:
        features.append({
            "age": int(row["age"]),
            "salary": int(row["salary"]),
            "salary_per_age": int(row["salary"]) / int(row["age"])
        })

    return features