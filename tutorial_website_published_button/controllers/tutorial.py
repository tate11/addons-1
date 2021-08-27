from odoo import http
from odoo.http import request


class Tutorial(http.Controller):
    @http.route(["/tutorials"], type='http', auth="public", website=True)
    def tutorial_overview(self, **kw):
        # Get all tutorials from the database but only get the ones that are published!
        tutorials = http.request.env['tutorial'].search([("website_published", "=", True)])

        # Return the tutorial overview page with all tutorial records
        return request.render('tutorial_website_published_button.tutorial_overview',
                              {'tutorials': tutorials})

    @http.route(['/tutorial/<model("tutorial"):tutorial>'],
                type='http', auth='public', website=True)
    def tutorial_details(self, tutorial, **kw):
        # Load the tutorial details.
        """
        Notice the main_object option! If this value is not set and if you go to a tutorial page you will set the SEO
        description and keywords for all tutorial details. As you want to set specific SEO values per record you
        should add the main_object key to the dictionary so that Odoo knows to which record it applies.
        Without setting the main_object value you will also see no SEO information being set in the backend.
        """
        return request.render('tutorial_website_published_button.tutorial_detail_page',
                              {'tutorial': tutorial,
                               'main_object': tutorial})
