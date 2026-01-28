🚀 Vibe Coding Project: Một số prompt mẫu
====================================================

### 1\. Tạo biểu đồ theo mẫu
Hãy viết vẽ biểu đồ từ dữ liệu @vietnam_population_data.csv theo mẫu trong hình @bieu_do_mau.png để hiển thị theo mô tả sau: 
Biểu đồ đường (line chart) thể hiện cơ cấu dân số theo nhóm tuổi theo thời gian. Cụ thể:

Trục hoành (X): Năm, trải dài từ 1950 đến 2100.

Trục tung (Y): Quy mô dân số, đơn vị triệu người (từ 0 đến khoảng 70+ triệu).

Ba đường dữ liệu chính, phân biệt bằng màu sắc và nhãn:

Màu xanh lá – “Working age (15–64 years)”:
Dân số trong độ tuổi lao động. Đường này tăng mạnh từ 1950, đạt đỉnh khoảng giữa thế kỷ 21, sau đó giảm dần về cuối giai đoạn.

Màu đỏ – “Elderly (65+ years)”:
Dân số cao tuổi. Tăng chậm ban đầu, sau đó tăng nhanh từ khoảng 2030–2050 trở đi và tiếp tục tăng đến năm 2100.

Màu cam – “Young (under-15s)”:
Dân số trẻ em. Tăng đến khoảng cuối thế kỷ 20, rồi giảm dần trong nửa sau của giai đoạn.

Phong cách hiển thị:

Đường nét liền ở giai đoạn lịch sử, nét chấm cho giai đoạn dự báo tương lai.

Nền trắng, có đường kẻ ngang mờ để dễ so sánh giá trị.

Nhãn chú thích đặt trực tiếp ở cuối mỗi đường, không dùng hộp legend riêng.

### 2\. Tạo thanh trượt
Bạn là một AI developer chuyên xây dựng dashboard dữ liệu tương tác python ưu tiên trải nghiệm người dùng mượt mà và phản hồi theo thời gian thực.

Mục tiêu
Xây dựng một mô-đun Visualization & Time Filter cho phép:

Đọc dữ liệu từ file CSV

Hiển thị biểu đồ theo khoảng thời gian do người dùng lựa chọn

Yêu cầu giao diện

Tạo một Range Slider (thanh trượt chọn khoảng) để lọc thời gian:

Cho phép người dùng chọn năm bắt đầu – năm kết thúc

Giá trị mặc định:

Năm bắt đầu = năm nhỏ nhất trong file CSV

Năm kết thúc = năm lớn nhất trong file CSV

Thanh trượt có thể đặt:

Trong Sidebar (ưu tiên)

Hoặc phía trên biểu đồ

Yêu cầu chức năng

Sau khi người dùng điều chỉnh Range Slider:

Biểu đồ phải tự động cập nhật

Chỉ hiển thị dữ liệu trong khoảng năm được chọn

Trục X của biểu đồ phải thu hẹp hoặc mở rộng linh hoạt theo giá trị slider

Biểu đồ luôn:

Bắt đầu từ năm đầu tiên được chọn

Kết thúc tại năm cuối cùng được chọn

Không hiển thị dữ liệu ngoài phạm vi lọc

Yêu cầu xử lý dữ liệu

File CSV có ít nhất một cột:

year (hoặc cột tương đương biểu diễn thời gian)

Khi load dữ liệu:

Tự động xác định min(year) và max(year) để cấu hình slider

Yêu cầu kỹ thuật

Viết code theo hướng:

Tách riêng phần load CSV

Phần lọc dữ liệu theo năm

Phần vẽ biểu đồ

Biểu đồ phải reactive (không cần bấm nút submit)

Comment ngắn gọn để giải thích:
“Range Slider kiểm soát phạm vi hiển thị dữ liệu theo thời gian”

Kết quả mong muốn

Người dùng có thể:

Kéo thanh trượt để xem một giai đoạn cụ thể

Hoặc mở rộng để xem toàn bộ lịch sử & dự báo

Trải nghiệm mượt, phù hợp cho khám phá dữ liệu (data exploration)


### 3\. Mô hình dự đoán
Bạn là một AI Data Scientist chuyên phân tích và dự báo dữ liệu nhân khẩu học dựa trên dữ liệu lịch sử.

Mục tiêu
Xây dựng và đánh giá các mô hình dự báo cơ cấu dân số Việt Nam theo thời gian, sử dụng dữ liệu trong file:

📄 vietnam_population_data.csv

File này bao gồm:

Dữ liệu lịch sử

Dữ liệu tương lai (ground truth / projection) để dùng làm đối chiếu

1️⃣ Chuẩn bị & xử lý dữ liệu

Đọc file vietnam_population_data.csv

Xác định:

Cột thời gian (ví dụ: year)

Các biến mục tiêu (ví dụ: dân số theo nhóm tuổi: trẻ em, lao động, người cao tuổi)

Chia dữ liệu:

Tập huấn luyện (training set): dữ liệu lịch sử

Tập kiểm tra (test set): giai đoạn tương lai

2️⃣ Mô hình hóa (Modeling)

Áp dụng nhiều mô hình để so sánh, trong đó:

🔹 Mô hình ưu tiên độ chính xác

K-Nearest Neighbors (KNN Regression)
hoặc

Random Forest Regression

→ Phù hợp khi muốn học quan hệ phi tuyến từ dữ liệu lịch sử

🔹 Mô hình xu hướng dài hạn

Hồi quy đa thức (Polynomial Regression)

→ Phù hợp để:

Mô hình hóa xu hướng thay đổi cấu trúc tuổi dài hạn

Phân tích chiều hướng già hóa dân số

Yêu cầu:

Huấn luyện từng mô hình riêng

Dự báo cho giai đoạn tương lai

3️⃣ Đánh giá mô hình (Evaluation)

Đánh giá độ chính xác của từng mô hình bằng cách so sánh dự báo với dữ liệu tương lai có sẵn trong file, sử dụng các chỉ số:

RMSE (Root Mean Squared Error)

MAE (Mean Absolute Error)

R-squared (R²)

Yêu cầu:

Tính metric cho từng nhóm tuổi (nếu có)

Trình bày kết quả rõ ràng dưới dạng bảng

4️⃣ So sánh & phân tích

So sánh:

KNN / Random Forest vs Hồi quy đa thức

Phân tích:

Mô hình nào chính xác hơn về mặt số liệu

Mô hình nào phù hợp hơn để:

Dự báo ngắn hạn

Phân tích xu hướng dân số dài hạn

5️⃣ Yêu cầu kỹ thuật & trình bày

Sử dụng Python (pandas, numpy, scikit-learn, matplotlib)

Code rõ ràng, có comment giải thích:

Lý do chọn mô hình

Ý nghĩa của từng metric

Nếu có biểu đồ:

So sánh dự báo vs dữ liệu tương lai thực tế

Kết quả mong muốn

Một pipeline hoàn chỉnh:

Load dữ liệu → Train → Predict → Evaluate → Compare

Giải thích ngắn gọn:

Khi nào nên dùng mô hình ML

Khi nào nên dùng hồi quy xu hướng

Ưu tiên tính minh bạch, dễ diễn giải, phù hợp cho phân tích chính sách và mô phỏng dân số.