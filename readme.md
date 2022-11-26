 ## Django API project
 
This project allows buy products with stripe payment engine.

**Prerequisites**

 - Installed Docker Engine and Docker Compose.	For install this use
   [official documentation](https://docs.docker.com/desktop/)

**Install project**

 1. Clone this repository
	`gh repo clone Faraday13/api` or
    `git clone https://github.com/Faraday13/api.git`
 2. Register account in [Stripe](https://stripe.com/)
 3. Make file `.env` in subdirectory `/api`
 4. Add in `.env` two variables :
	`export STRIPE_API_PUBLIC_KEY=your_public_api_key` and
	`export STRIPE_API_PRIVATE_KEY=your_private_api_key`
 5.  In project folder run `docker-compose up -d`

**Start project**

We use default database SQLite3. Instatnce of db with test products located in the project folder.
For start web service open [http://127.0.0.1:8000/item/1/](http://127.0.0.1:8000/item/1/)  in your browser. 
This is test product so you can see the functions of the service. Add more you can on [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Default login and password `admin`, `qwerty`