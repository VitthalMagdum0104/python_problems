# def compute_binary(num):
#     if num == 0:
#         return 0
#     if num >= 1:
#         return str(compute_binary(num//2))+str(num % 2)


# print(compute_binary(8))


def compute_binary(num):
    if num >= 1:
        compute_binary(num // 2)
        print(num % 2, end='')


compute_binary(8)
# print(bin(8).replace("0b", ""))
