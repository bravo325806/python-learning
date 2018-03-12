

from PIL import Image
import glob


# put file name to list
train_list = []
train_path = 'train/'
for file_name in glob.glob(train_path+"*"):
    train_list.append(file_name[6:])

# put file name to list
test_list = []
test_path = 'test1/'
for file_name in glob.glob(test_path+"*"):
    test_list.append(file_name[6:])


# ImageDataGenerator
# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `save_dir/` directory

for train_img in train_list:
    img = load_img(train_path+train_img)
    x = img_to_array(img)
    x = x.reshape((1,)+x.shape)
    
    # run 20 
    i=0
    for batch in datagen.flow(x,batch_size=1,save_to_dir='save_dir', save_prefix=train_img[:3], save_format='jpeg'):
        i = i + 1
	if i > 21:break;
	
