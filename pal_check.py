from pal_funct import palindrome_checker 

def lambda_handler(event, context):
    counter = 0
    for key in event:
        print event[key]
        if (palindrome_checker(event[key])):
            counter+=1
    print counter
    return counter
        
        

