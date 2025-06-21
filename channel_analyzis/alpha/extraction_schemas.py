from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class OpportunitySchema(BaseModel):
    """
    The LLM will be provided with text in Ukrainian that typically describes
    educational or self-development opportunities such as internships, fellowships,
    conferences, workshops, and similar events. The input text will generally contain
    details about the event’s name, location, dates, application requirements, and
    additional relevant information.

    The LLM is expected to extract the relevant fields and ensure that they are filled
    out in Ukrainian, maintaining consistency with the source material. Dates and times
    must be extracted in the format dd.mm.yy hh:mm (if the time is available).
    """

    name: Optional[str] = Field(
        default=None,
        description="The full name of the event or educational/self-development opportunity.",
    )
    location: Optional[str] = Field(
        default=None,
        description="The geographical location where the event or opportunity will take place. "
        "This can include a country, city, or institution (if mentioned). A string "
        "in Ukrainian representing the location. If the event is online write 'Online'",
    )
    type: Optional[str] = Field(
        default=None,
        description="The type of opportunity. Choose one of the following options:\n"
        "Scholarship, Exchange Program, Internship, Fellowship, Workshop, "
        "Conference, Competition, Training Program, Research Funding, Startup "
        "Incubator/Accelerator, Hackathon, Volunteer Program, Educational Camp.",
    )
    field_name: list[str] = Field(
        default=None,
        description="The specific field or discipline related to the opportunity. Choose one "
        "or more options from the following:\nSTEM, Social Sciences, Arts and Humanities, "
        "Business and Management, Law, Health and Medicine, Environmental Studies, Education, "
        "Information Technology, Engineering, Agriculture, Economics, Political Science, "
        "Communications, Creative Arts, Psychology, Languages and Literature, History, Startups.\n"
        "Return empty list if a specific field cannot be determined.",
    )
    starting_date: Optional[str] = Field(
        default=None,
        description="The starting date (and time if available) when the event or opportunity begins. "
        "If a date range is given, extract the earliest date. Format: dd.mm.yy hh:mm "
        "(if time is available). Example: '01.05.24 09:00'.",
    )
    end_date: Optional[str] = Field(
        default=None,
        description="The ending date (and time if available) when the event or opportunity ends. "
        "If a date range is given, extract the latest date. Format: dd.mm.yy hh:mm "
        "(if time is available). Example: '31.10.24 17:00'.",
    )
    deadline: Optional[str] = Field(
        default=None,
        description="The last possible date (and time, if available) to submit an application "
        "or register for the event. Format: dd.mm.yy hh:mm (if time is available). "
        "Example: '18.09.24 23:59'. Return null if the deadline is not mentioned.",
    )
    education: list[str] = Field(
        default=None,
        description="The required education level for participation. Choose one or more options:\n"
        "High School, Undergraduate (Bachelor's), Postgraduate (Master's), Doctoral (PhD), "
        "Postdoctoral, Professional Certification, No Formal Education Required, Vocational "
        "Training, MBA, Technical Diploma.\nReturn empty if there are no specific educational requirements.",
    )
    audience: list[str] = Field(
        default=None,
        description="The intended target audience for the opportunity. Choose one or more options:\n"
        "Students, Researchers, Professionals, Entrepreneurs, NGOs, Academics, Artists, Developers, Youth, "
        "Women, Underrepresented Groups, Early-Career Professionals, Mid-Career Professionals, Senior-Level "
        "Executives, Educators, Healthcare Professionals, Startups, Social Activists.\nReturn empty if there "
        "is no specific target group.",
    )
    language_requirements: list[str] = Field(
        default=None,
        description="The required level of language proficiency for participation. Choose one or more options:\n"
        "None, English B1, English B2, English C1, English C2, Ukrainian, Other.\nReturn empty if language "
        "proficiency requirements are not specified.",
    )
    outcomes: list[str] = Field(
        default=None,
        description="The expected outcomes for participants. Choose one or more options:\n"
        "Degree Awarded, Certification, Job Placement, Networking Opportunities, Skill Development, "
        "Funding, Research Publication, Professional Experience, Startup Investment, "
        "Internship Placement, Business Development, Project Implementation, Award/Recognition, Mentorship.\nReturn empty if there "
        "is no specific outcomes."
    )
    organizer: Optional[str] = Field(
        default=None,
        description="The organization, institution, or entity responsible for organizing the event or opportunity. "
        "Example: 'Mitacs', 'University of Toronto', 'British Council'.",
    )
    description: Optional[str] = Field(
        default=None,
        description="A summarization of the event, including key details about the opportunity and any additional "
        "information that does not fit into other fields, such as unique benefits, application instructions, "
        "or webinar details.",
    )
