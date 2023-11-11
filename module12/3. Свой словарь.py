class MyDict(dict):
    def get(self, key, default=None):
        return super().get(key, 0)


my_dict = MyDict()
my_dict['a'] = 1
my_dict['b'] = 2

print(my_dict.get('a'))
print(my_dict.get('c'))
