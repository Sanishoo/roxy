# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: AssetRegister
class AssetTag:
    def __init__(self, tag_id, name):
        self.tag_id = tag_id
        self.name = name

    @property
    def is_active(self):
        return not self.deleted

    def delete(self):
        self.deleted = True


class TagManager:
    _next_id = 1000

    def __init__(self, assets):
        self.assets = assets
        self._tags = {}
        for asset in assets.values():
            for tag in asset.tags:
                self._tags[tag.tag_id] = tag

    def add_tag(self, name):
        if not any(t.name == name and t.is_active for t in self._tags.values()):
            tag = AssetTag(TagManager._next_id, name)
            TagManager._next_id += 1
            self._tags[tag.tag_id] = tag
            return tag
        else:
            raise ValueError(f"Тег '{name}' уже существует")

    def remove_tag(self, tag_id):
        if tag_id in self._tags and not self._tags[tag_id].deleted:
            self._tags[tag_id].delete()
            if self._tags[tag_id].is_active:
                raise KeyError(f"Тег не найден или уже удалён")

    def apply_tags(self, asset_id, tags):
        for tag in tags:
            if isinstance(tag, str):
                existing = [t for t in self._tags.values() if t.name == tag and t.is_active]
                if not existing:
                    new_tag = AssetTag(TagManager._next_id, tag)
                    TagManager._next_id += 1
                    self._tags[new_tag.tag_id] = new_tag
                    asset.tags.append(new_tag)
                    return [new_tag]
            else:
                asset.tags.append(tag)
        return []

    def remove_tags(self, tags):
        removed = []
        for tag in tags:
            if isinstance(tag, str):
                found = next((t for t in self._tags.values() if t.name == tag and t.is_active), None)
                if found:
                    found.delete()
                    asset = next((a for a in self.assets.values() if any(t.tag_id == found.tag_id for t in a.tags)), None)
                    if asset:
                        asset.tags = [t for t in asset.tags if t.name != tag]
                        removed.append(tag)
            elif isinstance(tag, AssetTag):
                asset = next((a for a in self.assets.values() if any(t.tag_id == tag.tag_id for t in a.tags)), None)
                if asset:
                    asset.tags = [t for t in asset.tags if t.tag_id != tag.tag_id]
                    removed.append(tag)
        return removed
