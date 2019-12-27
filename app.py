from flask import Flask, render_template, redirect, request

from block import check_integrity, write_block

app = Flask(__name__)


@app.route('/')
def main(blocks=None, error=False):
	content  = {
		'blocks': blocks,
		'error': error
	}
	return render_template(
		'index.html', **content
	)


@app.route('/')
def add_block():
	pass


@app.route('/')
def check_block():
	pass


@app.errorhandler(404)
def page_not_found(error):
	return redirect('/')


if __name__ == '__main__':
	app.run()
