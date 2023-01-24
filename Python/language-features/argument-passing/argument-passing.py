import sys

# Python passes arguments by assignment. At first the parameter
# points to same memory address. If it is assigned something
# inside the body of the function, it gets a different memory
# address. We can verify it by using id() function which returns
# an unique integer representing the given object. This value is
# constant during lifetime of the object.
def compare_ids(param):
    print(f"ID of the parameter before assignment: {id(param)}")
    param += 1
    print(f"ID of the parameter after assignment: {id(param)}")


def get_ref_count(param):
    return sys.getrefcount(param)


# If passed object is immutable, for example integer, tuple,
# string, Python acts like pass by value. If passed object is
# mutable, Python acts like pass by reference which means object
# content can be changed in place. But, if a new object is
# assigned to the reference inside the function, object in the
# caller's scope won't be changed anymore. So Python initially
# behaves as call by reference, but changes to call by value as
# soon as a new object is assigned. Another related point is if
# augmented operators are used with mutable types, for exanmple
# +=, it will change the object in place. If we don't want such
# side effects we  should use = operator to assign result to a
# new object to not change provided argument.
def pass_by_value(obj):
    print(f"id before assigmnent: {id(obj)}")
    obj = type(obj)(obj)
    print(f"id after assigmnent: {id(obj)}")


def pass_with_side_effects(list_param):
    print(f"id before assigmnent: {id(list_param)}")
    list_param += list_param
    print(f"id after assigmnent: {id(list_param)}")


if __name__ == "__main__":
    # A related topic is reference counter. When an object is
    # asssigned to a name, Python first looks whether this value
    # is being represented by another object. If it's the case
    # this object is assigned to the name and its reference
    # counter is increased which is number of names or references
    # that points to the object. This counter can be obtained via
    # a call to sys.getrefcount(). Finally an antry is added to
    # the current namespaces which represent name-value pair. This
    # dictionary can be obtained via locals() or globals().
    my_arg = 5
    print(f"ID of the argument before passing to the function: {id(my_arg)}")
    compare_ids(my_arg)
    print(f"ID of the argument after passing to the function: {id(my_arg)}")

    # When a value is passed to a Python function, reference count
    # of the object is increased. Because get_ref_count function
    # also passes same value to another function, its reference
    # count is increased two times.
    print(sys.getrefcount("my arg"))
    print(get_ref_count("my arg"))

    # Force to pass by value
    pass_by_value([1, 2])

    # Pass by reference
    list_argument = [1, 2]
    print(f"List before assigmnent: {list_argument}")
    pass_with_side_effects(list_argument)
    print(f"List after assigmnent: {list_argument}")
