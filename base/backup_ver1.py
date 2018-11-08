import os
import time

# 需备份的目录
source = ['"D:\\projects_ai\\python_demo\\doc\\source"']
# 备份目录
target_dir = 'D:\\projects_ai\\python_demo\\doc\\target'
# 备份文件被压缩 zip
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('successful backup to ', target)
else:
    print('Backup Failed')






