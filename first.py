def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -',end=" ")

def print_post():
    print('|        ',end=" ")

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

print_beams()
print_posts()

def print_total():
    print_beams()
    do_four(print_posts)

print_total()

def print_totals():
    do_twice(print_total)
    print_beams()

print_totals()
