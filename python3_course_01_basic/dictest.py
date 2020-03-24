import sys

bags=dict()
for item in sys.argv[1:]:
    item=item.split(':')
    bags['ID']=item[0]
    bags['Name']=item[1]
    print('ID:'+bags['ID']+' '+'Name:'+bags['Name'])
