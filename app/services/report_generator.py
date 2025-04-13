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
    
    # Call the transformation function with both dataframes
    try:
        df_output = apply_transformation(df_input, df_reference)
    except Exception as e:
        logger.exception("Error in transformation")
        raise HTTPException(status_code=500, detail=f"Error applying transformation: {str(e)}")
    
    output_path = os.path.join(UPLOAD_DIR, "output.csv")
    try:
        df_output.to_csv(output_path, index=False)
    except Exception as e:
        logger.exception("Error writing the output CSV file")
        raise HTTPException(status_code=500, detail=f"Error writing the CSV file: {str(e)}")

    logger.info("Report generation completed", extra={"output_path": output_path})
    return {"message": "Report generated successfully", "output_path": output_path}
