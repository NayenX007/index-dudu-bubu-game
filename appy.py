import streamlit as st

# Passkey Protection
passkey = st.sidebar.text_input("Enter Passkey:", type="password")

if passkey == "dudububu":
    st.title("🌟 Sajib's Article Blog")
    
    # Article Input
    title = st.text_input("Article Title")
    content = st.text_area("Write your article here...")
    image_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])

    if st.button("Publish"):
        if title and content:
            st.markdown("---")
            st.subheader(title)
            if image_file:
                st.image(image_file)
            st.write(content)
            st.success("Published Successfully!")
        else:
            st.warning("Please add both title and content.")
else:
    st.warning("Please enter the correct passkey (dudububu)")
