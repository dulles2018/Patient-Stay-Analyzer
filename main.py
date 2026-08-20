import os
import pandas as pd
import matplotlib.pyplot as plt

def run_analysis():
    # 1. Load Excel file
    excel_path = os.path.join("data", "healthcare_dataset_100rows_Visualization-1.xlsx")
    df = pd.read_excel(excel_path, sheet_name=0)

    # 2. Clean data (standardize names and drop missing records)
    df["Name"] = df["Name"].str.title()
    df_clean = df.dropna(subset=["Test Results", "length_stay"])

    # 3. Calculate average length of stay per test result category
    summary = df_clean.groupby("Test Results")["length_stay"].mean()
    print("=== Average Hospital Stay (Days) by Test Result ===")
    print(summary.round(1))

    # 4. Generate and save chart
    os.makedirs("graphs", exist_ok=True)
    plt.figure(figsize=(8, 4))
    summary.plot(kind="bar", color=["#4C72B0", "#DD8452", "#55A868"], edgecolor="black")
    plt.title("Average Hospital Stay by Test Result")
    plt.xlabel("Test Result")
    plt.ylabel("Average Stay (Days)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    chart_path = os.path.join("graphs", "avg_stay_by_test_result.png")
    plt.savefig(chart_path)
    plt.close()
    
    print(f"\nChart saved successfully to {chart_path}")

if __name__ == "__main__":
    run_analysis()
