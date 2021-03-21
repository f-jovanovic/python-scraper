import urllib.parse as urllib


def lambda_find_logo():
    return lambda value: value and "logo" in value


def lambda_check_for_homepage(base_url):
    return lambda value: value and value == base_url or value == "/"


filters = [
    {"class_": lambda_find_logo()},
    {"id": lambda_find_logo()},
    {"src": lambda_find_logo()},
]


def get_logo(html, base_url):
    if html:
        filters.append({"href": lambda_check_for_homepage(base_url)})
        result = test(html, base_url)
        if result:
            return result

        result = find_img_tag(html, base_url)
        return result


def iterate_through_tags(tags, base_url):
    if tags:
        for tag in tags:
            return find_img_tag(tag, base_url)


def find_img_tag(item, base_url):
    if item.name == "img":
        image = item
    else:
        image = item.find("img")

    if image:
        return format_image_source(image, base_url)


def format_image_source(image_tag, base_url):
    image_source = image_tag.get("src")

    if not image_source:
        return None

    if not bool(urllib.urlparse(image_source).netloc):
        image_source = urllib.urljoin(base_url, image_source)
    return image_source


def test(html, base_url):
    for item in filters:
        tags = html.find_all(**item)
        result = iterate_through_tags(tags, base_url)
        if result:
            return result
