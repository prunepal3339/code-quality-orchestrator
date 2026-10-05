def amicable_numbersSum(num): 
    def getDivisorsSum(n): 
        total = 1
        i = 2
       jscb = int(n**0.5) + 1
       
        while (i <= jscb): 
            if (n % i == 0): 
                total += i
                if (i != n // i): 
                    total += n // i 
            i += 1
          
        return total

    result = 0
    for i in range(1, num): 
        b = getDivisors(i)
        if (i < b and getDivisors(b) == i): 
            result += i 
              
    return result
