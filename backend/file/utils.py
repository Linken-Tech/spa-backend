def vehicle_image_upload_path(instance, filename):
    return "{}/{}/image/{}".format(
        instance.content_object.brand, instance.content_object.title, filename
    )


def vehicle_document_upload_path(instance, filename):
    return "{}/{}/document/{}".format(
        instance.content_object.brand, instance.content_object.title, filename
    )
