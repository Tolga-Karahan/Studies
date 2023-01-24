class BaseClass:
    # For providing default value
    n_base_calls = 0

    def call_me(self):
        print("Base class is called!")
        self.n_base_calls += 1


class LeftSubClass(BaseClass):
    # For providing default value
    n_left_sub_calls = 0

    def call_me(self):
        # super() is used to prevent
        # calling base class twice.
        super().call_me()
        # BaseClass.call_me(self)
        print("Left sub class is called!")
        self.n_left_sub_calls += 1


class RightSubClass(BaseClass):
    # For providing default value
    n_right_sub_calls = 0

    def call_me(self):
        super().call_me()
        # BaseClass.call_me(self)
        print("Right sub class is called!")
        self.n_right_sub_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    # For providing default value
    n_sub_calls = 0

    def call_me(self):
        super().call_me()
        # LeftSubClass.call_me(self)
        # RightSubClass.call_me(self)
        print("Sub class is called!")
        self.n_sub_calls += 1


diamond_obj = SubClass()
diamond_obj.call_me()

# As can be shown from output of the code block below
# call_me method on base class is called twice. It can
# cause critical issues on production.
print(
    f"n_base_calls: {diamond_obj.n_base_calls}\n"
    + f"n_left_sub_calls: {diamond_obj.n_left_sub_calls}\n"
    + f"n_right_sub_calls: {diamond_obj.n_right_sub_calls}\n"
    + f"n_sub_calls: {diamond_obj.n_sub_calls}\n"
)

# Method resolution order can be shown via __mro__
# dunder. super() method is following names in
# __mro__ attribute. It means that super() doesn't
# always calls base class. If inheritance hierarchy
# has a diamond like shape, then leftmost class in
# the same level calls next sibling class.
print(SubClass.__mro__)
