#  HSN Code Validation Agent (Using Google ADK)

This project builds an intelligent agent using the **Google ADK (Agent Development Kit)** framework to **validate HSN codes** with multiple layers of logic, including hierarchy checks. It leverages a master Excel sheet (`HSN_SAC.xlsx`) for validation and responds interactively to user inputs such as single or multiple HSN codes.

---

##  Features

-  Validates format (2, 4, 6, or 8-digit) of HSN codes
-  Checks existence of codes in the master Excel sheet
-  Performs **hierarchical validation** (e.g., confirms parent codes of 8-digit HSN)
-  Interactive agent using the **Gemini-2.0-flash** model
-  Tool-based modular architecture using `google.adk`

---

##  Agent Structure

Agent is named **`validator_agent`** and is powered by:
- Language model: `gemini-2.0-flash`
- Purpose: Inform users about validity of HSN codes and detect hierarchy inconsistencies
- Tools:
  - `validate_hsn_codes_from_input()`
  - `validate_hierarchy()`

---

##  Functions

### `extract_valid_hsn_codes(user_input: str) -> (list, list)`
Extracts valid (2/4/6/8-digit) numeric HSN codes from a user input string.
- Returns: `(qualified_codes, unqualified_codes)`

---

### `validate_hierarchy(hsncode: str, hsn_column: list) -> dict`
Checks if the **parent levels** (2, 4, 6 digits) of an 8-digit HSN code exist.
- Returns messages indicating whether parent codes are missing or complete.

---

### `validate_hsn_codes_from_input(user_input: str) -> dict`
Main validation function used by the agent.
- Validates code format
- Checks presence in Excel file (`HSN_SAC.xlsx`)
- If 8-digit, invokes `validate_hierarchy()`
- Returns structured results or error messages

---

### `root_agent = Agent(...)`
Defines the main agent with:
- Model: `gemini-2.0-flash`
- Description and behavior rules
- Tools: validation functions defined above
- Output key: `"agent_output"`

---

##  Libraries Used

| Library        | Purpose                              |
|----------------|--------------------------------------|
| `pandas`       | Reading and manipulating Excel files |
| `re`           | Regex for extracting numeric codes   |
| `openpyxl`     | Backend engine for reading `.xlsx`   |
| `google.adk`   | Framework for defining agents        |

---

##  Environment Setup

1. **Clone the Repository**
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

2. **Create and Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
Your requirements.txt should include:

google-adk[database]==0.3.0
yfinance==0.2.56
psutil==5.9.5
litellm==1.66.3
google-generativeai==0.8.5
python-dotenv==1.1.0

---

##  Usage Instructions

Once your environment is set up and the Excel file `HSN_SAC.xlsx` is available at the specified path:

**Run the agent interface (customized as needed)**:
``` bash
adk web
```

## File Structure

HSN_PROJECT/
│
├── .venv/                                 # Python virtual environment (should be in .gitignore)
│
├── 2_tool_agent/                          # Main working directory
│   │
│   ├── HSN_SAC.xlsx                       # HSN Master Excel file
│   ├── README.md                          # Documentation
│   ├── requirements.txt                   # List of required libraries
│   │
│   └── validator_agent/                   # Package containing the validation agent
│       ├── __init__.py                    # Makes this a Python package
│       ├── .env                           # Environment variables (e.g., file paths, secrets)
│       └── agent.py                       # Main agent logic, tools, and configuration


##  License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute as long as the original author is credited.

## Contributing
Contributions are welcome! Here's how you can help:

 Report bugs via Issues tab

 Suggest features or improvements

 Submit a pull request with fixes or enhancements


📬 Contact
For questions, collaborations, or support, contact:

Suraj Kumar Sahu
✉️ surajksahu112@gmail.com
