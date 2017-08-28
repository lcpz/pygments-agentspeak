# -*- coding: utf-8 -*-
"""
    pygments.styles.jacamo
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017 by
        Jomi F. Hübner, Rafael H. Bordini, and Luke Bonham.
    :license: LGPL.
"""

from pygments.style import Style
from pygments.token import Token, Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation


class JaCaMoStyle(Style):
    """
    A style created just for JaCaMo.
    """

    default_style = ""

    styles = {
        # unused for now
        Token.EventBel   : 'bold #BB0000',
        Token.EventGoal  : 'bold #0000BB',
        Token.EventTGoal : 'bold #0000A4',
        Token.Belief     : '#BB0000',
        Token.Goal       : '#0000BB',
        Token.TGoal      : '#0000A4',
        Token.Action     : '#CC8800',

        Comment          : 'italic #777777',

        Keyword          : '#00A800',

        Operator         : '#000000',
        Operator.Word    : 'bold #000000',
        Operator.Logical : '#DD0000',

        Punctuation      : '#000000',

        Name.Builtin     : '#BB7700',
        Name.Function    : '#00A800',
        Name.Class       : '#0808FF',
        Name.Namespace   : '#907020',
        Name.Variable    : '#8432AD',
        Name.Constant    : '#AA0000',
        Name.Entity      : '#000000',
        Name.Attribute   : '#770000',
        Name.Tag         : 'bold #1E90FF',
        Name.Decorator   : '#888888',

        String           : '#E548B9',
        String.Symbol    : '#0000AA',
        String.Regex     : '#009999',
        String.Atom      : '#009999',

        Number           : '#E12856',

        Error            : '#F00 bg: #FAA',
    }
