# 基础知识考察
def hint_message():
    print('######################################')
    print('---         学生管理系统 v1.0        ---')
    print('######################################')
    print('   1.添加学生')
    print('   2.删除学生')
    print('   3.修改信息')
    print('   4.查询个体')
    print('   5.查询所有')
    print('   6.退出系统')
    print('"""')


# 添加学生方法
def add_student(student_list: list, s_message: dict):
    # 添加数据
    student_list.append(s_message)
    print('添加成功')


# 删除学生
def del_student(student_list: list, name: str):
    # 状态
    state = True
    # 遍历查找数据
    for i in range(len(student_list)):
        # 删除信息
        if student_list[i]['name'] == name:
            student_list.pop(i)
            print('删除成功')
            state = False
            break
        i = i + 1

    if state:
        print('该学生不存在')


# 修改信息
def update_student(student_list: list, name: str, s_message: dict):
    # 状态
    state = True
    # 遍历查找数据
    for i in range(len(student_list)):
        # 删除信息
        if student_list[i]['name'] == name:
            student_list[i] = s_message
            print('修改成功')
            state = False
            break
        i = i + 1
    if state:
        print('该学生不存在')


# 查询个体
def find_student(student_list: list, name: str):
    # 查询状态
    state = True
    # 打印数据
    for student in student_list:
        if student['name'] == name:
            print('姓名：' + student['name'] + ', 年龄:' + student['age'] +
                  ',班级：' + student['grade'])
            state = False
    # 判断是否查询成功
    if state:
        print('查询学生不存在')


# 查询所有学生方法
def find_all_student(student_list: list):
    # 打印数据
    for student in student_list:
        print('姓名：' + student['name'] + ', 年龄:' + student['age'] +
              ',班级：' + student['grade'])


# 主方法
def main(student_list: list):
    # 提示信息
    hint_message()
    # 系统运行状态
    sys_state = True
    # 运行系统
    while sys_state:
        # 获取选择码
        select_code = input()
        # 判断是否添加学生
        if select_code == '1':
            # 获取内容
            s_message = input("请输入学生姓名，年龄，班级\n")
            # 设置信息
            s_message = s_message.split(' ')
            s_message = {'name': s_message[0], 'age': s_message[1], 'grade': s_message[2]}
            add_student(student_list, s_message)
        # 删除学生
        elif select_code == '2':
            name = input('输入你想删除的学生姓名：')
            del_student(student_list, name)

        # 修改信息
        elif select_code == '3':
            name = input('输入你想修改的学生姓名：')
            s_message = input('输入修改信息（姓名，年龄，班级）：')
            # 设置信息
            s_message = s_message.split(' ')
            s_message = {'name': s_message[0], 'age': s_message[1], 'grade': s_message[2]}
            update_student(student_list, name, s_message)

        # 查询个体
        elif select_code == '4':
            name = input('请输入查询学生姓名：')
            find_student(student_list, name)

        # 查询所有学生
        elif select_code == '5':
            find_all_student(student_list)

        # 判断 是否退出系统
        elif select_code == '6':
            # 关闭系统
            sys_state = False
        else:
            print("请选择正确的数字选项！")


if __name__ == '__main__':
    # 学生数据
    student_list = [
        {'name': '李四', 'age': '16', 'grade': '1班'}
    ]
    main(student_list)
