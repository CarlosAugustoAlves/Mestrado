import collections
import numpy
import heapq
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
    matrix_draw_result = numpy.array(Value).reshape(
        (matrix_draw_max_y, matrix_draw_max_x))

    img = plt.imshow(matrix_draw_result, interpolation='nearest')
    img.set_cmap('gray')
    img.axes.get_xaxis().set_visible(False)
    img.axes.get_yaxis().set_visible(False)
    # remove rectangle borders and axes plt.axis('off')
    plt.savefig(directory_report + "\prioritized-sweeping-result.png")
    # plt.show()


def neighbors(state):
    neighbors_list = []
    for state_neighbor in range(states_count):
        for action in range(actions_count):
            if transition_matrix[state_neighbor, action, state] > 0 and state_neighbor not in neighbors_list:
                neighbors_list.append(state_neighbor)
    return neighbors_list


fill_transition_matrix()

fill_reward_states()

# First iteration: initialize values arbitrarily, e.g., zero
Value = [0 for state in range(states_count)]
policy = [None for state in range(states_count)]

priority_queue = []
state_priority = {}

file_results = open(directory_report + "\prioritized-sweeping-result.txt", "a")

iteration = 0

bellman_operator_execution = 0
policy_change_count = 0
total_iteration_by_state = 0

conver_state = [False for state in range(states_count)]
iteration_conver = 0
iteration_conver_dict = {}


for state in range(states_count):

    best_state_value = 0
    best_state_action = None

    for action in range(actions_count):
        calculed_value = sum([transition_matrix[state, action,
                                                sNext] * (reward[sNext] + (gama * Value[sNext])) for sNext in range(states_count)])

        bellman_operator_execution += states_count

        if calculed_value != 0 and (best_state_value == 0 or calculed_value > best_state_value):
            best_state_value = calculed_value
            best_state_action = action

    delta = abs(best_state_value - Value[state])
    if delta > 0:
        heapq.heappush(priority_queue, (-delta, state))
        state_priority[state] = -delta

while len(priority_queue) > 0:

    total_iteration_by_state += 1

    _, state = heapq.heappop(priority_queue)
    del state_priority[state]

    best_state_value = 0
    best_state_action = None

    for action in range(actions_count):
        calculed_value = sum([transition_matrix[state, action,
                                                sNext] * (reward[sNext] + (gama * Value[sNext])) for sNext in range(states_count)])

        bellman_operator_execution += states_count

        if calculed_value != 0 and (best_state_value == 0 or calculed_value > best_state_value):
            best_state_value = calculed_value
            best_state_action = action

    delta = abs(best_state_value - Value[state])

    if policy[state] != best_state_action:
        policy_change_count += 1

    if delta > epsilon:
        Value[state] = best_state_value
        policy[state] = best_state_action
        iteration_conver_dict[str(
            total_iteration_by_state)] = iteration_conver
    else:
        policy[state] = best_state_action

        if conver_state[state] is False:
            conver_state[state] = True
            iteration_conver += 1

        iteration_conver_dict[str(
            total_iteration_by_state)] = iteration_conver

        continue

    for state_neighbor in neighbors(state):
        new_priority = - \
            max([delta * transition_matrix[state_neighbor, action, state]
                 for action in actions])
        if new_priority < 0:
            if state_neighbor in state_priority and state_priority[state_neighbor] > new_priority:
                old_priority = state_priority[state_neighbor]
                index = priority_queue.index((old_priority, state_neighbor))
                priority_queue[index] = (new_priority, state_neighbor)
                state_priority[state_neighbor] = new_priority
            elif state_neighbor not in state_priority:
                heapq.heappush(priority_queue, (new_priority, state_neighbor))
                state_priority[state_neighbor] = new_priority
    iteration += 1

for state in range(states_count):
    print("Iteration: "+str(iteration)+" State: " + str(state + 1) +
          " Policy: " + str(policy[state]) + " Value: " + str(Value[state]))

    file_results.write("Iteration: "+str(iteration)+" State: " + str(state + 1) +
                       " Policy: " + str(policy[state]) + " Value: " + str(Value[state]) + "\n")


converg_by_iteration = [0 for state in range(total_iteration_by_state)]

for key, value in iteration_conver_dict.items():
    converg_by_iteration[int(key) - 1] = value

file_results.write(', '.join(str(x) for x in converg_by_iteration))

file_results.close()

draw_result_figure()

print("Total Bellman Operator Execution: " + str(bellman_operator_execution))
print("Total Policy Change: " + str(policy_change_count))
print("Total State Iterationl: " + str(total_iteration_by_state))
