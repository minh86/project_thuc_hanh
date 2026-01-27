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

-   `Anaconda` (miniconda): Môi trường thực thi.

-   `Cursor` hoặc `Windsurf`: Công cụ để **Vibe coding**.

* * * * *

🛠 Nhiệm vụ Prompting (Milestones)
----------------------------------

Dự án được chia thành các giai đoạn Prompt cụ thể để bạn luyện tập:

### 1\. Visualization Vibe

-   **Mục tiêu:** Đọc file CSV và tái hiện lại biểu đồ từ hình ảnh mẫu.

-   **Prompt Key:** Yêu cầu AI đọc cấu trúc file, sử dụng thư viện (như Plotly hoặc Matplotlib) để vẽ biểu đồ diện tích (area chart) thể hiện tỷ trọng 3 nhóm tuổi: 0-14, 15-64, và 65+.

### 2\. Interactive Simulation (Sidebar)

-   **Mục tiêu:** Biến biểu đồ tĩnh thành một công cụ giả thuyết.

-   **Prompt Key:** Yêu cầu AI thêm một thanh **Sidebar** (trong Streamlit/Dash). Khi thay đổi biến số **Tỉ lệ sinh (Total Fertility Rate)**, các đường dữ liệu dự báo dân số trong tương lai phải tự động tính toán và cập nhật theo.

### 3\. Analytical Reasoning

-   **Mục tiêu:** Tìm ra "điểm chạm" của dân số vàng.

-   **Prompt Key:** Sử dụng AI như một nhà phân tích dữ liệu để trả lời câu hỏi: *"Với tỉ lệ sinh bao nhiêu thì Việt Nam giữ được tỷ trọng dân số vàng (nhóm 15-64 chiếm ưu thế) lâu nhất?"*

### 4\. Automated Reporting & Presentation

-   **Mục tiêu:** Chuyển đổi dữ liệu thành tri thức.

-   **Prompt Key:** * Yêu cầu AI viết báo cáo phân tích hiện trạng và đề xuất giải pháp chính sách.

    -   Prompt AI chuyển đổi nội dung báo cáo đó thành cấu trúc Slide chuyên nghiệp (Sử dụng định dạng Markdown hoặc tạo file PPTX).

* * * * *

🎯 Mục tiêu học tập
-------------------

-   **Kỹ năng Prompting:** Cách mô tả logic nghiệp vụ phức tạp cho AI.

-   **Context Management:** Cách đưa dữ liệu và hình ảnh mẫu vào prompt để AI hiểu đúng ngữ cảnh.

-   **Iterative Development:** Tinh chỉnh code thông qua đối thoại để đạt được kết quả mong muốn.