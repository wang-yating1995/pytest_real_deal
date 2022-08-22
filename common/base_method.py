import yaml

# class BaseMethod():
def open_yaml(filepath):
    content = yaml.safe_load(open(filepath,encoding="UTF-8"))
    return content
