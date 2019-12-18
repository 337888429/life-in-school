# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2019-12-17 15:36:20
# @Last Modified by:   Nessaj
# @Last Modified time: 2019-12-17 15:38:13

from django.utils.deprecation import MiddlewareMixin#
from django.shortcuts import HttpResponse

class Md1(MiddlewareMixin):

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = "content-type"
        response['Access-Control-Allow-Methods'] = "DELETE,PUT"
        print("跨域请求...")
        return response