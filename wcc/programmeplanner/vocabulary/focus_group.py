from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class FocusGroup(grok.GlobalUtility):
    grok.name('wcc.programmeplanner.focus_group')
    grok.implements(IVocabularyFactory)

    _terms = [{
        'value': 'inter-religious',
        'title': 'Inter Religious',
    },{
        'value': 'gender',
        'title': 'Gender',
    },{
        'value': 'indigenous-people',
        'title': 'Indigenous People',
    },{
        'value': 'youth',
        'title': 'Youth',
    }]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
