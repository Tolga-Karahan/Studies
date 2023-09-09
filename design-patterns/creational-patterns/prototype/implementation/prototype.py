# Python provides prototype pattern out-of-the-box via copy library
# To implement specific copying logic that will be used by the copy
# methods, we can implement __copy__ and __deepcopy__ methods
import copy


class SelfReferencingClass:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Cloneable:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        copied_some_list_of_objects = copy.copy(self.some_list_of_objects)
        copied_some_circular_ref = copy.copy(self.some_circular_ref)

        clone_obj = self.__class__(
            self.some_int, copied_some_list_of_objects, copied_some_circular_ref
        )
        clone_obj.__dict__.update(self.__dict__)

        return clone_obj

    def __deepcopy__(self):
        # memo dictionary is used by deepcopy to prevent
        # infinite copies in case of circular dependencies
        if memo is None:
            memo = {}

        deep_copied_some_list_of_objects = copy.deepcopy(self.some_list_of_objects)
        deep_copied_some_circular_ref = copy.deepcopy(self.some_circular_ref)

        clone_obj = self.__class__(
            self.some_int,
            deep_copied_some_list_of_objects,
            deep_copied_some_circular_ref,
        )
        clone_obj.__dict__.update(self.__dict__)

        return clone_obj
