import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

# we need blueprints from flask
from flask import Blueprint
import ckanext.custom_page.blueprints as custom_page_blueprints

class CustomPagePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'custom_page')

    # Custom pages
    def get_blueprint(self):
        # Create Blueprint for custom routes
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = u'templates'
        rules = [
            (u'/participate', u'render_about_custom_page', custom_page_blueprints.render_about_custom_page),
        ]
        for rule in rules:
            blueprint.add_url_rule(*rule)

        return blueprint
