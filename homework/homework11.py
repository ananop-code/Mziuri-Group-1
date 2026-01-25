sheyvanili_tseli=input("sheiyvane weli: ")
f=open("oscars.txt", "r", encoding="utf-8")
yvela_striqoni=f.readlines()
f.close()
print(f"{sheyvanili_tseli} wlis oscarosnebi arian:")
yvelaze_axalgazrda=None
for x in yvela_striqoni:
    monacemebi=x.strip().split(",")
    tseli=monacemebi[0]
    sqesi=monacemebi[1]
    asaki=int(monacemebi[2])
    saxeli=monacemebi[3]
    filmi=monacemebi[4]
    if tseli==sheyvanili_tseli:
        print("- "+saxeli)
    if yvelaze_axalgazrda==None or asaki < yvelaze_axalgazrda[2]:
        yvelaze_axalgazrda=(saxeli, asaki)
if yvelaze_axalgazrda:
    print("\nყyvelaze axalgazrda:")
    print(f"saxeli: {yvelaze_axalgazrda[0]}, asaki: {yvelaze_axalgazrda[1]}")