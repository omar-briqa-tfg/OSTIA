IPV6_PATTERN = r"^([a-fA-F0-9:]+|[uU]nknown), "
WEB_EXTENSIONS = r'.*\.(js|woff|jpg|css|png(.*)?|ico|txt|gif)$'
HANDLE = r'((2099(.[1-4])?|2117)\/\d+)'
BITSTREAM = r'bitstream\/id\/([^\/]*)\/'
SEARCH_KEYS = [
    'discover?', 'scholar?', 'examens?',
    'browse?', 'browse-', '-search?', 'search?', 'search-filter?',
    'community?', 'community-list',
    'item?', 'items-by-', 'items-by-',
    'fonsantic?', 'llibres?', 'video?', 'videos?',
    'e-prints', 'eprintsrecercat?', 'revistes?', 'tesis'
]
