
def minion_game(string):
    vowels = 'AEIOU'
    n = len(string)
    
    stuart_score = 0
    kevin_score = 0
    
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n-i
        else:
            stuart_score += n-i
    
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")
    
    
        
      

