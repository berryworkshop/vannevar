from invoke import task

apps = [
    'vannevar',
    'catalog',
    'cms',
]

@task
def build(context):
    '''
    automatically run other essential build commands
    '''
    bundle(context)
    css(context)
    js(context)


@task
def bundle(context):
    '''
    * bundle global js dependencies into `vannevar/static/base.js`
        * react
        * react-dom
    * minify
    *
    '''
    print('main js bundled!')



@task
def watch(context, app):
    '''watch for css or js changes'''
    pass

@task
def css(context):
    '''convert sass and combine css'''
    pass

@task
def js(context):
    '''lint, bundle and minify app-level js'''
    src = 'catalog/static/catalog/scripts/hello.jsx'
    out = 'catalog/static/catalog/dist/base.js'
    context.run(('browserify -t [ babelify ] '
                 '--external react --external react-dom '
                 '{} -o {}').format(src, out))

@task
def vendors(context):
    '''bundle and minify global css and js'''

    # global css
    # context.run(('cleancss node_modules/normalize.css/normalize.css '
    #             'vannevar/static/vannevar/css/vendors.css'))

    # global js
    context.run(('browserify -r react -r react-dom -r d3 '
                 '> vannevar/static/vannevar/js/vendors.js && '
                 'browserify -r react -r react-dom -r d3 | uglifyjs '
                 '> vannevar/static/vannevar/js/vendors.min.js'))
