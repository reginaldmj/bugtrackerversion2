<h1 align="center">Welcome to Bugtracker 🪳</h1>

> A website to track development progress on bug reports and feature request tickets.
>
> File tickets, assign users, edit existing tickets, add details, and update ticket status. View the status of every ticket direcly from the homepage.
>
> Site is limited to authenticated users, only. Each user has an overview page where their contact info and assigned tickets are displayed.

## Prerequisites
- [`Python 3`](https://www.python.org/downloads/)
- [`Poetry`](https://python-poetry.org/)

## Install

After dowloading the repo, do the following:

```sh
poetry install
poetry shell
python manage.py migrate
```

## Usage

On first use, create a new `superuser`:

```sh
poetry shell
python manage.py createsuperuser
```

To start a local server:

```sh
python manage.py runserver
```

To view the website in your browser, navigate to `localhost:8000`.

Login with the username and password created for your superuser

## Author

👤 **Reginald Jefferson**

* Website: 
* Github: (https://github.com/reginaldmj)
* LinkedIn: (https://www.linkedin.com/in/reginald-jefferson-42b0b61a8/)
