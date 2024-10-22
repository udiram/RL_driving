import gym
import metadrive

# List all available environments
envs = [env_spec.id for env_spec in gym.envs.registry.values()]
for env in envs:
    if "MetaDrive" in env:
        print(env)