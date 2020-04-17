
from distutils.core import setup
setup(
  name = 'pygamePhysics',         # How you named your package folder (MyLib)
  packages = ['pygamePhysics'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple physics engine for pygame',   # Give a short description about your library
  author = 'Ethan Culp',                   # Type in your name
  author_email = 'ethan.culp101@gmail.com,      # Type in your E-Mail
  url = 'https://github.com/seventyfox92475',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/seventyfox92475/pygamePhysics/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['PHYSICS', 'PHYSICS', 'EASY'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pygame',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

