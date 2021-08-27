from odoo import models, fields, api, modules, _
from odoo.addons.http_routing.models.ir_http import slug

import base64


class Tutorial(models.Model):
    _name = 'tutorial'
    """
    We inherit the website.published.mixing (abstract) model, which allows us to reuse the default publishing options.
    See https://github.com/odoo/odoo/blob/344d20a6c40e2be73af3dbdb32ce9a2fa721ca01/addons/website/models/website.py#L913
    The inherit 'website.published.mixin' is for creating a direct link to the page in the frontend and handling
    publishing or unpublishing of records.
    The website.published.mixin model adds three fields on your own model:
    - website_published (boolean)
    - is_published (boolean): if this field is true the record is set to active for the frontend.
    - website_url (char): the URL where this record can be viewed. This has to be set in an override of the function
    _compute_website_url.
    """
    _inherit = ['website.published.mixin']
    _description = 'Tutorial for a specific object'

    # Function to set a default image on our records, this is to demonstrate our SEO preview dialogs for social media.
    def _get_default_image(self):
        if not self.preview_image:
            with open(modules.get_module_resource('tutorial_website_published_button',
                                                  'static/src/img',
                                                  'default_tutorial_image.jpg'), 'rb') as f:
                return base64.b64encode(f.read())

    name = fields.Char(string='Tutorial name', required=True, copy=False)
    preview_image = fields.Binary("Image preview", copy=False, default=_get_default_image)
    author_id = fields.Many2one('res.partner', string='Author', copy=False)
    description = fields.Text(string='Intro (preview) text', copy=False)

    def _compute_website_url(self):
        # We override this function, which comes from the abstract model 'website.published.mixin'.
        # We have to set the website_url so that it links to the right place in the frontend.
        super()._compute_website_url()
        for tutorial in self:
            # This website url will be set and when you click on the published button in the backend it'll open this URL
            tutorial.website_url = "/tutorial/%s" % slug(tutorial)
