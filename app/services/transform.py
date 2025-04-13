import json
import os
import pandas as pd
from fastapi import HTTPException

TRANSFORM_CONFIG_PATH = os.path.join("config", "transform_rules.json")

def load_transformation_rules():
    try:
        with open(TRANSFORM_CONFIG_PATH, "r") as f:
            config = json.load(f)
            return config.get("transformations", {})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading transformation rules: {str(e)}")

def apply_transformation(df):
    rules = load_transformation_rules()
    
    if rules.get("outfield1") == "field1 + field2":
        df["outfield1"] = df["field1"].astype(str) + df["field2"].astype(str)
    else:
        df["outfield1"] = "Not Implemented"
    
    if rules.get("outfield2") == "refdata1":
        df["outfield2"] = df["refdata1"]
    else:
        df["outfield2"] = "Not Implemented"
    
    if rules.get("outfield3") == "refdata2 + refdata3":
        df["outfield3"] = df["refdata2"].astype(str) + df["refdata3"].astype(str)
    else:
        df["outfield3"] = "Not Implemented"
    
    if rules.get("outfield4") == "field3 * max(field5, refdata4)":
        df["outfield4"] = pd.to_numeric(df["field3"], errors="coerce") * df[["field5", "refdata4"]].max(axis=1)
    else:
        df["outfield4"] = "Not Implemented"
    
    if rules.get("outfield5") == "max(field5, refdata4)":
        df["outfield5"] = df[["field5", "refdata4"]].max(axis=1)
    else:
        df["outfield5"] = "Not Implemented"
    
    output_columns = ["outfield1", "outfield2", "outfield3", "outfield4", "outfield5"]
    return df[output_columns]
