from google.adk.agents import Agent
from google.adk.tools import google_search
import pandas as pd
import re


def extract_valid_hsn_codes(user_input: str):
    codes = re.findall(r'\b\d{2,8}\b', user_input)
    valid_lengths = [2, 4, 6, 8]

    qualified_codes = [code for code in codes if len(code) in valid_lengths]
    unqualified_codes = [code for code in codes if len(code) not in valid_lengths]

    return qualified_codes,  unqualified_codes



def validate_hierarchy(hsncode: str, hsn_column:str) -> dict:

    hierarchy_levels = [hsncode[:i] for i in [2, 4, 6] if i < len(hsncode)]
    missing_levels = [level for level in hierarchy_levels if level not in hsn_column]

    if missing_levels:
        return {
            "result": f"{hsncode} is found, but parent codes {missing_levels} are missing.",
        }
    else:
        return {
            "result": f"{hsncode} and all its parent levels exist.",
        }

def validate_hsn_codes_from_input(user_input: str) -> dict:
    """
    Validate if the {user_input} HSN code is of length 2, 4, 6, or 8.
    Then check if it exists in the first column of the provided Excel file.
    """
    try:
        df = pd.read_excel("C:/Users/suraj/Documents/HSN_project/2_tool_agent/HSN_SAC.xlsx", engine='openpyxl')
        hsn_code_column = df.iloc[:, 0].astype(str).tolist()

        qualified_codes, unqualified_codes = extract_valid_hsn_codes(user_input)
        results = {}

        if unqualified_codes:
            return {"error": f"These codes {unqualified_codes} don't qualify as HSN codes"}

        for code in qualified_codes:
            if code in hsn_code_column:
                results[code] = "Valid and available in the Excel file"
                if len(code) == 8:
                    hierarchy_check = validate_hierarchy(code, hsn_code_column)
                    results[code] += f" | {hierarchy_check['result']}"
            else:
                results[code] = "Not available in the Excel file"

        return results

    except Exception as e:
        return {"error": str(e)}



root_agent = Agent(
    name="validator_agent",
    model="gemini-2.0-flash",
    description="informer for HSN validation",
    instruction="""
    You are a helpful assistant that can take HSN code from the user abd 
    validate and state if hierarchy or parent codes are present as per returned result from  validate_hsn_codes_from_input tool and validate_hierarchy
    """,
    tools=[validate_hsn_codes_from_input,validate_hierarchy],
    output_key="agent_output"
    
)


