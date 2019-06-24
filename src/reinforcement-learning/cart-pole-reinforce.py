import numpy as np
import matplotlib.pyplot as plt
import gym
import tensorflow as tf
from tensorflow.contrib.layers import fully_connected
import warnings

BATCH_SIZE = 10
MAX_EPISODES = 2000
GAMMA = 0.99


class policy_estimator(object):

    def __init__(self, sess, env):
        # Pass TensorFlow session object
        self.sess = sess
        # Get number of inputs and outputs from environment
        self.n_inputs = env.observation_space.shape[0]
        self.n_outputs = env.action_space.n
        self.learning_rate = 0.01

        # Define number of hidden nodes
        self.n_hidden_nodes = 16

        # Set graph scope name
        self.scope = "policy_estimator"

        # Create network
        with tf.variable_scope(self.scope):
            initializer = tf.contrib.layers.xavier_initializer()

            # Define placholder tensors for state, actions, and rewards
            self.state = tf.placeholder(tf.float32, [None, self.n_inputs],
                                        name='state')
            self.rewards = tf.placeholder(tf.float32, [None], name='rewards')
            self.actions = tf.placeholder(tf.int32, [None], name='actions')

            layer_1 = fully_connected(self.state, self.n_hidden_nodes,
                                      activation_fn=tf.nn.relu,
                                      weights_initializer=initializer)
            output_layer = fully_connected(layer_1, self.n_outputs,
                                           activation_fn=None,
                                           weights_initializer=initializer)

            # Get probability of each action
            self.action_probs = tf.squeeze(
                tf.nn.softmax(output_layer - tf.reduce_max(output_layer)))

            # Get indices of actions
            indices = tf.range(0, tf.shape(output_layer)[0]) \
                * tf.shape(output_layer)[1] + self.actions

            selected_action_prob = tf.gather(tf.reshape(self.action_probs, [-1]),
                                             indices)

            # Define loss function
            self.loss = - \
                tf.reduce_mean(tf.log(selected_action_prob) * self.rewards)

            # Get gradients and variables
            self.tvars = tf.trainable_variables(self.scope)
            self.gradient_holder = []
            for j, var in enumerate(self.tvars):
                self.gradient_holder.append(tf.placeholder(tf.float32,
                                                           name='grads' + str(j)))

            self.gradients = tf.gradients(self.loss, self.tvars)

            # Minimize training error
            self.optimizer = tf.train.AdamOptimizer(self.learning_rate)
            self.train_op = self.optimizer.apply_gradients(
                zip(self.gradient_holder, self.tvars))

    def predict(self, state):
        probs = self.sess.run([self.action_probs],
                              feed_dict={
                                  self.state: state
        })[0]
        return probs

    def update(self, gradient_buffer):
        feed = dict(zip(self.gradient_holder, gradient_buffer))
        self.sess.run([self.train_op], feed_dict=feed)

    def get_vars(self):
        net_vars = self.sess.run(tf.trainable_variables(self.scope))
        return net_vars

    def get_grads(self, states, actions, rewards):
        grads = self.sess.run([self.gradients],
                              feed_dict={
            self.state: states,
            self.actions: actions,
            self.rewards: rewards
        })[0]
        return grads


def discount_rewards(rewards, gamma):
    discounted_rewards = np.zeros(len(rewards))
    cumulative_rewards = 0
    for i in reversed(range(0, len(rewards))):
        cumulative_rewards = cumulative_rewards * gamma + rewards[i]
        discounted_rewards[i] = cumulative_rewards
    return discounted_rewards


def reinforce(env, policy_estimator, num_episodes=MAX_EPISODES,
              batch_size=BATCH_SIZE, gamma=GAMMA):

    total_rewards = []

    # Set up gradient buffers and set values to 0
    grad_buffer_pe = policy_estimator.get_vars()
    for i, g in enumerate(grad_buffer_pe):
        grad_buffer_pe[i] = g * 0

    # Get possible actions
    action_space = np.arange(env.action_space.n)

    for ep in range(num_episodes):
        # Get initial state
        s_0 = env.reset()
        reward = 0
        episode_log = []
        complete = False

        # Run through each episode
        while complete == False:

            # Get the probabilities over the actions
            action_probs = policy_estimator.predict(
                s_0.reshape(1, -1))
            # Stochastically select the action
            action = np.random.choice(action_space,
                                      p=action_probs)
            # Take a step
            s_1, r, complete, _ = env.step(action)

            # Append results to the episode log
            episode_log.append([s_0, action, r, s_1])
            s_0 = s_1

            # If complete, store results and calculate the gradients
            if complete:
                episode_log = np.array(episode_log)

                # Store raw rewards and discount episode rewards
                total_rewards.append(episode_log[:, 2].sum())
                discounted_rewards = discount_rewards(
                    episode_log[:, 2], gamma)

                print('Episode: {}, Score: {}'.format(
                    ep, episode_log[:, 2].sum()))

                # Calculate the gradients for the policy estimator and
                # add to buffer
                pe_grads = policy_estimator.get_grads(
                    states=np.vstack(episode_log[:, 0]),
                    actions=episode_log[:, 1],
                    rewards=discounted_rewards)
                for i, g in enumerate(pe_grads):
                    grad_buffer_pe[i] += g

        # Update policy gradients based on batch_size parameter
        if ep % batch_size == 0 and ep != 0:
            policy_estimator.update(grad_buffer_pe)
            # Clear buffer values for next batch
            for i, g in enumerate(grad_buffer_pe):
                grad_buffer_pe[i] = g * 0

    return total_rewards


env = gym.make('CartPole-v0')
tf.reset_default_graph()
sess = tf.Session()

pe = policy_estimator(sess, env)

# Initialize variables
init = tf.global_variables_initializer()
sess.run(init)

rewards = reinforce(env, pe)

smoothed_rewards = [np.mean(rewards[max(0, i-10):i+1])
                    for i in range(len(rewards))]

plt.figure(figsize=(12, 8))
plt.plot(smoothed_rewards)
plt.title('REINFORCE - Policy Estimation')
plt.xlabel('Episódios')
plt.ylabel('Recompensa')
plt.show()

file_results = open('.\REINFORCE-Results.txt', 'a')
file_results.write(', '.join(str(x) for x in rewards))
file_results.close()
