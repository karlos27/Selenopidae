# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NauticaItem(scrapy.Item):
    # define the fields for your item here like:
    # product info
    
    nombre = scrapy.Field()
    url = scrapy.Field()
    modelo = scrapy.Field()
    categoria = scrapy.Field()
    precio = scrapy.Field()
    descripcion = scrapy.Field()
    opiniones = scrapy.Field()
    imagen = scrapy.Field()

    

