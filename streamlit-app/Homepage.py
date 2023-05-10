import streamlit as st

# cho người dùng chọn epoch, test size, train size 
# có 3 cái slidebar cho epoch, test size, train size. Khi nào người dùng chọn đủ 3 cái thì bấm nút submit, sau đó split train, test theo số lượng của người dùng rồi train model dựa trên epoch

"----"
st.sidebar.title("Select Page")

st.markdown(
    """
    <h1 style='text-align: center;'>Project Homepage</h1>
    """,
    unsafe_allow_html=True,
)

"----"
with st.container(): 
    st.subheader("***Main Concept***") 
    st.write("Lorem ipsum")


"----"
with st.container(): 
    st.subheader("***About us*** :sunglasses:")
    