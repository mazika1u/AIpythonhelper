import subprocess
import tempfile

def run_code(code: str) -> str:
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=True) as f:
        f.write(code)
        f.flush()
        try:
            result = subprocess.run(
                ["python", f.name], capture_output=True, text=True, timeout=5
            )
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return "Error: Execution timed out"
