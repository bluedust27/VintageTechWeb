# Deploy this application on EC2 instance
#### 1. Create virtual environment
	python3 -m venv /django/VintageTechWeb/<name of virtual env>
#### 2. Activiate virtual env.
    source /django/VintageTechWeb/venv/bin/activate
#### 3. Install all requirements
- Install Django
    	pip3 install django
- Install crispyforms
    	pip3 install django-crispy-forms

#### 4. Start django development server
	python3 manage.py runserver

#### 5. Check if page available
	wget http://127.0.0.1/admin

#### 6. Add instance’s DNS name/IP to “Allowed Hosts” in settings.py

#### 7. Open port 8000 for your ec2 instance

Navigate to page from a browser
http://13.59.16.197/collectibles/

#### 8. Edit the httpdconf file
###### sudo nano /etc/httpd/conf/httpd.conf

	Alias /static /django/VintageTechWeb/core/static
	<Directory  /django/VintageTechWeb/core/static>
		Require all granted
	</Directory>

	<Directory /django/VintageTechWeb/core/core>
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory>

	WSGIScriptAlias / /django/VintageTechWeb/core/core/wsgi.py
	WSGIProcessGroup core
	WSGIDaemonProcess core python-home=/django/VintageTechWeb/venv python-path=/django/VintageTechWeb/core/
