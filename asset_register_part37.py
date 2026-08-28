# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: AssetRegister
import unittest

class TestAssetRegister(unittest.TestCase):
    def setUp(self):
        from asset_register import AssetRegister
        self.reg = AssetRegister()

    def test_add_asset(self):
        self.reg.add_asset("Laptop", "IT", "active", "2026-01-01", "user1")
        assets = self.reg.get_assets()
        self.assertEqual(len(assets), 1)
        self.assertEqual(assets[0]["name"], "Laptop")
        self.assertEqual(assets[0]["owner"], "user1")

    def test_get_asset_by_id(self):
        self.reg.add_asset("Monitor", "IT", "active", "2025-06-01", "user2")
        asset = self.reg.get_asset_by_id("Monitor")
        self.assertIsNotNone(asset)
        self.assertEqual(asset["owner"], "user2")

    def test_get_asset_not_found(self):
        asset = self.reg.get_asset_by_id("NonExistent")
        self.assertIsNone(asset)

    def test_remove_asset(self):
        self.reg.add_asset("Keyboard", "IT", "active", "2025-01-01", "user3")
        self.reg.remove_asset("Keyboard")
        assets = self.reg.get_assets()
        self.assertEqual(len(assets), 0)

    def test_update_status(self):
        self.reg.add_asset("Mouse", "IT", "active", "2025-01-01", "user4")
        self.reg.update_status("Mouse", "maintenance")
        asset = self.reg.get_asset_by_id("Mouse")
        self.assertEqual(asset["status"], "maintenance")

    def test_history(self):
        self.reg.add_asset("Printer", "IT", "active", "2025-01-01", "user5")
        self.reg.update_status("Printer", "maintenance")
        self.reg.update_status("Printer", "active")
        history = self.reg.get_history("Printer")
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0]["status"], "maintenance")
        self.assertEqual(history[1]["status"], "active")

    def test_get_due_for_inspection(self):
        self.reg.add_asset("Router", "IT", "active", "2024-06-01", "user6")
        self.reg.add_asset("Switch", "IT", "active", "2025-06-01", "user7")
        due = self.reg.get_due_for_inspection()
        self.assertEqual(len(due), 1)
        self.assertEqual(due[0]["name"], "Router")

    def test_get_due_not_due(self):
        self.reg.add_asset("Cable", "IT", "active", "2025-06-01", "user8")
        due = self.reg.get_due_for_inspection()
        self.assertEqual(len(due), 0)

    def test_get_assets_empty(self):
        self.assertEqual(len(self.reg.get_assets()), 0)

    def test_get_due_for_inspection_empty(self):
        due = self.reg.get_due_for_inspection()
        self.assertEqual(len(due), 0)

if __name__ == "__main__":
    unittest.main()
