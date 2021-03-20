import urllib.parse as urlparser


def get_logo(html, baseurl):
    if html:
        logoclass = html.find_all(class_=lambda x: x and "logo" in x)
        result = iterate_through_tags(logoclass, baseurl)
        if result:
            return result

        logoid = html.find_all(id=lambda x: x and "logo" in x)
        result = iterate_through_tags(logoid, baseurl)
        if result:
            return result

        imagesource = html.find_all(src=lambda x: x and "logo" in x)
        result = iterate_through_tags(imagesource, baseurl)
        if result:
            return result

        homepagehref = html.find(
            href=lambda value: value and value == baseurl or value == "/"
        )
        if homepagehref:
            result = find_img_tag(homepagehref, baseurl)
            if result:
                return result

        result = find_img_tag(html, baseurl)
        return result


def iterate_through_tags(tags, baseurl):
    if tags:
        for tag in tags:
            return find_img_tag(tag, baseurl)


def find_img_tag(item, baseurl):
    if item.name == "img":
        image = item
    else:
        image = item.find("img")

    if image:
        return format_image_source(image, baseurl)


def format_image_source(image_tag, baseurl):
    imagesource = image_tag.get("src")

    if not imagesource:
        return None

    if not bool(urlparser.urlparse(imagesource).netloc):
        imagesource = urlparser.urljoin(baseurl, imagesource)
    return imagesource
