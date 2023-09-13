from models.machine import MachineBase, MachineCreate, MachineUpdate
from typing import Optional
from sqlmodel import Session
from sqlmodel.sql.expression import select
from datetime import datetime
from database.database import engine


def create_machine(machine_data: MachineCreate):
    """Create a new machine record in the database."""
    machine_data = machine_data.dict()
    machine_data.pop("id", None)
    machine_data["created_at"] = datetime.utcnow()
    machine_data["edited_at"] = datetime.utcnow()

    with Session(engine) as session:
        machine = MachineBase(**machine_data)
        session.add(machine)
        session.commit()
        session.refresh(machine)
        return machine


def get_machine(id: Optional[int] = None, email: Optional[str] = None):
    """Get machines from the database based on ID or email."""
    with Session(engine) as session:
        query = select(MachineBase)
        if id:
            query = query.where(MachineBase.id == id)
        if email:
            query = query.where(MachineBase.email == email)
        machines = session.exec(query).all()
        return machines


def update_machine(machine_id: int, machine_data: MachineUpdate):
    """Update an existing machine record in the database."""
    machine_data = machine_data.dict()
    machine_data.pop("id", None)
    machine_data["edited_at"] = datetime.utcnow()

    with Session(engine) as session:
        machine = session.get(MachineBase, machine_id)
        if not machine:
            return None
        for key, value in machine_data.items():
            setattr(machine, key, value)
        session.commit()
        session.refresh(machine)
        return machine
