🚀 Vibe Coding Project: Vietnam Population Hypothesis
=====================================================

Dự án này là một bài tập thực hành kỹ năng **Vibe Coding** (Lập trình bằng ngôn ngữ tự nhiên). Mục tiêu không phải là viết code thủ công, mà là sử dụng bộ dữ liệu có sẵn để **Prompt** cho AI tạo ra một ứng dụng phân tích dân số hoàn chỉnh.

📌 Tổng quan dự án
------------------

Dự án sử dụng dữ liệu dân số Việt Nam để xây dựng một dashboard tương tác. Mọi tính năng từ xử lý dữ liệu, vẽ biểu đồ đến viết báo cáo đều được thực hiện thông qua việc điều khiển AI.

### Tài nguyên có sẵn:

-   `vietnam_population.csv`: Dữ liệu dân số Việt Nam (đã qua xử lý).

-   `/assets`: Các hình ảnh biểu đồ mẫu để AI tham khảo "vibe" thiết kế.

### Môi trường phát triển:

-   `Python`: Ngôn ngữ lập trình chính.

-   `Anaconda (miniconda)`: Môi trường thực thi.

-   `Cursor` hoặc `Windsurf`: Công cụ để **Vibe coding**.

* * * * *

🛠 Nhiệm vụ Prompting (Milestones)
----------------------------------

Dự án được chia thành các giai đoạn Prompt cụ thể để bạn luyện tập:

### 1\. Visualization Vibe

-   **Mục tiêu:** Đọc file CSV và tái hiện lại biểu đồ từ hình ảnh mẫu.

-   **Prompt Key:** Yêu cầu AI đọc cấu trúc file, sử dụng thư viện (như Plotly hoặc Matplotlib) để vẽ biểu đồ diện tích (area chart) thể hiện tỷ trọng 3 nhóm tuổi: 0-14, 15-64, và 65+.

### 2\. Visualization & Time Filter (Bộ lọc thời gian)

-   **Mục tiêu:** Đọc file CSV và hiển thị dữ liệu linh hoạt.

-   **Prompt Key:** Yêu cầu AI tạo một **thanh trượt (Range Slider)** cho phép chọn khoảng năm (ví dụ: 1950 - 2100). Biểu đồ phải tự động thu hẹp hoặc mở rộng khoảng hiển thị dựa trên giá trị của thanh trượt này, bắt đầu từ năm đầu tiên đến năm cuối cùng có trong bộ dữ liệu.


### 3\. Analytical Reasoning

-   **Mục tiêu:** Tìm ra "thời điểm vàng" của dân số.

-   **Yêu cầu:** Từ biểu đồ đã vẽ, lựa chọn khoảng dữ liệu mình chú ý. Sử dụng AI như một nhà phân tích dữ liệu để: *"Bình luận về dân số Việt Nam trong giai đoạn đã lựa chọn?"*

### 4\. Automated Reporting & Presentation

-   **Mục tiêu:** Xây dựng báo cáo phân tích và đề xuất giải pháp chính sách.

-   **Yêu cầu:** Yêu cầu AI viết `dàn ý` báo cáo phân tích hiện trạng và đề xuất giải pháp chính sách. 

    -   Sử dụng công cụ AI (Kimi, Gamma,...)  chuyển đổi nội dung dàn ý báo cáo đó thành cấu trúc Slide chuyên nghiệp.

### 5\. Một số gợi ý
-   **Dùng AI viết prompt:** Có thể dùng ChatGPT, Gemini để vuốt lại prompt cho đúng ý hơn
-   **Dùng AI thiết kế giao diện:** Có thể dùng ChatGPT, Gemini để thiết kế giao diện đẹp hơn từ hình ảnh mẫu.
-   **Dùng kết hợp nhiều công cụ AI** Có thể dùng mọi công cụ AI phù hợp.

