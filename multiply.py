

import math
import random


if __name__ == "__main__":
    num_1 = random.randint(0, 32767)
    num_2 = random.randint(0, 32767)
    print("the first number is ")
    print( num_1)
    print("the sencnd number is ")
    print( num_2)

    p_1 = math.log(num_1/3) / math,log(2) +2 
    p_2 = math.log(num_2/3) / math,log(2) +2 

    result = p_1 * num_2 + p_2*num_1 - p_1*p_2
    print (result)
    