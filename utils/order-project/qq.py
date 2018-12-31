# -*- coding: utf-8 -*-

order_project_dict = {}

# 这里存放的是需要匹配的订单号，需要提前从excel中copy出来
target_order_file = "./target_order.txt"
# 这里存放的是项目名和订单号的对应关系，需要从excel把这两列copy到文件里
project_order_file = "./project_order.txt"

# 结果数据输出在这里
result_file = "order_to_project.txt"
project = ""

with open(project_order_file, 'r', encoding = 'utf8') as f:
    for line in f:
        # 运单号都是以M开头的
        if not "M" in line:
            continue
        line = line.replace(".", "").replace("\"", "")
        # 项目名都是以A开头的
        if line.startswith("A"):
            project = line.split("\t")[0]
            line = line.split("\t")[1]

        for order in line.split(" "):
            if order.startswith("M"):
                order_project_dict[order.strip()] = project


with open(target_order_file, 'r', encoding= 'utf8') as f:
    target_file = open(result_file, 'w', encoding='utf-8')
    for line in f:
        order = line.strip()
        if order in order_project_dict:
            target_file.write(order + "\t" + order_project_dict[order] + "\n")
        else:
            target_file.write(order + "\t" + "none" + "\n")
    target_file.close()
