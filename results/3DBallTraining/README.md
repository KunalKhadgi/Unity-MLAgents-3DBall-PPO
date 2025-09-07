---
library_name: ml-agents
tags:
  - 3d-ball
  - deep-reinforcement-learning
  - reinforcement-learning
  - ppo
  - unity-ml-agents
---

# 3DBall Trained Agent

This is a trained model of a PPO agent playing the 3DBall environment, created using the Unity ML-Agents library. The agent learns to balance a ball on a moving platform for as long as possible.

### Training Hyperparameters

The agent was trained using the following configuration from the `3DBall.yaml` file:

```yaml
behaviors:
  3DBall:
    trainer_type: ppo
    hyperparameters:
      learning_rate: 0.0003
      learning_rate_schedule: linear
      beta: 0.0005
      epsilon: 0.2
      lambd: 0.95
      num_epoch: 3
      buffer_size: 2048
      batch_size: 256
      time_horizon: 1024
    network_settings:
      normalize: false
      hidden_units: 128
      num_layers: 2
      vis_encode_type: simple
    reward_signals:
      extrinsic:
        gamma: 0.99
        strength: 1.0
    checkpoint_interval: 500000
    threaded: true
```

### Video Demo

Here is a video of the trained agent in action, demonstrating the learned behavior.

<video controls width="100%">
  <source src="3DBall_Demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
