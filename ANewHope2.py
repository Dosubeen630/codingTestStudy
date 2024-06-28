def hope(numbers):
    return "A long time ago in a galaxy " + ", ".join(["far"]*numbers) + " " + "away..."

assert(hope(5) == "A long time ago in a galaxy far, far, far, far, far away...")
assert(hope(4) == "A long time ago in a galaxy far, far, far, far away...")
assert(hope(1) == "A long time ago in a galaxy far away...")
