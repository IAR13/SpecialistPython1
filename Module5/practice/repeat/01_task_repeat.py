# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    import random
    res_list=[]
    for i in range(size):
        res_list.append(random.randint(of,to))
    return res_list

print(gen_list(35,-20, 20))

