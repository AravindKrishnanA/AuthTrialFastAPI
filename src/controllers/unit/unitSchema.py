from pydantic import BaseModel

class UnitDetails(BaseModel):
    property_id: int
    tenant_id: int
    name: str
    type: str

    #rent_cycle: int #represented in number of days regardless of annual or monthly rent cycles. ALREADY AN ENTITY IN TENANCY_AGREEMENT
    floors: int # -1 if not applicable
