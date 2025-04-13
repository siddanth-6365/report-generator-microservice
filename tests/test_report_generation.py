import os
import pytest
from fastapi.testclient import TestClient

UPLOAD_DIR = "uploads"

def setup_files():
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    with open(os.path.join(UPLOAD_DIR, "input.csv"), "w") as f:
        f.write("field1,field2,field3,field4,field5,refkey1,refkey2\n")
        f.write("Alice,Bob,123,foo,100,REF001,REF101\n")
    with open(os.path.join(UPLOAD_DIR, "reference.csv"), "w") as f:
        f.write("refkey1,refdata1,refkey2,refdata2,refdata3,refdata4\n")
        f.write("REF001,DataAlpha,REF101,ExtraA,ExtraB,150\n")

@pytest.mark.usefixtures("auth_header", "test_client")
def test_report_generation(auth_header, test_client: TestClient):
    setup_files()
    response = test_client.post("/report/generate", headers=auth_header)
    assert response.status_code == 200, response.text
    
    data = response.json()
    output_path = None
    if "output_path" in data:
        output_path = data["output_path"]
    elif "output_file" in data and isinstance(data["output_file"], dict):
        output_path = data["output_file"].get("output_path")
    
    assert output_path is not None, "No output file path returned in the response."
    assert isinstance(output_path, str), "Output path should be a string."
    
    assert os.path.exists(output_path), f"Output file not found at {output_path}"