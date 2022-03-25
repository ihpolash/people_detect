# Instruction for Setup

1. Create an virtual environments for the project

2. install all the requirements using following

>> pip install -r requirements

3. Then, just run the server using following command

>> python manage.py runserver


# If you want to check with whole html file list, just follow the steps

1. For preparing the dataset, run the command

>> python prepare_dataset.py file save_dir_name/

For example, 
>> python prepare_dataset.py html/Hotel-Images-1 Hotel-Images-1/

2. For detecting people in the image, run the command

>> python detect.py save_dir_name/

For example,
>> python detect.py Hotel-Images-1/

3. For generating txt file of url list of people in the images, run the command

>> python generate_txt.py save_dir_name/ file txt_name.txt

For example,
>> python generate_txt.py Hotel-Images-1/ Hotel-Images-1 Hotel-Images-1.txt