#1
hashes=("abc123", "ffd222", "9af010", "ffd222", "x0x0x0")
print("Occur rate: ",hashes.count("ffd222"))
#2
users=("guest", "moderator", "admin", "root")
print("admin index: ",users.index("admin"))
#3
key_params=("AES", 256, "CBC")
algorithm, key_size, mode=key_params
print("Algorithm: ",algorithm)
print("Key size: ",key_size)
print("Mode: ",mode)
#4
log=("login", "download", "upload", "logout")
print(log[len(log)-1])
#5
ips = ("192.168.0.1", "10.0.0.2", "172.16.0.3")
ip=input("ip address: ")
if ip in ips:
    print("IP found")
else:
    print("IP not found")
#6
name=input("name: ")
role=input("role: ")
status=input("status: ")
my_tuple=(name,role,status)
print(my_tuple)
#7
access=("read", "write", "execute")
new=input("new value: ")
access1=(access[0],new,access[2])
print(access1)
#8
attempts=("success", "fail", "fail", "success", "fail", "fail")
print("success: ",attempts.count("success"))
print("fail: ",attempts.count("fail"))
#9
admins=("root", "admin")
users= ("alex", "bob")
new_tuple=(admins,users)
print(new_tuple)
#10
logs=("login", "upload", "download", "logout")
start,*middle,end=logs
print("Start: ",start)
print("Middle: ",middle)
print("End: ",end)
# Вопросы
#1 Список-это изменяемая последовательность, в которой можно менять элементы, а Кортеж-неизменяемая последовательность и её нельзя менять после её создания.
#2 Из-за того что их нельзя менять
#3 Нет, элементы кортежа нельзя менять, но можно поменять изменяемые объекты в кортеже, например списки.
#4 Упаковка-это собирание нескольких значений в один кортеж, а распаковка-это распределение элементов кортежа по переменным.
#5 count()-возвращает, сколько раз элемент встречается в кортеже, а index()-возвращает, сколько раз элемент встречается в кортеже.
#6 Да, это называется неявная упаковка.
#7 Для хранения неизменяемых конфигураций, таких как ключей или пар данных(IP-адрес), использование кортежей как ключей в словарях, например, для подсчета количества атак, защита данных от случайного изменения.




