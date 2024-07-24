from app import app

# Entry point for Vercel
def handler(event, context):
    return app(event, context)
