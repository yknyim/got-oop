
# name
# avatar: (profile picture)
# inventory

# def do_stuff():
#     pass

class Character():
    # the "dunder init" method is the constructor
    def __init__(self, new_name):
        # `self` is the customary way to refer to the instance being built
        # In some other languages, they use `this`
        self.name = new_name