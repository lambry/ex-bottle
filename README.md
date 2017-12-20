# Ex Bottle

A super basic bottle (example) app utilzing sqlite for convenience.

```bash
# Install bottle and bottle-sqlite
pip install -r requirements.txt

# Start the server
python index.py
```

### Routes

```python
# Display routes
@get('/')
@get('/posts/<slug>')

# Admin / post managment routes
@get('/admin/new')
@post('/admin/new')
@get('/admin/edit/<id>')
@post('/admin/edit/<id>')
@post('/admin/delete/<id>')
```