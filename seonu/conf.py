# -*- coding: utf-8 -*-

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Scieldas'

exclude_patterns = ['_build']

html_theme = 'insegel'
html_theme_options = {

}

html_last_updated_fmt = '%d %b %Y'

releases_github_path = 'autophagy/scieldas'
# Our pre-0.x releases are unstable / mix bugs+features
releases_unstable_prehistory = True
