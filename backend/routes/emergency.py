from fastapi import APIRouter, Depends, HTTPException
from models.schemas import EmergencyReport, EmergencyOut, StatusUpdate
from services.gemini_service import classify_emergency, assign_priority
from services.db_service import (
    store_emergency, get_all_emergencies, update_emergency_status
)
from core.security import get_current_user
from loguru import logger

router = APIRouter()


# 🚨 REPORT EMERGENCY
@router.post("/report-emergency", response_model=EmergencyOut)
async def report_emergency(report: EmergencyReport, user=Depends(get_current_user)):
    try:
        # 🔹 AI classification
        category = await classify_emergency(report.message)

        # 🔹 NEW: assign priority
        priority = assign_priority(category)

        # 🔹 NEW: include user
        emergency = await store_emergency(
            message=report.message,
            category=category,
            priority=priority,
            user=user["username"]
        )

        logger.info(f"Emergency reported: {emergency}")
        return emergency

    except Exception as e:
        logger.error(f"Error reporting emergency: {e}")
        raise HTTPException(status_code=500, detail="Failed to report emergency")


# 📊 GET ALERTS (WITH FILTERING)
@router.get("/get-alerts", response_model=list[EmergencyOut])
async def get_alerts(
    status: str = None,
    type: str = None,
    user=Depends(get_current_user)
):
    try:
        emergencies = await get_all_emergencies()

        # 🔹 NEW: filtering
        if status:
            emergencies = [e for e in emergencies if e["status"] == status]

        if type:
            emergencies = [e for e in emergencies if e["type"] == type]

        return emergencies

    except Exception as e:
        logger.error(f"Error fetching alerts: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch alerts")


# 🔁 UPDATE STATUS
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