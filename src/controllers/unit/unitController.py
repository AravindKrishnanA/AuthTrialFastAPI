from fastapi import APIRouter, Depends, HTTPException
from auth import AuthHandler
from controllers.property.propertySchema import PropertyDetails, PName
import database.services.propertyService as propertyService

# app = FastAPI()
property = APIRouter()


auth_handler = AuthHandler()


@property.post('/getpropertydetails')
def get_property_details(pname: PName, role=Depends(auth_handler.auth_wrapper)):
    if 'viewProperty' not in role:
        raise HTTPException(status_code=403, detail='Forbidden')
    return propertyService.get_all_property(pname.name)

@property.get('/getownedpropertydetails')
def get_owned_property_details(owner_id: int, role=Depends(auth_handler.auth_wrapper)):
    if 'viewProperty' not in role:
        raise HTTPException(status_code=403, detail='Forbidden')
    return propertyService.get_owned_properties(owner_id)

@property.post('/createproperty')
def create_property(property_details: PropertyDetails, role=Depends(auth_handler.auth_wrapper)):
    if 'createProperty' not in role:
        raise HTTPException(status_code=403, detail='Forbidden')
    return propertyService.create_property(property_details.owner_id, property_details.name, property_details.type, property_details.nunits, property_details.floors)

