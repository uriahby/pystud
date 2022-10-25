def circle_or_square(rad, area):
    circumference = rad * 3.14 * 2
    square_perimeter = 4 * (area ** (0.5))
    return circumference > square_perimeter


print(circle_or_square(5, 100))


nums = [1,2]
nums[0],nums[1] = nums[1],nums[0]
print(nums)
