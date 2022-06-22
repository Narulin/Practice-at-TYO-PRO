rabbit = 10
rabbit2 = rabbit +1
x = 1

if rabbit <= 9 :
  while x <rabbit2:
    print(f"ウサギが{x}匹")
    x+=1
else:
  x = 1
  while x <= rabbit:
    if x<= rabbit-1:
      print(f"ウサギが{x}匹")
      x+=1
    elif x>rabbit-1:
      print("zzz...")
      x+=1
    else:
      break
  