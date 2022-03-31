import json
'''
这个文件主要构建了从 json数据包中分离出所需的sql语句的功能
'''
# 读取一份测试用的样例数据
def loadTestFile():
    with open('../datas/protocal.json','r') as f:
        return json.loads(f.read())
    
# 转化为SQL语句
def parseToSQL(obj, PrimaryKey:str):
    # SELECT
    tmp_column = []
    # FROM
    tmp_Table = []
    # Where
    tmp_Time = []
    
    for table in obj:
        tmp = table['values']
        tableName = tmp['targetTable']
        selectTitles = tmp['targetTitle']
        selectTime = tmp['selectTimeActivate']
        timeRange = tmp['targetTimeRange']
        if tableName not in tmp_Table:
            tmp_Table.append(tableName)
        for col in selectTitles:
            tmp_column.append("{}.{}".format(tableName,col))
        if selectTime:
            tmp_Time.append("{}.time > '{}' AND {}.time < '{}'".format(tableName, timeRange[0], tableName, timeRange[1]))
    # SELECT    
    str_col = tmp_column[0]
    for i in range(1,len(tmp_column)):
        str_col += ',' + tmp_column[i]
    # FROM
    str_tab = tmp_Table[0]
    for i in range(1, len(tmp_Table)):
        str_tab += ',' + tmp_Table[i]
    # where 
    str_connect = ""
    tmp_connect = []
    if len(tmp_Table) > 1:
        baseTable = tmp_Table[0]
        for i in range(1, len(tmp_Table)):
            tmp_connect.append("{}.{}={}.{}".format(baseTable, PrimaryKey, tmp_Table[i], PrimaryKey) )

    tmp_connect = tmp_connect + tmp_Time
    if len(tmp_connect) > 0:
        str_connect = tmp_connect[0] 
    print(tmp_Time)
    print(tmp_connect)
    for i in range(1, len(tmp_connect)):
        str_connect += ' AND ' + tmp_connect[i]

    sql = "SELECT {} FROM {} ".format(str_col, str_tab)
    if len(tmp_connect) != 0:
        sql = "{} WHERE {};".format(sql, str_connect)
    else:
        sql += ';'
    return tmp_column, sql
if __name__ =='__main__':
    a = loadTestFile()
    a = parseToSQL(a, 'ID')
    print(a)