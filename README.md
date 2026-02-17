# portfolio-webpage

## Personal Portfolio Website

Welcome to the source code for **Rashidat Adekoya's Personal Portfolio Website** A Django-based site showcasing my work, skills, and contact information.

---


## About Me 

**Hi, I'm Rashidat Adekoya**
A Software Developer passionate about Full-Stack Development, Python | Django, Java | Spring Boot | CSS, BootStrap, JS and building user-friendly web applications.

---


![GitHub last commit](https://img.shields.io/github/last-commit/Shida18719/portfolio-webpage?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/Shida18719/portfolio-webpage?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Shida18719/portfolio-webpage?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/Shida18719/portfolio-webpage?style=for-the-badge)


## CONTENTS
* [Overview](#overview)
  * [Project Goals](#project-goals)

* [Features](#features)
  * [Existing Features Across Page](#existing-features-across-page)

* [Technologies Used](#technologies-used)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)

* [What I Learned](#what-i-learned)
* [Connect](#connect)




## Overview

This project is a personal portfolio website built with Django. It is designed to showcase my skills, projects, and provide an easy way for visitors or potential employers to contact me. The site features a modern, responsive design using JavaScript, Vanilla CSS, Bootstrap 5, a theme switcher (light/dark mode), and dynamic project and contact sections. The codebase is structured for easy maintenance and future enhancements, making it both a professional presence and a playground for learning and experimenting with new technologies.

Link to deployed site: [Rashidat Adekoya's Personal Portfolio Website](https://portfolio-webpage-gf7s.onrender.com/)


### Project Goals

- **To showcase Skills & Projects:**  
  Present my development skills, technologies, and completed projects in a visually appealing and organized way.

- **Responsive Design:**  
  Ensure the portfolio is fully responsive and accessible on all devices (mobile, tablet, desktop).

- **Easy Contact:**  
  Provide a simple and secure way for visitors to contact me via a form, with email notifications. Alternatively, via social networks.

- **Modern UI/UX:**  
  Use Bootstrap 5 design principles, and interactive elements (like theme switching) for a professional look and feel.

- **Maintainability:**  
  Structure the codebase for easy updates, scalability, and future enhancements using Django best practices.

- **Learning & Experimentation:**  
  Serve as a platform to experiment with new technologies, Django features, back-end techniques, testing and AI tools.

- **Professional Presence:**  
  Offer a central, up-to-date place for recruiters and collaborators to learn about me and my work.


## Features

The website is comprised of 4 pages which are extended from a base template. A very different approach to other portfolio websites.

* Home page
* About page
* Projects
* Contact

### Existing Features Across Page

- **Responsive Design:** Looks great on all devices using CSS/Bootstrap 5.
- **Project Showcase:** Dynamic project cards with tags and GitHub links.
- **Contact Form:** Users can send messages directly to my email.
- **Theme Switcher:** Toggle between light and dark mode, with preference saved in localStorage.
- **Django Messages:** User feedback for contact form submissions and alerts.
- **Social Links:** Connect via LinkedIn and GitHub.
- **Modern UI:** Clean, accessible, and easy to navigate.

---

## Technology Used

- **Backend:** Django 4.x
- **Frontend:** CSS, Bootstrap 5, JavaScript, FontAwesome icons
- **Rich Text:** [djrichtextfield](https://pypi.org/project/django-richtextfield/)
- **Email:** Django's email backend for contact form
- **UX:** jQuery (for message fade-out), custom JS for theme toggle

---


## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtual environment


### Installation

1. **Clone the repo:**
    ```sh
    git clone https://github.com/Shida18719/agog-dev.git

    cd agog-dev
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

4. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

5. **Visit:**  
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## What I Learned

- How to configure Email, using google SendEmails API.
- The importance of saving theme preference in localStorage for a consistent user experience. - If theme is not stored in local storage the chosen theme is not kept - it switches on the click of page load.
- Managing content dynamically and leverage Django’s features: Django’s ORM (querying, relationships, admin editing), for scalable projects.
- Using `RichTextField` for flexible content editing.
- djhtml: For consistent django template (djhtml .)/ (djhtml template name)

---


## Connect

- [LinkedIn](https://www.linkedin.com/in/rashidat-adekoya-668843245/)
