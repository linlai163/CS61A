def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)
    
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)
    
# result = is_even(4)
# print(result)

def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n-1)
        
def play_bob(n):
    if n == 0:
        print("Alice wins")
    else:
        play_alice(n-1)
        
play_alice(9)