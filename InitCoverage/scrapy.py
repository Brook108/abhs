import time
import subprocess
from cairosvg import surface
import networkx as nx
import requests
import matplotlib.pyplot as plt
import json
import os
import cairosvg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import markdown


branches_num_map = {}


img_url_base = "https://raw.githubusercontent.com/Brook108/abhs/main/InitCoverage/"
repo_path = "/Users/xu/work/abhs"
id_path_func_dict = {}
id_function_map_file = "01函数ID和函数名对应.json"
amust_coverage_file = "02AMUST覆盖率数据.json"

cookies = {
    'gdp_user_id': '31546220-86c6-407c-8449-3c79210299e0',
    'b3222f5ad5658c1a_gdp_cs1': 'lirr25286',
    'b3222f5ad5658c1a_gdp_gio_id': 'lirr25286',
    'UqFC-yTtp36PRHYItgG2s3CcQP9YoNETJ4o_': 'v1Q9cyJQSDlNv',
    'SHIROSESSIONID': '17397942-ec90-47f3-80a6-255348065dd9',
    'projectId': 'c484ca9b20a44bf89561c62b36861731',
    'vId': 'c484ca9b20',
    'b3222f5ad5658c1a_gdp_session_id': 'e75aab2a-5e41-430d-b418-682bcf84e067',
    'b3222f5ad5658c1a_gdp_session_id_e75aab2a-5e41-430d-b418-682bcf84e067': 'true',
    'b3222f5ad5658c1a_gdp_esid': '11',
}

