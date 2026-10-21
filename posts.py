def render_post(post: dict) -> str:
    # TODO: post body is not HTML-escaped. Escape before rendering.
    return f"<h1>{post['title']}</h1><div>{post['body']}</div>"
