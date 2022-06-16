# Belajar Default Argument Value


def say_hello(first_name="Irawan", last_name=""):
    print(f"Hello {first_name} - {last_name}")


say_hello("Tedi")
say_hello(last_name="Saputra", first_name="Tedi")
