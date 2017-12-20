"""Setup bottle app"""
from bottle import install, get, post, redirect, request, template, static_file, run
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='storage/database.sqlite', keyword='store'))

@get('/')
def index(store):
    """Load the index view"""
    posts_data = store.execute('SELECT title, slug, intro FROM posts order by id desc').fetchall()
    return template('index', posts=posts_data)

@get('/posts/<slug>')
def show_post(slug, store):
    """Load a single post by slug"""
    post_data = store.execute('SELECT id, title, intro, content FROM posts WHERE slug=?', (slug,)).fetchone()
    return template('post', id=post_data['id'], title=post_data['title'], intro=post_data['intro'], content=post_data['content'])

@get('/admin/new')
def show_new():
    """Display the new post form"""
    return template('form', id='', title='', intro='', content='')

@post('/admin/new')
def save_post(store):
    """Store a new post and redirect home"""
    title = request.forms.get('title').strip()
    slug = title.lower().replace(' ', '-')
    intro = request.forms.get('intro')
    content = request.forms.get('content')
    store.execute('insert into posts (title, slug, intro, content) values (?, ?, ?, ?)', (title, slug, intro, content,))
    redirect('/')

@get('/admin/edit/<id:int>')
def show_edit(id, store):
    """Display the post edit form"""
    post_data = store.execute('SELECT id, title, intro, content FROM posts WHERE id=?', (id,)).fetchone()    
    return template('form', id=post_data['id'], title=post_data['title'], intro=post_data['intro'], content=post_data['content'])

@post('/admin/edit/<id:int>')
def update_post(id, store):
    """Update an existing post and redirect home"""
    title = request.forms.get('title').strip()
    slug = title.lower().replace(' ', '-')
    intro = request.forms.get('intro')
    content = request.forms.get('content')
    store.execute('update posts set title=? , slug=?, intro=?, content=? where id=?', (title, slug, intro, content, id))
    redirect('/')

@post('/admin/delete/<id:int>')
def delete_post(id, store):
    """Delete an existing post"""
    post_data = store.execute('delete from posts where id=?', (id,))
    redirect('/')

@get('/public/<filepath:path>')
def public_assets(filepath):
    """Load an public assets"""
    return static_file(filepath, root='public')

run(host='localhost', port=8080, debug=True, reloader=True)
