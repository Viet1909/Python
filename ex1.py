import math
string = input()
l = len(string)
if l % 2 != 0:
  print('The central point of the string is '+string[math.floor(l/2)]+'.')
  s_1 = string[:math.floor(l/2):]
  s_2 = string[math.floor(l/2)+1::]
else:
  print('There is no central point.')
  s_1 = string[:math.floor(l/2):]
  s_2 = string[math.floor(l/2)::]
if s_1==s_2:
  print('Symmertical String!')
elif s_1>s_2:
  print('Left Bias!')
else:
  print('Right Bias!')