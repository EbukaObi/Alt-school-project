# Altschool Second Semester Examination Project



### OVERVIEW

You need to create a blogging app. The fundamental concept is that anyone visiting the website should be able to read a blog post written by them or another user because the app has a landing page that lists a variety of articles written by different authors.

## SPECIFICATIONS


The Blog should have a Home Page, About Page, Contact Page, the Blog application should have a user authentication where a user can create an account and login so that they could be able to create a blog, also the Blog should have the logout ability.

## MILESTONES

- There should be a variety of users who can access the program and contribute content to the blogging platform.
- Every user needs to have a first name, last name, email, and (you can add other attributes you want to store about the user)
- The blog app should allow users to register and login.
- The home page of the app should provide a list of blogs produced by various users.
- Each blog should show the user that created it and the time the blog was created.
- Signed in and non signed in users should be able to visit this page
- If a user is signed in and visits an article they created, they should see an edit button to edit either the title or the body of the article.
- Clicking on the edit button on an article should take the user to the edit page.
- Your database should contain User information and should be able to store every information about the User there.
- Try to be creative as we will be paying attention to the details. 

# FEATURES
- Authentication and authorization 
- Password reset (pending)
- View , create , update and delete post 
- Add image to post (pending)
- Add profile image (pending)


## ENPOINTS
| ROUTE | FUNCTIONALITY |ACCESS|
| ----- | ------------- | ------------- |
| ```/signup``` | _Register new user_| _Any user_|
| ```/login``` | _Login user_| _Any_|
| ```/logout``` | _Logout user_| _Authenticated user_|
| ```/``` | _Home page_| _Any_|
| ```/post_details/<id>``` | _Retrive a post_| _Authenticated user_|
| ```/add_post``` | _Create a post_| _Authenticated user_|
| ```/add_post/<id>/edit``` | _Edit a post_| _Authenticated user and post author_|
| ```/delete/<id>``` | _Delete a post_| _Authenticated user and post author_|
| ```/contact``` | _Contact_| _Any_|
| ```/about``` | _About xenith_| _Any_|

A quick look at some of the pages

-The Home page
![homepage](https://user-images.githubusercontent.com/90873641/200201685-3d3c88dc-1a11-4362-b482-ac951c9abd07.JPG)

-The About page
![About Page](https://user-images.githubusercontent.com/90873641/200201759-ddbe3e75-632d-44f0-8bd3-948e59f87943.JPG)

-The Contact page
![Contact page](https://user-images.githubusercontent.com/90873641/200201772-c5682bc3-89fa-42a4-9aed-98f9f410821b.JPG)

-The post detail page (When a blog post is clicked on the home page, it takes you to this post detail page where you can read the entire blog in full)
-The post detail page authored by a particular user shows edit and delete buttons if that user is logged in at that moment.
- The blog was designed in such a way that blog posts can only be deleted by the author.
- ![post details page](https://user-images.githubusercontent.com/90873641/200202010-7e37da0e-95ce-4aec-b8e5-801575d2f82c.JPG)




