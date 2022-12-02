"""Girilen adı, isim ve soyisim olarak ayırır."""
# Kürşat Emre Özkara
# 02.12.2022

in_student_name = str(input("Öğrenci adı ve soyadı giriniz. Örnek=Mahmut Tuncer: ")).split(" ")
# print(in_student_name)
in_student_name = [i.strip() for i in in_student_name if i != ""]
# print(in_student_name)

student_name = in_student_name[:-1]
student_name = " ".join(student_name)

student_surname = in_student_name[-1]

del in_student_name

print(f"İsim: {student_name}")
print(f"Soyisim: {student_surname}")
