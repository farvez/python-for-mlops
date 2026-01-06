REQUIRED_FIELDS = ["id", "age", "salary"]

def validate_schema(records):
    errors = []
    for idx,row in enumerate(records):
        for field in REQUIRED_FIELDS:
            if field not in row:
                errors.append(
                f"Missing filed {field} in row {idx}")
    return errors

def validate_data(records):
    errors = []

    for idx,row in enumerate(records):
        if not row["age"]:
            errors.append(f"Row {idx}: age is missing")

        if row["salary"] and int(row["salary"]) < 30000:
            errors.append(f"Row {idx}: salary is too low")
    return errors