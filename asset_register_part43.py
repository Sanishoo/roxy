# === Stage 43: Добавь пагинацию длинных списков ===
# Project: AssetRegister
def paginate(assets, page=1, per_page=10):
    pages = max(1, (len(assets) + per_page - 1) // per_page)
    page = max(1, min(page, pages))
    start = (page - 1) * per_page
    end = start + per_page
    page_items = assets[start:end]
    return {
        'page': page,
        'pages': pages,
        'total': len(assets),
        'items': page_items,
        'has_next': end < len(assets),
        'has_prev': page > 1,
    }
