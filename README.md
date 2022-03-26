- ## Building Web Applications

### For Context

We want to learn how to create robust web applications using Django(a high-level Python Web framework that encourages rapid development and clean, pragmatic design) along with Continuous Integration(the practice of automating the integration of code changes from multiple contributors into a single software project). You are to focus on learning and understanding the following:

- Creating web applications with Django
- Use PostgreSQL as Django Database backend
- Setting up continuous integration using Github Actions

### Expectations

By the end of the tasks, you should be able to have an in-depth understanding of the concept and implementations of the following:

1. Django components and how they fit together to form a whole:
      - Models
      - Views
      - URLs in Django
      - Request and Response Cycle
      - Django Template Engine

2. Continuous Integration
      - Testing Django applications
      - Setting up continuous integration using Github actions

## Part I → Polls App

In this part, you are to follow Django official documentation tutorial to create polls app. This tutorial comprises of 7 parts with each part explaining a concept or component of Django project. [Polls App Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)

**Note: Make sure you deeply conceptualize, comprehend and understand the current part before moving on to the next.**

### Setup

- Clone this repository from Github classroom.
- You will find it only contains a README file and a .gitignore file.
- Create and checkout to a new git branch called `setup_ci`. And in this branch …
- Create a .github folder. In this folder …
- Create PULL_REQUEST_TEMPLATE.md file and add PR format of your choice.
- Create a workflow folder and add `ci.yml` file and implement configuration for continuous integration.
- Make a commit for your changes in the setup_ci branch and push the branch to your repository.
- Visit the repository on Github and create a pull request from the branch and merge it to master or main branch.
- Go back to GIT and checkout to master and pull the merged changes into your local master.
- So you start the cycle again for each part of the tutorial and name each branch the topic treated in the part.

## Part II → Create a Blog Web Application

In this part, you are to create a personal weblog Application.
A blog (a shortened version of “weblog”) is an online journal or informational website where a writer or a group of writers share their views on an individual subject.

### Minimum Viable Product (MVC)

The project should at least have the following features

1. Login
2. Register
3. Read Blog
4. Create Blog
5. Update Blog
6. Delete Blog

### User Story

1. All Users should be able to read blogs.
2. Registered Users should be able to create blog post.
3. Blog can only be updated and or deleted by the user who created it or Admin.

### Approach

You are expected to complete this project using the following approach

- Create a personal GitHub repository for this application.
- Make sure you write a proper and understandable readme describing what the application is all about and how the application can be run locally (Getting started).
- Make sure you put both your frontend and backend skills into usage and build a unique, attractive and smashing web application that you will be proud of, after all, it’s your personal blog.
- When you are done with your implementation add the GitHub link to `part 1` readme file.
- [OPTIONAL] Host the web application on any hosting platform of your choice (Heroku, Pythonanywhere, Digital Ocean, AWS etc) and add the link to `part 1` readme file.
