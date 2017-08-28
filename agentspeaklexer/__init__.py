# -*- coding: utf-8 -*-
"""
    pygments.lexers.agentspeak
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer for AgentSpeak extenstion interpreted by Jason, and Jason/JaCaMo MAS
    definition files.

    :copyright: Copyright 2017 by Luke Bonham.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
Number, Punctuation

__all__ = ['AgentSpeakLexer']

class AgentSpeakLexer(RegexLexer):
    """
    Lexer for AgentSpeak files.
    """
    name = 'AgentSpeak'
    aliases = ['agentspeak']
    filenames = ['*.asl', '*.mas2j', '*.jcm']
    mimetypes = ['text/x-agentspeak']

    # TODO: to complete
    keywords = (
        'begin', 'end', 'include', 'namespace', 'mas', 'agent', 'agents',
        'atomic', 'asl-path'
    )

    # TODO: to complete
    builtins = (
        'makeArtifact', 'disposeArtifact', 'lookupArtifact', 'adoptRole',
        'leaveRole', 'createScheme', 'removeScheme', 'commitMission',
        'leaveMission', 'setGoalAchieved', 'createWorkspace', 'joinWorkspace',
        'joinRemoteWorkspace', 'shutdownNode', 'focus', 'createGroup',
        'setOwner'
    )

    # define your custom CArtAgO operations here
    operations = (
        'sendOffer', 'adjustOffer'
    )

    flags = re.DOTALL | re.UNICODE | re.MULTILINE

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
            (r'[(jia)\b]?[.](\w*)', Name.Builtin),
            (words(builtins, suffix=r'\b'), Name.Builtin),

            # artifact operations with no arguments
            (r'(?<!\?)(?<!\:)(?<!\+)\w*;', Name.Builtin),

            # problem: fetching artifact operations with arguments seems
            # currently impossible, since in JaCaMo their syntax doesn't differ
            # from the predicates one, hence for the time being, we'll let the
            # user define before compilation
            (words(operations, suffix=r'\b'), Name.Builtin),

            # beliefs
            (r"~?\w*.'", String.Atom),
            (r'\-?\+:?:?[A-Z-a-z]+', Name.Function),

            # plans
            (r'[\-|\+]?!\w*:?:?\w*', Name.Class),

            (r'[\[\](){}|.,:;?]', Punctuation),
            (r':-|<-|\-\+', Punctuation),

            # operators
            (r'(<|>|=<|>=|==|\\==|=|/|\*|\+|\-|&|\!)', Operator),
            (r'(div|not|::|if|else|else if|while|for|cut)\b', Operator.Word),

            # taken from PrologLexer
            (r'"(?:\\x[0-9a-fA-F]+\\|\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|'
             r'\\[0-7]+\\|\\["\nabcefnrstv]|[^\\"])*"', String.Double),
            (u'([a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             u'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*)'
             u'(\\s*)(:-|<-)',
             bygroups(Name.Constant, Text, Operator)),
            (u'([a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             u'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*)'
             u'(\\s*)(\\()',
             bygroups(Name.Function, Text, Punctuation)),
            (u'[a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             u'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*',
             String.Atom),
            (u'[#&*+\\-./:<=>?@\\\\^~\u00a1-\u00bf\u2010-\u303f]+',
             String.Atom),
            (r'[A-Z_]\w*', Name.Variable),
            (u'\\s+|[\u2000-\u200f\ufff0-\ufffe\uffef]', Text)
        ]
    }
