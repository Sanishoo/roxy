# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: AssetRegister
class AssetHistory:
    """Tracks all operations on assets for rollback support."""
    
    def __init__(self, max_history=10):
        self.history = []
        self.max_history = max_history
    
    def record(self, operation_type, asset_id, old_state=None, new_state=None):
        """Record an operation to the history."""
        if len(self.history) >= self.max_history:
            self.history.pop(0)
        
        self.history.append({
            'operation': operation_type,
            'asset_id': asset_id,
            'old_state': old_state,
            'new_state': new_state,
            'timestamp': datetime.now().isoformat()
        })
