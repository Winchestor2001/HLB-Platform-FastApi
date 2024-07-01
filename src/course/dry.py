import base64
import os


async def course_poster_image(data, base_url):
    image = data.pop("poster_image")
    image_data = base64.b64decode(image)

    file_name = f"{data['name']}_poster.png"
    file_path = f"media/course_posters/{file_name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(image_data)

    image_path = f"{base_url}media/course_posters/{file_name}"
    data.update({"poster_image": image_path})
    return data
