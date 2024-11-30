import pickle

# Mở file pickle ở chế độ đọc nhị phân ('rb')
with open('image-caption-generator/ixtoword.pkl', 'rb') as file:
    # Sử dụng pickle.load() để giải nén nội dung của file
    data = pickle.load(file)

# Kiểm tra dữ liệu đã được đọc từ file
print(data)