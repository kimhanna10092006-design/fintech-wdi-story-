import streamlit as st

st.set_page_config(
    page_title="FinTech WDI Story",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.block-container {max-width: 1100px; padding-top: 2rem; padding-bottom: 4rem;}
.hero {padding: 2.2rem 0 1.2rem 0;}
.kicker {font-size: 0.9rem; letter-spacing: .08em; text-transform: uppercase; color: #6b7280; font-weight: 700;}
.hero h1 {font-size: 3rem; line-height: 1.08; margin-bottom: .8rem;}
.lead {font-size: 1.15rem; line-height: 1.75; color: #374151; max-width: 900px;}
.section-label {font-size: .82rem; letter-spacing: .08em; text-transform: uppercase; color: #6b7280; font-weight: 700; margin-top: 2.2rem;}
.insight {border-left: 4px solid #111827; padding: .8rem 1rem; background: rgba(127,127,127,.06); margin: 1rem 0 1.5rem 0;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<div class="kicker">World Bank WDI · Việt Nam · Thái Lan · Singapore</div>
<h1>Số hóa mở rộng tiếp cận tài chính — nhưng lợi ích có được phân bổ đồng đều?</h1>
<div class="lead">
Bài viết dữ liệu này theo dõi quá trình số hóa, mở rộng sở hữu tài khoản và thay đổi bất bình đẳng tại Việt Nam, Thái Lan và Singapore. Trọng tâm không chỉ là mức độ kết nối, mà là việc kết nối số có thực sự chuyển thành tài chính toàn diện hay không.
</div>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown('<div class="section-label">Phần 1 · Cuộc rượt đuổi số hóa</div>', unsafe_allow_html=True)
st.header("Việt Nam đang thu hẹp khoảng cách Internet")
st.write("""
Giai đoạn 2010–2024 cho thấy ba quốc gia có quỹ đạo số hóa khác nhau. Việt Nam chưa dẫn đầu về tỷ lệ sử dụng Internet, nhưng tốc độ hội tụ là điểm đáng chú ý nhất.
""")
st.image("images/image4.png", use_container_width=True)
st.markdown("""
<div class="insight"><b>Điểm chính:</b> Việt Nam tăng tỷ lệ sử dụng Internet từ khoảng 31% năm 2010 lên khoảng 84% năm 2024. Thái Lan tăng từ khoảng 23% lên hơn 90%, trong khi Singapore duy trì mức rất cao và tiến gần trạng thái bão hòa.</div>
""", unsafe_allow_html=True)
st.write("""
Điều đáng chú ý không nằm ở việc Việt Nam đứng đầu, mà ở tốc độ thu hẹp khoảng cách. Internet vì vậy được xem là điều kiện nền cho tài chính số, nhưng chưa trực tiếp chứng minh mức độ sử dụng FinTech hay tài chính toàn diện.
""")

st.divider()

st.markdown('<div class="section-label">Phần 2 · Nghịch lý tài chính toàn diện</div>', unsafe_allow_html=True)
st.header("Tài khoản tăng, bất bình đẳng không tự động giảm")
st.write("""
Theo kỳ vọng của tài chính toàn diện, khả năng tiếp cận tài chính rộng hơn có thể đi cùng với bất bình đẳng thấp hơn. Tuy nhiên, dữ liệu trong báo cáo cho thấy mối quan hệ này không đơn giản.
""")
st.image("images/image3.png", use_container_width=True)
st.markdown("""
<div class="insight"><b>Điểm chính:</b> Việt Nam có tỷ lệ sở hữu tài khoản tăng từ khoảng 31% lên 56%, trong khi Gini lại tăng từ khoảng 34,8 lên 36,1. Thái Lan có tỷ lệ sở hữu tài khoản cao hơn nhưng Gini không giảm đều. Singapore có tỷ lệ sở hữu tài khoản rất cao, trong khi Gini vẫn ở mức cao trong các điểm dữ liệu của báo cáo.</div>
""", unsafe_allow_html=True)
st.write("""
Kết quả này gợi ý một câu hỏi quan trọng: mở rộng tiếp cận tài khoản có thể là điều kiện cần của tài chính toàn diện, nhưng chưa đủ để bảo đảm lợi ích kinh tế được phân bổ đồng đều.
""")

st.divider()

st.markdown('<div class="section-label">Phần 3 · Bất bình đẳng thay đổi thế nào?</div>', unsafe_allow_html=True)
st.header("Cả ba nước đều cải thiện, nhưng tốc độ rất khác nhau")
st.image("images/image2.png", use_container_width=True)
st.write("""
Trong báo cáo, Gini có xu hướng giảm từ đầu kỳ đến cuối kỳ ở cả ba quốc gia. Singapore giảm nhẹ từ khoảng 42,5 xuống 41,0. Thái Lan giảm rõ hơn, từ khoảng 39,3 xuống 33,3. Việt Nam giảm từ khoảng 39,3 xuống 36,1.
""")
st.markdown("""
<div class="insight"><b>Điểm chính:</b> Thái Lan có mức cải thiện mạnh nhất trong biểu đồ, trong khi Việt Nam cải thiện chậm hơn và vẫn có Gini cao hơn Thái Lan ở cuối kỳ.</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown('<div class="section-label">Phần 4 · Bức tranh tổng thể</div>', unsafe_allow_html=True)
st.header("Một nền kinh tế số mạnh cần nhiều hơn tốc độ")
st.write("""
Biểu đồ radar trong báo cáo chuẩn hóa Min–Max về thang 0–100 để so sánh bốn khía cạnh: tăng trưởng GDP, Internet, sở hữu tài khoản và bình đẳng.
""")
st.image("images/image1.png", use_container_width=True)
st.write("""
Singapore thể hiện cấu trúc tương đối cân bằng ở các trụ cột số hóa, tài khoản và bình đẳng. Thái Lan cũng có cấu trúc khá đồng đều. Việt Nam nổi bật ở tăng trưởng và Internet, nhưng yếu hơn ở sở hữu tài khoản và bình đẳng trong phép chuẩn hóa của báo cáo.
""")
st.markdown("""
<div class="insight"><b>Thông điệp:</b> Tốc độ số hóa cao không tự động đồng nghĩa với tài chính toàn diện. Điều quan trọng là khả năng chuyển hạ tầng số thành cơ hội tiếp cận tài chính rộng hơn cho các nhóm dân cư.</div>
""", unsafe_allow_html=True)

st.divider()
st.header("Kết luận")
st.write("""
Ba quốc gia cho thấy ba trạng thái khác nhau của quá trình chuyển đổi số. Việt Nam đang hội tụ nhanh về kết nối Internet, nhưng khoảng cách giữa kết nối số, sở hữu tài khoản và kết quả phân phối vẫn là vấn đề cần tiếp tục kiểm tra. Vì vậy, câu hỏi quan trọng không chỉ là *bao nhiêu người đã được kết nối*, mà là *ai thực sự được hưởng lợi từ quá trình số hóa tài chính*.
""")

with st.expander("Dữ liệu và phương pháp"):
    st.write("""
    - Nguồn chính: World Bank World Development Indicators (WDI) và các dữ liệu được tổng hợp trong báo cáo của nhóm.
    - Quốc gia: Việt Nam, Thái Lan, Singapore.
    - Phương pháp trình bày: so sánh xu hướng, scatter plot và chuẩn hóa Min–Max cho biểu đồ radar.
    - Lưu ý: trước khi nộp chính thức nên kiểm tra lại từng số liệu và nguồn của chỉ số Gini, đặc biệt với Singapore.
    """)

st.caption("FinTech WDI Story · Data article prototype")
