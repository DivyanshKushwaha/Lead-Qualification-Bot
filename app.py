import streamlit as st
import json
import os
from crew import LeadManagementCrew

json_file_path = "output/routed_and_archived_leads.json"

st.title("Lead Management System")
st.header("Process and Manage Leads")

lead_text = st.text_area("Enter Lead Text", placeholder="Type the lead text here...")

if st.button("Submit"):
    if lead_text.strip():
        input_text = {"input_text": lead_text}

        with st.spinner("Processing your lead..."):
            LeadManagementCrew().crew().kickoff(inputs=input_text)

        st.success("Processing completed! Displaying the results:")

        if os.path.exists(json_file_path):
            with open(json_file_path, "r") as file:
                data = json.load(file)

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
