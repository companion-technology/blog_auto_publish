# Auto Scheduled Blogger for Odoo

This module extends the standard Odoo blogging system by adding an auto-publish feature. Blog posts can be scheduled for future publication by setting a `post_date`. If the `auto_publish` field is set to `True`, the post will be automatically published once the current date surpasses the `post_date`.

## Features

- **Scheduled Publishing**: Set a future date and time for your blog post to be automatically published.
- **Auto Publish Toggle**: Decide on a per-post basis if you want the auto-publish feature to be active with a simple checkbox.

## Usage

1. Navigate to the Blog Posts section in Odoo.
2. Create or edit a blog post.
3. You'll find an `auto_publish` checkbox. If you want the post to be auto-published, ensure this is checked.
4. Set the `post_date` to the desired future date and time for publication.
5. Save the post. It will be automatically published once the current date surpasses the `post_date`, provided `auto_publish` is set to `True`.

## Dependencies

- **Odoo Blog**: This module extends the standard Odoo blogging system, so you need to have the `website_blog` module installed and running.

## Cron Job

The module runs a scheduled action every 10 minutes to check for any blog posts that should be published. Ensure your Odoo instance's scheduled actions (cron jobs) are active for this module to function correctly.

## Troubleshooting

1. **Post not publishing**: Ensure the `post_date` is set correctly, and the `auto_publish` checkbox is checked.
2. **Scheduled action not running**: Navigate to `Settings > Technical > Scheduled Actions` and ensure the action related to this module is active and running at the expected intervals.

## License

This module is licensed under the LGPL-3.0 License. See the [LICENSE](LICENSE) file for more details.

## Contribution

If you find any issues or want to contribute to the development of this module, please create an issue or pull request on our GitHub repository.
