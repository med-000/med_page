from django import template
from django.utils.safestring import mark_safe
import markdown
from markdownx.utils import markdownify
from markdownx.settings import (
    MARKDOWNX_MARKDOWN_EXTENSIONS,
    MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
)
from markdown.extensions import Extension

register = template.Library()


@register.filter
def markdown_to_html(text):
    return mark_safe(markdownify(text))


class EscapeHtml(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.deregister('html_block')
        md.inlinePatterns.deregister('html')


@register.filter
def markdown_to_html_with_escape(text):
    extensions = MARKDOWNX_MARKDOWN_EXTENSIONS + [EscapeHtml()]
    html = markdown.markdown(text, extensions=extensions, extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS)
    return mark_safe(html)

@register.filter
def markdown_to_html(text):
    html = markdown.markdown(
        text,
        extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
    )
    return mark_safe(html)

# サイドバー用：目次（TOC）だけを生成
@register.simple_tag
def extract_toc(text):
    md = markdown.Markdown(
        extensions=MARKDOWNX_MARKDOWN_EXTENSIONS + ['toc'],
        extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
    )
    md.convert(text)  
    return mark_safe(md.toc)