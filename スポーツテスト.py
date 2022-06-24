sport = {"握力":6,"上体起こし":7,"長座体前屈":8,
"反復横跳び":7,"走る":3,"シャトルラン":6,
"ハンドボール投げ":6,"立ち幅跳び":6}

goukei = sport.get("握力")+sport.get("上体起こし")+sport.get("長座体前屈")+sport.get("反復横跳び")+sport.get("走る")+sport.get("シャトルラン")+sport.get("ハンドボール投げ")+sport.get("立ち幅跳び")
# heikin = goukei/len(sport)

# print(goukei)

if goukei >= 57:
  print("A判定")
if 51 <= goukei <= 56:
  print("B判定")
if 41 <= goukei <= 50:
  print("C判定")
if 31 <= goukei <= 40:
  print("D判定")
if goukei <=30:
  print("E判定")