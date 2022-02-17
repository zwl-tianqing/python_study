[toc]

## python 简介

### 1 python 的简史

* 起源

    > Python 由 Guido van Rossum 于 1989 年年底出于某种娱乐目的而开发

* 基于 ABC 语言

    > Python 基于 ABC 教学语言，ABC 语言非常强大，专门为非专业程序员设计。
    > 但 ABC 却没有被广泛认可，Guido 认为是 非开放导致的

* 升级事件

    > 2008年12月，python 发布 3.0 版本，没有考虑 Python 2.x 的兼容
    > 导致割裂，使得用户不愿升级到 3.0 版本
    > 但是由于 3.x 版本更加**简洁、方便**，很多开发者还是投向了 3.x 版本的怀抱

### 2 python是什么

> Python 是一种面向对象、解释型、弱类型的脚本语言

### 3 Python 的特点

* 代码简单，上手容易

    > 比如我们用 Java 完成某个功能，可能需要100来描述，而 py 可能只用 20 行就搞定了，这是它吸引人的方面

* 速度快

    > 底层使用的 C 语言编写，很多标准库和低三方库也是使用 C 写的，运行速度快

* 免费、开源

* 高层语言

    > 无需考虑如何管理程序使用的内存一类的细节

* 可以移植性

    > 在 Windows 上开发，在 Linux 上也能运行

* 解释性

    > py 解释器，运行 py 文件，边翻译边解释，直接出结果

* 面向对象

    > py 既面向对象，也面向编程
    > 面向过程:
    > 讲一个问题分成一步又一步来解决
    > 面向对象:
    > 将问题中的各个事务封装成对象
    > 建立对象不是为了完成某个步骤，而是为了描述某个对象在解决问题步骤中的某个行为
    
* 可扩展性

    > Python中可以写 C 程序

* 可植入性

    > 可以把 py 嵌入 C/C++ 程序

* 丰富的库

    > 除了强大的标准库，py 还有很多其它高质量的库

* 规范代码

    > 强制缩进，是的代码具有很强的可读性

### 4 pip 的使用

#### 4.1 pip 换源

* windows

    > 在 c 盘用户目录下创建 pip 目录 
    > 在 pip 目录下创建配置文件 pip.ini
    > 配置文件内容如下:
    > [global]
    > timeout = 6000 #设置超时时间
    > index-url = "镜像url" 
    > trusted-host = 镜像域名

* Linux

    > 修改 ~/.pip/pip.conf (没有就创建一个)
    > 修改 index-url 为你想要的镜像源

#### 4.2 pip命令

* pip list 

  > 列出匹配管理的包有哪些

* pip 安装指定版本

    > 命令：pip install 库名==版本号
    >
    > 例子：pip install redis == 3.2.0

* pip uninstall  

    > 命令：pip uninstall 库名 （卸载指定库）

* pip -V

    > 查看 pip 版本

* pip freeze > requirement.text

    > 将项目依赖的包输出到指定的 requirement 文件中

* pip install -r requirement.text

    > 使用 pip 安装 requirement.text 中依赖的文件

* pip 安装的包位置

    > 在  Python 文件中的 Lib 文件夹中的 site-packages 文件夹中

### 5 cmd 使用 Python 编辑器

* 进入编译器

  > 命令：python

* 退出编译器

  > 命令：exit()

* 升级包管理器

  > 命令：Python -m pip install -- upgrade pip

### 6 python 使用

* Python 文件格式

  > xxx.py 为  Python 源文件的格式，扩展名为 .py

* 运行文件

  > 方式一：进入文件所在的文件夹中，使用 Python 文件名.py 就执行了文件
  >
  > 方式二：Python 文件所在路径/文件名.py，就执行了文件

