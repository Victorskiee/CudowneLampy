FROM prestashop/prestashop:1.7.7.8

COPY ./webshop/ /var/www/html

RUN a2enmod ssl

EXPOSE 80
EXPOSE 443
