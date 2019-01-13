import json

'''
    按照一定标准修改内容，修正成 用于ERP项目
'''

print("============== 产品序列号：产品中文名称")
part_SerialId_names = {} # 'name': '产品物料中文名'

with open('erp.parts.json', 'rb') as f:
    parts = json.load(f)
    for part in parts:
        serialId_key = part['serialId']
        if (serialId_key in part_SerialId_names):
            part_SerialId_names[serialId_key] = part['name']
        else:
            serialId_str = '{\"' + serialId_key + '\" : \"null\"}'
            serialId = json.loads(serialId_str, strict=False)
            serialId[serialId_key] = part['name']
            part_SerialId_names.update(serialId)

print("============== 产品id：产品序列号")
part_id_serialIds = {} # 'name': '产品id_serialIds'

with open('erp.parts.json', 'rb') as f:
    parts = json.load(f)
    for part in parts:
        id_key = part['_id']
        if (id_key in part_id_serialIds):
            part_id_serialIds[id_key] = part['serialId']
        else:
            pis_str = '{\"' + id_key + '\" : \"null\"}'
            serialId = json.loads(pis_str, strict=False)
            serialId[id_key] = part['serialId']
            part_id_serialIds.update(serialId)

print("============== 产品序列号：被使用的次数")
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

def count_father(child_serialId):
    '''
    根据 serialId 查找父产品 serialId，并返回父产品 serialId 被使用的次数
    '''
    fathers_count = 0
    with open('erp.boms.json', 'rb') as f:
        boms = json.load(f)
        for bom in boms:
            recipes = bom['recipe']
            for recipe in recipes:
                serialId_key = recipe['serialId']
                if (child_serialId == serialId_key):
                    fathers_count += serialIds[serialId_key]
    print(fathers_count)
    return fathers_count

# 遍历所有的 serialIds，统计其父产品被使用的次数
for serialId in serialIds:
    serialIds[serialId] += count_father(serialId)


print("start write")

with open('erp.parts_counts.txt', 'wt', encoding='utf-8') as f:
    str1 = '=======产品序列号======='.ljust(50)
    str2 = '=======产品序名称======='.ljust(50)
    str3 = "被引用次数".ljust(50)
    line = str1 + " \t " + str2 + " \t " + str3 + "\n"
    f.write(line)
    for serialId in serialIds:
        if(serialId in part_SerialId_names):
            f.write(serialId.ljust(50) + " \t " + part_SerialId_names[serialId].ljust(50) + " \t " + str(serialIds[serialId]).ljust(50) + "\n")
            print(serialId)
        else:
            f.write(serialId + " 此序列号的产品，在产品清单中找不到\n")
            print("skip serialId: " + serialId)
















































