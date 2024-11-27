from enum import StrEnum
from datetime import datetime, time
from typing import Set

from app import db
from sqlalchemy import DateTime, ForeignKey, Float, Date, Time, Table, Integer, Boolean, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id: Mapped[str] = mapped_column(db.String, primary_key=True)
    password: Mapped[LargeBinary] = mapped_column(db.LargeBinary)
    events: Mapped[Set['Event']] = relationship("Event")
    tasks: Mapped[Set['Task']] = relationship("Task")

class CalendarObjectType(StrEnum):
    event = 'event'
    task = 'task'

class CalendarObject(db.Model):
    id: Mapped[str] = mapped_column(db.String, primary_key=True) # need an id to discern between different events with (potentially) same attributes
    type: Mapped[CalendarObjectType] = mapped_column(db.Enum(CalendarObjectType))
    title: Mapped[str] = mapped_column(db.String) # title of event
    date: Mapped[Date] = mapped_column(db.Date)
    start_time: Mapped[DateTime] = mapped_column(db.DateTime) # datetime library
    notes: Mapped[str] = mapped_column(db.String, nullable=True)
    user_id: Mapped[str] = mapped_column(db.String, ForeignKey(User.id))
    __mapper_arguments = {
        'polymorphic_identity': 'calendarObject',
        'polymorphic_on': 'type'
    }

class Event(CalendarObject):
    id: Mapped[str] = mapped_column(ForeignKey(CalendarObject.id),  primary_key=True)
    end_time: Mapped[DateTime] = mapped_column(db.DateTime) # datetime library
    __mapper_arguments__ = {'polymorphic_identity': 'event'}

class Task(CalendarObject):
    id: Mapped[str] = mapped_column(ForeignKey(CalendarObject.id), primary_key=True)
    is_complete: Mapped[bool] = mapped_column(db.Boolean) # completion separates 'events' from 'tasks'
    __mapper_arguments__ = {'polymorphic_identity': 'task'}
