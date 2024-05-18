import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import pandas as pd
import urllib.parse
import sqlite3

# Function to load the Teachable Machine model and labels
def load_model_and_labels(model_path, labels_path):
    model = tf.keras.models.load_model(model_path)
    with open(labels_path, "r") as f:
        labels = f.read().splitlines()
    return model, labels

# Function to preprocess the image for model prediction
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Function to display antivenom hospitals district-wise
def display_antivenom_hospitals_districtwise():
    st.title("Antivenom Hospitals District-wise")

    hospitals_dict = {
        # Hospital information here...
        # Hospital information here...
        "Thiruvananthapuram": [
            "Government Medical College Thiruvananthapuram, Phone: 0471 – 2528300",
            "Sree Gokulam Medical College and Research Foundation, Phone: 0472- 2815000",
            "Somervell Memorial CSI Medical College, Phone: 0471 – 2250233",
            "General Hospital Neyyattinkara, Thiruvananthapuram, Phone: 0471 – 2221935"
        ],
        "Kollam": [
            "Azeezia Medical College Hospital, Meeyannoor, Kollam, Phone: 0474 – 272 22 22, 272 23 19, 858 99 27 222",
            "Ideal Hospital, Karunagappilly, Phone: 0476 – 262 0323",
            "Joseph’s Mission Hospital, Anchal, Phone: 0475 – 2271341",
            "Upasana Hospital, Punaloor, Phone: 0474 – 2762889",
            "Travancore Medical College Hospital, Umayanalloor, Phone: 0474 – 2721999",
            "Kollam Government District Hospital, Chinnakada, Phone: 0474 – 2768668",
            "Holy Cross Super Speciality Hospital, Kottiyam, Phone: 0474 – 2530121"
        ],
        "Alappuzha": [
            "Azeezia Medical College Hospital, Meeyannoor, Kollam, Phone: 0474 – 272 22 22, 272 23 19, 858 99 27 222",
            "Ideal Hospital, Karunagappilly, Phone: 0476 – 262 0323",
            "Joseph’s Mission Hospital, Anchal, Phone: 0475 – 2271341",
            "Upasana Hospital, Punaloor, Phone: 0474 – 2762889",
            "Travancore Medical College Hospital, Umayanalloor, Phone: 0474 – 2721999",
            "Kollam Government District Hospital, Chinnakada, Phone: 0474 – 2768668",
            "Holy Cross Super Speciality Hospital, Kottiyam, Phone: 0474 – 2530121"
        ],
        "Kottayam": [
            "Kottayam Medical College, Gandhinagar P.O, Kottayam, Phone: 0481-2597311",
            "Caritas Hospital, Thellakom P.O, Kottayam, Phone: 0481-2790025",
            "St. Joseph's Hospital, Dharmagiri, Kothanalloor P.O, Kottayam, Phone: 0482-2201951",
            "Holy Cross Hospital, Kurishummoodu, Kottayam, Phone: 0481-2531100"
        ],
        "Idukki": [
            "Idukki District Hospital, Painavu P.O., Phone: 0486-2222324",
            "Mangattuchira CHC, Thodupuzha, Phone: 0486-2222324"
        ],
        "Ernakulam": [
            "Government Medical College, Kalamassery, Phone: 0484-2841234",
            "Amrita Institute of Medical Sciences, Edappally, Phone: 0484-2851234",
            "Lourdes Hospital, Pachalam, Phone: 0484-4123456"
        ],
        "Thrissur": [
            "Government Medical College, Thrissur, Phone: 0487-2200317",
            "Westfort Hi-Tech Hospital, Pottore, Phone: 0487-2205261",
            "Amala Institute of Medical Sciences, Thrissur, Phone: 0487-2304000"
        ],
        "Palakkad": [
            "Government Medical College, Palakkad, Phone: 0491-2509000",
            "Sevana Hospital and Research Centre, Kanjikode, Phone: 0491-2509000"
        ],
        "Malappuram": [
            "Government Medical College, Malappuram, Phone: 0483-2730500",
            "MES Medical College Hospital, Perinthalmanna, Phone: 0493-7328000"
        ],
        "Kozhikode": [
            "Government Medical College, Kozhikode, Phone: 0495-2355662",
            "Baby Memorial Hospital, Kozhikode, Phone: 0495-2723272"
        ],
        "Wayanad": [
            "Government District Hospital, Kalpetta, Phone: 04936-204151",
            "Assumption Hospital, Mananthavady, Phone: 04935-240202"
        ],
        "Kannur": [
            "Government Medical College, Pariyaram, Phone: 0497-2808100",
            "Ananthapuri Hospital, Kannur, Phone: 0497-2702333"
        ],
        "Kasaragod": [
            "Government District Hospital, Kasaragod, Phone: 04994-228611",
            "Nirmal Hospital, Kanhangad, Phone: 0467-2204222"
        ]
        # Add the rest of the districts and hospitals here
    }

    for district, hospitals_list in hospitals_dict.items():
        st.subheader(f"{district} Hospitals:")
        for hospital_info in hospitals_list:
            hospital_name, phone_number = hospital_info.rsplit(', Phone: ', 1)
            encoded_hospital_name = urllib.parse.quote_plus(hospital_name)
            google_maps_link = f"https://www.google.com/maps/search/?api=1&query={encoded_hospital_name}"
            st.markdown(f"[{hospital_name}]({google_maps_link}) - Phone: {phone_number}")

