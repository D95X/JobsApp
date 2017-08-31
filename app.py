from flask import Flask,render_template,redirect,flash,url_for,session,request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask("__name__")

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jobs'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
 #initialize MYSQL
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template( 'home.html')

@app.route('/jobs')
def jobs():
    # Create cursor
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM job")

    job = cur.fetchall()

    if result > 0:
        return render_template('jobs.html', job=job)
    else:
        msg = 'No Jobs Found'
        return render_template('jobs.html', msg=msg)
    # Close connection
    cur.close()

@app.route('/job/<string:id>/')
def job(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get job
    result = cur.execute("SELECT * FROM job WHERE id = %s", [id])

    job = cur.fetchone()
    return render_template('job.html', job=job)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('add_job'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

@app.route('/add_job')
@is_logged_in
def add_job():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get jobs
    result = cur.execute("SELECT * FROM job")

    job = cur.fetchall()

    if result > 0:
        return render_template('add_job.html', job=job)
    else:
        msg = 'No Jobs Found'
        return render_template('add_job.html', msg=msg)
    # Close connection
    cur.close()

# Add Job Form Class
class JobForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    company = StringField( 'Company', [validators.Length( min=1, max=30 )] )
    description = TextAreaField('Description', [validators.Length(min=20)])

@app.route('/job_add',methods=['GET', 'POST'])
@is_logged_in
def job_add():
    form = JobForm( request.form )
    if request.method == 'POST' and form.validate():
        title = form.title.data
        company = form.company.data
        description = form.description.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute( "INSERT INTO job(title, company, description) VALUES(%s, %s, %s)",
                     (title, company, description))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Job Created', 'success')

        return redirect(url_for( 'add_job' ))

    return render_template( 'job_add.html', form=form )

# Edit Job
@app.route('/edit_job/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_job(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get job by id
    result = cur.execute("SELECT * FROM job WHERE id = %s", [id])

    job = cur.fetchone()
    cur.close()
    # Get form
    form = JobForm(request.form)

    # Populate job form fields
    form.title.data = job['title']
    form.company.data = job['company']
    form.description.data = job['description']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        company = request.form['company']
        description = request.form['description']

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(title)
        # Execute
        cur.execute ("UPDATE job SET title=%s,company=%s,description=%s WHERE id=%s",(title, company, description, id))
        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Job Updated', 'success')

        return redirect(url_for('add_job'))

    return render_template('edit_job.html', form=form)

# Delete Job
@app.route('/delete_job/<string:id>', methods=['POST'])
@is_logged_in
def delete_job(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM job WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Job Deleted', 'success')

    return redirect(url_for('add_job'))

class ApplyForm(Form):
    cover = TextAreaField('Description', [validators.Length(min=20)])

@app.route('/apply/<string:id>', methods=['GET','POST'])
def apply(id):
    form = ApplyForm(request.form)
    if request.method == 'POST':
        cover = form.cover.data
        #create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO job(cover) VALUES %s",(cover))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash( 'your application successfully sent', 'success' )

        return redirect( url_for( 'login' ) )

    return render_template('apply.html', form=form)

if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug=True)
