# toy_AI_code_helper

An AI-powered code debugging assistant that uses large language models and function-calling tools to automatically analyze, debug, and iteratively improve Python codebases.

This project was built as part of a guided agentic AI course, then extended and customized independently.

---

## Features

- **LLM-Powered Debugging**  
  - Uses an LLM (Gemini) to analyze error messages and source code.  
  - Generates hypotheses about the root cause of bugs.  
  - Proposes and applies code changes via structured tool calls.

- **Tool-Calling / Agentic Design**  
  - The model can call tools to:
    - Read and write files
    - Run tests / execute the Python code
    - Inspect error output and logs
  - Iteratively refines the code based on runtime feedback.

- **Automated Test-Driven Workflow**  
  - Runs tests to detect failing cases.  
  - Uses test failures and tracebacks to drive the debugging loop.  
  - Re-runs tests after applying fixes to verify that issues are resolved.

- **Extensible Architecture**  
  - Modular tool definitions for filesystem access and code execution.  
  - Easy to plug in additional tools (e.g. refactoring, formatting, or static analysis).  
  - Designed so the underlying LLM provider/model can be swapped with minimal changes.

---

## Tech Stack

- **Language:** Python  
- **AI / LLM:** Google Gemini (via REST API)  
- **Agent Pattern:** Function-calling / tool-use loop with re-prompting  
- **Other:**  
  - `dotenv` / environment variables for API keys  
  - `subprocess` (or similar) for executing tests/commands  
  - `git` for version control

---

## How It Works

At a high level, the agent follows this loop:

1. **Collect context**
   - Read relevant project files.
   - Optionally run tests or a specified script to gather errors.

2. **Ask the LLM for a plan**
   - Provide the code, test output, and tool schema to the model.
   - The model decides whether to:
     - Inspect more files
     - Modify code
     - Re-run tests
     - Or stop if the issue appears resolved.

3. **Execute tool calls**
   - When the model requests a tool (e.g. "write_file", "run_tests"), the agent:
     - Executes the tool in Python.
     - Captures outputs (e.g. new errors, diff summaries).
     - Feeds them back into the model as context.

4. **Iterate**
   - Repeat the reasoning + tool-calling cycle until:
     - Tests pass, or
     - A max number of iterations is reached.

This pattern loosely resembles how tools like Cursor / Claude Code work, but as a simplified “toy” implementation intended for learning and experimentation.

---

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/JeremiahNSUBE/toy_AI_code_helper.git
   cd toy_AI_code_helper

2. **Create a virtual environment and install dependencies**

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

3. **Set your environment variables**

cp .env.example .env
# Then open .env and set GEMINI_API_KEY=your_api_key_here

4. **Run the agent**

python main.py


## Note

This was a learning project and not meant for production use. THe agent may make mistakes, always double check.

## Example Usage

Once the agent is running, you can point it at a Python project and give it a goal. For example:

```bash
python main.py --project-path /path/to/your/project --command "Fix failing tests in tests/test_calculator.py"
