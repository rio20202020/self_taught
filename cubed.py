def pow_3(integer):
    return integer**3

with open("st.txt", "r") as r:
    print(r.read())

import csv
with open("st.csv","w", newline='', encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(["lemon", "spycy", "sower","フレッシュ"])
    w.writerow(["melon", "georjous", "bolumy","デリシャス"])
    w.writerow(["cherry","small", "cute","リトル"])
