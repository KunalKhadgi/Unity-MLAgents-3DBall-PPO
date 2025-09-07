# Unity ML-Agents 3DBall Project

This repository contains a deep reinforcement learning project using the Unity ML-Agents toolkit. The goal is to train an agent to balance a ball on a moving platform in the 3DBall environment.

## Project Overview

The 3DBall environment is a classic reinforcement learning task where an agent learns to balance a ball on a platform by adjusting its rotation. The agent receives a reward for every step it keeps the ball on the platform and a penalty if the ball falls off.

This project utilizes the **Proximal Policy Optimization (PPO)** algorithm to train the agent, a state-of-the-art method for reinforcement learning.

## Setup and Installation

Follow these steps to set up the project and train the agent from scratch.

### 1. Clone the Repository

Clone this repository and create a new Python virtual environment.

```
git clone https://github.com/Unity-Technologies/ml-agents.git
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install Python Dependencies

Install the required Python packages, including `mlagents` and `torch`.

```
pip install mlagents==1.1.0
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 3. Build the Unity Environment

1. Open the Unity Hub and open the `ml-agents/Project` folder.
2. In the Unity Editor, open the 3DBall scene from `Assets/ML-Agents/Examples/3DBall/Scenes/3DBall.unity`.
3. Go to **File > Build Settings**.
4. Select **PC, Mac & Linux Standalone** as the platform.
5. Check the **Headless Mode** box.
6. Before building, create the output folder by running this command in your terminal:

```
mkdir -p ml-agents/trained-envs-executables/windows/3DBall
```

7. Click **Build** and save the executable to the `ml-agents/trained-envs-executables/windows/3DBall` folder.

### 4. Run the Training

Use the provided `train_3DBall.py` script to start the training process. The script will automatically connect to your Unity executable.

```
python train_3DBall.py
```

## How to Use the Trained Model

You can use the pre-trained model from this project in your own Unity environment.

1. Download the `3DBall.onnx` model file from the Hugging Face repository.
2. Open your Unity 3DBall project.
3. In the **Project** panel, navigate to `Assets/ML-Agents/Examples/3DBall/Prefabs`.
4. Select the **Agent** GameObject within the 3DBall prefab.
5. In the **Inspector** panel, locate the **Behavior Parameters** component.
6. Drag the `3DBall.onnx` model file into the **Model** field.
7. Press the **Play** button in the Unity Editor to see the agent in action.
