Project is divided in 6 parts
1. Surfing Internet
2. Database
3.Detecting Object
4.Editing Photos
5.Uploading posts, updating database and files


===================================================
Surfing Internet
BrowserData
----<platform>
-----------<AppData>

-SurferHelpers
--Drivers.py    (Setup selenium driver)

*SurfInternet
    class Login   (logging into different platforms)
    Object  <object_name> = Login(insta_login={'username': 'username', 'password': 'password'})
    Object.Login_instagram  (login into instagram)

====================================================