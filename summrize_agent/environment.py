# features/environment.py
from pathlib import Path
import shutil

def before_all(context):
    artifacts = Path("artifacts")
    if artifacts.exists():
        shutil.rmtree(artifacts)
