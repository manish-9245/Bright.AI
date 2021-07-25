
# Bright.AI

Skin diseases are common problem to everyone and different types of skin allergies are becoming more and more common.Especially in rural communities where access to healthcare is limited and individuals rely on farming for food and income, the impact of skin diseases may be greater. Nowadays, there is a high prevalence of skin diseases coupled with limited availability of trained dermatologist which is a major issue.

Artificial intelligence (AI) has the potential to help clinicians care for patients and treat disease more efficiently. In Bright.AI, We have combined these advances in AI with other web technologies to provide an  accessible solution to everyone
## Demo

[![Alt text](https://res.cloudinary.com/talk-amigo/image/upload/v1627221078/Screenshot_2021-07-25_184832_i8vfyw.png)](https://youtu.be/FfwKyJNprHs)

  
## Technologies used

- We build the Machine learning model using images. We have used various types of image processing and image segmentation algorithms to extract the affected area from the image and classify into various categories.
- Website is built using a php, React and MySQL database.
- To integrate the Blogs section, Ghost CMS is used.
- Jitsi API is used to facilitate video consultation with doctors.
- The 3D Skin model is created with the help of echoAR.





  
## Features

- Analyze skin disease: User can check the type of skin disease by uploading the image. Also, they can checkout the necessary steps and precautions to take by clicking on Find out more tab.
- Consultation : In case of severe issues, we also provide the option to consult with doctors. User can connect with doctor either through Video calling or Chatting.
- AR skin model: 3D view of Skin model can be viewed to know more about the inner layers and cell structure.
- Blogs:.This platform can unlock new ways for people to stay better informed about skin disorders through expert curated blogs.
- Admin Panel: Admin can manage data about all the chatrooms, users, and blogs.

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/JoelJJoseph/HACKY.git
```

- Install PHP and Xampp on system
- Run Apache and Mysql server from Xampp controls
- Open localhost/phpmyadmin on your browser and click on import and import the files users.sql and chat_system.sql in chatting folder
- Change connection variables accordingly in db_connect.php files
- Copy all the files to c/Xampp/htdocs.
- Now type localhost/filename(that you copied in htdocs)

To run Ghost CMS 

```bash
  cd project
```
```bash
  cd bright-blogs
```
```bash
  ghost start
```

  
## Screenshots

### Admin Panel
![Admin Panel](https://res.cloudinary.com/talk-amigo/image/upload/v1627221589/Screenshot_2021-07-25_192804_j5lilq.png)


### Add Chat room page
![Add Chat Room](https://res.cloudinary.com/talk-amigo/image/upload/v1627221590/Screenshot_2021-07-25_192847_hznaex.png)

### Users list with Password Hashing

![Users list with Password Hashing](https://res.cloudinary.com/talk-amigo/image/upload/v1627221591/Screenshot_2021-07-25_192925_yutqtp.png)

### AR model on EchoAR

![AR model on EchoAR](https://res.cloudinary.com/talk-amigo/image/upload/v1627221423/screencapture-console-echoar-xyz-webar-2021-07-25-17_26_02_izeieb.png)

### Analyze Diseases

![Analyze Diseases](https://res.cloudinary.com/talk-amigo/image/upload/v1627221388/Screenshot_2021-07-25_184925_tnyejg.png)

### Blog page
![Blog page](https://res.cloudinary.com/talk-amigo/image/upload/v1627221405/Screenshot_2021-07-25_185004_tqcnvg.png)

