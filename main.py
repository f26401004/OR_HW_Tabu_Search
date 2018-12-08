import copy
import timeit

time = [10, 10, 13, 4, 9, 4, 8, 15, 7, 1, 9, 3, 15, 9, 11, 6, 5, 14, 18 ,3]
date = [50, 38, 49, 12, 20, 105, 73, 45, 6, 64, 15, 6, 92, 43, 78, 21, 15, 50, 150, 99]
weight = [10, 5, 1, 5, 10, 1, 5, 10, 5, 1, 5, 10 ,10 ,5, 1 ,10, 5, 5, 1, 5]

def compute_tardness(current, length):
	result = 0
	for index1 in range(0, length):
		buf = 0
		for index2 in range(0, index1 + 1):
			buf += time[current[index2] - 1]
		buf -= date[current[index1] - 1]
		buf *= weight[current[index1] - 1]
		result += max(buf, 0)
	return result

def tabu_search(initial, tabu_size, iteration):
	current = copy.copy(initial)
	tabu_list = []
	solution_list = []
	solution_tardness = 999999999
	while iteration > 0:
		buffer_tabu_pair = []
		buffer_list = []
		buffer_value = []
		for index in range(0, 19):
			if [current[index + 1], current[index]] not in tabu_list:
				buffer_tabu_pair.append([current[index], current[index + 1]])
				current[index], current[index + 1] = current[index + 1], current[index]
				buffer_value.append(compute_tardness(current, len(initial)))
				buffer_list.append(copy.copy(current))
				current[index], current[index + 1] = current[index + 1], current[index]
		min_index = buffer_value.index(min(buffer_value))
		if solution_tardness > min(buffer_value):
			solution_tardness = min(buffer_value)
			solution_list = buffer_list[min_index]
		tabu_list.append(buffer_tabu_pair[min_index])
		if len(tabu_list) > tabu_size:
			tabu_list.pop(0)
		current = buffer_list[min_index]
		iteration = iteration - 1
	return [solution_tardness, solution_list]


best_solution = {
	"fitness_function_value": 99999999,
	"list": [],
	"waste_time": 0,
	"tabu_list_size": 0,
	"search_iteration": 0
}
for index1 in range(1, 11):
	for index2 in range(1, 101):
		start = timeit.default_timer()
		result = tabu_search(range(1, 21), index1, index2)
		end = timeit.default_timer()

		if best_solution["fitness_function_value"] > result[0]:
			best_solution["fitness_function_value"] = result[0]
			best_solution["list"] = result[1]
			best_solution["waste_time"] = end - start
			best_solution["tabu_list_size"] = index1
			best_solution["search_iteration"] = index2
		print("Tabu list size: {}".format(index1))
		print("Tabu search iteration: {}".format(index2))
		print('Time: {}'.format(end - start))
		print("Solution tardness: {}".format(result[0]))
		print("Solution list: {}".format(result[1]))
		print("")

print("==================== find solution process complete ====================")
print("")
print("Best solution infomation:")
print("1. Fitness function value: {}".format(best_solution["fitness_function_value"]))
print("2. Tabu list size: {}".format(best_solution["tabu_list_size"]))
print("3. Waste time: {}".format(best_solution["waste_time"]))
print("4. Search iteration: {}".format(best_solution["search_iteration"]))
