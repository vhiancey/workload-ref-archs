# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import openstackdocstheme
import subprocess

sys.path.insert(0, os.path.abspath('../..'))
# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# extensions = [
#    'sphinx.ext.autodoc',
#    #'sphinx.ext.intersphinx',
#    'oslosphinx'
#]
extensions = []

# autodoc generation is a bit aggressive and a nuisance when doing heavy
# text edit cycles.
# execute "export SPHINX_DEBUG=1" in your terminal to disable

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Workload-Reference-Architecture'
bug_tag = u"workload-ref-archs"
copyright = u'2017, OpenStack Foundation'

# We ask git for the SHA checksum
# The git SHA checksum is used by "log-a-bug"
giturl = u'https://git.openstack.org/cgit/openstack/workload-ref-archs/tree/doc/source'
git_cmd = ["/usr/bin/git", "log", "-1"]
last_commit = subprocess.Popen(git_cmd, stdout=subprocess.PIPE)
first_line_cmd = ["head", "-n1"]
gitsha = subprocess.Popen(first_line_cmd, stdin=last_commit.stdout,
               stdout=subprocess.PIPE).communicate()[0].split()[-1].strip()
# tag that reported bugs will be tagged with
# source tree
# pwd = os.getcwd()
# html_context allows us to pass arbitrary values into the html template
#html_context = {"pwd": pwd, "gitsha": gitsha}
html_context = {"gitsha": gitsha, "bug_tag": bug_tag,
                "giturl": giturl,
                "bug_project": "workload-ref-archs"}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Must set this variable to include year, month, day, hours, and minutes.
html_last_updated_fmt = '%Y-%m-%d %H:%M'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme_path = ["."]
# html_theme = '_theme'
# html_static_path = ['static']
html_theme = 'openstackdocs'
html_theme_path = [openstackdocstheme.get_html_theme_path()]

# If false, no index is generated.
html_use_index = False

# If true, links to the reST sources are added to the pages.
# This one is needed for "Report a bug".
html_show_sourcelink = False

# If true, publish source files
html_copy_source = False

# Output file base name for HTML help builder.
htmlhelp_basename = '%sdoc' % project

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index',
     '%s.tex' % project,
     u'OpenStack Workload Reference Architecture',
     u'OpenStack Enterprise Working Group', 'manual'),
]

# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'http://docs.python.org/': None}


# -- Options for Internationalization output ------------------------------
locale_dirs = ['locale/']

# -- Options for PDF output --------------------------------------------------
#pdf_documents = [
#    ('index', u'openstack-workload-ref-archs-documentation',
#     u'OpenStack Workload Reference Architectures',
#     u'OpenStack contributors')
#]
