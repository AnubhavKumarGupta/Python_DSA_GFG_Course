def toggle_bits(n):
    binary_str = bin(n)[2:]
    binary_list = list(binary_str)
    length = len(binary_str)

    if length % 2 == 0:
        middle_left_index = length // 2 - 1
        middle_right_index = length // 2

        if binary_list[middle_left_index] == "1":
            binary_list[middle_left_index] = "0"
        else:
            binary_list[middle_left_index] = "1"

        if binary_list[middle_right_index] == "1":
            binary_list[middle_right_index] = "0"
        else:
            binary_list[middle_right_index] = "1"
    else:
        middle_index = (length + 1) // 2 - 1

        if binary_list[middle_index] == "1":
            binary_list[middle_index] = "0"
        else:
            binary_list[middle_index] = "1"

    modified_binary_str = "".join(binary_list)
    return int(modified_binary_str, 2)


if __name__ == "__main__":
    test_cases = int(input("Enter the number of test cases: "))

    for _ in range(test_cases):
        num = int(input("Enter a decimal number: "))
        result = toggle_bits(num)
        print(f"Modified number: {result}")
