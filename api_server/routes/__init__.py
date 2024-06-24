from fastapi import APIRouter
from routes.helloworld import router as helloworld_router

router = APIRouter()

router.include_router(helloworld_router, prefix="", tags=["helloworld"])

# router.include_router(
#     docs_manager_router, prefix="/docs-manager", tags=["pdf_manager"]
# )
# router.include_router(
#     simple_assistant_route, prefix="/simple-assistant", tags=["simple assistants"]
# )

# router.include_router(
#     appointment_support_route, prefix="/appointment-support", tags=["automotive assistants"]
# )
