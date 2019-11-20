n = int (input ())
red = []
green = []
blue = []
for i in range (n) :
    input_str = input ()
    input_list = input_str.split()
    red.append(int(input_list[0]))
    green.append(int(input_list[1]))
    blue.append(int(input_list[2]))

dp_red = []
dp_green = []
dp_blue = []

dp_red.append(red[0])
dp_green.append(green[0])
dp_blue.append(blue[0])

for i in range (1, n) :
    dp_red.append(red[i] + min(dp_green[i - 1], dp_blue[i - 1]))
    dp_green.append(green[i] + min(dp_red[i - 1], dp_blue[i - 1]))
    dp_blue.append(blue[i] + min(dp_red[i - 1], dp_green[i - 1]))

print (min(dp_red[-1], dp_green[-1], dp_blue[-1]))
