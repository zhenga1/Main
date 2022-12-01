def print_sums(k):
    print(k)
    def next_sum(n):
        return print_sums(n+k)
    return next_sum

print_sums(1)(3)(5)(7)


split = lambda n: (n//10,n%10)
def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
