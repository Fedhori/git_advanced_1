from typing import List

def even_list(int_list: List[int]) -> List[int]:

    even_int_list = []

    for value in int_list:
        if value % 2 == 0:
            even_int_list.append(value)

    return even_int_list

def sum_of_squares_of_even(even_int_list: List[int]) -> int:

    sum = 0
    for value in even_int_list:
        if value % 2 == 0:
            sum += value * value

    return sum

# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

# Boilerplate code

if __name__ == "__main__":
    main()