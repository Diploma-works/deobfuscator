left_op = 1
right_op = 2

try:
    1 / (right_op % 2)
except Exception:
    sum_two_things = left_op + right_op
finally:
    sum_two_things = left_op - right_op
