import subprocess
import os
import sys
import cv2
import numpy as np
import time
import pygetwindow as gw

def run_command_async(command):
    """Helper function to run shell commands asynchronously without waiting for them to finish."""
    print(f"Executing: {' '.join(command)}")
    try:
        # Use subprocess.Popen to run the command without blocking
        return subprocess.Popen(command)
    except FileNotFoundError:
        print(f"Error: Command not found. Make sure the executable is in your PATH: {command[0]}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    mlagents_dir = "ml-agents"
    platform_name = "windows"
    executable_name = "UnityEnvironment.exe"
    executable_path = os.path.join(mlagents_dir, "trained-envs-executables", platform_name, executable_name)

    # Check if the executable exists
    if not os.path.exists(executable_path):
        print(f"Error: The executable was not found at {executable_path}.")
        sys.exit(1)

    # Define the command to run the Unity executable with graphics
    unity_run_command = [executable_path]

    # Start the executable process
    print("Launching Unity environment with graphics for video recording...")
    unity_process = run_command_async(unity_run_command)

    # Wait for a moment for Unity to open
    time.sleep(10)

    # Find the Unity game window by title
    try:
        # The window title will be "UnityEnvironment"
        unity_window = gw.getWindowsWithTitle('UnityEnvironment')[0]
        unity_window.activate()
    except IndexError:
        print("Error: Could not find the Unity game window. Make sure it is open.")
        sys.exit(1)

    # You may need to install 'mss' for screen capture
    # pip install mss
    from mss import mss
    sct = mss()
    monitor = {"top": unity_window.top, "left": unity_window.left, "width": unity_window.width, "height": unity_window.height}

    # Set up video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('3DBall_Demo.mp4', fourcc, 30.0, (monitor["width"], monitor["height"]))

    print("Recording video... Press Ctrl+C to stop.")
    try:
        while unity_process.poll() is None:
            # Capture the screen
            img = np.array(sct.grab(monitor))

            # Convert to BGR for OpenCV
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            # Write the frame to the video file
            out.write(img)

    except KeyboardInterrupt:
        print("\nStopping recording...")
    finally:
        out.release()
        cv2.destroyAllWindows()
        unity_process.terminate()

    print("Video recording saved as 3DBall_Demo.mp4")