"""
A simple Flask API developed to the Ubiwhere Challenge

.. moduleauthor:: Rui Dias <https://github.com/ruipedrodias94>

"""

from ubiwhere_challenge import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
