from django import template
import re
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def highlight(text, query):
    if not query:
        return text
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    highlighted = pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", text)
    return mark_safe(highlighted)

@register.filter
def highlight_multi(text, query):
    if not query:
        return text

    keywords = query.strip().split()
    for kw in keywords:
        if not kw:
            continue
        pattern = re.compile(re.escape(kw), re.IGNORECASE)
        text = pattern.sub(
            lambda m: f"<mark>{m.group(0)}</mark>", text
        )
    return mark_safe(text)

@register.filter
def excerpt_with_highlight(text, query, radius=10):
    import re
    if not query:
        return text[:radius*2] + '...'

    keywords = [re.escape(kw) for kw in query.strip().split() if kw]
    if not keywords:
        return text[:radius*2] + '...'

    pattern = re.compile("(" + "|".join(keywords) + ")", re.IGNORECASE)
    snippets = []

    for match in pattern.finditer(text):
        start = max(match.start() - radius, 0)
        end = min(match.end() + radius, len(text))
        snippet = text[start:end]
        # 抜粋内でハイライト
        snippet = pattern.sub(lambda m: f'<mark>{m.group(0)}</mark>', snippet)
        snippets.append(snippet)

    # 重複除去
    unique_snippets = []
    for s in snippets:
        if s not in unique_snippets:
            unique_snippets.append(s)

    return mark_safe('...'.join(unique_snippets) + '...')
