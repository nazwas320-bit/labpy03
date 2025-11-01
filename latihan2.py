modal = 100000000
laba = []

for i in range(1, 9):
    if i ==1 or i == 2:
        persentase = 0
    elif i ==3 or i ==4:
        persentase = 0.01
    elif i ==5 or i ==6 or i ==7:
        persentase = 0.05
    elif i ==8:
        persentase = 0.03

    laba_bulan = modal * persentase
    laba.append(laba_bulan)
    print("laba bulan ke-", i, "sebesar:", laba_bulan)

total = sum(laba)
print("total laba adalah:", total)