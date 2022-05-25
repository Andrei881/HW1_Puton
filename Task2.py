# Задача 02
# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой. 

a = 'Корабли лавировали, лавировали, да не вылавировали.'
b = 'лав'


def numSubString(lSource,lSubstr):
    ret = 0
    i = 0
    while i != -1:
        i = lSource.find(lSubstr,i+1)
        ret += 1
    return ret


print(f"{numSubString( a, b)}")


