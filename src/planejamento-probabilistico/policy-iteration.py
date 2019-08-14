import collections
import numpy
from pathlib import Path
import matplotlib.pylab as plt
import datetime

start_time = datetime.datetime.now()

current_path = Path().absolute()

directory_report = str(current_path) + "\\Datasets\\Env_1"


states = [state for state in range(135)]
actions = [0, 1, 2, 3, 4, 5]  # North, South, East, West, Up, Down
gama = 1
epsilon = 0.00001
states_count = len(states)
actions_count = len(actions)
transition_matrix = numpy.zeros((states_count, actions_count, states_count))
reward = []

def fill_transition_matrix():
    for i in range(actions_count):
        file_action_transition = open(directory_report + "\Action0" +
                                      str(i + 1) + ".txt", "r")
        file_info = file_action_transition.readlines()
        for line in file_info:
            state_from = int(float(line.split()[0])) - 1
            state_to = int(float(line.split()[1])) - 1
            state_probability = float(line.split()[2])
            transition_matrix[state_from, i, state_to] = state_probability


def fill_reward_states():
    file_reward = open(directory_report + "\Rewards.txt", "r")
    for line in file_reward.readlines():
        reward.append(float(line))
 
# Metrics For Report
policy_change_count = 0
state_iteration_count = 0
converged_states = [False for state in range(states_count)]
converged_states_by_iteration_timeline = []
# end

fill_transition_matrix()

fill_reward_states()

Value = numpy.zeros(states_count)

continue_iteration = True

# step 1: initialize policy arbitrarily, e.g., zero
policy = [0 for state in range(states_count)]

while continue_iteration == True:
    continue_iteration = False

    # step 2: setting state value for chosen policy
    for state in range(states_count):
        Value[state] = sum([transition_matrix[state, policy[state], sNext] *
                            (reward[sNext] + (gama * Value[sNext])) for sNext in range(states_count)])

    # step 3: policy improviment
    for state in range(states_count):

        state_iteration_count += 1

        best_state_value = 0
        best_state_action = 0

        for action in range(actions_count):
            calculed_value = sum([transition_matrix[state, action,
                                                    sNext] * (reward[sNext] + (gama * Value[sNext])) for sNext in range(states_count)])

            if calculed_value != 0 and (best_state_value == 0 or calculed_value > best_state_value):
                best_state_value = calculed_value
                best_state_action = action

        if policy[state] != best_state_action:
            policy_change_count += 1

        # step 3.1: stop criteria
        if abs(best_state_value - Value[state]) > epsilon:
            policy[state] = best_state_action
            continue_iteration = True
        else:
            if best_state_action != None:
                policy[state] = best_state_action

            if converged_states[state] is False:
                converged_states[state] = True

        converged_states_by_iteration_timeline.append(
            numpy.count_nonzero(converged_states))

end_time = datetime.datetime.now()

for state in range(states_count):
    print("Iteration: "+str(state_iteration_count)+" State: " + str(state + 1) +
                       " Policy: " + str(policy[state]) + " Value: " + str(Value[state]) + "\n")

print("Execution Time: " +
                   str((end_time - start_time).total_seconds() * 1000) + "\n")
print("Total Policy Change: " +
                   str(policy_change_count) + "\n")
print("Total State Iteration: " +
                   str(state_iteration_count) + "\n")

matrix_draw_max_x = 15
matrix_draw_max_y = 9
matrix_draw_result = numpy.array(Value).reshape((matrix_draw_max_y, matrix_draw_max_x))

img = plt.imshow(matrix_draw_result, interpolation='nearest')
img.set_cmap('gray')
img.axes.get_xaxis().set_visible(False)
img.axes.get_yaxis().set_visible(False)
plt.show()