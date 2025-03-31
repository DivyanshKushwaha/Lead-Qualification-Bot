import streamlit as st
import json
import os
from crew import LeadManagementCrew

# Path to the output JSON file
json_file_path = "output/routed_and_archived_leads.json"

# Streamlit App
st.title("Lead Management System")
st.header("Process and Manage Leads")

# Input Text Box
lead_text = st.text_area("Enter Lead Text", placeholder="Type the lead text here...")

if st.button("Submit"):
    if lead_text.strip():
        # Run the crew process
        input_text = {"input_text": lead_text}

        with st.spinner("Processing your lead..."):
            # Kickoff the crew process
            LeadManagementCrew().crew().kickoff(inputs=input_text)

        st.success("Processing completed! Displaying the results:")

        # Check if the JSON file was generated
        if os.path.exists(json_file_path):
            # Load the JSON data
            with open(json_file_path, "r") as file:
                data = json.load(file)

            # Display Routed Leads in a styled way
            st.subheader("Routed Leads")
            if "routed" in data and data["routed"]:
                for lead in data["routed"]:
                    st.markdown(
                        f"""
                        - **Company Name:** {lead['company_name']}
                        - **Contact Person:** {lead['contact_person']}
                        - **Title:** {lead['title']}
                        - **Email:** {lead['email']}
                        - **Phone:** {lead['phone']}
                        - **Website:** {lead['website']}
                        - **Budget:** {lead['budget']}
                        - **Timeline:** {lead['timeline']}
                        - **Score:** {lead['score']}
                        - **Decision:** {lead['decision']}
                        """
                    )
            else:
                st.write("No Routed Leads found!")

            # Display Archived Leads in a styled way
            st.subheader("Archived Leads")
            if "archived" in data and data["archived"]:
                for lead in data["archived"]:
                    st.markdown(
                        f"""
                        - **Company Name:** {lead['company_name']}
                        - **Contact Person:** {lead['contact_person']}
                        - **Title:** {lead['title']}
                        - **Email:** {lead['email']}
                        - **Phone:** {lead['phone']}
                        - **Website:** {lead['website']}
                        - **Budget:** {lead['budget']}
                        - **Timeline:** {lead['timeline']}
                        - **Score:** {lead['score']}
                        - **Decision:** {lead['decision']}
                        """
                    )
            else:
                st.write("No Archived Leads found!")
        else:
            st.error("The final JSON file was not found! Ensure the crew has processed the lead data.")
    else:
        st.error("Please enter a valid lead text!")
