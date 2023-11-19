def do_twice2(f):
    f()
    f()
    f()
    f()

def do_four2(f):
    do_twice2(f)
    do_twice2(f)

def print_beam2():
    print('+ - - - -',end=" ")

def print_post2():
    print('|        ',end=" ")

def print_beams_2():
    do_twice2(print_beam2)
    print('+')

def print_posts_2():
    do_twice2(print_post2)
    print('|')

print_beams_2()
print_posts_2()

def print_total2():
    print_beams_2()
    do_four(print_posts_2)

def print_totals2():
    do_twice(print_total2)
    print_beams()
print_totals2()

import pandas as pd
def greeter():
    print("How are you doing?")
    print("I love you!")

