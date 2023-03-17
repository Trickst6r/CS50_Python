# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# Remove #2 from set:
s.remove(2)
print(s)

# Sử dụng hàm len() để tính xem có bao nhiêu giá trị ở trong set đó.
# Sau đó hàm len nằm trong ký hiệu ngoặc nhon (curly braces notation)
# sẽ lấy số đã tính và gán vào trong chuỗi
print(f"The set has {len(s)} elements.")
