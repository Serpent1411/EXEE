x=2345
sum =0
step =1
while x >9:
    while  (x%10)>0 :
        y= x%10
        sum = sum + y
        a = sum
        x = int(x/10)
    x = sum
    #print("Step-",step," Sum:",sum)
    print(f"Step-{step} Sum:{sum}")
    sum=0
    step += 1