headers = {
    'authority': 'blade.hundsun.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'gdp_user_id=31546220-86c6-407c-8449-3c79210299e0; b3222f5ad5658c1a_gdp_cs1=lirr25286; b3222f5ad5658c1a_gdp_gio_id=lirr25286; UqFC-yTtp36PRHYItgG2s3CcQP9YoNETJ4o_=v1Q9cyJQSDlNv; SHIROSESSIONID=17397942-ec90-47f3-80a6-255348065dd9; projectId=c484ca9b20a44bf89561c62b36861731; vId=c484ca9b20; b3222f5ad5658c1a_gdp_session_id=e75aab2a-5e41-430d-b418-682bcf84e067; b3222f5ad5658c1a_gdp_session_id_e75aab2a-5e41-430d-b418-682bcf84e067=true; b3222f5ad5658c1a_gdp_esid=11',
    'origin': 'https://blade.hundsun.com',
    'referer': 'https://blade.hundsun.com/zoa/projectVersion/Incumulate/4/c484ca9b20a44bf89561c62b36861731/AMUST3.0/AMUST3.0-STOCKV202201.06.000.LS/@subSysStr/320619/320882/4599/@microServers/1',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

def get_function_list(dirname, filename):
    headers = {
        'authority': 'blade.hundsun.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'gdp_user_id=31546220-86c6-407c-8449-3c79210299e0; b3222f5ad5658c1a_gdp_cs1=lirr25286; b3222f5ad5658c1a_gdp_gio_id=lirr25286; SHIROSESSIONID=21261dbe-3a99-4db6-9cec-ebf94350de26; projectId=c484ca9b20a44bf89561c62b36861731; vId=c484ca9b20; UqFC-yTtp36PRHYItgG2s3CcQP9YoNETJ4o_=v1Q9cyJQSDlNv; b3222f5ad5658c1a_gdp_esid=165',
        'origin': 'https://blade.hundsun.com',
        'pragma': 'no-cache',
        'referer': 'https://blade.hundsun.com/zoa/projectVersion/Incumulate/4/c484ca9b20a44bf89561c62b36861731/AMUST3.0/AMUST3.0-STOCKV202201.06.000.LS/@subSysStr/303955/308513/4380/' + dirname + '/' + filename +'/@microServers/1',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    #data = 'sessionID=%7B%22cookie%22%3A%7B%22originalMaxAge%22%3Anull%2C%22expires%22%3Anull%2C%22httpOnly%22%3Atrue%2C%22path%22%3A%22%2F%22%7D%2C%22productId%22%3A%22c484ca9b20a44bf89561c62b36861731%22%2C%22product%22%3A%22AMUST3.0%22%2C%22round%22%3A%22AMUST3.0-STOCKV202201.06.000.LS%22%2C%22versionId%22%3A%22303955%22%2C%22dataType%22%3A%224%22%2C%22baseVersionId%22%3A%22308513%22%2C%22packageName%22%3A%22'+dirname+'%22%2C%22className%22%3A%22'+ filename + '%22%2C%22projectID%22%3A%224380%22%2C%22subSysVersion%22%3A%22%40subSysStr%22%2C%22microServers%22%3A%22%40microServers%22%2C%22proflag%22%3A%221%22%2C%22type%22%3A%220%22%7D'
    data = 'sessionID=%7B%22cookie%22%3A%7B%22originalMaxAge%22%3Anull%2C%22expires%22%3Anull%2C%22httpOnly%22%3Atrue%2C%22path%22%3A%22%2F%22%7D%2C%22productId%22%3A%22c484ca9b20a44bf89561c62b36861731%22%2C%22product%22%3A%22AMUST3.0%22%2C%22round%22%3A%22AMUST3.0-STOCKV202201.06.000.LS%22%2C%22versionId%22%3A%22320619%22%2C%22dataType%22%3A%224%22%2C%22baseVersionId%22%3A%22320882%22%2C%22packageName%22%3A%22'+dirname+'%22%2C%22className%22%3A%22'+filename+'%22%2C%22projectID%22%3A%224599%22%2C%22subSysVersion%22%3A%22%40subSysStr%22%2C%22microServers%22%3A%22%40microServers%22%2C%22proflag%22%3A%221%22%2C%22type%22%3A%220%22%7D'


    print(f"##data:{data}")

    response = requests.post('https://blade.hundsun.com/zoa/gethundSunMethodCov', cookies=cookies, headers=headers, data=data)

    print("function list: ", response.text)
    data = json.loads(response.text)
    for item in data['methodList']:
        print("function name: ", item['funcName'])
        print("function id: ", item['funID'])
        print("path: ", item['className'])
        id_path_func_dict[item['funID']] = [item['className'].replace('*', '/').replace('.', '/', 1), '/' + item['funcName']]


def get_file_list(dir_name):
    
    headers = {
        'authority': 'blade.hundsun.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'gdp_user_id=31546220-86c6-407c-8449-3c79210299e0; b3222f5ad5658c1a_gdp_cs1=lirr25286; b3222f5ad5658c1a_gdp_gio_id=lirr25286; SHIROSESSIONID=21261dbe-3a99-4db6-9cec-ebf94350de26; projectId=c484ca9b20a44bf89561c62b36861731; vId=c484ca9b20; UqFC-yTtp36PRHYItgG2s3CcQP9YoNETJ4o_=v1Q9cyJQSDlNv; b3222f5ad5658c1a_gdp_session_id=128c183b-000b-4468-8f1e-f87787b62802; b3222f5ad5658c1a_gdp_session_id_128c183b-000b-4468-8f1e-f87787b62802=true; b3222f5ad5658c1a_gdp_esid=165',
        'origin': 'https://blade.hundsun.com',
        'pragma': 'no-cache',
        'referer': 'https://blade.hundsun.com/zoa/projectVersion/Incumulate/4/c484ca9b20a44bf89561c62b36861731/AMUST3.0/AMUST3.0-STOCKV202201.06.000.LS/@subSysStr/303955/308513/4380/' + dir_name + '/@microServers/1',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = 'sessionID=%7B%22cookie%22%3A%7B%22originalMaxAge%22%3Anull%2C%22expires%22%3Anull%2C%22httpOnly%22%3Atrue%2C%22path%22%3A%22%2F%22%7D%2C%22productId%22%3A%22c484ca9b20a44bf89561c62b36861731%22%2C%22product%22%3A%22AMUST3.0%22%2C%22round%22%3A%22AMUST3.0-STOCKV202201.06.000.LS%22%2C%22versionId%22%3A%22320619%22%2C%22dataType%22%3A%224%22%2C%22packageName%22%3A%22' + dir_name + '%22%2C%22baseVersionId%22%3A%22320882%22%2C%22projectID%22%3A%224599%22%2C%22subSysVersion%22%3A%22%40subSysStr%22%2C%22microServers%22%3A%22%40microServers%22%2C%22proflag%22%3A%221%22%2C%22type%22%3A%220%22%7D'


    response = requests.post('https://blade.hundsun.com/zoa/gethundSunClassCov', cookies=cookies, headers=headers, data=data)
    print("file list: ", response.text)
    data = json.loads(response.text)
    for item in data['fileList']:
        print("file name: ", item['fileName'])
        get_function_list(dir_name, item['fileName'])

def get_dir_list():

    data = {
    'sessionID': '{"cookie":{"originalMaxAge":null,"expires":null,"httpOnly":true,"path":"/"},"productId":"c484ca9b20a44bf89561c62b36861731","product":"AMUST3.0","round":"AMUST3.0-STOCKV202201.06.000.LS","versionId":"320619","dataType":"4","baseVersionId":"320882","projectID":"4599","type":"0","subSysVersion":"@subSysStr","microServers":"@microServers","proflag":"1"}',
}
    response = requests.post('https://blade.hundsun.com/zoa/gethundSunPackageCov', cookies=cookies, headers=headers, data=data)

    print("#response:", response.text)
    data = json.loads(response.text)
    for item in data['pathList']:
        if item['pathName'] == '':
            continue
        print("dir name: ", item['pathName'])
        get_file_list(item['pathName'])


    with open(id_function_map_file, "w") as file:
        json.dump(id_path_func_dict, file)

    file.close()

def method_call_chart(methodid, filepath, filename):

    headers = {
        'authority': 'blade.hundsun.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'gdp_user_id=31546220-86c6-407c-8449-3c79210299e0; b3222f5ad5658c1a_gdp_cs1=lirr25286; b3222f5ad5658c1a_gdp_gio_id=lirr25286; SHIROSESSIONID=21261dbe-3a99-4db6-9cec-ebf94350de26; projectId=c484ca9b20a44bf89561c62b36861731; vId=c484ca9b20; UqFC-yTtp36PRHYItgG2s3CcQP9YoNETJ4o_=v1Q9cyJQSDlNv; b3222f5ad5658c1a_gdp_session_id=6935dd4a-8bd5-4c18-a44a-d7d6f0cf3cc5; b3222f5ad5658c1a_gdp_session_id_6935dd4a-8bd5-4c18-a44a-d7d6f0cf3cc5=true; b3222f5ad5658c1a_gdp_esid=156',
        'origin': 'https://blade.hundsun.com',
        'referer': 'https://blade.hundsun.com/zoa/traceability/320619/2647/320882/4?cookie%5BoriginalMaxAge%5D=&cookie%5Bexpires%5D=&cookie%5BhttpOnly%5D=true&cookie%5Bpath%5D=%2F&productId=c484ca9b20a44bf89561c62b36861731&product=AMUST3.0&round=AMUST3.0-STOCKV202201.06.000.LS&versionId=320619&dataType=4&baseVersionId=320882&packageName='+os.path.dirname(filepath)+'&className='+os.path.basename(filepath)+'&projectID=4599&subSysVersion=%40subSysStr&microServers=%40microServers&proflag=1&type=0',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'methodId': methodid,
        'coverageType': '7',
        'level': '1000',
        'verId': '320619##320882',
    }




    response = requests.post('https://blade.hundsun.com/zoa/pageShowMethodCallChart', cookies=cookies, headers=headers, data=data)
    print("headers:", headers)
    print("response:", response.text)
    f = open (filename, 'w')
    f.write(response.text)
    f.close()

def push_git():
    try:
        os.chdir(repo_path)
        subprocess.run(["git", "add", "."])

        subprocess.run(["git", "commit", "-m", "by python code"])

        subprocess.run(["git", "push"])

    except subprocess.CalledProcessError as e:
        print("An error occurred while executing Git command:", e)

    except OSError as e:
        print("An OS-related error occurred:", e)

    except Exception as e:
        print("An unexpected error occurred:", e)

def convert_to_tree(graph_text):
    # Create an empty directed graph
    tree = nx.DiGraph()

    # Add edges to the graph
    for parent, children in graph_text.items():
        tree.add_edges_from([(parent, child) for child in children])

    # Find the root node of the tree
    roots = [node for node in tree.nodes if tree.in_degree(node) == 0]

    # Select the first root as the main root (assuming there's only one root)
    root = roots[0]

    # Create a depth-first search tree starting from the main root
    dfs_tree = nx.dfs_tree(tree, root)

    return dfs_tree

def draw_tree(tree):
    # Set up the layout
    pos = nx.nx_pydot.graphviz_layout(tree, prog="dot")

    # Draw the tree
    nx.draw(tree, pos, with_labels=True, arrows=True, node_size=500, font_size=10, font_color="black", edge_color="gray")

    # Display the tree
    plt.axis("off")
    plt.show()

def format_percentage(string):
    try:
        value = float(string.strip('%'))
        formatted_string = '{:.2f}%'.format(value)
        return formatted_string
    except ValueError:
        return string

class InterfaceData:
    def __init__(self):
        self.total_branches_num = 0
        self.markdown_content = ''
        self.total_covered_branches_num = 0
        self.id_methodname_map = {}
        self.method_order_dict = {}
        self.en_file= ''
        self.img_path= ''

def load_branches_num():
    with open(amust_coverage_file) as file:
         data = json.load(file)

    all_data = data['AllData'][1]
    method_cov = all_data['MethodCov']


    for method in method_cov:
        class_name = method['ClassName']
        method_name = method['MethodName']
        branches_num = method['cdcSumblock']
        branches_covered_num = method['cdcRunblock']
        coverage = format_percentage(method['CDC'])
        # Create the key as class_name + ":" + method_name + ":" + coverage
        key = method_name + ":" + coverage
        # Assign branches_num to the corresponding key in the branches_num_map
        branches_num_map[key] = str(branches_num) + ":" + str(branches_covered_num)

    #for key ,value in  branches_num_map.items():
    #    print("num map ", key, value)


def preorder_traversal(tree, node, reqData):
    id2method_list = []
    if  reqData.method_order_dict.get(node) is not None:
        for value in reqData.method_order_dict.get(node):
            id2method_list.append(reqData.id_methodname_map[value].rsplit('_', 1)[0]+'()')

    method_str = '->'.join(id2method_list)

    method_name = reqData.id_methodname_map[node].rsplit('_', 1)[0]
    coverage = reqData.id_methodname_map[node].rsplit('_', 1)[1]
    key = method_name + ":" + coverage
    branch_num = int(branches_num_map[key].split(':')[0])
    branch_covered_num = int(branches_num_map[key].split(':')[1])
    branch_coverage = reqData.id_methodname_map[node].split('_')[1]
    coverage_info = "分支数: " + str(branch_num) + "<br>" + "分支覆盖率: " + branch_coverage + "<br>" 
    #print("  @@branch_num: ", total_branches_num)
    #print("@@total_branches_num: ", total_branches_num)
    reqData.total_covered_branches_num += branch_covered_num
    reqData.total_branches_num += branch_num
    pngfname = get_picture_by_id(node, reqData)

    reqData.markdown_content += "##" + method_name+"() " + "\n"
    reqData.markdown_content += "函数ID: " + node + "<br>"
    reqData.markdown_content += coverage_info
    reqData.markdown_content += "调用链：" + "\n"
    reqData.markdown_content += method_name+'()->' + method_str + "<br>"
    reqData.markdown_content += f"![Alt Text]({img_url_base}/{pngfname})\n"

    print("picture name: ", pngfname)
    for child in tree.successors(node):
        preorder_traversal(tree, child, reqData)


def convert_to_tree(graph_text):
    tree = nx.DiGraph()

    for parent, children in graph_text.items():
        tree.add_edges_from([(parent, child) for child in children])

    roots = [node for node in tree.nodes if tree.in_degree(node) == 0]
    root = roots[0]

    dfs_tree = nx.dfs_tree(tree, root)

    return dfs_tree

def method_map(reqData):

    print(f"##enfile:{reqData.en_file}")
    with open(reqData.en_file, 'r') as file:
        data = json.load(file)

    #print("data:", data)
    for node in data['nodes']:
        label = node['label']
        reqData.id_methodname_map[node['id']] = label
        #print(node['id'], " -> ", label)

    for edge in data["edges"]:
        #source = id_methodname_map[edge['source']]
        #target = id_methodname_map[edge['target']]
        source = edge['source']
        target = edge['target']
        if reqData.method_order_dict.get(source) is None:
            reqData.method_order_dict[source] = []

        reqData.method_order_dict[source].append(target)

def request_svg2png(methodid, reqData):
    headers = {
        'authority': 'blade.hundsun.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'gdp_user_id=31546220-86c6-407c-8449-3c79210299e0; b3222f5ad5658c1a_gdp_cs1=lirr25286; b3222f5ad5658c1a_gdp_gio_id=lirr25286; SHIROSESSIONID=21261dbe-3a99-4db6-9cec-ebf94350de26; projectId=c484ca9b20a44bf89561c62b36861731; vId=c484ca9b20; UqFC-yTtp36PRHYItgG2s3CcQP9YoNETJ4o_=v1Q9cyJQSDlNv; b3222f5ad5658c1a_gdp_session_id=d211e445-102a-4260-911c-c8ac338e5fcb; b3222f5ad5658c1a_gdp_session_id_d211e445-102a-4260-911c-c8ac338e5fcb=true; b3222f5ad5658c1a_gdp_esid=3',
        'origin': 'https://blade.hundsun.com',
        'pragma': 'no-cache',
        'referer': 'https://blade.hundsun.com/zoa/traceability/303955/' +methodid + '/308513/4?cookie%5BoriginalMaxAge%5D=&cookie%5Bexpires%5D=&cookie%5BhttpOnly%5D=true&cookie%5Bpath%5D=%2F&productId=c484ca9b20a44bf89561c62b36861731&product=AMUST3.0&round=AMUST3.0-STOCKV202201.06.000.LS&versionId=303955&dataType=4&baseVersionId=308513&packageName=tradestock*stock*Sources*ust*biz_func&className=ust_stock_func_entry.cpp&projectID=4380&subSysVersion=%40subSysStr&microServers=%40microServers&proflag=1&type=0',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = 'sessionID=%7B%22cookie%22%3A%7B%22originalMaxAge%22%3Anull%2C%22expires%22%3Anull%2C%22httpOnly%22%3Atrue%2C%22path%22%3A%22%2F%22%7D%2C%22productId%22%3A%22c484ca9b20a44bf89561c62b36861731%22%2C%22product%22%3A%22AMUST3.0%22%2C%22round%22%3A%22AMUST3.0-STOCKV202201.06.000.LS%22%2C%22versionId%22%3A%22320619%22%2C%22dataType%22%3A%224%22%2C%22baseVersionId%22%3A%22320882%22%2C%22packageName%22%3A%22tradestock*stock*Sources*ust*biz_func%22%2C%22className%22%3A%22ust_stock_func_entry.cpp%22%2C%22projectID%22%3A%224599%22%2C%22subSysVersion%22%3A%22%40subSysStr%22%2C%22microServers%22%3A%22%40microServers%22%2C%22proflag%22%3A%221%22%2C%22type%22%3A%220%22%2C%22user%22%3A%7B%22userid%22%3A4%7D%7D&type=10&clientwidth=1531&clientheight=60&isprojectable=1&methodID=' + methodid + '&testcaseId=0&verId=320619%23%23320882'



    response = requests.post('https://blade.hundsun.com/zoa/getSvgByMethodByForwardTrace', cookies=cookies, headers=headers, data=data)

    print(response.text)
    print(methodid)
    data = json.loads(response.text.replace('times','Songti SC'))
    svg_data = data["svgStr"]["info"]
    methodID = data["methodid"]
    svg_fname  = os.path.join(reqData.img_path, methodid+ ".svg")
    file = open(svg_fname, 'w')
    file.write(svg_data)
    file.close()
    png_fname = os.path.join(reqData.img_path,methodid + ".png")
    cairosvg.svg2png(url=svg_fname, write_to=png_fname)


    return png_fname


def get_picture_by_id(method_id, reqData):
    png_fname = os.path.join(reqData.img_path, method_id[2:] + ".png")
    if os.path.exists(png_fname):
        #print(png_fname, " is exists!")
        pass
    else:
        png_fname = request_svg2png(method_id[2:], reqData)
    return png_fname

all_branches_num = 0
all_covered_branches_num = 0
#def ProcessReqInterface(funcid, interface_info):
def ProcessReqInterface(funcid, interface_name, filepath):
    global all_branches_num
    global all_covered_branches_num
    reqData = InterfaceData()
    reqData.en_file= interface_name + ".json"
    if not os.path.exists(reqData.en_file):
        method_call_chart(funcid, filepath, reqData.en_file)

    reqData.img_path= interface_name + "_Img"
    os.makedirs(reqData.img_path, exist_ok=True)

    method_map(reqData)
    #print("dict:", reqData.method_order_dict)
    #print("#edges: ", method_order_dict)
    #print("#id method map:", id_methodname_map)
    if len(reqData.method_order_dict) != 0:
        tree = convert_to_tree(reqData.method_order_dict)
        root = [node for node in tree.nodes if tree.in_degree(node) == 0][0]
        preorder_traversal(tree, root, reqData)

    all_branches_num += reqData.total_branches_num
    all_covered_branches_num += reqData.total_covered_branches_num

    print("##接口：", interface_name )
    print("  总分支数：" + str(reqData.total_branches_num))
    print("  已覆盖分支数：" + str(reqData.total_covered_branches_num))
    reqData.markdown_content +=  "##总分支数：" + str(reqData.total_branches_num) + "\n"
    reqData.markdown_content += "##已覆盖分支数：" + str(reqData.total_covered_branches_num) + "\n"
    with open('覆盖率统计_' + interface_name + '.md', 'w') as file:
        file.write(markdown.markdown(reqData.markdown_content,extensions=['markdown.extensions.toc']))


    print("all interface branches numbrer: ", all_branches_num)
    print("all covered interface branches numbrer: ", all_covered_branches_num)

def main():

    target_interface_dict = {
        'ReqETFOrderInsert': 'tradestock/stock/Sources/ust/biz_func/ust_stock_func_entry.cpp',
        'ReqModHoldReal': 'tradestock/stock/Sources/ust/api/api_impl/trade_api/stock_ust_api.h',
        'ReqNewInstance': 'tradestock/stock/Sources/ust/api/api_impl/trade_api/stock_ust_api.h',
        'ReqOrderAction': 'tradestock/stock/Sources/ust/biz_func/ust_stock_func_entry.cpp',
        'ReqOrderInsert': 'tradestock/stock/Sources/ust/biz_func/ust_stock_func_entry.cpp',
        'ReqQryInstancePosition': 'tradestock/stock/Sources/ust/api/api_impl/trade_api/stock_ust_api.h',
        'ReqQryOrder': 'tradestock/stock/Sources/ust/query/ust_query.cpp',
        'ReqQryPosition': 'tradestock/stock/Sources/ust/query/ust_query.cpp',
        'ReqQryTrade': 'tradestock/stock/Sources/ust/query/ust_query.cpp',
        'ReqQryTradingAccount': 'tradestock/stock/Sources/ust/query/ust_query.cpp',
        'ReqUpdateInstancePosition': 'tradestock/stock/Sources/ust/api/api_impl/trade_api/stock_ust_api.h',
        'SubscribeTradeMsg': 'tradestock/stock/Sources/ust/api/api_impl/trade_api/stock_ust_api.h'
    }

    if not os.path.exists(id_function_map_file):
        get_dir_list()
    else:
        with open(id_function_map_file, "r") as file:
            id_path_func_dict = json.load(file)

    load_branches_num()

    for key, value in id_path_func_dict.items():
        for k, v in target_interface_dict.items():
            if value[0] == v and value[1][1:] == k:
                print(f"funcid:{key}, interfacename:{k}, filepath:{v}")
                ProcessReqInterface(key, k, v)

    #for key, value in target_interface_dict.items():
    #    print(key, value[1])
    #    #ProcessReqInterface(key, value)
    #push_git()

if __name__ == "__main__":
    main()
