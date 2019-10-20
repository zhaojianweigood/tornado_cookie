import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

# 查看数据库列表
db_list = my_client.list_database_names()
print('db_list', db_list)

# 创建数据库
my_db = my_client['runoobdb']
# 创建集合
my_clo = my_db['sites']
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
# 查询
rest = my_clo.find({}, mydict)
for r in rest:
    print(r)
# 插入
if not rest:
    x = my_clo.insert_one(mydict)
    print(x)
