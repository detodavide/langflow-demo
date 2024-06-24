from fastapi import APIRouter
from routes.helloworld import router as helloworld_router
from routes.rag_search import router as rag_search_router

router = APIRouter()

router.include_router(helloworld_router, prefix="", tags=["helloworld"])
router.include_router(rag_search_router, prefix="/rag-search", tags=["RAG"])


