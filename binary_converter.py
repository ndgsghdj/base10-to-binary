def decimal_to_binary(num):
    if num == 0:
        return "0"
    else:
        if num == 0:
            return ""
        else:
            return decimal_to_binary(num // 2) + str(num % 2)


print(decimal_to_binary(10)) 
print(decimal_to_binary(0))
