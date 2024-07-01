"""Initial migration

Revision ID: 1c8716fd12a7
Revises: 
Create Date: 2024-06-23 18:58:38.495996

"""
from typing import Sequence, Union
from datetime import datetime, timedelta

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '1c8716fd12a7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('working_hours',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('day_of_week', sa.Integer(), nullable=False),
        sa.Column('start_time', sa.String(), nullable=False),
        sa.Column('end_time', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('non_working_days',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.DateTime(), nullable=False),
        sa.Column('reason', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Create the appointments table
    op.create_table('appointments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('customer_name', sa.String(), nullable=False),
        sa.Column('vehicle_plate', sa.String(), nullable=False),
        sa.Column('service_type', sa.String(), nullable=False),
        sa.Column('datetime', sa.DateTime(), nullable=False),
        sa.Column('booked', sa.Boolean(), nullable=False, default=False),
        sa.PrimaryKeyConstraint('id')
    )

    insert_working_hours()
    insert_non_working_days()

def downgrade() -> None:
    op.drop_table('appointments')
    op.drop_table('non_working_days')
    op.drop_table('working_hours')

def insert_working_hours():
    conn = op.get_bind()
    working_hours = find_working_hours()

    for day in working_hours:
        conn.execute(
            sa.text("INSERT INTO working_hours (day_of_week, start_time, end_time) VALUES (:day_of_week, :start_time, :end_time)"),
            {"day_of_week": day['day_of_week'], "start_time": day['start_time'], "end_time": day['end_time']}
        )

def find_working_hours():
    working_hours = []
    for day_of_week in range(5):  # Monday (0) to Friday (4)
        working_hours.append({
            'day_of_week': day_of_week,
            'start_time': '09:00',
            'end_time': '18:00'
        })
    return working_hours

def insert_non_working_days():
    conn = op.get_bind()
    non_working_days = find_saturdays_and_sundays(2024)

    for day in non_working_days:
        conn.execute(
            sa.text("INSERT INTO non_working_days (date, reason) VALUES (:date, :reason)"),
            {"date": day, "reason": "Weekend"}
        )

def find_saturdays_and_sundays(year: int):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    delta = timedelta(days=1)
    current_date = start_date

    weekends = []
    while current_date <= end_date:
        if current_date.weekday() in (5, 6):  # Saturday (5) or Sunday (6)
            weekends.append(current_date)
        current_date += delta

    return weekends