# Function to open the Forest Officer Contacts link
def open_forest_officer_contacts():
    st.title("Forest Officer Contacts")
    st.markdown("[Click here to view Forest Officer Contacts](https://forest.kerala.gov.in/images/tender/mob_nos.pdf)")

# Function to display snake database content
#def display_snake_database_content():
    st.title("Snake Database Content")

    # Connect to the SQLite database
    conn = sqlite3.connect(r'C:\Users\Amalt\Downloads\snakeproject\snake_database.db')
    c = conn.cursor()

    # Execute a query to retrieve data from the database
    c.execute('SELECT * FROM snakes')  # Replace 'your_table_name' with the name of your table
    data = c.fetchall()

    # Display the data in a DataFrame
    if data:
        df = pd.DataFrame(data, columns=[column[0] for column in c.description])
        st.dataframe(df)
    else:
        st.write("No data found in the Snake Database.")

    # Close the database connection
    conn.close()

# Main function to run the Streamlit app
def main():
    st.title("Snake Information Hub")

    # Navigation links on the main page
    selected_page = st.sidebar.selectbox(
        "Select a page",
        ["Snake Identification", "First Aid Video", "Antivenom Hospitals", "Forest Officer Contacts", "Snake Database"]
    )

    if selected_page == "Snake Identification":
        st.subheader("Snake Identification")
        uploaded_file = st.file_uploader("Choose a snake image...", type="jpg")

        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Snake Image.", use_column_width=True)
            st.write("")
            st.write("Classifying...")

            # Load the Teachable Machine model and labels
            model, labels = load_model_and_labels(r"C:\Users\Amalt\Downloads\snakeproject\snake\keras_model.h5", r"C:\Users\Amalt\Downloads\snakeproject\snake\labels.txt")

            # Preprocess the image for model prediction
            image_array = preprocess_image(uploaded_file)

            # Make prediction
            prediction = model.predict(image_array)
            predicted_class = labels[np.argmax(prediction)]

            st.write(f"Prediction: {predicted_class}")

    elif selected_page == "First Aid Video":
        st.title("First Aid Video")
        st.image(Image.open(r'C:\Users\Amalt\Downloads\snakeproject\snake\firstaid.png'), use_column_width=True)
        
        # Option 1: Embed a YouTube video
        youtube_video_link = "https://youtu.be/qnOeiMa8mMc?si=TQxG_wwAdNiG9qeJ"
        st.write("Embedding YouTube Video:")
        st.video(youtube_video_link)
        
        # Option 2: Provide a link to a downloaded video
        # video_path = "path/to/your/video.mp4"
        # st.write("Link to Downloaded Video:")
        # st.video(video_path)

    elif selected_page == "Antivenom Hospitals":
        st.title("Antivenom Hospitals")
        st.image(Image.open(r'C:\Users\Amalt\Downloads\snakeproject\snake\hospital.webp'), use_column_width=True)
        display_antivenom_hospitals_districtwise()

    elif selected_page == "Forest Officer Contacts":
        #st.title("Forest Officer Contacts")
        #st.image(Image.open(r''), use_column_width=True)
        open_forest_officer_contacts()

    #elif selected_page == "Snake Database":
        #display_snake_database_content()

# Run the app
if __name__ == "__main__":
    main()
