print("NGUYỄN HUY NGUYÊN")
print("MSSV:235752021610019")

# Mở file với mã hóa utf-8
with open(r'C:\Users\asus\Documents\0.1.py', 'r', encoding='utf-8') as input_file:
    # Đọc từng dòng trong file
    for line in input_file:
        # Đảo ngược thứ tự các ký tự trong dòng
        reversed_line = line[::-1]
        # In ra dòng đã đảo ngược
        print(reversed_line)
