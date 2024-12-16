def count_good_number(num):
    def is_good_number(n):
        str_n = str(n)
        for i,digit in enumerate(str_n[::-1]):
            if i%2==0: #奇数位
                if int(digit)%2==0:
                    return False
            else: #偶数位
                if int(digit)%2!=0:
                    return False
        return True

    count = 0
    for n in range(1,num+1):
        if is_good_number(n):
            count += 1
    return count


num=int(input())
count=count_good_number(num)
print(count)
