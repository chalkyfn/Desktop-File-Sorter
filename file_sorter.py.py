import os
import shutil

download_folder = "C:/Users/HP/Downloads"
image = "hello"


directories = os.listdir(download_folder)


images_jpg = [x for x in directories if ".jpg"  in x]
images_png = [x for x in directories if ".png"  in x]
images_jpeg = [x for x in directories if ".jpeg"  in x]
videos = [y for y in directories if ".mp4" in y]
pdf    = [z for z in directories if ".pdf" in z]
circ = [i for i in directories if ".circ" in i]
circ_asm = [i for i in directories if ".asm" in i]
word_files = [j for j in directories if ".docx" in j]
ppt_files = [j for j in directories if ".pptx" in j]
ppt_files2 = [j for j in directories if ".ppt" in j] 


#### PNG IMAGES ###
# os.mkdir("sorted_images2")

# for image in images_png:
#     main_path = f"{download_folder}\\{image}"
#     new_path = "sorted_images/" + image
#     shutil.move(main_path,new_path)


#### JPG IMAGES ###
# os.mkdir("sorted_jpg")

# for image in images_jpg:
#     main_path = f"{download_folder}\\{image}"
#     new_path = "sorted_jpg/" + image
#     shutil.move(main_path,new_path)
# os.mkdir("sorted_jpg")

#### JPEG IMAGES ####
# os.mkdir("sorted_jpeg")

# for image in images_jpeg:
#     main_path = f"{download_folder}\\{image}"
#     new_path = "sorted_jpeg/" + image
#     shutil.move(main_path,new_path)


#### MP4 VIDEOS ####
# os.mkdir("sorted_mp4")

# for image in videos:
#     main_path = f"{download_folder}\\{image}"
#     new_path = "sorted_mp4/" + image
#     shutil.move(main_path,new_path)

#### PDF ####
# os.mkdir("sorted_pdf")

# for image in pdf:
#     main_path = f"{download_folder}\\{image}"
#     new_path = "sorted_pdf/" + image
#     shutil.move(main_path,new_path)

#### CIRC FILES ####
# os.mkdir("sorted_circ")

# for image in circ:
#     main_path = f"{download_folder}\\{image}"
#     new_path = "sorted_circ/" + image
#     shutil.move(main_path,new_path)


#### CIRC_ASM FILES ####
# os.mkdir("sorted_circ_asm")

# for image in circ_asm:
#     main_path = f"{download_folder}\\{image}"
#     new_path = "sorted_circ_asm/" + image
#     shutil.move(main_path,new_path)


#### WORD FILES ####
# os.mkdir("sorted_wordfiles")

# for image in word_files:
#     main_path = f"{download_folder}\\{image}"
#     new_path = "sorted_wordfiles/" + image
#     shutil.move(main_path,new_path)

#### PPT FILES ####
# os.mkdir("sorted_ppt")

# for image in ppt_files:
#     main_path = f"{download_folder}\\{image}"
#     new_path = "sorted_ppt/" + image
#     shutil.move(main_path,new_path)

#### PPT FILES ####
os.chdir("C:\Users\HP\Documents\c projects\file sorter\sorted_ppt")

for image in ppt_files2:
    main_path = f"{download_folder}\{image}"
    new_path = "sorted_ppt/" + image
    shutil.move(main_path,new_path)