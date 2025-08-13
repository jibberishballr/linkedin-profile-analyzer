import shlex
import subprocess
from pathlib import Path, PurePosixPath
import modal

# Define container dependencies and include the local file
backend_script_local_path = Path(__file__).parent / "main.py"
backend_script_remote_path = str(PurePosixPath("/root/main.py"))

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("fastapi", "uvicorn", "scikit-learn", "requests")
    .add_local_file(backend_script_local_path, backend_script_remote_path)
)

app = modal.App(name="linkedin-analyzer-backend", image=image)

# Define the web server function
@app.function(
    allow_concurrent_inputs=100,
    secrets=[modal.Secret.from_name("hunter-api-key")],
)
@modal.web_server(8000)
def run():
    # The file is at /root/main.py, and /root is in the PYTHONPATH
    target = "main"
    cmd = f"uvicorn {target}:app --host 0.0.0.0 --port 8000"
    subprocess.Popen(cmd, shell=True)

if __name__ == "__main__":
    app.serve()
