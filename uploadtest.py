import tkinter as tk
from tkinter import font

def add_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    label_result.config(text="النتيجة: " + str(result))

# إنشاء نافذة Tkinter
window = tk.Tk()
window.title("جمع الأرقام")
window.geometry("400x300")

# إنشاء خط جميل
custom_font = font.Font(family="Helvetica", size=12)

# إنشاء واجهة أولى
frame1 = tk.Frame(window)
frame1.pack(pady=20)

label1 = tk.Label(frame1, text="الرقم الأول:", font=custom_font)
label1.pack(side=tk.LEFT)

entry1 = tk.Entry(frame1, font=custom_font)
entry1.pack(side=tk.LEFT)

# إنشاء واجهة ثانية
frame2 = tk.Frame(window)
frame2.pack(pady=20)

label2 = tk.Label(frame2, text="الرقم الثاني:", font=custom_font)
label2.pack(side=tk.LEFT)

entry2 = tk.Entry(frame2, font=custom_font)
entry2.pack(side=tk.LEFT)

# إنشاء زر للجمع
button = tk.Button(window, text="جمع", font=custom_font, command=add_numbers)
button.pack(pady=20)

# إنشاء مساحة نصية لعرض النتيجة
label_result = tk.Label(window, font=custom_font)
label_result.pack()

# تشغيل الحلقة الرئيسية للتطبيق
window.mainloop()