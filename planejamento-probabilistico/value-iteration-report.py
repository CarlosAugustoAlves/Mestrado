import collections
import numpy
from pathlib import Path
import matplotlib.pylab as plt

current_path = Path().absolute()

# Run Ambiente1
directory_report = str(current_path) + "\Dados_Relatorio1\Ambiente1"
states = [state for state in range(135)]
actions = [0, 1, 2, 3, 4, 5]  # North, South, East, West, Up, Down
matrix_draw_max_x = 15
matrix_draw_max_y = 9

# Run Ambiente0
# directory_report = str(current_path) + "\Dados_Relatorio1\Ambiente0"  # -> folder data
# states = [state for state in range(10)]  # -> count states
# actions = [0, 1, 2, 3]  # North, South, East, West -> vector actions
# matrix_draw_max_x = 5
# matrix_draw_max_y = 2

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
    img.set_cmap('hot')
    img.axes.get_xaxis().set_visible(False)
    img.axes.get_yaxis().set_visible(False)
    # remove rectangle borders and axes plt.axis('off')
    plt.savefig(directory_report + "\\value-iteration-results.png")
    #plt.show()

fill_transition_matrix()

fill_reward_states()

# First iteration: initialize values arbitrarily, e.g., zero
Value = [[0.0] * states_count]
policy = [None for state in range(states_count)]

iteration = 0
continue_iteration = True
file_results = open(directory_report + "\\value-iteration-results.txt", "a")

while continue_iteration:
    iteration += 1
    continue_iteration = False

    Value.append([0] * states_count)

    for state in range(states_count):

        best_state_value = 0
        best_state_action = None

        for action in range(actions_count):
            calculed_value = sum([transition_matrix[state, action,
                                                    sNext] * (reward[sNext] + (gama * Value[iteration - 1][sNext])) for sNext in range(states_count)])

            if calculed_value != 0 and (best_state_value == 0 or calculed_value > best_state_value):
                best_state_value = calculed_value
                best_state_action = action

        if abs(best_state_value - Value[iteration - 1][state]) > epsilon:
            Value[iteration][state] = best_state_value
            policy[state] = best_state_action
            continue_iteration = True
        else:
            Value[iteration][state] = Value[iteration - 1][state]
            policy[state] = best_state_action

        print("Iteration: "+str(iteration)+" State: " + str(state + 1) + " Policy: " +
              str(policy[state]) + " Value: " + str(Value[iteration][state]))

        file_results.write("Iteration: "+str(iteration)+" State: " + str(state + 1) +
                           " Policy: " + str(policy[state]) + " Value: " + str(Value[iteration][state]) + "\n")


file_results.close()

draw_result_figure()