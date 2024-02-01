import yaml

if __name__ == '__main__':

    # print(__file__)
    # print(os.path.dirname(os.path.abspath(__file__)))

    # 从YAML文件中加载数据
    with open('/Users/joy/Documents/workshop/python_projects/projects/documentExport/application.yaml', 'r') as file:
        data = yaml.safe_load(file)
        # 打印加载的数据
        print(data)