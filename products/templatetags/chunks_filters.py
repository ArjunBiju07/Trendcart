from django import template

register = template.Library()

@register.filter(name = 'chunks_filters')
def chunks(list_items, chunk_size):
    chunk = []
    for data in list_items:
        chunk.append(data)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk