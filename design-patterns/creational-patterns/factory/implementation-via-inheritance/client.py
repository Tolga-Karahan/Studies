from factory import Creator, ConcreteCreator1, ConcreteCreator2


def operate(creator: Creator):
    print("I don't know the exact type, but still it works!")
    print(creator.operation())


if __name__ == "__main__":
    creator1 = ConcreteCreator1()
    creator2 = ConcreteCreator2()

    operate(creator1)
    operate(creator2)
