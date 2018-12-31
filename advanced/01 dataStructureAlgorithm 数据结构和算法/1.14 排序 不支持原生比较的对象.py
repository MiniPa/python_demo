# 排序类型相同的对象，但对象不支持原生的比较操作
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print('==========1==========')
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
sort_notcompare()

from operator import attrgetter

print('==========2==========')
users = [User(23), User(3), User(99)]
print(sorted(users, key=attrgetter('user_id')))
# sroted是不更原来的对象的

min(users, key=attrgetter('user_id'))
max(users, key=attrgetter('user_id'))


