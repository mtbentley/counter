FROM matthewbentley/counter-base

WORKDIR /app

RUN git clone https://github.com/matthewbentley/counter.git /app/
RUN rm -rf .git .gitignore Dockerfile

RUN python manage.py migrate

EXPOSE 80

CMD ["/bin/bash", "-c", "cd /app/; gunicorn -b 0.0.0.0:80 -w 3 counter.wsgi:application"]
