import configparser

# 指定配置文件的路径及表头Section名称
propFilePath = "resultant/repo_status.prop"
propFileSection = "Data"

# 从上面指定的配置文件读取key
# 本项目仅仅一个存储数据的文件，因此不需要在参数中指定过多，非通用Util
def readProp(key):
    print("从%s中获取key为：%s的数据" % (propFilePath, key))
    cf = configparser.ConfigParser()
    cf.read(propFilePath)
    value = cf.get("Data", key)

    return value


# 仅一个文件，就不写成Util了，由需要再改
def setProp(key, value):
    cf = configparser.ConfigParser()
    cf.read(propFilePath)
    cf.set(propFileSection, key, value)
    fh = open(propFilePath, 'w')
    cf.write(fh)
    fh.close()

