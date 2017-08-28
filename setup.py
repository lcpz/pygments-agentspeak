#!/usr/bin/env python3

from setuptools import setup, find_packages

setup (
  name='pygments-agentspeak',
  version=0.1,
  description='Pygments lexer for Jason AgentSpeak.',
  long_description=open('README.md').read(),
  keywords='pygments agentspeak jason jacamo lexer',
  license='BSD',
  packages=find_packages(),
  install_requires=['pygments'],
  entry_points =
  """
  [pygments.lexers]
  agentspeak = agentspeaklexer:AgentSpeakLexer
  """
  classifiers=[
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ]
)
