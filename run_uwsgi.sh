source /var/www/yBlogApp/venv_blog/bin/activate
sleep 1
uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi --module yBlogApp --callable app

