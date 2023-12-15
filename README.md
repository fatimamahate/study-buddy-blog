![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Study Buddy Blog
This is my project called Study Buddy Blog. It is aimed towards teenagers who going through exams upto university students.

[You can view the live project here](hhttps://study-buddy-blog-01ab6e2c45d9.herokuapp.com/)

### Project Goals:
The aim was to create a minimalist blog post website to provide insight, tips and trick  into studying. We have the CRUD functionality, where the usess are able to create comments, read comments, Update (or Edit) comments and delete comments. 

### Methodology
This project used the Agile Methodology. The Kanban Boards on Github were used to organise User Stories and Epics. Furthermore, labels of must, should, won't fix and maybe not. 

### User Stories
Each Epic is made up of some User Stories

- **Epic-Admin/Authorization**
  - Account Sign Up 
  - Manage Posts
  - Create Drafts
  + Add Own posts
 
- **Epic-View**
  
  - See the post (on landing page)
  - Read the post (when you click)
- **Epic-Comments**
  
  - Edit Comments
  - Comment Compliance
  - Commenting
  - View Comments
- **Epic-Likes**
  
  + View Likes
  + Like a post
  + Unlike 

The User Stories with an + are not implemented. 

You can find the project board [here](https://github.com/users/fatimamahate/projects/10)

1. Add own posts was not implemented at this stage due to time constraints
2. The likes were removed due to the fact that this is aimed at teenagers. Whilst conversation is encouraged, this website is not just about who can have the most popular blog post. It is not designed for competition. Rather it is to students study and move into university. Eventually, this blog site will be available to many authorised users who can make their own posts. Therefore, it has potential to become a site only concerned about bringing in likes especially since it will be opened to many poeple in the future. 

### Features
#### Current Features
##### Navigation
The navbar is at the top of each page with sign in, sign out and home links to take you to respective pages. 
![Navbar](/documentation/images/navbar.JPG)
When the screen size is smaller, the navbar responds by making the links as part of a 'hamburger menu' i.e a menu where the links are one on top of each other.
##### Homepage
- The homepage includes the latest blogposts. It ensures the user can see up to date articles everytime they visit the page. It would be useful to have a search function so that a user can search for older blog posts. 
- When we click on Sign Up, we are redirected to the sign up page.
- This is where a new user could sign up using email, a user name and password.
![Sign Up](/documentation/images/sign-up-page.JPG)
- When we click on Sign In, the user can use their credentials to log in.
![Sign in](/documentation/images/sign-in-page.JPG)
- There is also a page which asks user if they are sure about signing out. 
![Sign Out Options](/documentation/images/sign-out-options.JPG)
- The footer has links to the social media sites - facebook, instagram and youtube. The footer also has a dark background to also make it stand out.

- In the corner, there is a message to say if you are signed in or signed out. 
![Not logged in](/documentation/images/not-signed-in.JPG)
![Logged in](/documentation/images/signed-in.JPG)

##### Posts
![Blog Post](/documentation/images/blog-post.JPG)
- The comment section is available when the user has logged in. Otherwise, they can only see regular comments. They are able to delete comments as wll as edit comments. 
![Comments-not signed in](/documentation/images/comments-not-signed-in.JPG)
![Comments-signed in](/documentation/images/comments-signed-in.JPG)
![Sign up](/documentation/images/sign-up-page.JPG)
- The buttons change colour when it is hovered over in comments and on posts. 

- Favicon was used for links

#### Wireframes
The following wireframes were used. As the coding took place,there were some changes but overall look similar. 

![Wireframe homepage](/documentation/wireframes/wireframe-home.png)
![Wireframe post and comment](/documentation/wireframes/wireframe-postcomment.png)
![Sign In](/documentation/wireframes/wireframe-signin.png)
![Sign Out](/documentation/wireframes/wireframe-signout.png)
![Sign Up](/documentation/wireframes/wireframe-signup.png)
![Smaller Device](/documentation/wireframes/wireframe-smaller.png)

#### Testing
I have tested manually tested each function such as sign in and blog posts on Google Chrome and Microsoft Edge (the browser I used).

##### Python Testing
Furthermore, there is automated testing to test each function is working. 
![test](/documentation/test/blog-test-forms.JPG)

These are the user stories that were tested: 

- **Epic-Admin/Authorization**
  - Account Sign Up 
  - Manage Posts
  - Create Drafts
- 

- **Epic-View**
  
  - See the post (on landing page)
  - Read the post (when you click)
- **Epic-Comments**
  
  - Edit Comments
  - Comment Compliance
  - Commenting
  - View Comments
  
  Furthermore, the hover functions also work. 

#### Deployment

1. Login to [Heroku](https://dashboard.heroku.com/apps)
2. Click on New
3. Click on Create New app
4. Choose a name for your file it must be unique!
5. Choose the closest place to you.
6. Log in to ![ElephancSQL](https://www.elephantsql.com/)
7. Click on create new instance
8. set up you plan.
9. Give it a name.
10. Select Tiny Turtle (Free) plam
11. Select Region
12. Choose a data center closest to you
13. Click review
14. Check your details
15. Click create instance
16. Go back to the ElephantSQL dashboard and click on the database youve just created
17. In details, copy the database URL
18. Open up your workspace
19. Add a file env.py
20. Add the line import os
21. Set the environment variables by os.environ["DATABASE_URL"]="your copied Url"
22. Then add os.environ["SECRET_KEY"]="some secret key you can make up"
23. Save the file
24. Open settinfs.py file
25. Add the following code:
 import os
 import dj_database_url
 if os.path.isfile('env.py'):
     import env
26. Scroll down to SECRET_KEY and replace the brackets with your own secret key
27. Scroll to DATABASES and comment out the code
28. Replace it with the following
    DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }
29. In your terminal, type python manag.py migrate
30. Go to Heroku Dashboard
31. Open up setting
32. Add two config vars
33. DATABASE_URL --> add the database url from elephantsql
34. SECRET_KEY --> add your secret key. 
35. Login in to CLoudinary
36. Go to dashboard
37. Go to cloudinary_url and copy it
38. In the env.py file, type os.environ["CLOUDINARY_URL"] = paste your url here
39. Go back to Heroku
40. Navigate to settings tab
41. Scroll to Config vars
42. Add CLOUDINARY_URL and paste in the url
43. And in another one add, DISABLE_STATIC and 1
44. This must be removed at final deployment
45. In the settings.py file:Add Cloudinary Libraries to INSTALLED_APPS in order ’cloudinary_storage',  ’django.contrib.staticfiles', ’cloudinary',
46. Add the following code below STATIC_URL = ’/static/' to use Cloudinary to store media and static files:
      - STATICFILES_STORAGE = ’cloudinary_storage.storage.StaticHashedCloudinaryStorage'
      - STATICFILES_DIRS = [os.path.join(BASE_DIR, ’static')]
      - STATIC_ROOT = os.path.join(BASE_DIR, ’staticfiles')
      - MEDIA_URL = '/media/'
      - DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
47. Now type TEMPLATES_DIR = os.path.join(BASE_DIR, ’templates')
48. type TEMPLATES_DIR: 'DIRS': [TEMPLATES_DIR],
49. Type ALLOWED_HOSTS = [”Your_Project_name.herokuapp.com”, ”localhost”]
50. In your files in your worksoacem create 3 folders: media, static and templates
51. Create Procfile in highest directory
52. In the Procfile add web: gunicorn PROJ_NAME.wsgi
53. Finally, use git to add, commit and push your changes. 
54. Go back to heroku and you can either deploy branch or enable automatic deploys
55. When you want to see the website, click on Open App. 

##### Credits

1. [Code Institute:](https://codeinstitute.net/) - projects (both old and new) and tutor support (who were amazing!)
2. [Stack Overflow:](https://stackoverflow.com) - edit/delete
3. [Unsplash: image by firmbee.com](https://unsplash.com/photos/person-writing-on-white-paper-gcsNOsPEXfs)
4. [Pexels: by lil artsy](https://www.pexels.com/photo/person-holding-orange-pen-1925536/)
5. [Pexels: by monstera production](https://www.pexels.com/photo/focused-students-doing-homework-together-in-light-workspace-6237955/)
6. [Pexels: by Karolina Grabowska](https://www.pexels.com/photo/girl-solving-an-equation-and-using-a-calculator-5877644/)
7. [Pexels: by Leeloo Thefirst](https://www.pexels.com/photo/close-up-shot-of-text-on-a-letter-board-8177961/)

##### Acknowledgements
Thank you to Code Institute for the walkthrough projects. 
Also thank you to my mentor Brian Macharia who provided a lot help earlier in the year. 
