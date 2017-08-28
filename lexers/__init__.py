# -*- coding: utf-8 -*-
"""
    pygments.lexers.agentspeak
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for AgentSpeak extension interpreted by Jason, and Jason/JaCaMo
    project files.

    :copyright: Copyright 2017 by
        Jomi F. Hübner, Rafael H. Bordini, and Luke Bonham.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, bygroups, inherit, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
Number, Punctuation

__all__ = ['JasonAgentLexer', 'JasonProjectLexer', 'JaCaMoProjectLexer']

class JasonAgentLexer(RegexLexer):
    """
    Lexer for Jason agent files.
    """
    name = 'Jason'
    aliases = ['jason']
    filenames = ['*.asl']
    mimetypes = ['text/x-jason']

    keywords = (
        'begin', 'end', 'include', 'namespace', 'atomic', 'true', 'false'
    )

    builtins = (
        'makeArtifact', 'disposeArtifact', 'lookupArtifact', 'adoptRole',
        'leaveRole', 'createScheme', 'removeScheme', 'commitMission',
        'leaveMission', 'setGoalAchieved', 'createWorkspace', 'joinWorkspace',
        'joinRemoteWorkspace', 'shutdownNode', 'focus', 'createGroup',
        'setOwner'
    )

    # define your custom artifact operations here
    operations = (
        'sendOffer', 'adjustOffer', 'providerInitialised'
    )

    flags = re.UNICODE | re.MULTILINE

    tokens = {
        'root': [
            # Java-like comments
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),

            # numbers
            (r'0\'.', String.Char),
            (r'0b[01]+', Number.Bin),
            (r'0o[0-7]+', Number.Oct),
            (r'[0-9]+', Number.Integer),
            (r'0x[0-9a-fA-F]+', Number.Hex),

            # keywords
            (words(keywords, suffix=r'\b'), Keyword),

            # internal actions
            (r'\.[a-z][\w\.]*', Name.Builtin), # standard internal actions
            (r'([a-z][\w]*)\.[\w\.]+', Name.Builtin), # internal actions
            (words(builtins, suffix=r'\b'), Name.Builtin),

            # artifact operations
            # problem: in JaCaMo, syntax is the same for both operations and
            # predicates, so for the time being, we'll let the user define
            # his/her custom operations before compilation
            (words(operations, suffix=r'\b'), Name.Builtin),

            # beliefs
            (r"~?[a-z]\w+=\..", String.Atom),
            (r'(-|\+|-\+)[a-z]\w+', Name.Function),
            (r'\?[a-z]\w*', Name.Class),

            # plans
            (r'[\-|\+]?!\w*:?:?\w*', Name.Class),

            # puntuactions
            (r'[\[\](){}|.,:;_?]', Punctuation),
            (r':-|<-|\-\+', Punctuation),

            # operators
            (r'(<|>|=<|>=|==|\\==|=|/|\*|\+|\-|\!)', Operator),
            (r'(if|else|else if|while|for|cut|not|mod|div)\b', Operator.Word),
            (r'(&|\|)', Operator.Logical),

            # variables
            (r'[A-Z]\w*', Name.Variable),

            # taken from PrologLexer
            (r'"(?:\\x[0-9a-fA-F]+\\|\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|'
             r'\\[0-7]+\\|\\["\nabcefnrstv]|[^\\"])*"', String.Double),
            (u'([a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             u'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*)'
             u'(\\s*)(:-|<-)',
             bygroups(String.Atom, Text, Operator)),
            (u'([a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             u'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*)'
             u'(\\s*)(\\()',
             bygroups(Name.Function, Text, Punctuation)),
            (u'[a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             u'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*',
             String.Atom),
            (u'[#&*+\\-./:<=>?@\\\\^~\u00a1-\u00bf\u2010-\u303f]+',
             String.Atom),
            (u'\\s+|[\u2000-\u200f\ufff0-\ufffe\uffef]', Text)
        ]
    }

class JasonProjectLexer(JasonAgentLexer):
    name = 'JasonProject'
    aliases = ['jasonproject']
    filenames = ['*.mas2j']
    mimetypes = ['text/x-jasonp']

    flags = re.UNICODE | re.MULTILINE
    tokens = {
        'root': [
            (r'MAS|environment|agents|infrastructure|classpath|aslSourcePath', Keyword),
            (r'agentArchClass|beliefBaseClass|agentClass', Keyword),
            (r'\#', Operator),
            (r':', Punctuation),
            inherit
        ]
    }

class JaCaMoProjectLexer(JasonAgentLexer):
    name = 'JaCaMoProject'
    aliases = ['jacamoproject']
    filenames = ['*.jcm']
    mimetypes = ['text/x-jcm']

    flags = re.UNICODE | re.MULTILINE
    tokens = {
        'root': [
            (r'mas|uses|agent|instances|class-path|asl-path|platform|debug', Keyword),
            (r'workspace|artifact|agents|focused-by', Keyword),
            (r'ag-arch|ag-bb-class|ag-class|beliefs|goals|focus|join|roles', Keyword),
            (r'organisation|group|responsible-for|scheme|players', Keyword),
            (r'\#', Operator),
            (r'[:@]', Punctuation),
            inherit
        ]
    }
