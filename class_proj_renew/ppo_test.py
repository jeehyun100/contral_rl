import numpy as np
from manipulator_2d import Manipulator2D
from stable_baselines import PPO2



# Gym Environment 호출
env = Manipulator2D()

load_model_path = "tmp11/model_15752000.zip"
#load_model_path = "ppo2-mani7.zip"
#저장된 학습 파일로부터 weight 등을 로드
model = PPO2.load(load_model_path)

# 시뮬레이션 환경을 초기화
obs = env.reset()


# for _ in range(5):
#     obs = env.reset()
#     while True:
#         # 학습된 모델로부터 observation 값을 넣어 policy network에서 action을 만들어냄
#         action, _states = model.predict(obs)
#         obs, reward, done, info = env.step(action)
#
#         if done:
#             #env.buffer = env.buffer_csv
#             break
#
#     env.render()

points = 0
total_time = 0

while(total_time <= 60):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    if dones:

        total_time += env.t

        # env.buffer = env.buffer_csv
        if "status" in info:
            if info["status"] == "0":
                points += 1
                print("get {0} in time {1}".format(points, env.t))
                #print("robot bound")
        #         #break
        env.render()
        obs = env.reset()
        #break

#env.render()