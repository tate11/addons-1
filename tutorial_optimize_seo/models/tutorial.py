from odoo import models, fields, api, modules, _
from odoo.addons.http_routing.models.ir_http import slug

import base64


class Tutorial(models.Model):
    _name = 'tutorial'
    # We inherit the website.seo.metadata (abstract) model, which allows us to reuse the default SEO functionalities.
    # See https://github.com/odoo/odoo/blob/a5ca064dc2c821844bfafb767be67d6885e31a71/addons/website/models/website.py#L809
    # The inherit 'website.published.mixin' is for creating a direct link to the page in the frontend
    _inherit = ['website.seo.metadata', 'website.published.mixin']
    _description = 'Tutorial for a specific object'

    # Function to set a default image on our records, this is to demonstrate our SEO preview dialogs for social media.
    def _get_default_image(self):
        if not self.preview_image:
            with open(modules.get_module_resource('tutorial_optimize_seo',
                                                  'static/src/img',
                                                  'default_tutorial_image.jpg'),
                      'rb') as f:
                return base64.b64encode(f.read())

    name = fields.Char(string='Tutorial name', required=True, copy=False)
    preview_image = fields.Binary("Image preview", copy=False, default=_get_default_image)
    author_id = fields.Many2one('res.partner', string='Author', copy=False)
    description = fields.Text(string='Intro (preview) text', copy=False)

    """
     This function will only be overriden if the controller also passed the record as 'main_object' in the dictionary
     values of the controller. See tutorial_details in the controller tutorial.py as an example.
     In this override we will set extra SEO values and alter the social media previews.
    """
    def _default_website_meta(self):
        # Overrides _default_website_meta from the abstract model
        res = super()._default_website_meta()

        # See http://ogp.me/ for all SEO options
        res['default_opengraph']['og:title'] = self.name + ' | Tutorials'
        res['default_opengraph']['og:image'] = "/web/image/tutorial/%s/preview_image" % self.id
        # As a tutorial can be considered an article we should mark it so in the SEO. By doing this we can add extra
        # tags for the article which will be indexed in search engines.
        res['default_opengraph']['og:type'] = 'article'
        res['default_opengraph']['article:published_time'] = self.create_date
        res['default_opengraph']['article:modified_time'] = self.write_date
        res['default_opengraph']['article:author'] = self.author_id.sudo().name
        # TIP: you could also set the article:tag and article:section parameters if you had tags on this model.

        # Twitter - this will set a default title and preview image for twitter. Otherwise it would be the page name
        # and the company logo, which is not as good.
        res['default_twitter']['twitter:title'] = self.name + ' | Tutorials'
        res['default_twitter']['twitter:image'] = "/web/image/tutorial/%s/preview_image" % self.id

        return res

    # This function is not needed to compute / set SEO values. We use this to create an easy link to the webpage
    # in the frontend for this tutorial
    def _compute_website_url(self):
        super()._compute_website_url()
        for tutorial in self:
            # The website_url that is generated here will tell Odoo where to go to when clicking on the smartbutton in
            # the form view of the tutorial.
            tutorial.website_url = "/tutorial/%s" % slug(tutorial)
