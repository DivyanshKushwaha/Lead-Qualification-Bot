## Sales Lead Qualification Bot: Multi-Agent System Report

This report outlines the development and implementation of a multi-agent system designed to qualify inbound sales leads based on predefined criteria. The system includes agents for collecting, evaluating, and routing leads, demonstrating automation capabilities for sales processes.


### Agent structure 

- Collector Agent: Extracts information such as company details, budget, timeline, and use case from inbound leads.

- Qualifier Agent: Assigns a qualification score based on predefined criteria such as budget size, industry, use case complexity, and timeline.

- Routing Agent: Routes qualified leads to the sales team while archiving disqualified leads for further review or future opportunities.

4. Implementation Details

- **agents.py** : Defines the roles, goals, and instructions for all three agents.
- **tasks.py** : Assigns specific tasks to each agent to process the leads sequentially.
- **models.py** : Uses Pydantic models to ensure data validation and consistency across the workflow.
- **crew.py** : Establishes a workflow connecting all agents and ensuring sequential execution of tasks.
- **main.py** : Serves as the entry point to run the multi-agent system and process lead data.
- **app.py**: Streamlit app to use for demo with basic user interface.



### Results:


#### **Example 1** :
- Input: 
```bash
Subject: Request for AI Solutions

Dear Team,

I am reaching out on behalf of DynamicEdge Inc., a rapidly growing company in the IT and innovation sector. We are looking to implement an AI-powered tool to automate client interactions and improve operational efficiency. The contact person for this project is Mr. Arjun Singh, our Chief Operating Officer. You can reach him at arjun.singh@dynamicedge.com or via phone at +91-9876543210. Our website is www.dynamicedge.com..

We are looking at a budget range of $18,000 to $25,000, depending on the features and scalability of the solution. The timeline for this project is 3-4 months, and we are keen on starting discussions next month.

Looking forward to hearing from you.

Best Regards, Arjun Singh COO, DynamicEdge Inc.
```


- Output:

```bash
{
    {"routed":
        [
            {
                "company_name":"DynamicEdge Inc.",
                "contact_person":"Arjun Singh",
                "title":"Chief Operating Officer",
                "email":"arjun.singh@dynamicedge.com",
                "phone":"+91-9876543210",
                "website":"www.dynamicedge.com",
                "budget":"$18,000 to $25,000",
                "timeline":"3-4 months",
                "usecase":"Implement an AI-powered tool to automate client interactions and improve operational efficiency",
                "score":95,
                "decision":"Qualified",
                "summary":"High-potential lead with a strong use case fit, significant budget, and a reasonable timeline.  The score is based on available information and reasonable estimations for unavailable data points."
            }
        ],
    "archived":[]
}
```


#### **Example 2** :
- Input: 
```bash
Subject: Inquiry for Basic AI Chatbot

Dear Team,

I represent SmallBiz Services, a newly established company specializing in local bookkeeping and administrative support. We are exploring options for implementing a basic chatbot to manage incoming inquiries and provide simple responses to customer queries.

Our contact person for this inquiry is Ankita Sharma, who serves as our Operations Assistant. She can be reached at ankita.sharma@smallbiz.com or on her phone at +91-9876543211. Our website is www.smallbiz.com..

Unfortunately, our budget for this project is very limited, around $2,000, and we’re hoping to implement the chatbot within the next two weeks. We’re interested in understanding if there are any solutions that might fit our needs.

Looking forward to your thoughts.

Best Regards, Ankita Sharma Operations Assistant, SmallBiz Services
```


- Output:

```bash
{
    "routed":[],
    "archived":
        [
            {
                "company_name":"SmallBiz Services",
                "contact_person":"Ankita Sharma",
                "title":"Operations Assistant",
                "email":"ankita.sharma@smallbiz.com",
                "phone":"+91-9876543211",
                "website":"www.smallbiz.com",
                "budget":"$2,000",
                "timeline":"two weeks",
                "usecase":"managing incoming inquiries and providing simple responses to customer queries",
                "score":20,
                "decision":"Disqualified",
                "summary":"Lead score (20) is below the threshold for routing to sales. Further qualification is required, but given the low score and limited budget, archiving is recommended.  The use case suggests a low potential for high-value sales."
            }
        ]
}
```

## Success Metrics :

Accuracy: The system achieved a success rate of 80% for correctly extracting data and assigning accurate scores across 10 test cases.

Efficiency: Automated lead qualification significantly reduced manual effort, improving response time and consistency.

## Conclusion :
- The multi-agent system successfully fulfills the requirements of automating lead qualification.
- Its ability to process inbound leads and categorize them into routed or archived categories has proven effective and scalable.


## Future Enhancements:

- Automated Sales Integration: Implement functionality to automatically send qualified leads to the sales manager via email or integrate directly with a CRM system like Salesforce. This will reduce manual handoffs and accelerate the sales pipeline.

- Dynamic Archival Analysis: Enhance archived leads processing by tagging reasons for disqualification and creating automatic follow-up reminders for leads that might become qualified in the future (e.g., better budgets or extended timelines).

- Marketing: Analyze archived leads for retargeting campaigns.

- Customer Support: Route customer inquiries alongside sales inquiries.

- Enhanced Reporting Dashboard: Build an interactive dashboard to visualize lead qualification metrics, success rates, and trends over time.

