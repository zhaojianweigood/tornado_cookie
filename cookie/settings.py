import os

APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

base_config = {
    'template_path': os.path.join(APP_DIR, "templates"),
    'static_path': os.path.join(APP_DIR, "static_path"),
}

prod_config = base_config.update({
    'debug': False,
})

dev_config = base_config.update({
    'debug': True

})

config = {
    'dev': dev_config,
    'prod': prod_config,
}
