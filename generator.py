import random

names = ["пром","агро","торг","урал","север","юг","техно",
"экспо","метал","нефть","сельхоз","фарм","строй",
"кредит","алмаз","девелопмент","развитие","мос",
"рос","кубань","сибирь","восток","нано","софт",
"микро","онлайн","инвест","текстиль","цемент"]

def random_name(number):
    company_name = set()
    while len(company_name) != number:
        company_name.add(random.choice(names).capitalize())
    for i in company_name:
        print(i, end=' ')

random_name(6)
