"""
the following is a demonstration of a function designed to identify whether more than half of the elements of any particular array are the same element as determined by inequality. The constraints this problem was developed under specify that the elements are not sortable, nor hashable.

this file contains two solutions

The original solution provided in class is named "identify_half_flawed" it has interesting probabilistic characteristics, but is ultimately inherently flawed. In a case where there is more than half the array of a certain value, it will nearly always degenerate into O(n**2). 

The solution provided named "identify_half" is an iterative solution to solve the problem. It will always make less than 5n element comparisons, 3n boolean array writes, and 13n additions. The sole difference between these algorithms is a completion array which prevents re-iteration on positions which are already guarenteed to be impossible.

Considerations

Though this solution is linear time. There are several characteristics which make it less desirable than a divide and conquer approach.

1. Divide and conquer approaches are innately more parallelizable.
2. This solution requires O(n) auxilluary memory complexity, the divide and conquer approach only requires O(log n) auxilluary memory.

"""

import random #used for the demo only

def identify_half(my_array):
    """
    Takes an array of objects of different equivalence classes. If any equivilance class takes up more than half the array's length that item of that class will be returned. If no such class exists the function will return one.

    returns a tuple containing the following:
    identified element: the element that is taking up more than half the list. None if no such element exists
    comparison count: number of element comparisions
    addition count: number of additions made counting modulus as additions since they are trivial modulus operations.

    """
    comparison_count = 0
    addition_count = 0
    if len(my_array) == 1:
        # trivial edge case
        return my_array[0] , comparison_count , addition_count
    completion = [False]*len(my_array)
    primary_position = 0
    while primary_position < len(my_array):
        if not completion[primary_position]:
            match_count = 1
            non_match_count = 0
            completion[primary_position] = True
            addition_count += 2
            secondary_position = (primary_position + 1) % len(my_array)
            while(match_count > non_match_count):
                comparison_count += 1
                if secondary_position == primary_position:
                    # if we have traveled all the way around then we have our more than half freequency value.
                    return my_array[primary_position] , comparison_count , addition_count
                if my_array[primary_position] == my_array[secondary_position]:
                    addition_count +=1
                    match_count += 1
                    # by some logic we can know that if this particular search doesn't find it then all the things it counts may also not be a start which will lead to a valid loop.
                    completion[secondary_position] = True
                else:
                    addition_count +=1
                    non_match_count += 1
                addition_count += 2
                secondary_position = (secondary_position + 1) % len(my_array)
        addition_count += 1
        primary_position += 1
    # no matches were found
    return None , comparison_count , addition_count

def identify_half_flawed(my_array):
    """
    FLAWED AND O(n^2) DO NOT USE 

    Takes an array of objects of different equivalence classes. If any equivilance class takes up more than half the array's length that item of that class will be returned. If no such class exists the function will return one.

    returns a tuple containing the following:
    identified element: the element that is taking up more than half the list. None if no such element exists
    comparison count: number of element comparisions
    addition count: number of additions made counting modulus as additions since they are trivial modulus operations.

    """
    comparison_count = 0
    addition_count = 0
    if len(my_array) == 1:
        # trivial edge case
        return my_array[0] , comparison_count , addition_count
    primary_position = 0
    while primary_position < len(my_array):
        match_count = 1
        non_match_count = 0
        addition_count += 2
        secondary_position = (primary_position + 1) % len(my_array)
        while(match_count > non_match_count):
            comparison_count += 1
            if secondary_position == primary_position:
                # if we have traveled all the way around then we have our more than half freequency value.
                return my_array[primary_position] , comparison_count , addition_count
            if my_array[primary_position] == my_array[secondary_position]:
                addition_count +=1
                match_count += 1
                # by some logic we can know that if this particular search doesn't find it then all the things it counts may also not be a start which will lead to a valid loop.
            else:
                addition_count +=1
                non_match_count += 1
            addition_count += 2
            secondary_position = (secondary_position + 1) % len(my_array)
        addition_count += 1
        primary_position += 1
    # no matches were found
    return None , comparison_count , addition_count

def demo():
    n = 1000000
    print("input size: %d\n" % (n*2))

    my_array =  ([0]*(n-1)) + ([1]*(n+1))
    print("simple case\nexpected result is 1")
    print("result: %d\ncomparisons: %d\nadditions: %d\n" % (*identify_half(my_array),))

    my_array =  ([0]*(n-1)) + ([1]*(n+1))
    random.shuffle(my_array)
    print("scrambled case\nexpected result is 1")
    print("result: %d\ncomparisons: %d\nadditions: %d\n" % (*identify_half(my_array),))

    my_array =  ([0]*(n)) + ([1]*(n))
    random.shuffle(my_array)
    a,b,c = identify_half(my_array)
    print("scrambled tied case\nexpected result is None")
    print(f"result: {a}\ncomparisons: {b}\nadditions: {c}\n")

    my_array = [random.randint(0,100000) for i in range(n*2)]
    a,b,c = identify_half(my_array)
    print("complete random case\nexpected result is None")
    print(f"result: {a}\ncomparisons: {b}\nadditions: {c}")

if __name__ == "__main__":
    demo()
