% rebase('layouts/base.tpl')

<section class="post">
    <h1 class="post-title">{{title}}</h1>
    <em class="post-intro">{{intro}}</em>
    <p class="post-content">{{content}}</p>
    <p class="post-edit"><a href="/admin/edit/{{id}}">Edit Post</a></p>
</section>