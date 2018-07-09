def work_work(img, remove_direction, num_of_seam_to_delete, algo_type):
    # Perform seam carving with save option
    import cv2
    from skimage import transform

    from algo import my_algorithm

    direction = remove_direction  # vertical/horizontal
    seams_per_iter = num_of_seam_to_delete  # number of pixels to remove each iteration (lower is cleaner)

    # # images resizing
    # print(img.shape)
    # size_change = img.shape
    # size_change = [int(x * 1) for x in size_change]
    # img = cv2.resize(img, (size_change[1], size_change[0]))
    # print(img.shape)
    energy_map = my_algorithm(img, algo_type)

    image_result = transform.seam_carve(img, energy_map, direction, seams_per_iter)
    # current_progress = str(num_of_seam_to_delete)
    return image_result


def work_work_progress(img, remove_direction, num_of_seam_to_delete, algo_type):
    # Perform seam carving without save option
    # don't save image if progress button is click, just show it, because if save, a lot of image will be save.

    import cv2
    from skimage import transform

    from algo import my_algorithm

    direction = remove_direction  # vertical/horizontal
    seams_per_iter = num_of_seam_to_delete  # number of pixels to remove each iteration

    cv2.imshow('Original Image', img)
    # # images resizing
    # print(img.shape)
    # size_change = img.shape
    # size_change = [int(x * 1) for x in size_change]
    # img = cv2.resize(img, (size_change[1], size_change[0]))
    # print(img.shape)

    energy_map = my_algorithm(img, algo_type)

    # put images into a array
    buffer_image = []
    for i in range(0, seams_per_iter):
        image_result = transform.seam_carve(img, energy_map, direction, i)
        buffer_image.append(image_result)

    # Show images only when the steps can be divided by 10
    for i in range(0, len(buffer_image)):
        current_progress = str(i)
        if i % 10 == 0:
            cv2.imshow("Result " + current_progress, buffer_image[i])
