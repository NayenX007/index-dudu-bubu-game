import streamlit as st

st.title("🌟 Sajib's Blog")
passkey = st.sidebar.text_input("Enter Passkey:", type="password")

if passkey == "dudububu":
    title = st.text_input("Article Title")
    content = st.text_area("Write your article here...")
    
    if st.button("Publish"):
        if title and content:
            st.success("Published!")
            st.subheader(title)
            st.write(content)
        else:
            st.warning("Please write something first.")
else:
    st.info("Please enter the passkey 'dudububu' to start.")
