import json
# f = open('file.json', 'w', encoding="utf-8")
# # # f.write("true")
# pere = [1,6.6,[0,0],(0,1), None, True, 'ENG', 'Рус']
# json.dump(pere, f, ensure_ascii=False)
# f.close()
#
#
#
# f = open('file.json', 'r', encoding="utf-8")
# # print(type(f.read()))
# content = json.load(f)
# print(content)
# print(type(content))
# f.close()

#
#
#
# f = open('file.txt', 'r', encoding='utf-8')
# u = f.readlines()
# f.close()
# slovar = {}
# for i in u:
#     p = i.split(': ')
#     slovar[p[0]] = p[1].rstrip()
# print(slovar)
#
#
# o = open('file.json', 'w', encoding='utf-8')
# json.dump(slovar, o, ensure_ascii=False)
# o.close()

#
# f = open('file.json', 'r', encoding='utf-8')
# sod = json.load(f)
# f.close()
# print(sod)
# for k,v in enumerate(sod):
#     if type(v) == str:
#         sod[k] += '!'
#     elif type(v) in (int,float):
#         sod[k] += 1
#     elif type(v) == bool:
#         sod[k] = not k
#     elif type(v) == list:
#         sod[k] *= 2
#     elif type(v) == dict:
#         sod[k]['newkey'] = None
#
# print(sod)




import requests


resp = requests.get(url='http://api.open-notify.org/iss-now.json').json()

print(resp['iss_position'])















