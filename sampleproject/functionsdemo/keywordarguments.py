def show_student_details(**kwargs):
    for k,v in kwargs.items():
        print(k," -> ",v)

show_student_details(fname="Santosh",course="Science",loc="Dallas")