% rebase('layouts/base.tpl')

<section class="posts">
    %for post in posts:
        %title, slug, intro = post
        <article class="post">
            <a href="/posts/{{slug}}">
                <h2 class="post-title">{{title}}</h2>
                <p class="post-intro">{{intro}}</p>
            </a>
        </article>
    %end
</section>