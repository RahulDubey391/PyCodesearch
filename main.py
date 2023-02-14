from pycodesearch import DirUtils, Search

path = ['C:\\Users\\rdubey5\\Desktop\\Projects\\NBCU\\SearchTool\\Sample_folder','C:\\Users\\rdubey5\\Desktop\\Projects\\Tegna\\ATTRIBUTION\\CRM_MATCHBACK\\CODE\\DAG']
du = DirUtils()
paths = du.from_list(path)
print(paths)

s = Search(paths,['CREATE','import'])
res = s.search_from_list()

for i in res:
    for j in i:
        print(len(j))
        #for path,word,line,start,end in j:
        print('Path: --- %s || Word --- %s || Line --- %s || Start --- %s || End --- %s'%(j[0],j[1],j[2],j[3],j[4]))