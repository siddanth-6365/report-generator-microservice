import os
from fastapi.testclient import TestClient
import pytest

UPLOAD_DIR = "uploads"

def setup_files():
    # Create sample input.csv and reference.csv in the uploads folder
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    with open(os.path.join(UPLOAD_DIR, "input.csv"), "w") as f:
        f.write("field1,field2,field3,field4,field5,refkey1,refkey2\n")
        f.write("Alice,Bob,123,foo,100,REF001,REF101\n")
    with open(os.path.join(UPLOAD_DIR, "reference.csv"), "w") as f:
        f.write("refkey1,refdata1,refkey2,refdata2,refdata3,refdata4\n")
        f.write("REF001,DataAlpha,REF101,ExtraA,ExtraB,150\n")

@pytest.mark.usefixtures("test_client", "auth_header")
def test_report_generation(auth_header, test_client: TestClient):
    # First, simulate the upload of files
    setup_files()
    
    # Call the generate report endpoint with auth header
    response = test_client.post("/report/generate", headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert "output_file" in data
    
    # Verify that the output file was created
    output_file = data["output_file"]
    assert os.path.exists(output_file)
