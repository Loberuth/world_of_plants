# World of plants

### This is a guide for this application.

## Technologies/tools used: 
     Python
     Tkinter (GUI module)
     SQLite database
     Libraries: pillow, matplotlib, numpy

When you download and unpack a .rar file, open the project in any IDE suitable for Python programming language (I used PyCharm, but other IDE-s should do just fine).

## **Login page**

When you run the application, the first page you see should be a login page. Login data should already be filled out in the input fields, but you can change the login data (see the My Profile section). You have an option to save your login data so that you don't have to fill them out every time you want to login, and all of the informations will be saved in a .txt file called userInfo.txt. If you choose to change the data, it will also change in userInfo.txt file, as well as in the SQLite database. In case you type a wrong username or password, you will not be able to login into the application. To see all the informations needed to login, you have to open SQLite database where all the data is stored.

## **Main page**

After a successful login, there will be 6 tabs which you can click to see a specific part of the application - List all pots, List all plants, Add a pot, Add a plant, Sensor simulation and My Profile. I will go through every tab and write all the necessary informations. Keep in mind that if you want to add, remove or update anything inside the application, **it will affect the database too, which means that everything you add, change or delete will also be changed inside the database**. When you do any changes inside the application, press the **Sync data** button to refresh the application!

## **Tab My profile**

Inside **My profile tab**, you can change all inputs except for the position input, because only admin has rights to manage the data. If you change certain informations, but not all, only the changed informations will be changed in SQLite database. Keep in mind that if you change username or password, or both, you will also have to write them again on **login page** since the old informations will be gone. Once you write them again, you will not have to fill out username and password if you click Save at login button on **login page**, and new informations will also be saved inside userInfo.txt.

## **Tab Sensor simulation**

Sensors are needed to tell you what to do with a certain plant - add more water, move to a place with more/less sunlight, etc. The way this works is: when you add a new plant, you will have to write some values for its ideal humidity, brightness, warmth and substrates. All the values you write for plants will then be compared to the sensor values, and based on that, an action will be needed. All the values that you enter are saved inside the database and you **have to enter all the sensor values**. You will be able to see sensors data inside a particular plant or pot window when you click show a pot/plant button, and based on that, you will be told what to do with them (not for real, just as a simulation). Inside **List all pots** tab, there is also an option to see sensor graphs per 1 frequency, which you can think of as every new package of new data (which you manually send, but for these purposes, this is more than enough).

## **Tab Add a plant**

When adding a new plant, you have to fill out all the fields and you have to choose an image. You can find some images I downloaded inside images folder, but you can also add more images. Once you fill everything out and click **Save button**, go to **List all plants** tab to see whether you new plant was added or not (although it should be added if you filled everything out).

## **Tab Add a pot**

Add a pot name, and choose whether you want you pot to be empty or you want it to have a plant inside it. If you press **Put a plant** radiobutton, a list of all the plants inside the application will be shown with all their informations. When you visit **List all pots** tab, you will be able to see your empty or full pot. **WARNING!** - If you choose an empty pot, you will not be able to add a new plant yet, that part is missing, but it will be added!

## **Tab List all plants**

Inside **List all plants** tab, you can see all the plants that you added or that were already added before. Informations that you see in every plant card is the data that was filled out during the process of adding a new plant, and when you click a **Show a plant** button, you can see a status which is actually the same thing I described in **Sensor simulation** section - plant data is compared to sensor data (humidity, brightness and soil warmth), and based on that, an action is needed. For example, if you have a humidity value that says High (I am not that thirsty!), this means that the plant has more water than it needs, so you might want to put it somewhere where humidity is not that high. If brightness value says Low (Give me light!), that means that you should probably put your plant where there is more light reaching to it. You can also update all the informations for a particular plant, and if you do so, the application will automatically change all the statuses and everything else that was affected with the new change. If you choose to delete a plant, **it will delete the plant from the list and from the database**.

## **Tab List all pots**

Finally, **List all pots** show all the pots with or without your plants inside them. There is also a status which says whether there is a plant inside a pot or not - **but there are some minor problems with showing the proper results - the results are shown, but only when you do some additional clicking**. If your pot is empty, sensors do not send any data to that pot and all the sensor statuses will have N/A next to them (not available). Also, there are no sensor graphs. If there is a plant inside your pot, then you will see all the sensors data and you will be able to see all the sensor graphs. Deleting the pot also **deletes it from the list and from the database**.

## **The end**

You made it! You would be able to figure out most of the things without me explaining everything, but there are some things which are not very clear unless you know what this application is about. There are some minor things that need to be changed (or added), but overall, this is it. Thank you for stopping by!
