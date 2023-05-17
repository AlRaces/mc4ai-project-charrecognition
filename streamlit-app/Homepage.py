import streamlit as st


# cho người dùng chọn epoch, test size, train size
# có 3 cái slidebar cho epoch, test size, train size. Khi nào người dùng chọn đủ 3 cái thì bấm nút submit, sau đó split train, test theo số lượng của người dùng rồi train model dựa trên epoch

st.sidebar.title("Select Page")

st.markdown(
    """
    <h1 style='text-align: center;'>Project Homepage</h1>
    """,
    unsafe_allow_html=True,
)

"----"
with st.container():
    st.subheader("***TÓM TẮT VỀ DỰ ÁN***")
    st.markdown("<p stype=''><h5 style='text-decoration: underline;'>CẢM HỨNG: </h5>Sau nhiều tuần trăn trở về ý tưởng chính của dự án, nhóm đã quyết định làm A.I về nhận dạng chữ cái cũng như chữ số. <b style='color: #f2cfdc; font-style: italic;'>Lấy cảm hứng từ dataset MNIST</b> mà cả nhóm đã quá quen thuộc sau nhiều bài Homework, nhóm đã tìm, cũng như tự tạo một dataset bao gồm các số từ 0-9 cũng như 26 chữ của Bảng chữ cái Tiếng Anh, cả chữ hoa và thường.</p>", unsafe_allow_html=True)
    st.markdown("<p><h5 style='text-decoration: underline;'>THỰC HIỆN:</h5>Ngay sau khi kết thúc kì thi cuối khóa, cả nhóm đã làm việc vô cùng chăm chỉ để đưa ra một sản phẩm hoàn thiện hết sức mình. Bắt đầu từ việc <b style='color: #90EE90; font-style: italic;'>tìm kiếm dataset trên Internet</b>, cùng với việc <b style='color: #90EE90; font-style: italic;'>thu thập chữ viết của các bạn trong trường</b>. Tiếp đến, nhóm <b style='color: #90EE90; font-style: italic;'>xử lý</b>, <b style='color: #90EE90; font-style: italic;'>phân loại</b>, và <b style='color: #90EE90; font-style: italic;'>sắp xếp</b> từng hình ảnh trong dataset</b>. Sau đó, cả nhóm cùng <b style='color: #90EE90; font-style: italic;'>huấn luyện model</b> để có thể đưa ra con số tối ưu nhất. Bước cuối cùng, cả nhóm cùng nhau xây dựng một website với <b style='color: #90EE90; font-style: italic;'>nhiều tính năng riêng biệt</b>, để người dùng có thể sử dụng cũng như cống hiến dữ liệu cho A.I.</p>",
                unsafe_allow_html=True)
    st.markdown("<p><h5 style='text-decoration: underline;'>TƯƠNG LAI:</h5>Hiện tại, A.I chỉ có thể nhận diện từng chữ cái một lúc. Nhưng trong tương lai, nhóm dự định sẽ cải tiến để A.I có thể <b style='font-style: italic; color: #D2B48C;'>nhận dạng từng từ</b>, <b style='font-style: italic; color: #D2B48C;'>từng câu</b>, cũng như có thể nhận dạng <b style='font-style: italic; color: #D2B48C;'>các loại ngôn ngữ khác nhau</b>. Từ đó, có thể thiết kế một website cho phép người dùng mở camera trực tiếp để phiên dịch những đoạn văn bản thuộc nhiều ngôn ngữ khác nhau. Ngoài ra, <b style='font-style: italic; color: #D2B48C;'>lượng dataset của nhóm vẫn còn rất nhỏ</b>, dẫn đến việc model dự đoán không chính xác. Cả nhóm hiện tại vẫn đang bổ sung dataset và cùng với chức năng <b style='font-style: italic; color: #D2B48C;'>cho phép người dùng đóng góp vào dataset</b> sẽ giúp cho model dự đoán chính xác hơn trong tương lai.</p>",
                unsafe_allow_html=True)
"----"
with st.container():
    st.subheader("***About us*** :sunglasses:")
