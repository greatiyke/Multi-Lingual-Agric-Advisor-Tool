import subprocess
import sys
import os

def test_worker():
    worker_path = os.path.join(os.getcwd(), 'services', 'tts_worker.py')
    text = "Yọ èpò kúrò lára àgbàdo."
    voice = "yo-NG-BunmiNeural"
    output = "manual_worker_test.mp3"
    
    cmd = [sys.executable, worker_path, "--text", text, "--voice", voice, "--output", output]
    
    print(f"Running command: {cmd}")
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    
    print(f"Return Code: {result.returncode}")
    print(f"Stdout: {result.stdout}")
    print(f"Stderr: {result.stderr}")
    
    if os.path.exists(output):
        print(f"File size: {os.path.getsize(output)}")
    else:
        print("File not created.")

if __name__ == "__main__":
    test_worker()
