from crew import LeadManagementCrew

def run():
    print("Enter the lead text: ")
    text = input(">> ")
    input_text={"input_text":text}
    processed_leads = LeadManagementCrew().crew().kickoff(inputs=input_text)
    return processed_leads
if __name__ == "__main__":
    run()
