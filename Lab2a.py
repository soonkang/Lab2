
def display_main_menu():
    print("Enter some numbers separated by space (e.g. 5 67 32)")
display_main_menu()

def get_user_input(str_list):
    float_list = []
    for string in str_list:
        try:
            float_list.append(float(string))
        except ValueError:
            print(f"Skipping non-numeric value: {string}")
    return float_list
print("Enter your numbers: ")
string_list = input().split() # Splitting the input string into a list of strings
float_list = get_user_input(string_list)
print(float_list)

def calc_average(float_list):
    total = sum(float_list)
    count = len(float_list)
    average = total / count
    print("The average is:", average)
calc_average(float_list)

def find_min_max(float_list):
    minimum=min(float_list)
    maximun=max(float_list)
    print("The minimum value is:", minimum)
    print("The maximum value is:", maximun)
find_min_max(float_list)

def sort_temperature(float_list):
    sorted_list = sorted(float_list)
    print("The sorted list is:", sorted_list)
    return sorted_list

sorted_list = sort_temperature(float_list)

def calc_median_temperature(sorted_list):
    list_length = len(sorted_list)
    middle_index = list_length // 2
    if list_length % 2 == 0:
        median = (sorted_list[middle_index-1] + sorted_list[middle_index ]) / 2
    else:
        median = sorted_list[middle_index]
    print("The median is:", median)

calc_median_temperature(sorted_list)