import os
import pandas as pd
import logging
from fastapi import HTTPException
from app.services.transform import apply_transformation

logger = logging.getLogger(__name__)

UPLOAD_DIR = "uploads"

def generate_report():
    input_path = os.path.join(UPLOAD_DIR, "input.csv")
    reference_path = os.path.join(UPLOAD_DIR, "reference.csv")
    
    logger.info("Starting report generation", extra={"input_path": input_path, "reference_path": reference_path})
    
    try:
        df_input = pd.read_csv(input_path)
        df_reference = pd.read_csv(reference_path)
    except Exception as e:
        logger.exception("Error reading CSV files")
        raise HTTPException(status_code=500, detail=f"Error reading CSV files: {str(e)}")
    
    try:
        df_merged = pd.merge(df_input, df_reference, on=["refkey1", "refkey2"], how="left")
    except Exception as e:
        logger.exception("Error merging CSV files")
        raise HTTPException(status_code=500, detail=f"Error merging CSV files: {str(e)}")
    
    output_df = apply_transformation(df_merged)
    output_file = os.path.join(UPLOAD_DIR, "output.csv")
    output_df.to_csv(output_file, index=False)
    
    logger.info("Report generated successfully", extra={"output_file": output_file})
    return output_file
