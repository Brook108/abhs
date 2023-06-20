import time
from cairosvg import surface
import networkx as nx
import requests
import matplotlib.pyplot as plt
from collections import OrderedDict
import json
import os
import cairosvg
from collections import defaultdict

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import markdown

markdown_content = ''
method_id_map = {}
edges_dict = {}
edges_name_dict2 = {} #id to name
call_dict = OrderedDict()
branches_num_map = {}


img_url_base = "https://cdn.jsdelivr.net/gh/Brook108/mdimg@main/img/"


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

total_branches_num = 0;
total_covered_branches_num = 0
def load_branches_num():
    file_path = "AMUST覆盖数据20230613.json"
    with open(file_path) as file:
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

    for key ,value in  branches_num_map.items():
        print("num map ", key, value)

cnt = 0;

def preorder_traversal(tree, node):
    global total_branches_num
    global cnt 
    global total_covered_branches_num
    global markdown_content 
    id2method_list = []
    if  edges_dict.get(node) is not None:
        for value in edges_dict.get(node):
            id2method_list.append(method_id_map[value].rsplit('_', 1)[0]+'()')

    method_str = '->'.join(id2method_list)

    method_name = method_id_map[node].rsplit('_', 1)[0]
    coverage = method_id_map[node].rsplit('_', 1)[1]
    key = method_name + ":" + coverage
    branch_num = int(branches_num_map[key].split(':')[0])
    branch_covered_num = int(branches_num_map[key].split(':')[1])
    branch_coverage = method_id_map[node].split('_')[1]
    coverage_info = "分支数: " + str(branch_num) + "<br>" + "分支覆盖率: " + branch_coverage + "<br>" 
    #print("  @@branch_num: ", total_branches_num)
    #print("@@total_branches_num: ", total_branches_num)
    total_branches_num += branch_num
    total_covered_branches_num += branch_covered_num
    pngfname = get_picture_by_id(node)

    markdown_content += "##" + method_name+"() " + "\n"
    markdown_content += "函数ID: " + node + "<br>"
    markdown_content += coverage_info
    markdown_content += "调用链：" + "\n"
    markdown_content += method_name+'()->'+method_str + "<br>"
    markdown_content += "![Alt Text](" + img_url_base + pngfname + "#pic_left )"  + "\n"

    for child in tree.successors(node):
        preorder_traversal(tree, child)

    #print("cnt:", cnt)
    #print("edges_dict:", edges_dict)
    #print("call_dict:", call_dict)

def convert_to_tree(graph_text):
    tree = nx.DiGraph()

    for parent, children in graph_text.items():
        tree.add_edges_from([(parent, child) for child in children])

    roots = [node for node in tree.nodes if tree.in_degree(node) == 0]

    root = roots[0]

    dfs_tree = nx.dfs_tree(tree, root)

    return dfs_tree

def method_map():
    file_path = "reqETFOrderInsert_call.json"
    with open(file_path) as file:
         data = json.load(file)

    for node in data['nodes']:
        label = node['label']
        method_id_map[node['id']] = label
        #print(node['id'], " -> ", label)


    for edge in data["edges"]:
        #source = method_id_map[edge['source']]
        #target = method_id_map[edge['target']]
        source = edge['source']
        target = edge['target']
        if edges_dict.get(source) is None:
            edges_dict[source] = []
        edges_dict[source].append(target)


