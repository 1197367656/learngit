import sys
from os.path import dirname,abspath

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path + "\\module")
from calcular import add

#调用add()函数
c = add(2,3)
print(c)