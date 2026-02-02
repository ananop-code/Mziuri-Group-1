from os import write

with open("titanix.txt") as f:
    inf={
        "passenger_account"

    }

    females = 0
    males = 0

    f_survive = 0
    m_survive = 0

    class1 = 0
    class2 = 0
    class3 = 0

    fare1 = []
    fare2 = []
    fare3 = []

        for line in f:
            gender = line.strip().split(',')
        if gender[4]=='female' and int(gender[1])==1:
            females += 1
            f_survive += 1
        elif gender[4]=='female':
            females += 1
        elif gender[4] == 'male' and int(gender[1]) == 1:
            males += 1
            m_survive += 1
        else:
            males += 1

        if int(gender[2])==1:
            class1 += 1
            fair2.append(int(gender[9]))
        elif int(gender[2])==2:
            class2 += 1
            fair2.append(int(gender[9]))
        else:
            class3 += 1
            fair2.append(int(gender[9]))
inf["passenger_account"]

f_pr=females*100/(males+females)
m_pr=males*100/(males+females)
print("Females:", f_gender)
print("females %", f_pr)
print("males %", m_pr)
print("males:", m_gender)

print("females that survived", f_survive)
print("males that survived", m_survive)

print("class1:", class1*100/(class1+class2+class3))
print("class2:", class2*100/(class1+class2+class3)
print("class3:", class3*100/(class1+class2+class3)

print("fare1:", fare1)
print("fare2:", fare2)
print("fare3:", fare3)


#2


#teoria
# 1
# r-read
# w-write
# a-append
# 2
# პითონი ავტომატურად შექმნის ახალ ფაილს მითითებული სახელით
# 3
# ლისტი არის ცვალებადი, შეგვიძლია ელემენტების ჩამატება, წაშლა ან შეცვლა. თაპლე კი არის უცვლელი
# 4
# dictionary-ში არის key გასაღები list-ში ელემენტებ მივმართავთ რიგითი ნომრით ინდექსით ხოლო dictionary-ში უნიკალური გასაჭბით.

