# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: AssetRegister
import unittest

class TestAssetRegisterEdgeCases(unittest.TestCase):
    def setUp(self):
        from asset_register import AssetRegister
        self.register = AssetRegister()
        self.register.create_asset('A1', 'owner1', 'good', '2025-01-15')
        self.register.create_asset('A2', 'owner2', 'needs_review', '2025-06-30')

    def test_nonexistent_asset_raises(self):
        with self.assertRaises(ValueError):
            self.register.get_asset('NONEXISTENT')

    def test_nonexistent_owner_raises(self):
        with self.assertRaises(ValueError):
            self.register.get_owner('NOOWNER')

    def test_invalid_status_raises(self):
        with self.assertRaises(ValueError):
            self.register.get_asset('A1', 'bad_status')

    def test_update_nonexistent_asset_raises(self):
        with self.assertRaises(ValueError):
            self.register.update_asset('NONEXISTENT', 'good', '2025-01-01')

    def test_update_invalid_status_raises(self):
        with self.assertRaises(ValueError):
            self.register.update_asset('A1', 'invalid', '2025-01-01')

    def test_update_nonexistent_owner_raises(self):
        with self.assertRaises(ValueError):
            self.register.update_asset('A1', 'good', '2025-01-01', 'NOOWNER')

    def test_get_history_unknown_asset_raises(self):
        with self.assertRaises(ValueError):
            self.register.get_history('UNKNOWN')

    def test_get_history_unknown_owner_raises(self):
        with self.assertRaises(ValueError):
            self.register.get_history('UNKNOWN', 'NOOWNER')

    def test_empty_register_raises(self):
        self.register = AssetRegister()
        with self.assertRaises(ValueError):
            self.register.get_asset('A1')

    def test_empty_owner_raises(self):
        self.register = AssetRegister()
        with self.assertRaises(ValueError):
            self.register.get_owner('A1')

    def test_empty_history_raises(self):
        self.register = AssetRegister()
        with self.assertRaises(ValueError):
            self.register.get_history('A1')

    def test_empty_history_by_owner_raises(self):
        self.register = AssetRegister()
        with self.assertRaises(ValueError):
            self.register.get_history('A1', 'A1')

    def test_get_all_assets_empty_raises(self):
        self.register = AssetRegister()
        with self.assertRaises(ValueError):
            self.register.get_all_assets()

    def test_get_all_owners_empty_raises(self):
        self.register = AssetRegister()
        with self.assertRaises(ValueError):
            self.register.get_all_owners()

    def test_get_all_assets_after_create(self):
        self.assertEqual(self.register.get_all_assets(), ['A1', 'A2'])

    def test_get_all_owners_after_create(self):
        self.assertEqual(self.register.get_all_owners(), ['owner1', 'owner2'])

    def test_update_status(self):
        self.register.update_asset('A1', 'needs_review', '2025-01-01')
        asset = self.register.get_asset('A1')
        self.assertEqual(asset['status'], 'needs_review')
