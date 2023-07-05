import os
import glob 
import markdown
import pdfkit


img_base_url = "https://raw.githubusercontent.com/Brook108/abhs/main/"

args = [
    "AccountRef",
    "MiniEntrustRatio",
    "ProductRef",
    "ProjectRef",
    "StrategyRef",
    "MacAddress",
    "IPAddress",
    "VolSerialNo",
    "TerminalInfo",
    "OrderRef",
    "ExchangeID",
    "StockCode",
    "StockAccountID",
    "SeatNo",
    "Direction",
    "OrderPrice",
    "OrderVolume",
    "OrderCommand"]

svg_ori_dir = './ReqOrderInsert_Img'

file_pattern = os.path.join(svg_ori_dir, '*.svg')
file_list = glob.glob(file_pattern)

# Iterate over the files and read their contents
markdown_content = ''
funcid_arg_dict = {}
modified_path = "ModifiedSvg"
for svg_file_path in file_list:
    with open(svg_file_path, 'r') as file:
        contents = file.read()
        for arg in args:
            if arg.lower() in contents.lower():
                print(f"Contents: {svg_file_path}", f"  arg: {arg}")
                function_id = svg_file_path.rsplit('/', 1)[-1].split('.')[0]
                if funcid_arg_dict.get(function_id) is None:
                    funcid_arg_dict[function_id] =  [] 
                funcid_arg_dict[function_id].append(arg)
                '''
                modified_svg_path =  f"{modified_path}/{function_id}.svg"
                with open(modified_svg_path, "w") as file:
                    file.write(modified_content)

                markdown_content += f"N_{function_id} :  {arg}:\n"
                markdown_content += "![Alt Text](" + modified_svg_path + ")"  + "\n"
                '''

for key, value in funcid_arg_dict.items():
    print(f"key:{key}, value:{value}")
    with open(f"{svg_ori_dir}/{key}.svg", "r") as file:
        contents = file.read()
        for v in value:
            contents = contents.replace(v, f'<tspan stroke="Red" fill="Blue">{v}</tspan>')

        modified_svg_path =  f"{modified_path}/{key}.svg"
        with open(modified_svg_path, "w") as file:
            file.write(contents)

        markdown_content += f"N_{key} :  {value}:\n"
        markdown_content += f"![alt text]({img_base_url}/{modified_svg_path})\n"



        #print(f"File: {svg_file_path}")
    with open('filter.md', 'w') as file:
        file.write(markdown.markdown(markdown_content,extensions=['markdown.extensions.toc']))


with open('./filter.md', 'r') as file:
    content = file.read()

html = markdown.markdown(content)
pdfkit.from_string(html, './filter.pdf')
