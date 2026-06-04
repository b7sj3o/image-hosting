from urllib.parse import urlparse, parse_qs

from config import settings


def validate_extension(filename: str) -> bool:
    ext = filename.split(".")[-1].lower()
    return ext in settings.allowed_file_types


def validate_size(size_bytes: int) -> bool:
    return size_bytes <= settings.max_file_size_mb * 1024 * 1024


def validate_query_params(url: str) -> dict | None:
    default_limit: int = 10
    default_page: int = 1
    default_direction: str = "desc"
    query_params = {}

    parsed_url = urlparse(url)
    if parsed_url.path == '/api':
        params = parse_qs(parsed_url.query)
        try:
            query_params['page'] = int(params['page'][0]) if params['page'][0].isdigit() else default_page
            query_params['limit'] = int(params['limit'][0]) if params['limit'][0].isdigit() else default_limit,
            query_params['direction'] = params['direction'][0].lower() if (params['direction'][0].lower() == "asc"
                                                                           or params['direction'][0].lower() == "desc") \
                else default_direction
        except KeyError:
            query_params = None
    return query_params
