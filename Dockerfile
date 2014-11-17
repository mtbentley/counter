FROM matthewbentley/counter-base

WORKDIR /app

RUN git clone https://github.com/matthewbentley/counter.git /app/
RUN git rev-parse HEAD | head -c10 > /app/rev

RUN rm -rf .git .gitignore Dockerfile requirements.txt coreos-stable-hvm

#RUN python manage.py migrate

EXPOSE 80

ENV DEBUG False

CMD ["/bin/bash", "-c", "cd /app/; python manage.py migrate; python manage.py runserver 0.0.0.0:80 "]
