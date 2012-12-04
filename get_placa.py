#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################
#
# Name: Scrapper para obtener datos de Seguro de Autos
# de la Superintendencia de Bancos del Ecuador.
#
# Version: 0.0.1
#
# Copyright (C) 2012 DAGANET WEB SOLUTIONS
# All rights reserved.
#
# This software is licensed as described in the file LICENSE, 
# which you should have received as part of this distribution.
#
# Authors: Dairon Medina <dairon@daganet.net>
#
################################################################
import sys, urllib2
import re
import random

import spynner
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *
from PyQt4.QtCore import QUrl

from lxml.html import document_fromstring

try:
    import json
except ImportError:
    import simplejson as json


class PlacasScrapper:
    """
    Scrapper que obtiene los datos de una placa introducida desde:
    http://soaprd.sbs.gob.ec:7778/AppWGP/sbs_soat_index.jsp
    """

    def __init__(self, num_placa):
        """
        Constructor
        """
        browser = spynner.Browser(user_agent=self.random_ua())
        browser.create_webview()
        
        #poner placa en mayuscula
        self.placa = num_placa.upper()

        self.headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1', 'Host': 'soaprd.sbs.gob.ec:7778', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Language':'es-ES,es;q=0.8' }
        
        index_url = 'http://soaprd.sbs.gob.ec:7778/AppWGP/sbs_soat_index.jsp'
        
        browser.load(index_url)
        
        gen_principal_url = 'http://soaprd.sbs.gob.ec:7778/AppWGP/sbs_gen_principal.jsp'
        
        browser.load(gen_principal_url)     
                              
        #la url de inicio
        self.url = 'http://soaprd.sbs.gob.ec:7778/AppWGP/sparametrosappgen'
        
        #variables get a pasar a la URL
        variables ="hid_codSoftware=110&hid_codReporte=6&hid_target=centroUP&txt_q_placa=%s" % self.placa
        
        datos_headers = dict(self.headers, **{'Origin': 'http://soaprd.sbs.gob.ec:7778', 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': 'http://soaprd.sbs.gob.ec:7778/AppSoat/sbs_soat_ctrConsulta.jsp?hid_codSoftware=110&hid_codReporte=6&hid_target=centroUP&hid_soporteExcel=S&COD_SOFTWARE=110&COD_UNIDAD_SUBUNIDAD=SRT&NOM_UNIDAD_SUBUNIDAD=SUBDIRECCION%20DE%20RECURSOS%20TECNOL%D3GICOS&COD_EMP=1747&PORTAL_USER=PCARGUA&STS_PERMITE_I=N&STS_PERMITE_D=N&STS_PERMITE_U=N&STS_PERMITE_S=S&COD_OPCION=393'})
        
        req = QNetworkRequest(QUrl(self.url))
        for k, v in datos_headers.items():
            req.setRawHeader(k, v)
            
        browser.webframe.load(req, QNetworkAccessManager.PostOperation, variables)
                       
        browser.wait_load()
        datos = unicode(browser.webframe.toHtml())
        browser.close()
                
        self.parse_data(datos)

    def parse_data(self, data):
        """
        Parsear los datos para dar salida
        """
        respuesta = {}
        
        dom = document_fromstring(data)
                
        tr = dom.xpath('//table[3]/tbody/tr/td/table/tbody/tr[position()=last()]')     
        for col in tr:
            respuesta['placa'] = self.placa
            respuesta['aseguradora'] = col[0].text_content()
            respuesta['no_certificado'] = col[1].text_content()
            respuesta['f_inicio'] = col[2].text_content()
            respuesta['f_fin'] = col[3].text_content()
            respuesta['vigencia'] = col[4].text_content()
        
        #devolver salidaen JSON
        #print json.dumps(respuesta)
        return json.dumps(respuesta)

    def random_ua(self):
        """
        Cambia User Agent desde una lista dinamica obtenida desde:
        http://www.zytrax.com/tech/web/browser_ids.htm
        """
        site = urllib2.urlopen('http://www.zytrax.com/tech/web/browser_ids.htm').read()
        pattern = re.compile(r'<p class=\"g-c-[ns]\">(.*?)<\/p>', re.S)
        browser_list = pattern.findall(site)
        ua = random.choice(browser_list)
        if ua:
            return ua
        else:
            return 'Mozilla/5 (Solaris 10) Gecko'

if len(sys.argv) != 2:
     print >>sys.stderr, 'uso: get_placa.py NUMERO-PLACA'
     exit(2)
else:
    cmd = PlacasScrapper(sys.argv[1])

