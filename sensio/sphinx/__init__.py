from sphinx.writers.html import HTMLTranslator
from docutils import nodes
from sphinx.locale import admonitionlabels, lazy_gettext

customadmonitionlabels = admonitionlabels
l_ = lazy_gettext
customadmonitionlabels['best-practice'] = l_('Best Practice')

class SensioHTMLTranslator(HTMLTranslator):
    def __init__(self, builder, *args, **kwds):
        HTMLTranslator.__init__(self, builder, *args, **kwds)

    def visit_admonition(self, node, name=''):
        self.body.append(self.starttag(node, 'div', CLASS=('admonition-wrapper')))
        self.body.append('<div class="' + name + '"></div>')
        self.body.append('<div class="admonition admonition-' + name + '">')
        if name and name != 'seealso':
            node.insert(0, nodes.title(name, customadmonitionlabels[name]))
        self.set_first_last(node)

    def depart_admonition(self, node=None):
        self.body.append('</div></div>\n')
