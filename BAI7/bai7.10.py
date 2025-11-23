print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import re # Sử dụng regex để tách từ hiệu quả

def find_longest_words(file_path):
    """Tìm và in ra từ/các từ dài nhất trong file."""
    longest_words = []
    max_length = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower() # Đọc toàn bộ và chuyển về chữ thường
            
            # Tách tất cả các "từ" (chuỗi ký tự chữ cái)
            words = re.findall(r'[a-zàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệđìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựýỳỷỹỵ]+', content)

            if not words:
                print("File không chứa từ nào.")
                return

            # Tìm độ dài lớn nhất
            for word in words:
                max_length = max(max_length, len(word))

            # Lọc ra các từ có độ dài bằng độ dài lớn nhất
            for word in words:
                if len(word) == max_length and word not in longest_words:
                    longest_words.append(word)

            print(f"Từ/Các từ dài nhất trong tệp '{file_path}' có độ dài {max_length}:")
            for word in longest_words:
                print(f"- {word}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng:
file_path = 'D:/a.txt'
find_longest_words(file_path)
