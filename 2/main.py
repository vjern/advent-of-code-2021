with open('input.txt') as f:
    items = [s.strip() for s in f.readlines()]

print(len(items))

x, z = 0, 0

for item in items:
    dir, num_str = item.split()
    num = int(num_str)
    dx = (dir == 'forward') * num
    dz = ((dir == 'down') - (dir == 'up')) * num
    x += dx
    z += dz

print(x, z)
print(x *z)

x, z = 0, 0
aim = 0

for item in items:
    dir, num_str = item.split()
    num = int(num_str)
    dx = (dir == 'forward') * num
    d_aim = ((dir == 'down') - (dir == 'up')) * num
    aim += d_aim
    dz = (dir == 'forward') * num * aim
    x += dx
    z += dz

print(x, z)
print(x *z)
