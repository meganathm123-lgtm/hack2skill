from fastapi import APIRouter, Depends, HTTPException, status
from models.schemas import EmergencyReport, EmergencyOut, StatusUpdate
from services.gemini_service import classify_emergency
from services.db_service import (
    store_emergency, get_all_emergencies, update_emergency_status
)
from core.security import get_current_user
from loguru import logger

router = APIRouter()

@router.post("/report-emergency", response_model=EmergencyOut)
async def report_emergency(report: EmergencyReport, user=Depends(get_current_user)):
    try:
        category = await classify_emergency(report.message)
        emergency = await store_emergency(report.message, category)
        logger.info(f"Emergency reported: {emergency}")
        return emergency
    except Exception as e:
        logger.error(f"Error reporting emergency: {e}")
        raise HTTPException(status_code=500, detail="Failed to report emergency")

@router.get("/get-alerts", response_model=list[EmergencyOut])
async def get_alerts(user=Depends(get_current_user)):
    try:
        emergencies = await get_all_emergencies()
        return emergencies
    except Exception as e:
        logger.error(f"Error fetching alerts: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch alerts")

@router.put("/update-status/{id}")
async def update_status(id: str, status_update: StatusUpdate, user=Depends(get_current_user)):
    try:
        updated = await update_emergency_status(id, status_update.status)
        if not updated:
            raise HTTPException(status_code=404, detail="Emergency not found")
        return {"detail": "Status updated"}
    except Exception as e:
        logger.error(f"Error updating status: {e}")
        raise HTTPException(status_code=500, detail="Failed to update status")
