from odoo import models, fields
from datetime import datetime

class BlogPost(models.Model):
    _inherit = 'blog.post'

    auto_publish = fields.Boolean(string="Auto Publish")

    def auto_publish_posts(self):
        current_time = datetime.now()
        posts_to_publish = self.search([
            ('auto_publish', '=', True),
            ('post_date', '<=', current_time),
            ('website_published', '=', False)
        ])
        for post in posts_to_publish:
            post.website_published = True
