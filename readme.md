 ## Django API project
 
This project allows buy products with stripe payment engine.

**Prerequisites**

 - Installed Docker Engine and Docker Compose.	For install this use
   [official documentation](https://docs.docker.com/desktop/)

**Install project**

 1. Clone this repository
	`gh repo clone Faraday13/api` or
    `git clone https://github.com/Faraday13/api.git`

 2. Register account in [Stripe](https://stripe.com/).

 3. Make file `.env` in project folder.

 4. Add in `.env` variables and input your data here :
	`STRIPE_API_PUBLIC_KEY=your_public_api_key`
	`STRIPE_API_PRIVATE_KEY=your_private_api_key`
	`DJANGO_SECRET_KEY=your_django_secret_key`
	`DJANGO_SUPERUSER_USERNAME=login_for_admin_panel`
	`DJANGO_SUPERUSER_PASSWORD=passwor_for_admin_panel`
	`DJANGO_SUPERUSER_EMAIL=email_for_admin_panel`
	`POSTGRES_HOST=db_host`
	`POSTGRES_PORT=db_port`
	`POSTGRES_DB=db_name`
	`POSTGRES_USER=db_user`
	`POSTGRES_PASSWORD=db_password`

 5.  In project folder run `docker-compose up -d`

 6.  Make miigration 
 `docker-compose exec web python manage.py migrate`

 7.  Create superuser for amin panel 
`docker-compose exec web python manage.py createsuperuser --noinput`

**Start project**

For start web service admin panel open [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) in your browser. 

Add product data in items.

First product can be finded on [http://0.0.0.0:8000/item/1/](http://0.0.0.0:8000/item/1)

Deployed project you can test [here](https://api-faraday13.herokuapp.com/item/1/).
This is test product so you can see the functions of the service. Add more you can in [admin panel](https://api-faraday13.herokuapp.com/admin). Default login and password `admin`, `qwerty`.