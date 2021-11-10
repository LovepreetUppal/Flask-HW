from myapp import myobj
from myapp import db
from myapp.models import City
from myapp.forms import TopCities
from flask import render_template, escape, flash, redirect

@myobj.route("/", methods = ['GET', 'POST'])
def home():
	name = "Lovepreet"
	title = 'Top Cities'
	form = TopCities()
	cityt = City.query.order_by(City.city_rank).all()
	if form.validate_on_submit():
		flash(f'{form.city_name.data} added to list, visited = {form.is_visited.data}')
		city = form.city_name.data
		rank = form.city_rank.data
		visited = form.is_visited.data
		city_ranked = City(city_name=city, city_rank=rank, is_visited = visited)

		db.session.add(city_ranked)
		db.session.commit()
		return redirect('/')
	return render_template('home.html', name = name, title =title, form = form, City=cityt)
	
	
