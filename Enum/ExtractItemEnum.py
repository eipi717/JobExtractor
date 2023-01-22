from enum import Enum


class ExtractedJobEnum(Enum):
    company = "company"
    role = "role"
    source = "source"
    url = "url"

class JobSource(Enum):
    jobsDB = "JobsDB"
    glassdoor = "Glassdoor"