# At Engineering Solutions

- [Github Repo Link](https://github.com/Robert-Clark-1990/atengineeringsolutions)

# Table of Contents

- [**Intro**](#introduction)
- [**Site Design**](#site-design)
- [**Features**](#features)
- [**Technologies Used**](#technologies-used)
- [**Testing and Bugs**](#testing-and-bugs)
- [**Deployment**](#deployment)
- [**Credits**](#credits)

---

# Introduction

AT Engineering Solutions is a welding and engineering business run by Will Tait and David Atkins. The purpose of this site is to demonstrate the work the duo are capable of and ilicit business from new or returning clients. The site is ran through one continuing homepage, split into sections for the homepage, about us, previous work, reviews and contact.

## User Stories

|   As A       |  I want to be able to...                                                                                   |
| :----------  | :--------------------------------------------------------------------------------------------------------- |
| Site User    | Quickly and easily understand the purpose of the site                                                      |
| Site User    | View a images of previous jobs and read customer reviews                                                   |
| Site User    | Easily locate a contact section with multiple forms of contact available, including inbuilt contact form   |
| Site Owner   | Log in via a site admin page and add new customer reviews as necessary                                     |
| Site Owner   | Upload images to a linked Instagram and have the images appear automatically in the previous works section |

---

# Site Design

Site users will be able to view everything available to them on the homepage, scrolling down through the various sections and using the links in the header to move straight to the sections they desire. The site will adopt a minimalist design, making use of the container margins to keep a clear design throughout the site.

While the site has no designated colour scheme, the use of blue, grey and white are the key sections to be used. Splashes of gold can be used in sections such as the review section to draw attention to important content.

Typography used is **Bebas Neue** for headers and **Roboto** for the rest of the text.

Reviews are contained in a json file which can be amended via the admin backend, accessible only to the AT Engineering Solutions team. The model follows this structure:

| Name      | Key     | Type               | Validation                |
| --------- | ------- | ------------------ | ------------------------- |
| Name      | name    | models.CharField   | max_length=254            |
| Review    | review  | models.TextField   |                           |


---

# Features

The site is broken down into these key sections:

- Homepage

    The homepage consists of a full page image (that may be changed to a full page video if one can be acquired) with the logo and a h1 tag overlaid over the top. A link to the contact form below can also be seen here.

- About Us

    The about us section showcases some edited images of previous work along with a brief description of what AT Engineering Solutions do. Another link to the contact form can be found here.

- Our Work

    Our Work is linked to the AT Engineering Solutions Instagram account. This should update as new images are uploaded to the Instragram account. Another link to the contact form will be here too. Elfsight is used to push Instagram content to the page, and uses the Lite version which limits monthly views to 200.

- Customer Reviews

    Again this section will showcase some more edited images of previous work, along with a carousel of reviews from previous clients. This carousel uses [Slick Slider](https://kenwheeler.github.io/slick/) and is updated via the admin backend. Another link to the contact form can be found here.

- Contact Us

    The contact us section is split into two parts with the first showing the contact details of AT Engineering Solutions, the address, and links to their social media accounts. The second part is a contact form that sends emails to their gmail account.

---

# Technologies Used


## Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

   HTML5 was used to provide the structure and content of this project.

* [CSS3](https://en.wikipedia.org/wiki/CSS)

   CSS3 was used to style to the HTML5 elements.

* [JQuery](https://jquery.com/)

   JQuery was used to provide JavaScript functionality.

* [Python](https://www.python.org/)

   Python was used to provide the backend of this project.


## APIS and Frameworks

* [Bootstrap4](https://getbootstrap.com/)

   Bootstrap was used to build the elements of the site.

* [Django](https://www.djangoproject.com/)

   Django was used for Python frameworks.

* [Allauth](https://django-allauth.readthedocs.io/en/latest/)

   Allauth was used for account registration and management.

* [Slick Slider](https://kenwheeler.github.io/slick/) 

   Slick Slider was used for the carousel effect on the reviews section.

* [Elfsight](https://elfsight.com/)

   Elfsight was used for integrating the Instagram feed.


## Hosting Databases and Version Control

* [Git](https://git-scm.com/)

   Git was used for version control, utilising the Gitpod terminal to commit to Git and Push to GitHub.

* [GitHub](https://github.com/)

   GitHub was used to store the project.
   
* [Heroku](https://www.heroku.com/)

   Heroku was used to deploy this site.


## Websites

* [Google Fonts](https://fonts.google.com/specimen/Bebas+Neue?preview.text=AT%20Engineering%20Solutions&preview.text_type=custom#license)

   The Bebas Neue and Roboto Google Fonts were used as the fonts in this project.

* [TinyPNG](https://tinypng.com/)

   Tinypng was used to optimise jpg and png images to increase performance.

* [W3C Markup Validation](https://validator.w3.org/#validate_by_input) 

   W3C Markup Validation was used to ensure HTML met the necessary standards.

* [Jigsaw](https://jigsaw.w3.org/css-validator/) 

   Jigsaw was used to validate CSS code used in the project.

* [JS Hint](https://jshint.com/) 
   
   JS Hint was used to validate JavaScript code used in the project.

* [PEP8](http://pep8online.com/) 

   PEP8 was used to validated Python code used in this project.


---

# Testing and Bugs



---

# Deployment



---

# Credits

- [Bebas Neue Font](https://fonts.google.com/specimen/Bebas+Neue?preview.text=AT%20Engineering%20Solutions&preview.text_type=custom#license)

- [Slick Slider](https://kenwheeler.github.io/slick/) 

- [Link to get Favicon working](https://www.ordinarycoders.com/blog/article/add-a-custom-favicon-to-your-django-web-app#:~:text=If%20you%20are%20still%20getting,folder%20%3E%20static%20%3E%20img%20folder.)