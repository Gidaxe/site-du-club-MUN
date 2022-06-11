def sort_source(liste):
    for container in liste:
        if container.img_url and not container.img_upload:
            container.img_url = container.img_url
        elif container.img_upload and not container.img_url:
            container.img_url = container.img_upload.url
        elif not container.img_upload and not container.img_url:
            container.img_url = '/static/images/grntriangles.jpg'
        else:
            container.img_url = container.img_upload.url
    return liste
