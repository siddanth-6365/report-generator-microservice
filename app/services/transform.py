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

def apply_transformation(df_input, df_reference):
    try:
        merged_df = pd.merge(df_input, df_reference, on=['refkey1', 'refkey2'], how='left')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error merging dataframes: {str(e)}")
    
    rules = load_transformation_rules()
    output_data = {}

    for outfield, expr in rules.items():
        try:
            # Evaluate the transformation expression per row.
            # We build an evaluation context with all row values.
            # Only the "max" function is exposed as a built-in.
            output_data[outfield] = merged_df.apply(
                lambda row: eval(expr, {"__builtins__": {}}, {**row.to_dict(), "max": max}),
                axis=1
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error applying transformation for '{outfield}': {str(e)}")
    
    output_df = pd.DataFrame(output_data)
    return output_df
