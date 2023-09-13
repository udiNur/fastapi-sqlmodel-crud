from fastapi import APIRouter, HTTPException, Query, Path
from typing import Optional, List
router = APIRouter()
from models.machine import MachineCreate, MachineUpdate, MachineRead
from database.operations import create_machine, get_machine, update_machine


@router.post("/machine/create", response_description="Machine created successfully", response_model=MachineRead)
async def create_machine_endpoint(machine: MachineCreate):
    """Create a new machine via the API."""
    return create_machine(machine)


@router.get("/machine/get", response_description="A list of machines", response_model=List[MachineRead])
async def get_machine_endpoint(id: Optional[int] = Query(None, description="The id of the machine to retrieve"),
                               email: Optional[str] = Query(None, description="The email of the machine to retrieve")):
    """Retrieve machines via the API based on ID or email."""
    return get_machine(id, email)


# Define the route with a path parameter called "method"
@router.get("/machine/schema/{method}", response_description="Machine schema based on method")
async def machine_schema(method: str = Path(..., description="The method to retrieve the schema for")):
    """Retrieve machine schema based on the specified method."""
    if method == "create":
        # Return the schema for creating a machine
        return MachineCreate.schema()
    elif method == "update":
        # Return the schema for updating a machine
        return MachineUpdate.schema()
    else:
        return {"error": "Invalid method provided"}


@router.put("/machine/update", response_description="Machine updated successfully", response_model=MachineRead)
async def update_machine_endpoint(machine_id: int, machine: MachineUpdate):
    """Update an existing machine via the API."""
    updated_machine = update_machine(machine_id, machine)
    if not updated_machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return updated_machine
