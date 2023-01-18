def remove_char(s:str):
    ltrs = []
    for i in s:
        ltrs.append(i)
    print(ltrs)
    ltrs.pop(0)
    ltrs.pop(-1)
    print(ltrs)
    new_str = ''.join(ltrs)
    print(new_str)
        
    
    

remove_char('hello world')

    