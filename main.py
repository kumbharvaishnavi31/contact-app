import requests
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title = " Contact App Project",
    page_icon = "📞"
)


st.title("Contact App")
st.write('Click on the button below to fetch the user data')

if st.button("Fetch Contacts"):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    
    users_data = []
    for user in users:
        users_data.append({
            "id" : user["id"],
            "name" : user["name"],
            "email" : user["email"],
            "website" : user["website"]
        })

    df = pd.DataFrame(users_data)
    
    st.subheader("Contact Information")
    st.dataframe(df)


