import collections
import numpy
from pathlib import Path
import matplotlib.pylab as plt

current_path = Path().absolute()

# Run Ambiente1
directory_report = str(current_path) + "\Dados_Relatorio1\Ambiente1"
states = [state for state in range(135)]
goal_state_index = 16
actions = [0, 1, 2, 3, 4, 5]  # North, South, East, West, Up, Down
matrix_draw_max_x = 15
matrix_draw_max_y = 9

# Run Ambiente0
# directory_report = str(current_path) + "\Dados_Relatorio1\Ambiente0"  # -> folder data
# states = [state for state in range(10)]  # -> count states
# goal_state_index = 4
# actions = [0, 1, 2, 3]  # North, South, East, West -> vector actions
# matrix_draw_max_x = 5
# matrix_draw_max_y = 2

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


def draw_result_figure():
    matrix_draw_result = numpy.array(V).reshape(
        (matrix_draw_max_y, matrix_draw_max_x))

    img = plt.imshow(matrix_draw_result, interpolation='nearest')
    img.set_cmap('hot')
    img.axes.get_xaxis().set_visible(False)
    img.axes.get_yaxis().set_visible(False)
    # remove rectangle borders and axes plt.axis('off')
    plt.savefig(directory_report + "\policy-iteration-results.png")
    # plt.show()


fill_transition_matrix()

fill_reward_states()

V = numpy.zeros(states_count)
iteration = 0
continue_iteration = True

# step 1: initialize policy arbitrarily, e.g., zero
policy = [0 for state in range(states_count)]
policy[goal_state_index] = None

file_results = open(directory_report + "\policy-iteration-results.txt", "a")

while continue_iteration == True:
    iteration += 1
    continue_iteration = False

    # step 2: setting state value for chosen policy
    for state in range(states_count):
        if state != goal_state_index:

            for sNext in range(states_count):
                teste = transition_matrix[state, policy[state], sNext]
                teste1 = reward[sNext]
                teste3 = V[sNext]

            V[state] = sum([transition_matrix[state, policy[state], sNext] *
                            (reward[sNext] + (gama * V[sNext])) for sNext in range(states_count)])

        print("Iteration: "+str(iteration)+" State: " + str(state + 1) +
              " Policy: " + str(policy[state]) + " Value: " + str(V[state]))

        file_results.write("Iteration: "+str(iteration)+" State: " + str(state + 1) +
                           " Policy: " + str(policy[state]) + " Value: " + str(V[state]) + "\n")

    # step 3: policy improviment
    for state in range(states_count):

        best_state_value = 0
        best_state_action = None

        for action in range(actions_count):
            calculed_value = sum([transition_matrix[state, action,
                                                    sNext] * (reward[sNext] + (gama * V[sNext])) for sNext in range(states_count)])
            
            if calculed_value != 0 and (best_state_value == 0 or calculed_value > best_state_value):
                best_state_value = calculed_value
                best_state_action = action

        # step 3.1: stop criteria
        if abs(best_state_value - V[state]) > epsilon:
            policy[state] = best_state_action
            continue_iteration = True

file_results.close()

draw_result_figure()