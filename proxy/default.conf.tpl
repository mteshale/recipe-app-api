server {
    listen ${LISTEN_PORT};

    location /static/ {
        alias /vol/static/;
    }

    location /media/ {
        alias /vol/media/;
    }

    location / {
        include /etc/nginx/uwsgi_params;
        uwsgi_pass ${APP_HOST}:${APP_PORT};
    }
}
