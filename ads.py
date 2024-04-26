from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

def filedel(filenames):
    # Loop through the list of filenames and delete each file
    filenames.sort()
    print(filenames)
    for i in range(0,len(filenames)):
        os.remove(filenames[i])


import shutil

def delete_folder_contents(folder_path):
    """
    Deletes all the contents of a folder, but does not delete the folder itself.
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Error deleting {file_path}: {e}')



# Read the Excel file into a pandas DataFrame
ff = input("Enter name of excel file")
df = pd.read_excel('{}.xlsx'.format(ff))
ll = input("Enter name of imgfile in jpg")
# Get the values from the 'Name' column as a list
names = df['Name'].tolist()
qq=[]
for i in names:
    qq.append(i.title())
# Print the list of names
print(names)
print(qq,len(qq))

recipients= qq
total=[]

for recipient in recipients:
    template = Image.open('{}.jpg'.format(ll))
    font = ImageFont.truetype('arialbd.ttf', 70) # Set font and font size
    fontd = ImageFont.truetype('arial.ttf', 20) # Set font and font size
    
    draw = ImageDraw.Draw(template)
    text = recipient
    text_size = draw.textsize(text, font=font)
    # textd = "18-02-23"
    text_sized = draw.textsize(text, font=fontd)
    
# Calculate the x and y coordinates for the center of the template image
    center_x = template.width // 2
    center_y = template.height // 2

# Calculate the x and y coordinates for the text
    text_x = center_x - text_size[0] // 2
    text_y = (center_y + 80) - text_size[1] // 2
    
    # Setting the values of the fields for the current recipient
    draw.text((text_x,text_y), recipient, fill=(0, 0, 0), font=font)
    # draw.text((0,(template.size[1] - text_sized[1])), "18-02-23", fill=(0, 0, 0), font=fontd)
    template.save('certificate/{}.png'.format(recipient.strip()))
    total.append('{}.png'.format(recipient.strip()))


g = input("do you want to delete files? (y/n): ")

if g == 'y':
   delete_folder_contents('certificate')

else:
    ("files created")