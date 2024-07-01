import os
from PIL import Image

# Функция для получения списка изображений из локальной папки и её подкаталогов
def get_image_files_from_folder(folder_path):
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.tif')
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(supported_formats):
                image_files.append(os.path.join(root, file))
    return image_files

# Функция для загрузки изображений из списка папок
def load_images_from_folders(folder_paths):
    images = []
    for folder_path in folder_paths:
        image_files = get_image_files_from_folder(folder_path)
        if not image_files:
            print(f"No images found in directory: {folder_path}")
        for image_file in image_files:
            try:
                img = Image.open(image_file)
                images.append(img)
                print(f"Loaded image: {image_file}")
            except Exception as e:
                print(f"Error loading image {image_file}: {e}")
    return images

# Функция для объединения изображений в один TIFF файл
def save_images_to_tiff(images, output_file):
    if images:
        images[0].save(output_file, save_all=True, append_images=images[1:], compression="tiff_deflate")
        print(f"TIFF file saved as: {output_file}")
    else:
        print("No images found to save.")

# Пример использования
folder_paths = [r'C:\Users\Asus\Desktop\Для тестового']  # Использование сырой строки
images = load_images_from_folders(folder_paths)
save_images_to_tiff(images, 'Result.tif')

# Проверка текущей рабочей директории и вывод пути к созданному файлу
current_directory = os.getcwd()
output_file_path = os.path.join(current_directory, 'Result.tif')


