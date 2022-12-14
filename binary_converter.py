def decimal_to_binary(num):
    if num == 0:
        return "0"
    else:
        if num == 0:
            return ""
        else:
            return decimal_to_binary(num // 2) + str(num % 2)

# Test the function
print(decimal_to_binary(1)) # Should print 1010
print(decimal_to_binary(0)) # Should print 0
