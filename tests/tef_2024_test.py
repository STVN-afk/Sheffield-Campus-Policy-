from src.dataset_scripts.teaching_excellence_framework import tef_2024
import os
import pandas as pd

def test_conversion_to_csv():

    test_ds_path = os.path.abspath("tests/test_datasets/file_example_XLSX_50.xlsx")

    # Call your conversion function
    test_csv = tef_2024.conversion_to_csv(test_ds_path)

    print(test_csv)
    

    # Check if the CSV was created
    assert os.path.exists(test_csv), "CSV was not created"

    # Load and test the CSV contents
    df = pd.read_csv(test_csv)
    assert not df.empty, "CSV is empty"

    # Clean up
    os.remove(test_csv)
    print("Test passed and file removed.")

if __name__ == "__main__":
    test_conversion_to_csv()
