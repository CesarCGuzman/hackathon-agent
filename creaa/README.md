// ...existing code...
# creaa — Quick start

1. Prerequisites
   - Python 3.8+ installed
   - Git (optional)

2. Setup (Windows)
   - Open PowerShell or Command Prompt
   - Create and activate a virtual environment (recommended):
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```

3. Run
   - Change into the agents folder and start the web server:
     ```
     cd agents
     adk web --port 5000
     ```
   - Open http://localhost:5000 in your browser.

4. Notes
   - If `adk` is not found, ensure the package that provides it is installed and your environment is activated.
   - Use Ctrl+C in the terminal to stop the server.

That's it — simple and ready to