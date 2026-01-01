from app import create_app
from decouple import config

def create_flask_app():
    env = config('FLASK_ENV', default='development', cast=str)
    debug_mode = config('DEBUG', default=True, cast=bool)

    app = create_app()
    app.debug = debug_mode

    # check project mode
    if env == 'production' and debug_mode:
        app.logger.warning("⚠️ WARNING: Debug mode is enabled in production environment! This is a security risk.")

    return app

def main():
    app = create_flask_app()

    host = config('FLASK_HOST', default='0.0.0.0', cast=str)
    port = config('FLASK_PORT', default='8000', cast=int)

    app.run(host=host, port=port, debug=app.debug, threaded=True)

if __name__ == '__main__':
    main()
