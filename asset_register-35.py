# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: AssetRegister
def get_next_action(asset: Asset) -> str:
    """Recommend next action based on asset state."""
    if asset.status == "active":
        if asset.last_check_date and asset.last_check_date < datetime.now() - timedelta(days=30):
            return "Schedule overdue inspection"
        if asset.next_review_date and asset.next_review_date < datetime.now() + timedelta(days=7):
            return "Approach upcoming review"
        return "Monitor normally"
    elif asset.status == "inactive":
        if asset.decommission_date and asset.decommission_date < datetime.now():
            return "Complete decommissioning"
        return "Keep inactive"
    elif asset.status == "damaged":
        if asset.repair_deadline and asset.repair_deadline < datetime.now() + timedelta(days=30):
            return "Initiate repair process"
        return "Assess repair necessity"
    elif asset.status == "lost":
        return "File replacement request"
    elif asset.status == "decommissioned":
        return "Archive records"
    return "Review asset status"
