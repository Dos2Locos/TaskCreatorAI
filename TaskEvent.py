from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import datetime

class RecurrenceFrequency(str, Enum):
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

class Recurrence(BaseModel):
    frequency: RecurrenceFrequency = Field(..., description="The frequency of recurrence")
    interval: Optional[int] = Field(None, ge=1, description="The interval of recurrence, e.g., every 2 weeks")
    days_of_week: Optional[List[str]] = Field(None, description="The days of the week on which the task recurs")
    nth_weekday_of_month: Optional[int] = Field(None, description="Defines the nth weekday recurrence in a month")

class TaskEvent(BaseModel):
    title: str = Field(..., description="Title of the task")
    description: Optional[str] = Field(None, description="Detailed description of the task")
    is_completed: Optional[bool] = Field(False, description="Indicates if the task is completed")
    due_date: Optional[str] = Field(None, description="The deadline for the task, if applicable")
    start_date: Optional[str] = Field(None, description="Start date of the task or event, if applicable")
    end_date: Optional[str] = Field(None, description="End date of the task or event, if applicable")
    assigned_to: Optional[str] = Field(None, description="The person to whom the task is assigned")
    subject: Optional[str] = Field(None, description="The subject or person related to the task")
    location: Optional[str] = Field(None, description="Location where the task is to be performed")
    is_recurring: Optional[bool] = Field(False, description="Indicates if the task is recurring")
    recurrence: Optional[Recurrence] = Field(None, description="Details about the recurrence pattern")
    emoji_icon: str = Field(..., description="An emoji representing the task")