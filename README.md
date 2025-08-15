# Demo: say_hello with dependency

This small demo shows a function with an intentional bug and its fix.
It uses `colorama` (listed in `requirements.txt`) to color the greeting.

Windows PowerShell instructions:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

What to expect:
- "Running buggy version:" will raise an exception and print the error.
- "Running fixed version:" will print a green "Hello, Alice!" message.
