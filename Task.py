from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from datetime import datetime

class Recurrence(BaseModel):
    """
    Represents a recurring task.

    Attributes:
    - frequency: Frequency of recurrence, e.g., hourly, daily, weekly, monthly, yearly.
    - interval: Recurrence interval, e.g., every 2 weeks.
    - days_of_week: Recurrence days of the week, e.g., ['Monday', 'Friday'].
    - nth_weekday_of_month: Recurrence nth weekday of the month, e.g., 1st Friday.
    """
    frequency: Optional[Literal["hourly", "daily", "weekly", "monthly", "yearly"]] = None
    interval: Optional[int] = None
    days_of_week: Optional[List[str]] = None
    nth_weekday_of_month: Optional[int] = None

class Task(BaseModel):
    """
    Represents a single task.

    Attributes:
    - title: Title of the task.
    - description: Optional description of the task.
    - is_completed: Indicates if the task is completed.
    - due_date: Due date of the task, if applicable.
    - start_date: Start date of the task, if applicable.
    - end_date: End date of the task, if applicable.
    - assigned_to: The person to whom the task is assigned.
    - subject: The subject or person related to the task.
    - location: Location where the task is to be performed, if applicable.
    - is_recurring: Indicates if the task is recurring.
    - recurrence: Recurrence pattern of the task, if applicable.
    - emoji_icon: Emoji representing the task.
    """

    title: str
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    due_date: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    assigned_to: Optional[str] = None
    subject: Optional[str] = None
    location: Optional[str] = None
    is_recurring: Optional[bool] = None
    recurrence: Optional[Recurrence] = None
    emoji_icon: str