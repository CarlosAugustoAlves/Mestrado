import gym
import numpy as np
from gym import wrappers
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

BATCH_SIZE = 64
MAX_EPISODES = 2000
GAMMA = 0.9  # Discount factor

env = gym.make('CartPole-v0')  # Instantiate a new environment

# Show the type and shape of observations
print('States:', env.observation_space)
# Show the type and shape of possible actions
print('Actions:', env.action_space)

env.reset()  # Set env to initial state

done = False
while not done:
    # env.render()
    _, _, done, _ = env.step(env.action_space.sample())  # Perform random actions

env.close()

model = Sequential()
model.add(Dense(32, activation='relu', name='fc1', input_shape=env.observation_space.shape))
model.add(Dense(32, activation='relu', name='fc2'))
model.add(Dense(env.action_space.n, name='fc3'))
model.summary()
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

# A circular buffer with max of 2000 samples
buffer = deque(maxlen=MAX_EPISODES)

while len(buffer) < BATCH_SIZE:  # Fill buffer with one batch, so we can start learning
    state = env.reset()
    done = False

    while not done:
        action = env.action_space.sample()
        new_state, reward, done, info = env.step(action)
        transition = (state, action, reward, new_state, done)
        buffer.append(transition)  # Store trasition in the buffer

exploration_decay = 0.995  # Decay rate
exploration_rate = 1.0    # Initial exploration rate
total_rewards = []

for episode in range(1, MAX_EPISODES+1):
    state = env.reset()
    done = False
    score = 0.0

    while not done:
        if np.random.rand() < exploration_rate:
            # If rand < exploration_rate agent must explore
            action = env.action_space.sample()
        else:
            # Else agent will use Q-Network to get the best action
            action = np.argmax(model.predict(state[None]))

        new_state, reward, done, info = env.step(action)  # Perform action
        transition = (state, action, reward, new_state, done)
        buffer.append(transition)  # Store transtion in the buffer

        state = new_state

        score += reward  # Update episode total score

    if exploration_rate > 0.01:
        # Update exploration_rate. It must be at least 1%
        exploration_rate *= exploration_decay

    total_rewards.append(score)

    # Experice Replay
    # Sample a random batch from buffer
    indexes = np.random.choice(len(buffer), BATCH_SIZE, replace=True)
    batch = [buffer[i] for i in indexes]
    states = np.array([item[0] for item in batch])
    actions = np.array([item[1] for item in batch])
    rewards = np.array([item[2] for item in batch])
    new_states = np.array([item[3] for item in batch])
    terminals = np.array([item[4] for item in batch])

    # Predict Q(s, a, theta) for states
    predictions = model.predict(states)

    # Update values according to Deep Q-Learnig algorithm
    for i in range(len(batch)):
        if terminals[i]:
            # yj = rj
            predictions[i, actions[i]] = rewards[i]
        else:
            # yj = rj + gamma * Q(s', a', theta)
            predictions[i, actions[i]] = rewards[i] + GAMMA * \
                np.max(model.predict(new_states[i][None]))

    # Train model with the batch
    loss, _ = model.train_on_batch(states, predictions)

    print('Episode: {}, Score: {}'.format(episode, score))

smoothed_rewards = [np.mean(total_rewards[max(0, i-10):i+1])
                    for i in range(len(total_rewards))]

plt.figure(figsize=(12, 8))
plt.plot(smoothed_rewards)
plt.title('Deep Q-Learning')
plt.xlabel('Episódios')
plt.ylabel('Recompensa') 
plt.show()

file_results = open('.\DeepQ-Learning-Results.txt', 'w')
file_results.write(', '.join(str(x) for x in total_rewards))
file_results.close()