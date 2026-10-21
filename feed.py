def build_feed(posts: list[dict]) -> list[dict]:
    # FIXME: feed loads every post into memory. Paginate.
    return sorted(posts, key=lambda p: p["date"], reverse=True)
