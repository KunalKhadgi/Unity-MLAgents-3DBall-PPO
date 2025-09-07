import subprocess
import os
import sys

def run_command(command):
    """Helper function to run shell commands and check for errors."""
    print(f"Executing: {' '.join(command)}")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)
        return result
    except FileNotFoundError:
        print(f"Error: Command not found. Make sure the executable is in your PATH: {command[0]}")
        raise
    except subprocess.CalledProcessError as e:
        print(f"Error during command execution. Command returned non-zero exit status {e.returncode}")
        print(f"Command: {' '.join(e.cmd)}")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    mlagents_repo_url = "https://github.com/Unity-Technologies/ml-agents"
    mlagents_dir = "ml-agents"
    
    # Determine OS and environment path
    platform_name = ""
    executable_name = ""
    if sys.platform.startswith('win'):
        platform_name = "windows"
        executable_name = "UnityEnvironment.exe"
    elif sys.platform.startswith('darwin'):
        platform_name = "macos"
        executable_name = "3DBall.app/Contents/MacOS/3DBall"
    else:
        platform_name = "linux"
        executable_name = "3DBall.x86_64"
    
    env_executables_dir = os.path.join(mlagents_dir, "trained-envs-executables", platform_name)
    executable_path = os.path.join(env_executables_dir, executable_name)
    config_path = os.path.join(mlagents_dir, "config", "ppo", "3DBall.yaml")
    run_id = "3DBallTraining"

    try:
        # Clone the ML-Agents repository
        if not os.path.exists(mlagents_dir):
            run_command(["git", "clone", "--depth", "1", mlagents_repo_url])
        else:
            print(f"ML-Agents directory '{mlagents_dir}' already exists. Skipping cloning.")

        # Create necessary directories
        os.makedirs(env_executables_dir, exist_ok=True)
        
        # Check if the executable exists before trying to run the training command
        if not os.path.exists(executable_path):
            print(f"\n--- IMPORTANT: MANUAL STEP REQUIRED ---")
            print(f"Please build the Unity environment executable for your OS ({platform_name}).")
            print(f"The executable should be located at: {executable_path}")
            print(f"-------------------------------------\n")
            print(f"Error: The executable was not found at {executable_path}.")
            print("Please follow the manual build and placement instructions.")
            sys.exit(1)

        # Define the training command with --force to overwrite previous runs
        train_command = [
            "mlagents-learn",
            config_path,
            f"--env={executable_path}",
            f"--run-id={run_id}",
            "--no-graphics",
            "--force"
        ]

        # Execute the training command
        run_command(train_command)

    except Exception as e:
        print(f"Script failed: {e}")
