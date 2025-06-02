import streamlit as st
from chepy import Chepy

def main():
    st.title("Chepy Streamlit App")

    st.sidebar.header("Chepy Operations")
    options = ["Text Operations", "Binary Operations", "File Operations", "Network Operations", "Data Transformation"]
    choice = st.sidebar.selectbox("Select an operation", options)

    if choice == "Text Operations":
        text_operations()
    elif choice == "Binary Operations":
        binary_operations()
    elif choice == "File Operations":
        file_operations()
    elif choice == "Network Operations":
        network_operations()
    elif choice == "Data Transformation":
        data_transformation()

def text_operations():
    st.subheader("Text Operations")
    text = st.text_area("Enter text")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Convert to Upper Case"):
            st.write(Chepy(text).to_upper_case().o.decode())
        if st.button("Convert to Lower Case"):
            st.write(Chepy(text).to_lower_case().o.decode())
        if st.button("Base64 Encode"):
            st.write(Chepy(text).to_base64().o.decode())
    
    with col2:
        if st.button("Reverse Text"):
            st.write(Chepy(text).reverse().o.decode())
        if st.button("URL Encode"):
            st.write(Chepy(text).to_url_encoding().o.decode())
        if st.button("Hash (SHA-256)"):
            st.write(Chepy(text).sha2_256().o.decode())

def binary_operations():
    st.subheader("Binary Operations")
    text = st.text_area("Enter binary data (hex format)")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Convert Hex to Binary"):
            st.write(Chepy(text).from_hex().o.decode())
        if st.button("Convert Binary to Hex"):
            st.write(Chepy(text).to_hex().o.decode())
    
    with col2:
        if st.button("Convert to Base64"):
            st.write(Chepy(text).to_base64().o.decode())
        if st.button("Convert from Base64"):
            st.write(Chepy(text).from_base64().o.decode())

def file_operations():
    st.subheader("File Operations")
    file = st.file_uploader("Upload a file")
    if file:
        file_content = file.read()
        st.write("File Content (Hex):")
        st.write(Chepy(file_content).to_hex().o.decode())

        if st.button("Calculate MD5 Hash"):
            st.write(Chepy(file_content).md5().o.decode())

def network_operations():
    st.subheader("Network Operations")
    url = st.text_input("Enter URL")
    
    if st.button("Perform GET Request"):
        response = Chepy(url).http_request().o
        st.write(response)
    
    if st.button("Download Content"):
        content = Chepy(url).http_request().o["body"]
        st.download_button(label="Download", data=content, file_name="downloaded_content.txt")

def data_transformation():
    st.subheader("Data Transformation")
    json_data = st.text_area("Enter JSON data")
    
    if st.button("Format JSON"):
        try:
            formatted_json = Chepy(json_data).beautify_json().o.decode()
            st.write(formatted_json)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == '__main__':
    main()
