from django import template
import re

register = template.Library()

@register.filter
def excerpt_highlight(text, keyword):
    if not keyword:
        return ""

    # HTMLタグ除去（マークダウンのレンダリング後などに備える）
    plain_text = re.sub(r'<[^>]+>', '', text)

    # キーワードの周辺30文字を抽出
    match = re.search(re.escape(keyword), plain_text, re.IGNORECASE)
    if match:
        start = max(match.start() - 30, 0)
        end = min(match.end() + 30, len(plain_text))
        snippet = plain_text[start:end]
        
        # 強調表示（HTMLでマークアップ）
        snippet = re.sub(
            re.escape(keyword),
            r'<mark>\g<0></mark>',
            snippet,
            flags=re.IGNORECASE
        )
        return f"...{snippet}..."
    return ""
