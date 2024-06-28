paint = int(input())
paint_per_cap = int(input())
dollars_per_cap = int(input())

num_caps = paint // paint_per_cap
result = num_caps * dollars_per_cap
paint = paint - num_caps * paint_per_cap
result = result + paint

print(result)
