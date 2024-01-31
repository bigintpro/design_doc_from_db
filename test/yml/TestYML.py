import yaml


if __name__ == '__main__':
    # 从YAML文件中加载数据
    with open('application.yaml', 'r') as file:
        data = yaml.safe_load(file)
        # 打印加载的数据
        print(data)