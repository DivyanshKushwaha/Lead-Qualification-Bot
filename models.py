from pydantic import BaseModel, EmailStr
from typing import List, Optional

class CollectedLead(BaseModel):
    company_name: str
    contact_person: str
    title: str
    email: EmailStr
    phone: str
    website: str
    budget: Optional[str]  
    timeline: Optional[str] 
    usecase: Optional[str]  

class QualifiedLead(BaseModel):
    company_name: str
    contact_person: str
    title: str
    email: EmailStr
    phone: str
    website: str
    budget: str
    timeline: str
    usecase: str
    score: int  
    decision: str  
    summary: str 

class ProcessedLead(BaseModel):
    company_name: str
    contact_person: str
    title: str
    email: EmailStr
    phone: str
    website: str
    budget: str
    timeline: str
    usecase: str
    score: int
    decision: str
    summary: str

class RoutedAndArchivedLeads(BaseModel):
    routed: List[ProcessedLead]  
    archived: List[ProcessedLead]  
