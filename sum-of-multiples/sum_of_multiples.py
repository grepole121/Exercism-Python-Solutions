def sum_of_multiples(limit, multiples):
    nums = []

    if 0 in multiples:
        multiples.remove(0)

    for num in multiples:
        for i in range(1, limit):
            if (i % num == 0) and (i not in nums):
                nums.append(i)
    return(sum(nums))


sum_of_multiples(150, [5, 6, 8])