def request_svg2png(methodid):

    cookies = {
        'gdp_user_id': '31546220-86c6-407c-8449-3c79210299e0',
        'UqFC-yTtp36PRHYItgG2s3CcQP9YoNETJ4o_': 'v1Q9cyJQSDlNv',
        'b3222f5ad5658c1a_gdp_cs1': 'lirr25286',
        'b3222f5ad5658c1a_gdp_gio_id': 'lirr25286',
        'SHIROSESSIONID': '8d832b0f-0b67-4782-967c-c30e4a98e44a',
        'b3222f5ad5658c1a_gdp_session_id': 'fd8c80a9-cf6e-41d7-b438-7a459825094b',
        'b3222f5ad5658c1a_gdp_session_id_fd8c80a9-cf6e-41d7-b438-7a459825094b': 'true',
        'projectId': 'c484ca9b20a44bf89561c62b36861731',
        'vId': 'c484ca9b20',
        'b3222f5ad5658c1a_gdp_esid': '57',
        'lang': 'zh-CN',
    }

    headers = {
        'authority': 'blade.hundsun.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'gdp_user_id=31546220-86c6-407c-8449-3c79210299e0; UqFC-yTtp36PRHYItgG2s3CcQP9YoNETJ4o_=v1Q9cyJQSDlNv; b3222f5ad5658c1a_gdp_cs1=lirr25286; b3222f5ad5658c1a_gdp_gio_id=lirr25286; SHIROSESSIONID=8d832b0f-0b67-4782-967c-c30e4a98e44a; b3222f5ad5658c1a_gdp_session_id=fd8c80a9-cf6e-41d7-b438-7a459825094b; b3222f5ad5658c1a_gdp_session_id_fd8c80a9-cf6e-41d7-b438-7a459825094b=true; projectId=c484ca9b20a44bf89561c62b36861731; vId=c484ca9b20; b3222f5ad5658c1a_gdp_esid=57; lang=zh-CN',
        'origin': 'https://blade.hundsun.com',
        'pragma': 'no-cache',
        'referer': 'https://blade.hundsun.com/zoa/traceability/303955/'+ methodid+ '/308513/4?cookie%5BoriginalMaxAge%5D=&cookie%5Bexpires%5D=&cookie%5BhttpOnly%5D=true&cookie%5Bpath%5D=%2F&productId=c484ca9b20a44bf89561c62b36861731&product=AMUST3.0&round=AMUST3.0-STOCKV202201.06.000.LS&versionId=303955&dataType=4&baseVersionId=308513&packageName=tradestock*stock*Sources*ust*biz_func&className=ust_stock_func_entry.cpp&projectID=4380&subSysVersion=%40subSysStr&microServers=%40microServers&proflag=1&type=0',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = 'sessionID=%7B%22cookie%22%3A%7B%22originalMaxAge%22%3Anull%2C%22expires%22%3Anull%2C%22httpOnly%22%3Atrue%2C%22path%22%3A%22%2F%22%7D%2C%22productId%22%3A%22c484ca9b20a44bf89561c62b36861731%22%2C%22product%22%3A%22AMUST3.0%22%2C%22round%22%3A%22AMUST3.0-STOCKV202201.06.000.LS%22%2C%22versionId%22%3A%22303955%22%2C%22dataType%22%3A%224%22%2C%22baseVersionId%22%3A%22308513%22%2C%22packageName%22%3A%22tradestock*stock*Sources*ust*biz_func%22%2C%22className%22%3A%22ust_stock_func_entry.cpp%22%2C%22projectID%22%3A%224380%22%2C%22subSysVersion%22%3A%22%40subSysStr%22%2C%22microServers%22%3A%22%40microServers%22%2C%22proflag%22%3A%221%22%2C%22type%22%3A%220%22%2C%22user%22%3A%7B%22userid%22%3A4%7D%7D&type=10&clientwidth=1538&clientheight=60&isprojectable=1&methodID=' + methodid + '&testcaseId=0&verId=303955%23%23308513'

    response = requests.post('https://blade.hundsun.com/zoa/getSvgByMethodByForwardTrace', cookies=cookies, headers=headers, data=data)

    data = json.loads(response.text.replace('times','Songti SC'))
    svg_data = data["svgStr"]["info"]
    methodID = data["methodid"]
    svg_fname  = methodid+ ".svg"
    file = open(svg_fname, 'w')
    file.write(svg_data)
    file.close()
    png_fname = methodid + ".png"
    cairosvg.svg2png(url=svg_fname, write_to=png_fname)


    return png_fname


def get_picture_by_id(method_id):
    png_fname = method_id[2:] + ".png"
    file_path = os.path.join("./", png_fname);
    if os.path.exists(method_id[2:] + ".svg"):
        print(png_fname, " is exists!")
    else:
        png_fname = request_svg2png(method_id[2:])
    return png_fname

def main():
    method_map()
    load_branches_num()

    global markdown_content


    #print("#edges: ", edges_dict)
    #print("#id method map:", method_id_map)
    tree = convert_to_tree(edges_dict)
    root = [node for node in tree.nodes if tree.in_degree(node) == 0][0]
    preorder_traversal(tree, root)


    markdown_content = markdown_content + "##总分支数：" + str(total_branches_num) + "\n"
    markdown_content = markdown_content + "##已覆盖分支数：" + str(total_covered_branches_num) + "\n"

    html_content = markdown.markdown(markdown_content, extensions=['extra'])
    with open('覆盖率统计_ReqETFOrderInsert.md', 'w') as file:
        file.write(markdown.markdown(markdown_content,extensions=['markdown.extensions.toc']))

if __name__ == "__main__":
    main()
