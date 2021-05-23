left_op = int(input())
right_op = int(input())
sum_two_things = left_op + right_op
other_sum = sum_two_things - 1

if sum_two_things % 2:
    print("sum_two_things: " + str(sum_two_things))
else:
    print("other_sum: " + str(other_sum))