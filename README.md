# Discord Rich-Presence Customizer
A easy to use tool, which allows you to customize your Discord Rich Presence, made in Python

## Installation

1. Download the latest release at: 
2. Run start.bat. It will install all the components needed.
3. Have fun.

## How to use

In Discord, Rich Presences require a application. So, if you want to (really) customize your Rich Presence, you have to create one. If you don't want to create one, we have created one for you :). It will look something like this:

![defaulttheme](https://user-images.githubusercontent.com/97536100/233160426-676cf07f-4c86-4590-9f65-643d38c50569.PNG)

Like you haven seen in the picture above, in your profile always appears "plays Customized" and you are not able to change the images at the left side.

If you are fine with that you can follow the instructions at "How to use (default edition)". 
If you want to create your own application, you can follow the instructions at "How to use (custom edition)"

## How to use (default edition)

If you are fine with having the default theme, you can follow these instructions. If you do, your discord profile will look something like this:

![defaulttheme](https://user-images.githubusercontent.com/97536100/233160426-676cf07f-4c86-4590-9f65-643d38c50569.PNG)

1. Follow the instructions at "Installation"
2. Run the command "createconfig"
3. Select a name for your config. (Remember it, you will need it to load your configuration later.)
4. Set the mode to "default" by typing "default" (omg)
5. Provide your first line of your rich presence. (It will appear below the title)
6. Provide your second line.

You will be asked if you want to add buttons. If you do not want you can type "no" and you are done. You can go to step ten.

7. Select "y". 
8. Select the URL of your Button. It will be visible in your profile. 
9. Provide the URL for your Button. (ex.: google.com) 

You will be asked if you want to add another button. If you do, you can just do the same again. 

Congratulations! You have created your first config! Now we want to load it, so it will appear on your Discord Profile.

10. Run the command "loadconfig"
11. Enter the name, you have selected in step 3 for your configuration file. (watch out for upper and lower case)
12. If no errors appear, congratulations! You should now see your customized rich presence! If you have encountered any errors, feel free to create an issue!

## How to use (custom edition)

You have the possibility to design your own rich presence. It's a bit more complicated, but i'm sure you'll make it :D

1. Go to https://discord.com/developers
2. Click on "New application", it's at the top right
3. Provide a name and click on "create". The name will appear as the title, like "playing [the name]"
4. Look at the left and select "Rich Presence".

![tutorial_richpresence_1](https://user-images.githubusercontent.com/97536100/233164553-b61e2658-cd05-4a46-bef7-46bbe50f991c.png)

5. In the sub menu you select "Art Assets". 
6. At the bottom you are able to upload images. Click on add images and provide a name for your image. (Rich Presence supports two images, one lare and one small)
7. When you are done, go to the left again and select "General information". Down there, you copy the "Application ID".

![copy_application_ID](https://user-images.githubusercontent.com/97536100/233166038-08aee1f2-a910-4041-b551-3ba6e4cfd78b.png)

8. Follow the instructions at "Installation"
9. Run the command "createconfig"
10. Select a name for your config. (Remember it, you will need it to load your configuration later.)
11. Set the mode to "custom" by typing "custom" (omg)
12. Provide your application ID, which you have copied in step 7
13. Provide the name of your large image (leave empty if you don't want one)
14. Do step 13 again, for the small image.
15. Provide your first line of your rich presence. (It will appear below the title)
16. Provide your second line.

You will be asked if you want to add buttons. If you do not want you can type "no" and you are done. You can go to step ten.

17. Select "y". 
18. Select the URL of your Button. It will be visible in your profile. 
19. Provide the URL for your Button. (ex.: google.com) 

You will be asked if you want to add another button. If you do, you can just do the same again. 

Congratulations! You have created your first config! Now we want to load it, so it will appear on your Discord Profile.

20. Run the command "loadconfig"
21. Enter the name, you have selected in step 3 for your configuration file. (watch out for upper and lower case)
22. If no errors appear, congratulations! You should now see your customized rich presence! If you have encountered any errors, feel free to create an issue!

## Commands

Here is a list of commands. Pay attention to upper and lower case letters and do not anyting to them.  You can see them in the application using the "commands" command.
```
createconfig - Allows you to create a configuration file. In comparation with it, you don't have to customize your profile every time you start the application.
loadconfig - Allows you to load a config you have created. Pay attention to upper and lower case letters.
defaultconfig - Allows you to set a configuration file as the default option. It will be automatically loaded, everytime you start the application.
commands - Shows you a list of commands.
clear - Clears the console. For those who love order :)
exit - Stops the application :(
```
