def square_digits(num):
    digits = []
    for i in str(num):
        digits.append(i)
    sqs = []
    for i in digits:
        sqs.append(int(i)**2)
    sq_str = []
    for i in sqs:
        sq_str.append(str(i))
    result = ''.join(sq_str)
    return int(result)
        
    
    
    
    
square_digits(69)