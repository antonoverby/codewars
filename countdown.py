# How I did it
def reverse_seq(n):
    countdown = []
    countdown.append(n)
    while n > 1:
        n -= 1
        countdown.append(n)
    return countdown

#Some other ways to do 

# def reverse_seq(n):
#     return list(range(n, 0, -1))