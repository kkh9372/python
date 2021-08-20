"""
날짜 : 2021/08/13
이름 : 김관후
내용 : 파이썬 클래스 상속 연습문제
"""

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def hello(self):
        print("----------")
        print('이름 :', self._name)
        print('나이 :', self._age)

class Student(Person):
    def __init__(self, name, age, school, major):
        super().__init__(name, age)
        self._school = school
        self._major = major

    def hello(self):
        super().hello()
        print('학교 :', self._school)
        print('전공 :', self._major)

class SalaryStudent(Student):
    def __init__(self, name, age, school, major, company):
        super().__init__(name, age, school, major)
        self._company = company

    def hello(self):
        super().hello()
        print('회사 :', self._company)

if __name__ == '__main__':
    kim = Person('김유신', 24)
    kim.hello()

    jang = Student('장보고', '21', '부산대', '영문과')
    jang.hello()

    lee = SalaryStudent('이순신', 31, '부경대', '경영학', '삼성전자')
    lee.hello()
