# 测试类的使用
class Test:
    # 类中参数的创建
    name: str

    # 类中方法的创建
    @classmethod
    def getName(cls):
        print(f"name:{cls.name}", end="\n")

    @classmethod
    def setName(cls, name: str):
        cls.name = name


if __name__ == '__main__':
    test = Test()
    test.setName("张三")
    test.getName()
    print("see you Python！")
