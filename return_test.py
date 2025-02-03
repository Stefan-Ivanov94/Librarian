#def no_return():
#    return ('a','b')
#
#nothing = no_return()
#if nothing:
#    print(f"Returned {nothing}")
#else:
#    print(nothing)
test_dict = {('a',1):2 ,('b',2):7, ('c',3):-3}
nothing = None
test_dict[nothing] = 42
print(test_dict)