from django import template
from markdownx.utils import markdownify
import re

register = template.Library()

@register.filter
def markdown_highlight(text, query):
    html = markdownify(text) 
    if not query:
        return html
    pattern = re.escape(query)
    return re.sub(f'({pattern})', r'<mark>\1</mark>', html, flags=re.IGNORECASE)
