"""
    @author long
    @time 2022/04/26 08:52
    @description
"""
class Student:

    # 初始化
    def __init__(self, id: int, name: str, age: int, sex: str, grade: str):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.grade = grade

    # 格式化输出方法
    def __str__(self):
      print(str.format('学号：{0}、'
                       '姓名：{1}、'
                       '年龄：{2}、'
                       '性别：{3}、'
                       '班级：{4}', self.id, self.name,
                       self.age, self.sex, self.grade))

class List_Student:
    # 初始化
    def __init__(self, list_student: list):
        self.list_student = list_student

    # 格式化输出方法
    def __str__(self):
        for student in self.list_student:
            student.__str__()

    # 查询所有学生方法
    def find_all_student(self):
        if len(self.list_student) == 0:
            print('还未录入学生')
        self.__str__()

    # 查找单个学生信息
    def find_student(self, id):
        index = -1
        # 查询学生信息
        for i in range(len(self.list_student)):
            if self.list_student[i].id == id:
                index = i
                return index
        # 查询无此人
        return index

    # 删除学生方法
    def delete_student(self, id):
        # 查询是否有该学生
        index = self.find_student(id)
        # 判断
        if index < 0:
            print('请输入正确的学号')
        else:
            # 删除学生
            self.list_student.pop(index)
            print('删除成功')

    # 修改学生信息
    def update_student(self, index, student):
        self.list_student[index] = student
        print('修改成功')

    # 添加学生
    def add_student(self, student):
        # 查询是否有该学生
        index = self.find_student(student.id)
        # 判断
        if index < 0:
            self.list_student.append(student)
            print('添加成功！')
        else:
            print('该学号已存在！')

class Main:

    # 提示信息方法
    def message(self):
        content = """
#####################################
****       学生管理系统 v1.0     ****
#####################################
    1.添加学生
    2.删除学生
    3.修改信息
    4.查询个体
    5.查询所有
    6.退出系统
"""
        print(content, end='')
        select_id = input('请输入序号:')
        return select_id

    # 主方法
    def main(self):
        # 创建学生容器
        list_s = List_Student([])
        # 程序运行设置
        Flag = True

        # 循环系统
        while Flag:
            select_id = self.message()
            if select_id == '1':
                # 获取数据
                student_info = input("请输入学生的学号、姓名、年龄、性别、班级，以空格分隔：\n")
                # 分割数据
                info_list = student_info.split(' ')
                # 创建数据
                student = Student(int(info_list[0]), info_list[1], int(info_list[2]), info_list[3], info_list[4])
                # 添加信息
                list_s.add_student(student)

            elif select_id == '2':
                # 获取数据
                id = int(input("请输入想删除学生的学号："))
                # 删除学生
                list_s.delete_student(id)

            elif select_id == '3':
                # 获取数据
                id = int(input("请输入修改学生的学号"))
                # 判断
                index = list_s.find_student(id)
                if index < 0:
                    print('请输入正确的学号')
                else:
                    student_info = input("不支持学生的学号，请学生的姓名、年龄、性别、班级，以空格分隔：\n")
                    # 分割数据
                    info_list = student_info.split(' ')
                    # 创建数据
                    student = Student(id, info_list[0], int(info_list[1]), info_list[2], info_list[3])
                    # 修改信息
                    list_s.update_student(index, student)

            elif select_id == '4':
                # 获取数据
                id = int(input("请输入查询学生的学号"))
                # 查询信息
                index = list_s.find_student(id)
                if index < 0:
                    print('请输入正确的学号')
                else:
                    list_s.list_student[index].__str__()

            elif select_id == '5':
                list_s.find_all_student()

            elif select_id == '6':
                Flag = False

            else:
                print('请输入正确的序号')


if __name__ == '__main__':
    main = Main()
    main.main()