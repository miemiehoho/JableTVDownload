import os


def move_film(source_file, destination_folder, film_name):
    file_mp4_temp_dir = os.path.join(source_file, f'{film_name}.mp4')
    file_jpg_temp_dir = os.path.join(source_file, f'{film_name}.jpg')

    move_file(file_mp4_temp_dir, destination_folder)
    move_file(file_jpg_temp_dir, destination_folder)


def move_file(source_file, destination_folder):
    file_name = os.path.basename(source_file)
    destination_file = os.path.join(destination_folder, file_name)
    os.rename(source_file, destination_file)
