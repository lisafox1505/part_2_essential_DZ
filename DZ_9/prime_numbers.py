def module_prime_numbers(num_end):
    start_num = 2
    while start_num <= num_end:
        is_prime = True
        for i in range(2, start_num):
            if start_num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield start_num
        start_num += 1

