# 创建和解压归档文件

import shutil

shutil.unpack_archive('Python-3.3.0.tgz')
shutil.make_archive('py33','zip','Python-3.3.0')

shutil.get_archive_formats()
# [('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"),('tar', 'uncompressed tar file'), ('zip', 'ZIP file')]

## tarfile, zipfile, gzip, bz2 等可处理多种归档格式








