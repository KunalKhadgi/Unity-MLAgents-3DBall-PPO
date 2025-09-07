Unity ML-Agents 3DBall Project
This repository contains a deep reinforcement learning project using Unity's ML-Agents toolkit. The goal is to train an agent to balance a ball on a moving platform in the 3DBall environment.

Project Overview
The 3DBall environment is a classic reinforcement learning task where an agent learns to balance a ball on a platform by adjusting its rotation. The agent receives a reward for every step it keeps the ball on the platform and a penalty if the ball falls off.

This project uses the Proximal Policy Optimization (PPO) algorithm to train the agent.

Setup and Installation
Follow these steps to set up the project and train the agent from scratch.

1. Clone the Repository
   Clone this repository and create a new Python virtual environment.

git clone [https://github.com/Unity-Technologies/ml-agents.git](https://github.com/Unity-Technologies/ml-agents.git)
python -m venv venv
.\venv\Scripts\activate

2. Install Python Dependencies
   Install the required Python packages, including mlagents and torch.

pip install mlagents==1.1.0
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)

3. Build the Unity Environment
   Open the Unity Hub and open the ml-agents/Project folder.

In the Unity Editor, open the 3DBall scene from Assets/ML-Agents/Examples/3DBall/Scenes/3DBall.unity.

Go to File > Build Settings.

Select PC, Mac & Linux Standalone as the platform.

Check the Headless Mode box.

Before building, create the output folder by running this command in your terminal:

mkdir -p ml-agents/trained-envs-executables/windows/3DBall

Click Build and save the executable to the new ml-agents/trained-envs-executables/windows/3DBall folder.

4. Run the Training
   Use the provided train_3DBall.py script to start the training process. The script will automatically connect to your Unity executable.

python train_3DBall.py

How to Use the Trained Model
You can use the pre-trained model from this project in your own Unity environment.

Download the 3DBall.onnx model file from the Hugging Face repository.

Open your Unity 3DBall project.

In the Project panel, navigate to Assets/ML-Agents/Examples/3DBall/Prefabs.

Select the Agent GameObject within the 3DBall prefab.

In the Inspector panel, locate the Behavior Parameters component.

Drag the 3DBall.onnx model file into the Model field.

Press the Play button in the Unity Editor to see the agent in action.

Video Demo
Here is a video of the trained agent in action, demonstrating the learned behavior.

<video controls width="100%">
<source src="3DBall_Demo.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

## Git Initialization and Commands

1.  **Initialize Git:**

    ```bash
    git init
    ```

2.  **Add files to staging area:**

    ```bash
    git add .
    ```

3.  **Commit the changes:**

    ```bash
    git commit -m "Initial commit"
    ```

4.  **Create a new repository on GitHub**

5.  **Link local repository to remote repository:**

    ```bash
    git remote add origin <repository_url>
    ```

    Replace `<repository_url>` with the URL of your GitHub repository.

6.  **Push the changes to GitHub:**

    ```bash
    git push -u origin main
    ```
