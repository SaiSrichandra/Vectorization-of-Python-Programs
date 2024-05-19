#!/usr/bin/env python

"""
Evaluate an environment and an agent.

Do this by running the agent in the environment for a while and measuring the
average reward.
"""

# 3rd party modules
import gym
# local modules
from rl_utils import get_parser, load_cfg, test_agent


def main(environment_name, agent_cfg_file):
    """
    Load, train and evaluate a Reinforcment Learning agent.

    Parameters
    ----------
    environment_name : str
    agent_cfg_file : str
    """
    cfg = load_cfg(agent_cfg_file)

    # Set up environment and agent
    env = gym.make(environment_name)
    cfg['env'] = env
    cfg['serialize_path'] = ('artifacts/{}-{}.pickle'
                             .format(cfg['model_name'], environment_name))
    agent = load_agent(cfg, env)
    rewards = test_agent(cfg, env, agent)
    print(f"Average reward: {rewards:5.3f}")
    print(f"Trained episodes: {agent.episode}")


if __name__ == "__main__":
    args = get_parser().parse_args()
    main(args.environment_name, args.agent_cfg_file)
