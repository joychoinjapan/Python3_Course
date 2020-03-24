import sys
output_dict={}
def handle_data(item):
    item = item.split(':')
    output_dict[item[0]]=item[1]
    return

def print_data(key,value):
    print('ID:'+key+' '+'Name:'+value)
    return

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        handle_data(arg)
    for key in output_dict:
        print_data(key,output_dict[key])