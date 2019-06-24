import collections
import numpy
from pathlib import Path
import matplotlib.pylab as plt

current_path = Path().absolute()

# Run Dataset 1
directory_report = str(current_path) + "\Datasets\1"
states = [state for state in range(135)]
actions = [0, 1, 2, 3, 4, 5]  # North, South, East, West, Up, Down
matrix_draw_max_x = 15
matrix_draw_max_y = 9

gama = 1
reward_default = 1
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


def draw_result_figure():
    matrix_draw_result = numpy.array(
        Value[len(Value) - 1]).reshape((matrix_draw_max_y, matrix_draw_max_x))

    img = plt.imshow(matrix_draw_result, interpolation='nearest')
    img.set_cmap('gray')
    img.axes.get_xaxis().set_visible(False)
    img.axes.get_yaxis().set_visible(False)
    # remove rectangle borders and axes plt.axis('off')
    plt.savefig(directory_report + "\\value-iteration-result.png")
    # plt.show()


fill_transition_matrix()

fill_reward_states()

# First iteration: initialize values arbitrarily, e.g., zero
Value = [[0.0] * states_count]
policy = [None for state in range(states_count)]

iteration = 0
continue_iteration = True
file_results = open(directory_report + "\\value-iteration-result.txt", "a")

policy_change_count = 0
total_iteration_by_state = 0

conver_state = [False for state in range(states_count)]
iteration_conver = 0
iteration_conver_dict = {}

while continue_iteration:
    iteration += 1
    continue_iteration = False

    Value.append([0] * states_count)

    for state in range(states_count):

        total_iteration_by_state += 1

        best_state_value = 0
        best_state_action = None

        for action in range(actions_count):
            calculed_value = sum([transition_matrix[state, action,
                                                    sNext] * (reward[sNext] + (gama * Value[iteration - 1][sNext])) for sNext in range(states_count)])

            if calculed_value != 0 and (best_state_value == 0 or calculed_value > best_state_value):
                best_state_value = calculed_value
                best_state_action = action

        if policy[state] != best_state_action:
            policy_change_count += 1

        if abs(best_state_value - Value[iteration - 1][state]) > epsilon:
            Value[iteration][state] = best_state_value
            policy[state] = best_state_action
            continue_iteration = True
            iteration_conver_dict[str(
                total_iteration_by_state)] = iteration_conver
        else:
            if conver_state[state] is False:
                conver_state[state] = True
                iteration_conver += 1

            iteration_conver_dict[str(
                total_iteration_by_state)] = iteration_conver

            Value[iteration][state] = Value[iteration - 1][state]
            policy[state] = best_state_action

for state in range(states_count):
    print("Iteration: "+str(iteration)+" State: " + str(state + 1) + " Policy: " +
          str(policy[state]) + " Value: " + str(Value[iteration][state]))

    file_results.write("Iteration: "+str(iteration)+" State: " + str(state + 1) +
                       " Policy: " + str(policy[state]) + " Value: " + str(Value[iteration][state]) + "\n")


converg_by_iteration = [0 for state in range(total_iteration_by_state)]

for key, value in iteration_conver_dict.items():
    converg_by_iteration[int(key) - 1] = value

file_results.write( ', '.join(str(x) for x in converg_by_iteration))

file_results.close()

draw_result_figure()

print("Total Policy Change: " + str(policy_change_count))
print("Total State Iterationl: " + str(total_iteration_by_state))
