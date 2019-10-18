## tornado 框架搭建

### 整体结构参考类次flask搭建

### 数据库
##### 1.1同步连接MongoDB， 可使用PyMongo
```
import pymongo
conn = pymongo.Conection(url) 
# url, mongodb://user:password@staff.mongohq.com:10066/your_mongohq_db
# url, "localhost", 27017
```

##### 1.2异步连接MongoDB, 可以使用[asyncmongo](https://github.com/bitly/asyncmongo)


##### 1.3同步连接mysql, 可以直接使用[sqlalchemy](https://docs.sqlalchemy.org/en/13/)
```angular2html
# "mysql+mysqlconnector://root:@localhost/test?charset=utf8mb4"
```

##### 1.4异步连接mysql， 使用[aiomysql](https://aiomysql.readthedocs.io/en/latest/)

##### 1.5 同步连接redis, 课直接使用redis模块

##### 1.6异步连接redis, 使用tornado-redis(比较老，依旧可用）
