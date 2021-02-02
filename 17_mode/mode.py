def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # provided solution looks more efficient 
    # (create dictionary of num and frequency with one iteraion of nums)

    max = 0
    for item in set(nums) :
        if nums.count(item) > max:
            result = item
            max = nums.count(item)
    return result