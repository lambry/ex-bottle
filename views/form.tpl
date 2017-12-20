% rebase('layouts/base.tpl')

<form method="POST" class="form form-edit">
    <div class="form-field">
        <label for="title">Title</label>
        <input type="text" name="title" value="{{title}}" required>
    </div>
    <div class="form-field">
        <label for="intro">Intro</label>
        <input type="text" name="intro" value="{{intro}}" required>
    </div>
    <div class="form-field">
        <label for="content">Content</label>
        <textarea name="content" required>{{content}}</textarea>
    </div>
    <button type="submit" class="button">Save Post</button>
</form>

% if id:
    <form method="POST" action="/admin/delete/{{id}}" class="form form-delete">
        <button type="submit" class="button button-alert">Delete Post</button>
    </form>
% end