
def get_weater(city):
    """
    Return cities current wheather.
    @params cuty: str
    @reutrn type: str
    """
    city = city.lower()
    data = {
        "xorazm" : '-1',
        "namangan" : '2',
        "navoiy" : '0',
        "qashaqadaryo" : '3'
    }
    return data.get(city, "unknown")

def get_students_ciy(student_name):
    """
    Return home city of student_name;
    @params student_name:str
    @reutrn type: str
    """
    students = {
        "asadbek" : "xorazm",
        "asilbek" : "qashqadaryo",
        "yusufjon" : "namangan",
        "jasurbek" : "navoiy",
    }
    return students.get(student_name, 'unknown')
