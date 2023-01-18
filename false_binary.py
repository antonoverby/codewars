# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

def fake_bin(x):
   nums = []
   for i in x:
       nums.append(int(i))
   
   fake_binary = []
   for num in nums:
       if num >= 5:
           fake_binary.append(1)
       else:
           fake_binary.append(0)
   
   bin_string = ''.join(str(fake_binary))
   
   
   print(fake_binary)
   print(bin_string)
    

fake_bin('156352')