import json

'''
    按照一定标准修改内容，修正成
'''

serialIds = {} # {'serialId': 0}

with open('erp.boms.json', 'rb') as f:
    boms = json.load(f)
    for bom in boms:
        recipes = bom['recipe']
        for recipe in recipes:
            serialId_key = recipe['serialId']
            if (serialId_key in serialIds):
                serialIds[serialId_key] += 1
            else:
                serialId_str = '{\"' + serialId_key + '\" : ' + '1}'
                serialId = json.loads(serialId_str)
                serialIds.update(serialId)

names = {} # 'name': '产品物料中文名'

with open('erp.parts.json', 'rb') as f:
    parts = json.load(f)
    for part in parts:
        serialId_key = part['serialId']
        if (serialId_key in names):
            names[serialId_key] = part['name']
        else:
            serialId_str = '{\"' + serialId_key + '\" : \"null\"}'
            serialId = json.loads(serialId_str, strict=False)
            serialId[serialId_key] = part['name']
            names.update(serialId)

print("start write")

with open('erp.parts_counts.txt', 'wt', encoding='utf-8') as f:
    str1 = '=======产品序列号======='.ljust(50)
    str2 = '=======产品序名称======='.ljust(50)
    str3 = "被引用次数".ljust(50)
    line = str1 + " \t " + str2 + " \t " + str3 + "\n"
    f.write(line)
    for serialId in serialIds:
        if(serialId in names):
            f.write(serialId.ljust(50) + " \t " + names[serialId].ljust(50) + " \t " + str(serialIds[serialId]).ljust(50) + "\n")
            print(serialId)
        else:
            f.write(serialId + " 此序列号的产品，在产品清单中找不到\n")
            print("skip serialId: " + serialId)
















































