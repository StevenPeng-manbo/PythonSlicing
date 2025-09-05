# Python slicing demonstration
# This file contains basic slicing examples

def basic_slicing_examples():
    """Demonstrate basic Python slicing operations"""
    
    # Example 1: Basic list slicing
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Original list:", my_list)
    print("Slice [2:5]:", my_list[2:5])  # Elements from index 2 to 4
    print("Slice [:5]:", my_list[:5])    # First 5 elements
    print("Slice [5:]:", my_list[5:])    # Elements from index 5 to end
    print("Slice [::2]:", my_list[::2])  # Every second element
    print("Slice [::-1]:", my_list[::-1]) # Reverse the list
    
    # Example 2: String slicing
    my_string = "Hello World"
    print("\nOriginal string:", my_string)
    print("Slice [0:5]:", my_string[0:5])  # 'Hello'
    print("Slice [6:]:", my_string[6:])    # 'World'
    print("Slice [::2]:", my_string[::2])  # 'HloWrd'
    
    # Example 3: Negative indexing
    print("\nNegative indexing:")
    print("Slice [-3:]:", my_list[-3:])    # Last 3 elements
    print("Slice [:-3]:", my_list[:-3])    # All except last 3 elements

if __name__ == "__main__":
    basic_slicing_examples()