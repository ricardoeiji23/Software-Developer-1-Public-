def insertion_sort_descending(arr):
    for i in range(1, len(arr)): #From 1 to the length of the arrray 
        value = arr[i] #This line stores the current element at index i in the variable value.
        j = i - 1 
        while j >= 0 and arr[j] < value: 
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = value

def main():
    # Initialize an empty list to store user input
    list_values = []

    # Take 5 integer values from the user
    for i in range(5):
        while True:
            try:
                value = int(input(f"Enter integer value {i + 1}: ")) #5 inputs
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        list_values.append(value) #Add the inputs in the list

    # Display the original array
    print("\nOriginal Array:", list_values)

    # Sort the array in descending order using "insertion sort"
    insertion_sort_descending(list_values)

    # Display the sorted array
    print("Sorted Array (Descending Order):", list_values)

if __name__ == "__main__":
    main()
