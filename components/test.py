def count_good_numbers(N):
    def is_good_number(num):
        num_str = str(num)
        for i, digit in enumerate(num_str[::-1]):  # 从右向左遍历，个位开始
            if i % 2 == 0:  # 奇数位（个位、百位、万位...）
                if int(digit) % 2 == 0:  # 奇数位应该是奇数
                    return False
            else:  # 偶数位（十位、千位、十万位...）
                if int(digit) % 2 != 0:  # 偶数位应该是偶数
                    return False
        return True

    good_numbers = []
    count = 0
    for num in range(1, N + 1):
        if is_good_number(num):
            good_numbers.append(num)
            count += 1
    return count, good_numbers

# 示例
N = int(input())
count, numbers = count_good_numbers(N)
print(count)
print(f"好数列表: {numbers}")