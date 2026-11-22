import os
import sys
import subprocess
import time
import signal

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    print("=" * 60)
    print("Launching Clinical Triage AI Local Environment...")
    print("=" * 60)

    backend_proc = subprocess.Popen(
        [sys.executable, "backend_server.py"],
        cwd=base_dir
    )
    print(f"[*] Started FastAPI Backend server (PID {backend_proc.pid}) on http://127.0.0.1:8000")

    time.sleep(1)

    frontend_proc = subprocess.Popen(
        ["node", "frontend_server.js"],
        cwd=base_dir
    )
    print(f"[*] Started Frontend Node server (PID {frontend_proc.pid}) on http://127.0.0.1:3000")
    print("\nApplication URLs:")
    print("  -> Website / Landing: http://localhost:3000")
    print("  -> Dashboard:         http://localhost:3000/dashboard")
    print("  -> Backend API:       http://localhost:8000/docs")
    print("=" * 60)
    sys.stdout.flush()

    try:
        while True:
            time.sleep(1)
            b_code = backend_proc.poll()
            f_code = frontend_proc.poll()
            if b_code is not None:
                print(f"[!] Backend process exited with code {b_code}")
                break
            if f_code is not None:
                print(f"[!] Frontend process exited with code {f_code}")
                break
    except KeyboardInterrupt:
        print("\nShutting down servers...")
    finally:
        for proc in (frontend_proc, backend_proc):
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    proc.kill()
        print("[*] All servers stopped.")

if __name__ == "__main__":
    main()

