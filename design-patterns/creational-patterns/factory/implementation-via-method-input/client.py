from factory import computer_factory

if __name__ == "__main__":
    pc = computer_factory(computer_type="pc", cpu="8core", ram="16gb", disk="512gb")
    server = computer_factory(
        computer_type="server",
        cpu="64core",
        ram="128gb",
        disk="2TB",
        purpose="Web Hosting",
    )

    print(pc)
    print(server)
