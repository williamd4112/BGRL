from gym.envs.registration import register

register(
		id = 'point-v0',
		entry_point='simpleenvs.point:PointEnv',
		max_episode_steps=50,
		)

register(
		id = 'pointmass-v0',
		entry_point='simpleenvs.pointmass:PointmassEnv',
		max_episode_steps=50,
		)


