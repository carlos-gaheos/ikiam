# -*- coding: utf-8 -*-
# from odoo import http


# class IkiamFichaSocioeconomica(http.Controller):
#     @http.route('/ikiam_ficha_socioeconomica/ikiam_ficha_socioeconomica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ikiam_ficha_socioeconomica/ikiam_ficha_socioeconomica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ikiam_ficha_socioeconomica.listing', {
#             'root': '/ikiam_ficha_socioeconomica/ikiam_ficha_socioeconomica',
#             'objects': http.request.env['ikiam_ficha_socioeconomica.ikiam_ficha_socioeconomica'].search([]),
#         })

#     @http.route('/ikiam_ficha_socioeconomica/ikiam_ficha_socioeconomica/objects/<model("ikiam_ficha_socioeconomica.ikiam_ficha_socioeconomica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ikiam_ficha_socioeconomica.object', {
#             'object': obj
#         })
