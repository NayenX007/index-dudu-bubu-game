import streamlit as st
from streamlit_gsheets import GSheetsConnection

# পাসওয়ার্ড প্রোটেকশন
passkey = st.sidebar.text_input("Enter Passkey:", type="password")

if passkey == "dudububu":
    st.title("🌟 Sajib's Permanent Blog")
    
    # গুগল শিট কানেকশন
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)

        # ইনপুট সেকশন
        with st.form(key="blog_form"):
            title = st.text_input("Article Title")
            content = st.text_area("Write your article here...")
            submit_button = st.form_submit_button(label="Publish")

        if submit_button:
            if title and content:
                new_data = {"Title": [title], "Content": [content]}
                import pandas as pd
                df = pd.DataFrame(new_data)
                conn.create(data=df)
                st.success("Successfully Published and Saved!")
            else:
                st.warning("Please fill all fields.")

        # পুরনো পোস্টগুলো দেখানো
        st.markdown("---")
        st.subheader("Previous Posts")
        existing_data = conn.read()
        st.table(existing_data)
        
    except Exception as e:
        st.error("Connection Error: Please check your Google Sheet share settings or Secrets link.")

else:
    st.info("Welcome! Please enter the correct passkey in the sidebar to access the blog.")
